---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 80
url: /sv/java/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Ibland behöver du generera bilden av ditt kalkylblad som en transparent bild. Du vill tillämpa transparens på alla celler som inte har fyllfärg. Aspose.Cells tillhandahåller egenskapen [**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) för att tillämpa transparens på kalkylbladsbilden. När denna egenskap är **falsk**, ritar den celler utan fyllfärger med vit färg och när den är **sann**, ritas celler utan fyllfärger transparent.

{{% /alert %}}

I följande arbetsbladsbild har inte transparens tillämpats. Celler utan fyllfärger är ritade vita.

**Kalkylbladsbild utan tillämpad transparens**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)

Medan i följande arbetsbladsbild har transparens tillämpats. Cellerna utan fyllfärger är transparenta.

**Kalkylbladsbild efter tillämpning av transparens**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)

Du kan använda följande exempelkod för att generera en transparent bild av ditt Excel-kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
{{< app/cells/assistant language="java" >}}
