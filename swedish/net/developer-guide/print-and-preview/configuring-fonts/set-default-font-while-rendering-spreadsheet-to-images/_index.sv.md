---
title: Ange standardfont medan du renderar kalkylblad till bilder
type: docs
weight: 360
url: /sv/net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

Använd egenskapen [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) för att ange standardfont medan du renderar kalkylblad till bilder. Denna egenskap kommer bara att vara effektiv när arbetsbokens standardfont inte kan rendera dina tecken. Den standardfont som anges med egenskapen [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) används för alla de celler som har ogiltiga eller obefintliga teckensnitt.

{{% /alert %}}

## Ange standardfont medan du renderar kalkylblad till bilder

Följande kodexempel skapar en arbetsbok, lägger till någon text i cell A4 på den första arbetsbladet och anger dess font till ogiltig eller icke-existerande font. Sedan tar den två bilder av arbetsbladet. Den första bilden tas genom att ange egenskapen [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) till *Courier New* och den andra bilden tas genom att ange egenskapen [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) till *Times New Roman*.

Detta är utdataavbildningen efter att ha satt egenskapen [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) till *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Detta är utmatningsbilden efter att ha ställt in egenskapen [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) till *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Exempelkod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
