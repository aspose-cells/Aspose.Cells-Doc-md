---
title: Använda bild som texture i en form
type: docs
weight: 1700
url: /sv/net/tile-picture-as-a-texture-inside-the-shape/
---

## **Möjliga användningsscenario**

När bilden är liten och täcker inte hela ytan av formen utan att förlora kvalitet, har du möjlighet att använda den som texture. Texturen fyller formens yta med en liten bild genom att upprepa dem som om de är kakel.

## **Använda bild som texture i en form**

Du kan fylla formytan med någon bild och kachelera den med [**Shape.Fill.TextureFill.IsTiling**](https://reference.aspose.com/cells/net/aspose.cells.drawing/texturefill/properties/istiling) egenskapen och ställa in den som **true**. Se följande exempelkod, dess [exempel-Excelfil](46465050.xlsx) samt skärmbilden för referens.

## **Skärmdump**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-TilePictureAsTextureInsideShape.cs" >}}
