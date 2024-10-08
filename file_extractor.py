import os

from pyunpack import Archive

from text_transliter import *


class FileExtractor(object):
    """file from user which has been sent in bot"""

    def __init__(self):
        pass

    @staticmethod
    def _get_file_user_sent(telebot, message):
        # get file and filename which have been sent by user in bot
        file_info = telebot.get_file(message.document.file_id)
        downloaded_file = telebot.download_file(file_info.file_path)
        filename = TextTransliter(message.document.file_name).get_translitet()
        return downloaded_file, filename

    def local_save_file(self, telebot, message, download_path):
        # save file from user to local folder
        downloaded_file, filename = self._get_file_user_sent(telebot, message)
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # todo make it throw regex, ept
        if filename.find('.zip') != -1:
            filename.isalnum()
            path_for_save = os.path.join(download_path, filename)
            with open(path_for_save, 'wb') as new_file:
                new_file.write(downloaded_file)
            Archive(path_for_save).extractall(download_path)
            return path_for_save.replace(".zip", "")
        if filename.find('.epub') != -1 or filename.find('.fb2') != -1 or filename.find('.txt') != -1:
            # remove special character
            filename.isalnum()
            # file_from_user = save_file(downloaded_file, path_for_save, filename)
            path_for_save = os.path.join(download_path, filename)
            with open(path_for_save, 'wb') as new_file:
                new_file.write(downloaded_file)
            return path_for_save
        else:
            return -1  # type error
