from wagtail.admin.panels import FieldPanel
from wagtail.blocks import StreamBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.api import APIField

from website.blocks import BannerBlock


class HomePage(Page):
    body = RichTextField(blank=True)
    blocks = StreamField(
        [
            ("banner", BannerBlock())
        ],
        blank=False,
        default=None,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
        FieldPanel("blocks")
    ]

    #TODO: Here we need to change this, cuz otherwise on the front
    # We will have problem rendering blocks.
    api_fields = [
        APIField("title"),
        APIField("body"),
        APIField("blocks")
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"