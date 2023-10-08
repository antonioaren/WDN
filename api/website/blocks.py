from django.utils.translation import gettext as _
from wagtail import blocks as b
from wagtail.images.blocks import ImageChooserBlock


class CTAButton(b.StructBlock):
    text = b.CharBlock(required=False)
    page = b.PageChooserBlock(
        required=False, help_text=_("Use this field to point to internal page.")
    )
    link = b.URLBlock(
        required=False, help_text=_("Use this field to point to an external page.")
    )
    isExternalLink = b.BooleanBlock(
        required=False,
        help_text=_("Make sure you mark this checkbox to improve performance."),
    )


class BannerBlock(b.StructBlock):
    image = ImageChooserBlock()
    title = b.CharBlock()
    description = b.RichTextBlock()
    cta = CTAButton()