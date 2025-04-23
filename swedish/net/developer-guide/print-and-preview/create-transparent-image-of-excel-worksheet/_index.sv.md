---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /sv/net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Ibland behöver du generera bilden av ditt arbetsblad som en transparent bild. Du vill applicera transparens på alla celler som inte har fyllnadsfärger. Aspose.Cells tillhandahåller egenskapen [**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent) för att applicera transparens på arbetsbilden. När denna egenskap är **false**, då ritas celler utan fyllnadsfärger med vit färg och när den är **true**, ritas celler utan fyllnadsfärger transparent.

{{% /alert %}} 

I följande arbetsbladsbild har inte transparens tillämpats. Celler utan fyllfärger är ritade vita.

|**Utdata utan transparens: cellens bakgrund är vit**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

Medan i följande arbetsbladsbild har transparens tillämpats. Cellerna utan fyllfärger är transparenta.

|**Utdata med aktiverad transparens**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

Följande exempelkod genererar en transparent bild från ett Excel-ark.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
