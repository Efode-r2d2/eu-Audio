"""
    <ed-Audio is an open source audio processing toolbox>
    Copyright (C) <2019>  <Efriem Desalew Gebie>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from Utilities import AudioManager
from Utilities import FileManager
from Utilities import DirectoryManager
from Effects import AudioEffects


class EffectManager(object):
    def __init__(self, directory_path=None, file_path=None):
        self.directory_path = directory_path
        self.file_path = file_path

    def apply_speed_change(self, percent, mode=1):
        pass
