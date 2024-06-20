---
title: Arbeta med bakgrund i ODS filer
type: docs
weight: 150
url: /sv/net/working-with-background-in-ods-files/
---

## **Bakgrund i ODS-filer**

Bakgrund kan läggas till i kalkylblad i ODS-filer. Bakgrunden kan antingen vara en färgad bakgrund eller en grafisk bakgrund. Bakgrunden är inte synlig när filen är öppen, men om filen skrivs ut som PDF är bakgrunden synlig i den genererade PDF:en. Bakgrunden är också synlig i utskriftsvisningen.

Aspose.Cells ger möjlighet att läsa bakgrundsinformation och lägga till bakgrunden i ODS-filer.

## **Läs bakgrundsinformation från ODS-fil**

Aspose.Cells tillhandahåller [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) klass för att hantera bakgrund i ODS-filer. Följande kodprov demonstrerar användningen av [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) klass genom att ladda in [käll-ODS](90112030.ods)-filen och läsa bakgrundsinformationen. Se konsoloutputen som genereras av koden som referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadODSBackground-1.cs" >}}

### **Konsoloutput**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Lägg till färgad bakgrund i ODS-fil**

Aspose.Cells tillhandahåller [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) klass för att hantera bakgrund i ODS-filer. Följande kodprov demonstrerar användningen av [**OdsPageBackground.Color**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/color) egenskap för att lägga till en färgbakgrund till ODS-filen. Se den [genererade ODS-filen](90112031.ods) som referens skapad av koden.

### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSColoredBackground-1.cs" >}}

## **Lägg till grafisk bakgrund i ODS-fil**

Aspose.Cells tillhandahåller [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) klass för att hantera bakgrund i ODS-filer. Följande kodprov demonstrerar användningen av [**OdsPageBackground.GraphicData**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/graphicdata) egenskap för att lägga till en grafisk bakgrund till ODS-filen. Se den [genererade ODS-filen](90112030.ods) som referens skapad av koden.

### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSGraphicBackground-1.cs" >}}
