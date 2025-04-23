---
title: Ange standardfont medan du renderar kalkylblad till bilder
type: docs
weight: 840
url: /sv/java/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}} 

Använd [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)-egenskapen för att ange standardtypsnittet vid rendering av kalkylblad till bilder. Denna egenskap är endast effektiv när arbetsbokens standardtypsnitt inte kan rendera dina tecken. Det standardtypsnitt som anges med [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)-egenskapen används för alla de celler som har ogiltiga eller inte existerande typsnitt.

{{% /alert %}} 
## **Ange standardtypsnitt vid rendering av kalkylark till bilder**
Det följande exempelkod skapar en arbetsbok, lägger till lite text i cell A4 i det första kalkylbladet och anger dess typsnitt till ogiltigt eller icke-existerande typsnitt. Därefter tas två bilder på kalkylbladet. Den första bilden tas genom att ange [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)-egenskapen till *Courier New* och den andra bilden tas genom att ange [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)-egenskapen till *Times New Roman*.

Detta är resultatbilden efter att [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)-egenskapen har ställts till *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Detta är resultatbilden efter att [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)-egenskapen har ställts till *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
{{< app/cells/assistant language="java" >}}
