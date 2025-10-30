---
title: Golang ile C++ kullanarak Pivot Tablo daki DataField un Veri Görüntüleme Formatları ile çalışma
linktitle: Pivot Tablo daki DataField in Veri Görüntüleme Formatlarıyla çalışma
type: docs
weight: 140
url: /tr/go-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Aspose.Cells for C++ kullanarak Pivot Tablo da DataField in veri görüntüleme formatlarıyla nasıl çalışılacağını öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, DataField'ın tüm veri görüntüleme formatlarını destekler.

{{% /alert %}}

## **"Smallest to Largest Sıralama" ve "Largest to Smallest Sıralama" Görüntüleme Format Seçeneği**

Aspose.Cells, pivot alanları için görüntüleme formatı ayarını yapma imkanı sağlar. Bunun için API, [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/) özelliğini sunar. En büyükten en küçüğe sıralamak için [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/) özelliği [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/) değerine ayarlanabilir. Aşağıdaki kod parçası, görüntüleme formatı ayarlarını gösterir.

Örnek kaynak ve çıktı dosyalarını buradan indirebilir ve örnek kodu test etmek için kullanabilirsiniz:

[Kaynak Excel Dosyası](101089332.xlsx)

[Çıktı Excel Dosyası](101089333.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithDataDisplayFormatsOfDatafieldInPivotTable.go" >}}
