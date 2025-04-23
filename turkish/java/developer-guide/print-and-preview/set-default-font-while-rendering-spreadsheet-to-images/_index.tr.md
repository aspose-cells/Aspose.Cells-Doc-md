---
title: Yaygın Olarak Kullanılan Yazı tipini Resimlere Dönüştürürken Belirleme
type: docs
weight: 840
url: /tr/java/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}} 

[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) özelliğini kullanarak, çalışsayısını resme dönüştürürken varsayılan yazı tipini belirlemek için lütfen [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) özelliğini kullanın. Bu özellik, çalışma kitabının varsayılan yazı tipi karakterleri render edemezse yalnızca bu özelliğe göre belirtilen varsayılan yazı tipini kullanacaktır.

{{% /alert %}} 
## **Yaygın Olarak Kullanılan Yazı tipini Resimlere Dönüştürürken Belirleme**
Aşağıdaki örnek kod, bir çalışma kitabı oluşturur, ilk çalışsayının A4 hücresine metin ekler ve yazı tipini geçersiz veya mevcut olmayan bir yazı tipine ayarlar. Ardından çalışsayısının iki resmini alır. İlk resmi [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) özelliğini *Courier New* olarak ayarlayarak alır ve ikinci resmi [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) özelliğini *Times New Roman* olarak ayarlayarak alır.

[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) özelliğini *Courier New* olarak ayarladıktan sonraki çıktı resmi.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Bu, [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) özelliğini *Times New Roman* olarak ayarladıktan sonra çıktı görüntüsüdür.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
{{< app/cells/assistant language="java" >}}
