---
title: Bağlantılı Şekillerin Değerlerini Yenile
type: docs
weight: 3000
url: /tr/java/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

Bazen, Excel dosyanızda bazı hücrelere bağlı bağlantılı bir şekle sahip olursunuz. Microsoft Excel'de bağlantılı hücrenin değerini değiştirmek, bağlantılı şeklin değerini de değiştirir. Çalışma kitabınızı XLS veya XLSX biçiminde kaydetmek istiyorsanız bu, Aspose.Cells ile de iyi çalışır. Ancak, çalışma kitabınızı PDF veya HTML formatında kaydetmek istiyorsanız, aramanız gerekecektir.[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue()) bağlantılı şeklin değerini yenileme yöntemi.

{{% /alert %}}

## Örnek

 Aşağıdaki ekran görüntüsü, aşağıdaki örnek kodda kullanılan kaynak Excel dosyasını göstermektedir. Bağlantısı var**Resim 1** A1 hücresine bağlı. A1 hücresinin değerini Aspose.Cells ile değiştirip sonra çağıracağız.[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue() ) değerini yenileme yöntemi**Resim 1** ve PDF formatında kaydedin.

![yapılacaklar:resim_alternatif_Metin](refresh-values-of-linked-shapes_1.png)

indirebilirsiniz[kaynak Excel dosyası](5472956.xlsx) ve[çıktı PDF](5472955.pdf) verilen linklerden

### Bağlantılı şekillerin değerlerini yenilemek için Java kodu

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
