import re

from database import *


class BooksLibrary(object):
    """class for manage user books and auto status"""

    def __init__(self):
        self.db = DataBase()
        self.lang_cache = {}
        self.hours_cache = {}
        self.audio_cache = {}
        self.pos_cache = {}

    def update_current_book(self, user_id, chat_id, book_name):
        lang = self.get_lang(user_id)
        self.db.update_current_book(user_id, chat_id, book_name, lang)
        pass

    def update_book_pos(self, user_id, current_book, new_pos):
        self.db.update_book_pos(user_id, current_book, new_pos)
        pass

    def switch_auto_staus(self, user_id):
        self.db.update_auto_status(user_id)
        pass

    def update_lang(self, user_id, lang):
        self.db.update_lang(user_id, lang)
        self.lang_cache[user_id] = lang
        return 0

    def update_working_hours(self, user_id, user_input) -> list:
        try:
            range_match = re.match(r'(\d{1,2})-(\d{1,2})', user_input)
            if range_match:
                start, end = map(int, range_match.groups())
                working_hours = list(range(start, end + 1))
            else:
                working_hours = list(map(int, user_input.split(',')))

            if not all(0 <= x <= 23 for x in working_hours):
                raise ValueError('Hours should be in range 0-23')

        except ValueError as e:
            print(e)
            working_hours = list(range(5, 18))  # 7-19 CEST

        self.db.update_working_hours(user_id, working_hours)
        self.hours_cache[user_id] = working_hours
        return working_hours

    def update_audio(self, user_id, audio):
        self.db.update_audio(user_id, audio)
        self.audio_cache[user_id] = audio
        return 0

    def get_pos(self, user_id, book_name):
        return self.db.get_pos(user_id, book_name)

    def get_lang(self, user_id):
        lang = self.lang_cache.get(user_id, None)
        if lang is None:
            lang = self.db.get_lang(user_id)
            if lang is None:
                lang = 'ru'
                self.update_lang(user_id, lang)
        return lang

    def rare_to_working_hours(self, user_id) -> str:
        rare = self.db.get_rare(user_id)
        if rare == '12':
            return '5-17'
        elif rare == '6':
            return '5,7,9,11,13,15,17'
        elif rare == '4':
            return '5,9,13,17'
        elif rare == '2':
            return '9,15'
        elif rare == '1':
            return '11'
        else:
            return '5-17'

    def get_working_hours(self, user_id):
        working_hours = self.hours_cache.get(user_id, None)
        if working_hours is None:
            working_hours = self.db.get_working_hours(user_id)
            if working_hours is None:
                hours_str = self.rare_to_working_hours(user_id)
                working_hours = self.update_working_hours(user_id, hours_str)
            else:
                self.hours_cache[user_id] = working_hours
        return working_hours

    def get_audio(self, user_id):
        audio = self.audio_cache.get(user_id, None)
        if audio is None:
            audio = self.db.get_audio(user_id)
            if audio is None:
                audio = 'off'
                self.update_audio(user_id, audio)
        return audio

    def get_user_books(self, user_id):
        return self.db.get_user_books(user_id)

    def get_auto_status(self, user_id):
        auto_status = self.db.get_auto_status(user_id)
        if auto_status is None:
            return -1
        return auto_status

    def get_users_for_autosend(self):
        return self.db.get_users_for_autosend()

    def get_current_book(self, user_id, format_name=False):
        current_book = self.db.get_current_book(user_id)
        if current_book is None:
            return -1
        if format_name:
            current_book = self._format_name(current_book, user_id)
        return current_book

    def _format_name(self, file_name, user_id):
        # Just del user_id and .txt from file_name
        formatted_name = file_name
        formatted_name = formatted_name.replace(str(user_id) + '_', '')
        formatted_name = formatted_name.replace('.txt', '')
        formatted_name = formatted_name.capitalize()
        return '📖' + formatted_name
