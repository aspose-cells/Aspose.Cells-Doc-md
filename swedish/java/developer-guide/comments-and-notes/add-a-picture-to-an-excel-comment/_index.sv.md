---
title: Lägg till en bild i en Excel-kommentar
type: docs
weight: 60
url: /sv/java/add-a-picture-to-an-excel-comment/
---
{{% alert color="primary" %}}

Microsoft Excel låter användare anpassa utseendet och känslan av kalkylblad i stor utsträckning. Det är till och med möjligt att lägga till bakgrundsbilder till kommentarer.

Kommentarer läggs till i celler för att spela in kommentarer, allt från detaljerna om hur en formel fungerar, var ett värde kommer ifrån eller frågor från granskare. Att lägga till en bakgrundsbild kan vara ett estetiskt val, eller användas för att stärka varumärket.

{{% /alert %}}

## Lägg till bild i Excel Kommentera med Microsoft Excel

Med Microsoft Excel 2007 är det möjligt att ha en bild som bakgrund till en cellkommentar. I Excel 2007 görs detta (förutsatt att kommentaren redan har lagts till) på detta sätt:

1. Högerklicka på cellen som innehåller kommentaren.
1.  Välja**Visa/dölj kommentarer** och ta bort all text från kommentaren.
1. Klicka på kommentarens kant för att välja den.
1.  Välja**Formatera** , då**Kommentar**.
1.  På fliken Färger och linjer klickar du på pilen för**Färg**.
1.  Klick**Fyllningseffekter**.
1.  Klicka på fliken Bild**Välj Bild**.
1. Leta upp och välj bilden
1.  Klick**OK**.

## Lägg till bild i Excel Kommentar med Aspose.Cells

Aspose.Cells tillhandahåller denna värdefulla funktion.

Exempelkoden nedan skapar en XLSX-fil från början och lägger till en kommentar med en bildbakgrund i cell A1.

Efter att ha kört koden har A1 en kommentar med en bakgrundsbild.

**Utdatafilen**

![todo:image_alt_text](add-a-picture-to-an-excel-comment_1.png)

## Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddPicturetoExcelComment-AddPicturetoExcelComment.java" >}}
