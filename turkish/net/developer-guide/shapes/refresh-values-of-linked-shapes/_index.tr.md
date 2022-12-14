---
title: Bağlantılı Şekillerin Değerlerini Yenile
type: docs
weight: 3200
url: /tr/net/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

Bazen, Excel dosyanızda bazı hücrelere bağlı bağlantılı bir şekle sahip olursunuz. Microsoft Excel'de bağlantılı hücrenin değerini değiştirmek, bağlantılı şeklin değerini de değiştirir. Çalışma kitabınızı XLS veya XLSX biçiminde kaydetmek istiyorsanız bu, Aspose.Cells ile de iyi çalışır. Ancak, çalışma kitabınızı PDF veya HTML formatında kaydetmek istiyorsanız, aramanız gerekecektir.[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) bağlantılı şeklin değerini yenileme yöntemi.

{{% /alert %}}

## Örnek

 Aşağıdaki ekran görüntüsü, aşağıdaki örnek kodda kullanılan kaynak Excel dosyasını göstermektedir. A1 ila E4 hücrelerine bağlı bağlantılı bir resme sahiptir. B4 hücresinin değerini Aspose.Cells ile değiştirip sonra çağıracağız.[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)resmin değerini yenileme ve PDF formatında kaydetme yöntemi.

![yapılacaklar:resim_alternatif_Metin](refresh-values-of-linked-shapes_1.jpg)

indirebilirsiniz[kaynak Excel dosyası](95584291.xlsx) ve[çıktı PDF](95584292.pdf) verilen linklerden

### Bağlantılı şekillerin değerlerini yenilemek için C# kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-RefreshValueOfLinkedShapes-1.cs" >}}
