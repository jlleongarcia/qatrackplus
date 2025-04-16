from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _l

# from qatrack.qa import models
from qatrack.reports import filters
from qatrack.reports.reports import (
    ORDERED_CONTENT_TYPES,
    BaseReport,
)
from qatrack.units import models as u_models


class RadiationUnitsDetailsReport(BaseReport):

    report_type = "radiationunits_details"
    name = _l("Radiation Units Details")
    filter_class = filters.RadiationUnitsFilter
    description = mark_safe(_l(
        "This report lists all Radiation Units for selected sites and rooms. "
        "Leave filters blank to include all."
    ))

    category = _l("Equipment")

    template = "reports/equipment/radiationunits_details.html" # Define the template path
    formats = ORDERED_CONTENT_TYPES

    __test__ = False  # supress pytest warning

    def get_queryset(self):
        """
        Return the base queryset of Units to be filtered.
        The BaseReportFilterSet handles the actual filtering.
        """
        # Pre-fetch related fields used in the template for efficiency
        qs = u_models.Unit.objects.select_related(
            'site', 'type'
        ).order_by('site__name', 'name') # Order for consistent display
        return qs

    def get_context(self):
        """Prepare context data for the template."""
        context = super().get_context()
        # The filtered queryset is automatically available in the filter_set
        context['units'] = self.filter_set.qs
        context['report_title'] = self.name
        context['description'] = self.description
        context['settings'] = settings
        return context

    def get_filename(self, report_format):
        """Generate a descriptive filename for report downloads."""
        # Example: radiation-units-details-site-hospital-a-unit-linac-1.pdf
        return slugify(f"{self.name}-{self.get_filter_string()}") + f".{report_format}"
