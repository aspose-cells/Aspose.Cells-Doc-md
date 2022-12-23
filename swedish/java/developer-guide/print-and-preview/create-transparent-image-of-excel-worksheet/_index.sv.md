---
title: Skapa transparent bild av Excel-kalkylblad
type: docs
weight: 80
url: /sv/java/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

 Ibland måste du skapa bilden av ditt kalkylblad som en transparent bild. Du vill tillämpa genomskinlighet på alla celler som inte har några fyllningsfärger. Aspose.Cells tillhandahåller[**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) egenskap för att tillämpa transparens på kalkylbladsbilden. När denna fastighet är**falsk** , sedan ritas celler utan fyllningsfärger med vit färg och när det är det**Sann**, celler utan fyllningsfärger ritas genomskinliga.

{{% /alert %}}

I följande kalkylbladsbild har inte genomskinlighet tillämpats. Cellerna utan fyllningsfärger ritas vita.

**Kalkylbladsbild utan att tillämpa transparens**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)

I följande kalkylbladsbild har genomskinlighet tillämpats. Cellerna utan fyllningsfärger är genomskinliga.

**Kalkylbladsbild efter applicering av genomskinlighet**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)

Du kan använda följande exempelkod för att skapa en transparent bild av ditt Excel-kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
