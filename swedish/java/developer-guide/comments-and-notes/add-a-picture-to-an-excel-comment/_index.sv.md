---
title: Lägg till en bild i en Excel kommentar
type: docs
weight: 60
url: /sv/java/add-a-picture-to-an-excel-comment/
---

{{% alert color="primary" %}}

Microsoft Excel låter användarna anpassa utseendet på kalkylblad i stor utsträckning. Det är även möjligt att lägga till bakgrundsbilder i kommentarer.

Kommentarer läggs till i celler för att spela in kommentarer, allt från detaljer om hur en formel fungerar, varifrån ett värde kommer eller frågor från granskare. Att lägga till en bakgrundsbild kan vara ett estetiskt val, eller användas för att förstärka varumärket.

{{% /alert %}}

## Lägg till bild i Excel-kommentar med Microsoft Excel

Med Microsoft Excel 2007 är det möjligt att ha en bild som bakgrund till en cellkommentar. I Excel 2007 görs detta (förutsatt att kommentaren redan har lagts till) på följande sätt:

1. Högerklicka på cellen som innehåller kommentaren.
1. Välj **Visa/dölj kommentarer** och rensa eventuell text från kommentaren.
1. Klicka på kommentarens kant för att markera den.
1. Välj **Format**, sedan **Kommentar**.
1. På fliken Färger och linjer klickar du på pilen för **Färg**.
1. Klicka på **Fyllnings effekter**.
1. På fliken Bild klickar du på **Välj bild**.
1. Hitta och markera bilden
1. Klicka på **OK**.

## Lägg till bild i Excel-kommentar med Aspose.Cells

Aspose.Cells tillhandahåller denna värdefulla funktion.

Provkoden nedan skapar en XLSX-fil från grunden och lägger till en kommentar med en bild som bakgrund till cellen A1.

Efter att ha kört koden har A1 en kommentar med en bakgrundsbild.

**Utgångsfilen**

![todo:image_alt_text](add-a-picture-to-an-excel-comment_1.png)

## Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddPicturetoExcelComment-AddPicturetoExcelComment.java" >}}
{{< app/cells/assistant language="java" >}}
