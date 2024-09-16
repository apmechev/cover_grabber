# Copyright (C) 2011 Jayson Vaughn <vaughn.jayson@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import mutagen
from mutagen.flac import FLAC
from cover_grabber.handler.handler import Handler
from cover_grabber.logging.config import logger

class FLACHandler(Handler):
    def __init__(self, dirname, filenames):
        """Initialize FLAC Handler"""
        super().__init__(dirname, filenames)
        self.audio_files = [
            os.path.join(dirname, filename)
            for filename in filenames
            if filename.lower().endswith('.flac')
        ]

    def get_album_and_artist(self):
        """Return FLAC tags for album and artist"""

        self.audio_files.sort()

        for filepath in self.audio_files:
            try:
                tags = FLAC(filepath)
                if tags:
                    if (
                        "album" in tags and tags["album"]
                        and "artist" in tags and tags["artist"]
                    ):
                        album = tags["album"][0]
                        artist = tags["artist"][0]
                        logger.debug(
                            'album -> {album}, artist -> {artist}'.format(
                                album=album, artist=artist
                            )
                        )
                        return album, artist
            except mutagen.flac.FLACNoHeaderError:
                logger.error('No FLAC Header data in file {}'.format(filepath))
                continue
        return None, None
