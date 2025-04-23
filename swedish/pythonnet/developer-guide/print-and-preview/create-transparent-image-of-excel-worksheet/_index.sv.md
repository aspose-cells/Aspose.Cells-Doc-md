---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /sv/python-net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Ibland behöver du generera en transparent bild av ditt arbetsblad. Du vill tillämpa transparens på alla celler som inte har fyllfärger. Aspose.Cells för Python via .NET erbjuder egenskapen [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent) för att tillämpa transparens på arbetsbladets bild. När denna egenskap är **false**, ritas celler utan fyllfärg i vitt. När den är **true**, renderas cellerna utan fyllfärg som transparenta.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-CreateTransparentImage-1.py" >}}

