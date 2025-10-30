---
title: Bağlı Şekillerin Değerlerini Yenile
type: docs
weight: 3200
url: /tr/python-net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Bazen, Excel dosyanızda bir bağlı şekil bulunur ve bu şekil, bazı hücrelere bağlıdır. Microsoft Excel'de, bağlı hücrenin değeri değiştiğinde, bağlı şeklin değeri de değişir. Bu, Aspose.Cells for Python via .NET ile de sorunsuz çalışır; eğer çalışma kitabınızı XLS veya XLSX formatında kaydetmek istiyorsanız. Ancak, çalışma kitabınızı PDF veya HTML formatında kaydetmek istiyorsanız, bağlı şeklin değerini yenilemek için [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) metodunu çağırmanız gerekir.

{{% /alert %}}

## Örnek

Aşağıdaki ekran görüntüsü, aşağıdaki örnek kodda kullanılan kaynak Excel dosyasını gösterir. Bağlantılı bir resim içerir ve A1 ile E4 hücrelerine bağlıdır. Aspose.Cells for Python via .NET kullanarak B4 hücresinin değerini değiştirecek ve ardından [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) yöntemini çağırarak resmin değerini yenileyecek ve PDF formatında kaydedeceğiz.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Verilen bağlantılardan [kaynak Excel dosyasını](95584291.xlsx) ve [çıktı PDF'sini](95584292.pdf) indirebilirsiniz.

### Bağlı şekillerin değerlerini yenilemek için C# kodu

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-RefreshValueOfLinkedShapes-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
