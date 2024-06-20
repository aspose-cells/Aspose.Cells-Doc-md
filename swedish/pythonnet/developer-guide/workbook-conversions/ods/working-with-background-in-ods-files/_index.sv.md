---
title: Arbeta med bakgrund i ODS filer
type: docs
weight: 150
url: /sv/python-net/working-with-background-in-ods-files/
description: Hur man hanterar bakgrund i ODS filer med Aspose.Cells för Python via .NET API.
keywords: Python hantera bakgrund i ODS filer, Läs bakgrundsinformation från ODS fil Pyton via NET, Lägg till färgad bakgrund i ODS fil med Python via NET, Python via NET Lägg till grafisk bakgrund i ODS fil.
---

## **Bakgrund i ODS-filer**

Bakgrund kan läggas till i kalkylblad i ODS-filer. Bakgrunden kan antingen vara en färgad bakgrund eller en grafisk bakgrund. Bakgrunden är inte synlig när filen är öppen, men om filen skrivs ut som PDF är bakgrunden synlig i den genererade PDF:en. Bakgrunden är också synlig i utskriftsvisningen.

Aspose.Cells for Python via .NET ger möjlighet att läsa bakgrundsinformation och lägga till bakgrunden i ODS-filer.

## **Läs bakgrundsinformation från ODS-fil**

Aspose.Cells for Python via .NET tillhandahåller [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) klassen för att hantera bakgrund i ODS-filer. Följande kodexempel demonstrerar användningen av [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) klassen genom att ladda den [käll-ODS](90112030.ods) filen och läsa bakgrundsinformationen. Se konsoloutput genererad av koden för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ReadODSBackground-1.py" >}}

### **Konsoloutput**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Lägg till färgad bakgrund i ODS-fil**

Aspose.Cells for Python via .NET tillhandahåller [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) klassen för att hantera bakgrund i ODS-filer. Följande kodexempel demonstrerar användningen av [**OdsPageBackground.color**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/color/) egenskapen för att lägga till en färgbakgrund till ODS-filen. Se [utdata ODS](90112031.ods) fil genererad av koden för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSColoredBackground-1.py" >}}

## **Lägg till grafisk bakgrund i ODS-fil**

Aspose.Cells for Python via .NET tillhandahåller [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) klassen för att hantera bakgrund i ODS-filer. Följande kodexempel demonstrerar användningen av [**OdsPageBackground.graphic_data**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/graphic_data/) egenskapen för att lägga till grafikbakgrund till ODS-filen. Se [utdata ODS](90112030.ods) fil genererad av koden för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSGraphicBackground-1.py" >}}
