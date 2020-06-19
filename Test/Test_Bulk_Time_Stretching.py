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
from Utilities import DirectoryManager
from EffectsManager import EffectsManager

# source directory of reference audios
ref_audios_dir = "../../Test_Data/Ref_Audios"
# destination directory of query audios
query_audio_dir = "../../Test_Data/Query_Audios/Time_Stretched"
# reference audios
reference_audios = DirectoryManager.find_wav_files(source_dir=ref_audios_dir)
# applying pitch shifting for set of reference audio files
for i in reference_audios:
    audio_name = i.split("/")[4]
    for j in range(-16, 18, 2):
        DirectoryManager.create_dir(source_dir=query_audio_dir + "/" + str(100 + j))
        EffectsManager.apply_time_stretching(original_audio_path=i,
                                             modified_audio_path=query_audio_dir + "/" + str(
                                                 100 + j) + "/" + audio_name,
                                             target_duration_in_percent=j,
                                             offset=None,
                                             duration=None)
