---
title: Använda bild som texture i en form
type: docs
weight: 1700
url: /sv/python-net/tile-picture-as-a-texture-inside-the-shape/
---

## **Möjliga användningsscenario**

När bilden är liten och täcker inte hela ytan av formen utan att förlora kvalitet, har du möjlighet att använda den som texture. Texturen fyller formens yta med en liten bild genom att upprepa dem som om de är kakel.

## **Använda bild som texture i en form**

Du kan fylla formytan med någon bild och kachelera den med [**Shape.fill.texture_fill.is_tiling**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/texturefill/is_tiling) egenskapen och ställa in den som **true**. Se följande exempelkod, dess [exempel-Excelfil](46465050.xlsx) samt skärmbilden för referens.

## **Skärmdump**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Options-TilePictureAsTextureInsideShape.py" >}}
