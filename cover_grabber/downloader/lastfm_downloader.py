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
import urllib.request
import urllib.parse
try:
    import xml.etree.cElementTree as ETree
except ImportError:
    import xml.etree.ElementTree as ETree

from cover_grabber.logging.config import logger


class LastFMDownloader(object):
    def __init__(self, album_name, artist_name):
        """Initializes LastFM Downloader"""
        self.LASTFM_API_KEY = os.environ.get("LASTFM_API_KEY")
        if not self.LASTFM_API_KEY:
            raise ValueError("LASTFM_API_KEY environment variable not set. Add it to .env and source it")
        self.LASTFM_URL = (
            "http://ws.audioscrobbler.com/2.0/?method=album.search&album={album_name}&api_key="
            + self.LASTFM_API_KEY
        )
        self.album_name = album_name
        self.artist_name = artist_name
        self.url = self.format_url()

    def format_url(self):
        """Sanitize and format URL for Last FM search"""
        album_name_encoded = urllib.parse.quote(self.album_name)
        return self.LASTFM_URL.format(album_name=album_name_encoded)

    def search_for_image(self):
        """Use LastFM's API to obtain a URL for the album cover art"""
        logger.info(
            'LastFM: Searching for "{artist_name} - {album_name}"'.format(
                artist_name=self.artist_name, album_name=self.album_name
            )
        )
        try:
            response = urllib.request.urlopen(self.url).read()
            response_str = response.decode("utf-8")
            start_index = response_str.index("<albummatches>")
            end_index = response_str.index("</albummatches>") + len("</albummatches>")
            response_str = response_str[start_index:end_index]
            xml_data = ETree.fromstring(response_str)

            for element in xml_data.iter("album"):
                artist_text = element.find("artist").text
                if artist_text and artist_text.lower() == self.artist_name.lower():
                    for elmnt in element.findall("image"):
                        if elmnt.attrib.get("size") == "extralarge":
                            url = elmnt.text
                            if url:
                                return url
            return None
        except Exception as e:
            logger.error("Error while searching for image: {}".format(e))
            return None
