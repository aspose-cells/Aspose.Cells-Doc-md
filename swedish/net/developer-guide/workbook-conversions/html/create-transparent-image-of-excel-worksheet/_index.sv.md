---
title: Skapa en transparent bild av Excel-kalkylblad
type: docs
weight: 170
url: /sv/net/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

 Ibland måste du skapa bilden av ditt kalkylblad som en transparent bild. Du vill tillämpa genomskinlighet på alla celler som inte har några fyllningsfärger. Aspose.Cells tillhandahåller[**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent) egenskap för att tillämpa transparens på kalkylbladsbilden. När denna fastighet är**falsk** , sedan ritas celler utan fyllningsfärger med vit färg och när det är det**Sann**, celler utan fyllningsfärger ritas genomskinliga.

{{% /alert %}} 

I följande kalkylbladsbild har inte genomskinlighet tillämpats. Cellerna utan fyllningsfärger ritas vita.

|**Utdata utan genomskinlighet: cellbakgrunden är vit**|
|:- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

I följande kalkylbladsbild har genomskinlighet tillämpats. Cellerna utan fyllningsfärger är genomskinliga.

|**Utdata med öppenhet aktiverad**|
|:- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

Följande exempelkod genererar en transparent bild från ett Excel-kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
