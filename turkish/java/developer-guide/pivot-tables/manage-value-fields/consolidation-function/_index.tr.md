---
title: Konsolidasyon Fonksiyonu
type: docs
weight: 20
url: /tr/java/consolidation-function/
description: Pivot tablosundaki veri alanlarına KonsolidasyonFonksiyonu uygula
---

## **Konsolidasyon fonksiyonu**

Aspose.Cells, Pivot tablosunun veri alanlarına (veya değer alanlarına) KonsolidasyonFonksiyonu uygulamak için kullanılabilir. Microsoft Excel'de, değer alanına sağ tıkladıktan sonra **Değer Alanı Ayarları...** seçeneğini seçebilir ve ardından **Değerleri Nasıl Özetleyeceğinizi Seçin** sekmesini seçebilirsiniz. Oradan, Sum, Count, Average, Max, Min, Product, DistinctCount vb. gibi istediğiniz herhangi bir KonsolidasyonFonksiyonunu seçebilirsiniz.

Aspose.Cells, aşağıdaki konsolidasyon işlevlerini desteklemek için [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) numaralı sıralamayı sağlamaktadır.

- ConsolidationFunction.SUM
- ConsolidationFunction.COUNT
- ConsolidationFunction.AVERAGE
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP
- ConsolidationFunction.DISTINCT_COUNT

### **Döndürme Tablosunun Veri Alanlarına Konsolidasyon İşlevi Uygulama**

Aşağıdaki kod, ilk veri alanına (veya değer alanına) **ORTALAMA** konsolidasyon fonksiyonunu ve ikinci veri alanına (veya değer alanına) **STD_DEV** konsolidasyon fonksiyonunu uygular.

Örnek kaynak dosyası ve çıktı dosyaları test etmek için buradan indirilebilir:

[Kaynak Excel Dosyası](source.xlsx)

[Çıktı Excel Dosyası](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

Farklı Sayı Sayımı konsolidasyon işlevi sadece Microsoft Excel 2013 tarafından desteklenmektedir.

{{% /alert %}}

{{< app/cells/assistant language="java" >}}
