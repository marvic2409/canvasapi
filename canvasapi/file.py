from __future__ import absolute_import, division, print_function, unicode_literals

from six import python_2_unicode_compatible

import threading

from canvasapi.canvas_object import CanvasObject


@python_2_unicode_compatible
class File(CanvasObject):
    def __str__(self):
        return "{}".format(self.display_name)

    def delete(self):
        """
        Delete this file.

        :calls: `DELETE /api/v1/files/:id  \
        <https://canvas.instructure.com/doc/api/files.html#method.files.destroy>`_

        :rtype: :class:`canvasapi.file.File`
        """
        response = self._requester.request("DELETE", "files/{}".format(self.id))
        return File(self._requester, response.json())

    def download(self):
        """
        Download the file to specified location.

        :param location: The path to download to.
        :type location: str
        """
        url = self.url
        return url
            
            
    def get_contents(self):
        """
        Download the contents of this file.

        :rtype: str
        """
        response = self._requester.request("GET", _url=self.url)
        return response.text
