---
title: Golang ve C++ ile Bağlantılı Şekillerin Değerlerini Güncelleyin
linktitle: Bağlı Şekillerin Değerlerini Yenile
type: docs
weight: 3200
url: /tr/go-cpp/refresh-values-of-linked-shapes/
description: Aspose.Cells for C++ kullanarak Excel dosyalarında bağlı şekillerin değerlerini nasıl yenileyeceğinizi öğrenin.
---

{{% alert color="primary" %}}

Excel dosyanızda bazı hücrelere bağlı şekilleriniz olabilir. Microsoft Excel'de bağlı hücrenin değerini değiştirerek bağlı şeklin değerini değiştirebilirsiniz. Eğer Aspose.Cells ile çalışıyorsanız ve çalışma kitabınızı XLS veya XLSX biçiminde kaydetmek istiyorsanız, bağlı şeklin değerini yenilemek için [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/) yöntemini çağırmanız gerekecektir.

{{% /alert %}}

## Örnek

Aşağıdaki ekran görüntüsü, aşağıdaki örnek kodda kullanılan kaynak Excel dosyasını gösterir. Bu dosyada A1 ile E4 hücreleri arasında bağlantılı bir resim vardır. Aspose.Cells ile B4 hücresinin değerini değiştirecek ve ardından [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/) metodunu çağırarak resmin değerini yenileyecek ve PDF formatında kaydedeceğiz.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Sağlanan bağlantılardan [ kaynak Excel dosyasını](95584291.xlsx) ve [çıktı PDF'sini](95584292.pdf) indirebilirsiniz.

### Bağlı şekillerin değerlerini yenilemek için C++ kodu

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshValuesOfLinkedShapes.go" >}}
