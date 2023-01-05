---
title: Ställ in standardteckensnitt när du renderar kalkylblad till bilder
type: docs
weight: 360
url: /sv/net/set-default-font-while-rendering-spreadsheet-to-images/
---
{{% alert color="primary" %}}

 Vänligen använd[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) egenskap för att ställa in standardteckensnittet medan kalkylblad renderas till bilder. Den här egenskapen kommer bara att vara effektiv när standardteckensnittet i arbetsboken inte kunde återge dina tecken. Standardteckensnittet som anges med[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) egenskapen används för alla de celler som har ogiltiga eller obefintliga teckensnitt.

{{% /alert %}}

## Ställ in standardteckensnitt när du renderar kalkylblad till bilder

Följande exempelkod skapar en arbetsbok, lägger till lite text i cell A4 i det första kalkylbladet och ställer in dess teckensnitt på ogiltigt eller obefintligt teckensnitt. Sedan tar det två bilder av kalkylbladet. Den första bilden tas genom att ställa in[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) egendom till*Courier Ny* och den andra bilden tas genom att ställa in[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) egendom till*Times New Roman*.

 Detta är utdatabilden efter att ha ställt in[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) egendom till*Courier Ny*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

 Detta är utdatabilden efter att ha ställt in[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) egendom till*Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Exempelkod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
