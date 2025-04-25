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
    name = _l("Equipos de Rayos X")
    filter_class = filters.RadiationUnitsFilter
    description = mark_safe(_l(
        "Este informe lista todos los equipos de radiodiagnóstico para los lugares y salas seleccionados. "
        "Deja en blanco los filtros para incluirlos todos."
    ))

    category = _l("Equipamiento")

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
        # context['report_title'] = self.title
        context['description'] = self.description
        context['settings'] = settings
        return context

    def get_filename(self, report_format):
        """Generate a descriptive filename for report downloads."""
        filter_string = ""
        # Safely get the filter string representation from the filter_set
        if hasattr(self, 'filter_set') and self.filter_set is not None:
            # Assuming the filter set has a method 'get_filter_string'
            # Adjust if the method name on your filter_set is different
            if hasattr(self.filter_set, 'get_filter_string') and callable(getattr(self.filter_set, 'get_filter_string')):
                 filter_string = self.filter_set.get_filter_string()
            # You might need other checks depending on the specific filter class used

        # Use self.title (user-provided) if available, otherwise default self.name
        report_name = self.title if hasattr(self, 'title') and self.title else self.name

        # Combine report name and filter string for the filename
        if filter_string:
            full_name = f"{report_name}-{filter_string}"
        else:
            full_name = report_name # No filters applied or filter string unavailable

        # Slugify the combined name and add the format extension
        return slugify(full_name) + f".{report_format}"
        # return slugify(f"{self.name}-{self.get_filter_string()}") + f".{report_format}"
