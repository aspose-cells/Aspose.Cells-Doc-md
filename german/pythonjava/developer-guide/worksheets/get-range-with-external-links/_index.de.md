---
title: Holen Sie sich Reichweite mit externen Links
type: docs
weight: 60
url: /de/python-java/get-range-with-external-links/
---
## **Holen Sie sich Reichweite mit externen Links**
Es gibt viele Fälle, in denen Excel-Dateien über externe Links auf Daten aus anderen Excel-Dateien zugreifen. Aspose.Cells für Python über Java bietet die Möglichkeit, diese externen Links abzurufen, indem Sie die verwenden[Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) Methode. Das[Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\))-Methode gibt ein Array vom Typ zurück[ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea). Das[ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea)Klasse bietet eine[ExternerDateiname](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName)-Eigenschaft, die den Namen der externen Datei zurückgibt.

Das folgende Code-Snippet zeigt, wie Sie externe Links erhalten.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
