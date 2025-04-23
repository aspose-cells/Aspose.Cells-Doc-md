---
title: Arbeta med bakgrund i ODS filer
type: docs
weight: 170
url: /sv/java/working-with-background-in-ods-files/
---

## **Bakgrund i ODS-filer**

Bakgrund kan läggas till på ark i ODS-filer. Bakgrunden kan vara antingen en färgbakgrund eller grafisk bakgrund. Bakgrunden syns inte när filen är öppen men om filen skrivs ut som PDF syns bakgrunden i den genererade PDF:en. Bakgrunden syns också i utskrift förhandsgranskningsdialog.

Aspose.Cells tillhandahåller möjligheten att läsa bakgrundsinformationen och lägga till bakgrund i ODS-filer.

## **Läs bakgrundsinformation från OSD-fil**

Aspose.Cells tillhandahåller klassen [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) för att hantera bakgrund i ODS-filer. Följande kodexempel visar användningen av klassen [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) genom att ladda in [källa ODS](GraphicBackground.ods)-filen och läsa bakgrundsinformationen. Se konsoloutputen som genereras av koden för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **Konsoloutput**

{{< highlight java >}}

Background Type: GRAPHIC

Backgorund Position: CENTER_CENTER

{{< /highlight >}}

## **Lägg till färgad bakgrund i ODS-fil**

Aspose.Cells tillhandahåller klassen [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) för att hantera bakgrund i ODS-filer. Följande kodexempel visar användningen av egenskapen [**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color) för att lägga till en färgbakgrund till ODS-filen. Se den [genererade ODS-filen](ColoredBackground.ods) som skapas av koden för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **Lägg till grafisk bakgrund i ODS-fil**

Aspose.Cells tillhandahåller klassen [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) för att hantera bakgrund i ODS-filer. Följande kodexempel visar användningen av egenskapen [**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData) för att lägga till grafisk bakgrund i ODS-filen. Se den [genererade ODS-filen](GraphicBackground.ods) som skapas av koden för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
{{< app/cells/assistant language="java" >}}
