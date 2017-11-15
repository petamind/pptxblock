"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import time
from xblock.core import XBlock
from xblock.fields import Integer, Scope, String
from xblock.fragment import Fragment
from slice_video import SliceVideo



class PptXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    video_url = String(
        default="", scope=Scope.settings,
        help="Video URL to download",
    )

    video_id = String(
        default="", scope=Scope.settings,
        help="Video id to store",
    )

    thumbs_html = String(
        default="", scope=Scope.settings,
        help="HTML code to display the result",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the PptXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/pptxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/pptxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/pptxblock.js"))
        frag.initialize_js('PptXBlock')
        return frag

    #Create simple setting for the xblock
    def studio_view(self, context=None):
        """
        The primary view of the PptXBlock, show settings.
        """
        html = self.resource_string("static/html/settings.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/pptxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/pptxblock.js"))
        frag.initialize_js('PptXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    # @XBlock.json_handler
    # def increment_count(self, data, suffix=''):
    #     """
    #     An example handler, which increments the data.
    #     """
    #     # Just to show data coming in...
    #     assert data['hello'] == 'world'

    #     self.count += 1
    #     return {"count": self.count}

    @XBlock.json_handler
    def submit_video_url(self, data, suffix=''):
        """
        A handler, which return the submited video_URL the data.
        """
        self.video_url = data['video_url'] 

        thread = SliceVideo(1, "1", self.video_url, self.thumbs_html)
        thread.start()
        while (thread.is_alive()):
            time.sleep(5)
        
        self.thumbs_html = thread.thumbs_html
        return {"video_url": thread.thumbs_html}
    #self.video_url


    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("PptXBlock",
             """<pptxblock/>
             """),
            ("Multiple PptXBlock",
             """<vertical_demo>
                <pptxblock/>
                <pptxblock/>
                <pptxblock/>
                </vertical_demo>
             """),
        ]
