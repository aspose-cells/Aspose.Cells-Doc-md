---
title: Holen Sie sich Reichweite mit externen Links
type: docs
weight: 140
url: /de/java/get-range-with-external-links/
---
## **Holen Sie sich Reichweite mit externen Links**

Häufig greifen Excel-Dateien über externe Links auf Daten aus anderen Excel-Dateien zu. Aspose.Cells bietet die Möglichkeit, diese externen Links abzurufen, indem Sie die verwenden[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) Methode. Das[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean))-Methode gibt ein Array vom Typ zurück[**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea). Das[**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)Klasse bietet eine[**ExternerDateiname**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)-Eigenschaft, die den Namen der externen Datei zurückgibt. Das[**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)Die Klasse macht die folgenden Member verfügbar.

- [**EndSpalte**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): Die Endspalte des Bereichs
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): Die Endreihe des Bereichs
- [**ExternerDateiname**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): Ruft den externen Dateinamen ab, wenn es sich um eine externe Referenz handelt
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): Gibt an, ob es sich um einen Bereich handelt
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): Gibt an, ob es sich um einen externen Link handelt
- [**Blattname**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): Gibt an, in welchem Blatt sich diese Referenz befindet
- [**StartSpalte**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): Die Startspalte des Bereichs
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): Die Startzeile des Bereichs

Der unten angegebene Beispielcode demonstriert die Verwendung von[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) Methode, um Bereiche mit externen Links zu erhalten.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
