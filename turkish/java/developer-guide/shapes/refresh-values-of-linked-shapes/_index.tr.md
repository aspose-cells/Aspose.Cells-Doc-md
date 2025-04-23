---
title: Bağlı Şekillerin Değerlerini Yenile
type: docs
weight: 3000
url: /tr/java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Bazen Excel dosyanızda bağlantılı bir şekliniz vardır ve bu, bazı hücrelere bağlıdır. Microsoft Excel'de, bağlı hücrenin değerini değiştirmek aynı zamanda bağlı şeklin değerini değiştirir. Bu durum aynı şekilde Aspose.Cells ile de çalışır, eğer çalışma kitabınızı XLS veya XLSX biçiminde kaydetmek istiyorsanız. Bununla birlikte, çalışma kitabınızı PDF veya HTML biçiminde kaydetmek istiyorsanız, o zaman bağlı şeklin değerini yenilemek için [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) yöntemini çağırmanız gerekecektir.

{{% /alert %}}

## Örnek

Aşağıdaki ekran görüntüsü, örnek kodun kullanıldığı kaynak Excel dosyasını göstermektedir. A1 hücresine bağlı **Resim 1** adlı bir şekle sahiptir. A1 hücresinin değerini Aspose.Cells ile değiştirecek ve sonra [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) yöntemini kullanarak **Resim 1**'in değerini yenileyecek ve PDF biçiminde kaydedeceğiz.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

Verilen bağlantılardan [kaynak Excel dosyasını](5472956.xlsx) ve [çıktı PDF'sini](5472955.pdf) indirebilirsiniz.

### Bağlantılı şekillerin değerlerini yenilemek için Java kodu

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
{{< app/cells/assistant language="java" >}}
