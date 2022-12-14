---
title: Arbeta med bakgrund i ODS-filer
type: docs
weight: 170
url: /sv/java/working-with-background-in-ods-files/
---
## **Bakgrund i ODS-filer**

Bakgrund kan läggas till ark i ODS-filer. Bakgrunden kan antingen vara en färgbakgrund eller grafisk bakgrund. Bakgrunden är inte synlig när filen är öppen men om filen skrivs ut som PDF så syns bakgrunden i den genererade PDF-filen. Bakgrunden är också synlig i dialogrutan för förhandsgranskning.

Aspose.Cells ger möjlighet att läsa bakgrundsinformationen och lägga till bakgrund i ODS-filer.

## **Läs bakgrundsinformation från OSD-fil**

Aspose.Cells tillhandahåller[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)klass för att hantera bakgrunden i ODS-filer. Följande kodexempel visar användningen av[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)klass genom att ladda[källa ODS](GraphicBackground.ods)fil och läsa bakgrundsinformationen. Se konsolutgången som genereras av koden för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **Konsolutgång**

Bakgrundstyp: GRAFISK

Bakgrundsposition: CENTER_CENTER

## **Lägg till färgad bakgrund till ODS-filen**

Aspose.Cells tillhandahåller[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)klass för att hantera bakgrunden i ODS-filer. Följande kodexempel visar användningen av[**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color)egenskap för att lägga till en färgbakgrund till ODS-filen. Vänligen se[utgång ODS](ColoredBackground.ods)fil genererad av koden för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **Lägg till grafisk bakgrund till ODS-fil**

Aspose.Cells tillhandahåller[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)klass för att hantera bakgrunden i ODS-filer. Följande kodexempel visar användningen av[**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData)egenskap för att lägga till grafisk bakgrund till ODS-filen. Vänligen se[utgång ODS](GraphicBackground.ods)fil genererad av koden för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
