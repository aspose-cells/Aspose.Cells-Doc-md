---
title: Bereich mit externen Links abrufen
type: docs
weight: 120
url: /de/net/get-range-with-external-links/
---

## **Bereich mit externen Links abrufen**

Oft greifen Excel-Dateien auf Daten aus anderen Excel-Dateien über externe Links zu. Aspose.Cells bietet die Möglichkeit, diese externen Links abzurufen, indem die Methode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) verwendet wird. Die Methode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) gibt ein Array vom Typ [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) zurück. Die Klasse [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) bietet eine Eigenschaft [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename), die den Namen der externen Datei zurückgibt. Die Klasse [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) stellt die folgenden Elemente bereit.

- [**EndColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): Die Endspalte des Bereichs
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): Die Endzeile des Bereichs
- [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): Holen Sie den Namen der externen Datei, wenn dies ein externer Verweis ist.
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Gibt an, ob dies ein Bereich ist.
- [**IsExternalLink**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): Gibt an, ob dies ein externer Link ist.
- [**SheetName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Gibt an, in welchem Blatt dieser Verweis steht.
- [**StartColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): Die Startspalte des Bereichs
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): Die Startzeile des Bereichs

Der unten angegebene Code demonstriert die Verwendung der Methode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) zum Abrufen von Bereichen mit externen Links.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
