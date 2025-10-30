---
title: Bağlı Şekillerin Değerlerini Yenile
type: docs
weight: 3200
url: /tr/python-java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Excel dosyanızda bazı hücrelere bağlı şekilleriniz olabilir. Microsoft Excel'de bağlı hücrenin değerini değiştirerek bağlı şeklin değerini değiştirebilirsiniz. Eğer Aspose.Cells ile çalışıyorsanız ve çalışma kitabınızı XLS veya XLSX biçiminde kaydetmek istiyorsanız, bağlı şeklin değerini yenilemek için [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/python-java/asposecells.api/shapecollection#updateSelectedValue()) yöntemini çağırmanız gerekecektir.

{{% /alert %}}

## Örnek

Aşağıdaki ekran görüntüsü, örnek kodda kullanılan kaynak Excel dosyasını göstermektedir. A1'den E4'e kadar olan hücrelere bağlı bir resim içerir. Aspose.Cells ile B4 hücresinin değerini değiştirecek ve ardından [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/python-java/asposecells.api/shapecollection#updateSelectedValue()) yöntemini çağırarak resmin değerini yenileyip PDF biçiminde kaydedeceğiz.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Verilen linklerden [kaynak Excel dosyasını](sampleRefreshValueOfLinkedShapes.xlsx) ve [çıktı PDF'sini](95584292.pdf) indirebilirsiniz.

### Bağlı şekillerin değerlerini yenilemek için C# kodu

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-RefreshValueOfLinkedShapes-1.py" >}}
{{< app/cells/assistant language="csharp" >}}
