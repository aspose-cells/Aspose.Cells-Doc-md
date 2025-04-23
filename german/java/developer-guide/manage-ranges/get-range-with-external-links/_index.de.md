---
title: Bereich mit externen Links abrufen
type: docs
weight: 140
url: /de/java/get-range-with-external-links/
---

## **Bereich mit externen Links abrufen**

Oft greifen Excel-Dateien auf Daten aus anderen Excel-Dateien über externe Links zu. Aspose.Cells bietet die Möglichkeit, diese externen Links mithilfe der Methode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas-boolean-) abzurufen. Die Methode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas-boolean-) gibt ein Array des Typs [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) zurück. Die Klasse [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) bietet eine [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)-Eigenschaft, die den Namen der externen Datei zurückgibt. Die Klasse [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) exponiert die folgenden Elemente.

- [**EndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): Die Endspalte des Bereichs
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): Die Endzeile des Bereichs
- [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): Holen Sie den Namen der externen Datei, wenn dies ein externer Verweis ist.
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): Gibt an, ob dies ein Bereich ist.
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): Gibt an, ob dies ein externer Link ist.
- [**SheetName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): Gibt an, in welchem Blatt dieser Verweis steht.
- [**StartColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): Die Startspalte des Bereichs
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): Die Startzeile des Bereichs

Der folgende Beispielscode zeigt die Verwendung der Methode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas-boolean-) zum Abrufen von Bereichen mit externen Links.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
{{< app/cells/assistant language="java" >}}
