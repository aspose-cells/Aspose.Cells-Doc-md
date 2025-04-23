---
title: Ange standardfont medan du renderar kalkylblad till bilder
type: docs
weight: 360
url: /sv/python-net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

Använd egenskapen [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) för att ange standardfont medan du renderar kalkylblad till bilder. Denna egenskap kommer bara att vara effektiv när arbetsbokens standardfont inte kan rendera dina tecken. Den standardfont som anges med egenskapen [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) används för alla de celler som har ogiltiga eller obefintliga teckensnitt.

{{% /alert %}}

## Ange standardfont medan du renderar kalkylblad till bilder

Följande kodexempel skapar en arbetsbok, lägger till någon text i cell A4 på den första arbetsbladet och anger dess font till ogiltig eller icke-existerande font. Sedan tar den två bilder av arbetsbladet. Den första bilden tas genom att ange egenskapen [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) till *Courier New* och den andra bilden tas genom att ange egenskapen [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) till *Times New Roman*.

Detta är utdataavbildningen efter att ha satt egenskapen [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) till *Courier New*.

![todo:image_alt_text](1.png)

Detta är utmatningsbilden efter att ha ställt in egenskapen [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) till *Times New Roman*.

![todo:image_alt_text](2.png)

## Exempelkod

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}

