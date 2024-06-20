---
title: Hämta intervall med externa länkar
type: docs
weight: 60
url: /sv/python-java/get-range-with-external-links/
---

## **Hämta intervall med externa länkar**
Det finns många fall där excelfiler får åtkomst till data från andra excelfiler genom användning av externa länkar. Aspose.Cells för Python via Java ger möjlighet att hämta dessa externa länkar genom att använda [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) metoden. [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) metoden returnerar en array av typ [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea). [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea) klassen ger en [ExternalFileName](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName) egenskap som returnerar namnet på den externa filen.

Följande kodsnutt visar hur man hämtar externa länkar.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
