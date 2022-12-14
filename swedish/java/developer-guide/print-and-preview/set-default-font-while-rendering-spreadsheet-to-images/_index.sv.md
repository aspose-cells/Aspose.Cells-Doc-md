---
title: Ställ in standardteckensnitt när du renderar kalkylblad till bilder
type: docs
weight: 840
url: /sv/java/set-default-font-while-rendering-spreadsheet-to-images/
---
{{% alert color="primary" %}} 

 Vänligen använd[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) egenskap för att ställa in standardteckensnittet medan kalkylblad renderas till bilder. Den här egenskapen kommer bara att vara effektiv när standardteckensnittet i arbetsboken inte kunde återge dina tecken. Standardteckensnittet som anges med[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)egenskapen används för alla de celler som har ogiltiga eller obefintliga teckensnitt.

{{% /alert %}} 
## **Ställ in standardteckensnitt när du renderar kalkylblad till bilder**
 Följande exempelkod skapar en arbetsbok, lägger till lite text i cell A4 i det första kalkylbladet och ställer in dess teckensnitt på ogiltigt eller obefintligt teckensnitt. Sedan tar det två bilder av kalkylbladet. Den första bilden tas genom att ställa in[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) egendom till*Courier Ny* och den andra bilden tas genom att ställa in[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) egendom till*Times New Roman*.

 Detta är utdatabilden efter att ha ställt in[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) egendom till*Courier Ny*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

 Detta är utdatabilden efter att ha ställt in[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) egendom till*Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
