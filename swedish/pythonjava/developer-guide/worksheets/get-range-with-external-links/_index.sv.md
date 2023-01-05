---
title: Få räckvidd med externa länkar
type: docs
weight: 60
url: /sv/python-java/get-range-with-external-links/
---
## **Få räckvidd med externa länkar**
Det finns många tillfällen där excel-filer kommer åt data från andra excel-filer genom att använda externa länkar. Aspose.Cells for Python via Java ger möjlighet att hämta dessa externa länkar genom att använda[Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) metod. De[Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) metod returnerar en array av typen[Refererat område](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea). De[Refererat område](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea)klass ger en[ExternalFileName](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName)egenskap som returnerar namnet på den externa filen.

Följande kodavsnitt visar hur man får externa länkar.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
