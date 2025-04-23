---
title: Bağlı Şekillerin Değerlerini Yenile
type: docs
weight: 3200
url: /tr/net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Excel dosyanızda bazı hücrelere bağlı şekilleriniz olabilir. Microsoft Excel'de bağlı hücrenin değerini değiştirerek bağlı şeklin değerini değiştirebilirsiniz. Eğer Aspose.Cells ile çalışıyorsanız ve çalışma kitabınızı XLS veya XLSX biçiminde kaydetmek istiyorsanız, bağlı şeklin değerini yenilemek için [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) yöntemini çağırmanız gerekecektir.

{{% /alert %}}

## Örnek

Aşağıdaki ekran görüntüsü, örnek kodda kullanılan kaynak Excel dosyasını göstermektedir. A1'den E4'e kadar olan hücrelere bağlı bir resim içerir. Aspose.Cells ile B4 hücresinin değerini değiştirecek ve ardından [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) yöntemini çağırarak resmin değerini yenileyip PDF biçiminde kaydedeceğiz.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Verilen bağlantılardan [kaynak Excel dosyasını](95584291.xlsx) ve [çıktı PDF'sini](95584292.pdf) indirebilirsiniz.

### Bağlı şekillerin değerlerini yenilemek için C# kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-RefreshValueOfLinkedShapes-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
