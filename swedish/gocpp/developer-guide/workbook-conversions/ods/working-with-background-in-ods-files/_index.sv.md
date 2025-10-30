---
title: Arbeta med bakgrund i ODS filer med Golang via C++
linktitle: Arbeta med bakgrund i ODS filer
type: docs
weight: 150
url: /sv/go-cpp/working-with-background-in-ods-files/
description: Lär dig att hantera färgade och grafiska bakgrunder i ODS filer med Aspose.Cells och Golang via C++
---

## **Bakgrund i ODS-filer**

Bakgrund kan läggas till i kalkylblad i ODS-filer. Bakgrunden kan antingen vara en färgad bakgrund eller en grafisk bakgrund. Bakgrunden är inte synlig när filen är öppen, men om filen skrivs ut som PDF är bakgrunden synlig i den genererade PDF:en. Bakgrunden är också synlig i utskriftsvisningen.

Aspose.Cells ger möjlighet att läsa bakgrundsinformation och lägga till bakgrunden i ODS-filer.

## **Läs bakgrundsinformation från ODS-fil**

Aspose.Cells tillhandahåller klassen [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) för att hantera bakgrund i ODS-filer. Följande kodexempel visar användningen av [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) klassen genom att ladda [käll-ODS](90112030.ods) filen och läsa bakgrundsinformationen. Se den genererade Konsolutdata för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles.go" >}}
### **Konsoloutput**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Lägg till färgad bakgrund i ODS-fil**

Aspose.Cells tillhandahåller klassen [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) för att hantera bakgrund i ODS-filer. Följande kodexempel visar användningen av [**OdsPageBackground.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/) egenskapen för att lägga till en färgbakgrund till ODS-filen. Se den genererade [output ODS](90112031.ods) filen för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-1.go" >}}
## **Lägg till grafisk bakgrund i ODS-fil**

Aspose.Cells tillhandahåller klassen [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) för att hantera bakgrund i ODS-filer. Följande kodexempel visar användningen av [**OdsPageBackground.GetGraphicData()**](https://reference.aspose.com/cells/go-cpp/odspagebackground/getgraphicdata/) egenskapen för att lägga till grafisk bakgrund till ODS-filen. Se den genererade [output ODS](90112030.ods) filen för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-2.go" >}}
