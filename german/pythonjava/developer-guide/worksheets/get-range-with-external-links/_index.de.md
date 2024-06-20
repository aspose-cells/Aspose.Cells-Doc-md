---
title: Bereich mit externen Links abrufen
type: docs
weight: 60
url: /de/python-java/get-range-with-external-links/
---

## **Bereich mit externen Links abrufen**
Es gibt viele Fälle, in denen Excel-Dateien Daten aus anderen Excel-Dateien über externe Links abrufen. Aspose.Cells für Python via Java bietet die Möglichkeit, diese externen Links mithilfe der Methode [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) abzurufen. Die Methode [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) gibt ein Array vom Typ [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea) zurück. Die Klasse [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea) bietet eine Eigenschaft [ExternalFileName](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName), die den Namen der externen Datei zurückgibt.

Der folgende Codeausschnitt zeigt, wie externe Links abgerufen werden.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
