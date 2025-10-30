---
title: Pivot Tablosundaki Veri Alanı nın Veri Görüntüleme Biçimleriyle Çalışma
type: docs
weight: 140
url: /tr/nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++, DataField'ın tüm veri gösterim formatlarını destekler.

{{% /alert %}}

## **"En Küçükten En Büyüğe Sırala" ve "En Büyükten En Küçüğe Sırala" görüntüleme formatı seçeneği**

Aspose.Cells, pivot alanları için görüntüleme biçimi seçeneğini ayarlamak için [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-) özelliğini sağlar. En büyükten en küçüğe sıralamak için [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-) özelliğini [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/nodejs-cpp/pivotfielddatadisplayformat/) olarak ayarlayabilirsiniz. Aşağıdaki kod örneği görüntüleme biçimi seçeneklerini ayarlamanın nasıl yapılacağını göstermektedir.

Örnek kaynak ve çıktı dosyalarını buradan indirebilir ve örnek kodu test etmek için kullanabilirsiniz:

[Kaynak Excel Dosyası](101089332.xlsx)

[Çıktı Excel Dosyası](101089333.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTableDataDisplayFormatRanking-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
