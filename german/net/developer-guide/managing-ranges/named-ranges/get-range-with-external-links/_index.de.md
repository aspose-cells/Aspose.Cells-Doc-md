---
title: Holen Sie sich Reichweite mit externen Links
type: docs
weight: 120
url: /de/net/get-range-with-external-links/
---
## **Holen Sie sich Reichweite mit externen Links**

Häufig greifen Excel-Dateien über externe Links auf Daten aus anderen Excel-Dateien zu. Aspose.Cells bietet die Möglichkeit, diese externen Links abzurufen, indem Sie die verwenden[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)Methode. Das[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)Die Methode gibt ein Array des Typs zurück[**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea). Das[**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) Klasse bietet eine[**ExternerDateiname**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)-Eigenschaft, die den Namen der externen Datei zurückgibt. Das[**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea)Die Klasse macht die folgenden Member verfügbar.

- [**EndSpalte**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): Die Endspalte des Bereichs
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): Die Endreihe des Bereichs
- [**ExternerDateiname**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): Ruft den externen Dateinamen ab, wenn es sich um eine externe Referenz handelt
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Gibt an, ob es sich um einen Bereich handelt
- [**IsExternalLink**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): Gibt an, ob es sich um einen externen Link handelt
- [**Blattname**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Gibt an, in welchem Blatt sich diese Referenz befindet
- [**StartSpalte**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): Die Startspalte des Bereichs
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): Die Startzeile des Bereichs

 Der unten angegebene Beispielcode demonstriert die Verwendung von[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)Methode zum Abrufen von Bereichen mit externen Links.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
