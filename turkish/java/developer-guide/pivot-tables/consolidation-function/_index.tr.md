---
title: Konsolidasyon Fonksiyonu
type: docs
weight: 20
url: /tr/java/consolidation-function/
description: Pivot tablonun veri alanlarına ConsolidationFunction uygulayın.
---
## **Konsolidasyon işlevi**

 Aspose.Cells, pivot tablonun veri alanlarına (veya değer alanlarına) ConsolidationFunction uygulamak için kullanılabilir. Microsoft Excel'de, değer alanına sağ tıklayıp ardından**Değer Alanı Ayarları...** seçeneği ve ardından sekmeyi seçin**Değerleri Şuna Göre Özetle**. Oradan, Toplam, Sayı, Ortalama, Maks, Min, Ürün, Ayrı Sayım vb. gibi istediğiniz herhangi bir BirleştirmeFonksiyonunu seçebilirsiniz.

 Aspose.Cells sağlar[**KonsolidasyonFonksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) aşağıdaki konsolidasyon işlevlerini desteklemek için numaralandırma.

- KonsolidasyonFonksiyonu.SUM
- Konsolidasyonİşlevi.COUNT
- KonsolidasyonFonksiyonu.ORTALAMA
- KonsolidasyonFonksiyonu.MAX
- KonsolidasyonFonksiyonu.MIN
- KonsolidasyonFonksiyonu.ÜRÜN
- Birleştirme İşlevi.COUNT_NUMS
- Konsolidasyon İşlevi.STD_DEV
- KonsolidasyonFonksiyonu.STD_DEVP
- KonsolidasyonFonksiyonu.VAR
- KonsolidasyonFonksiyonu.VARP
- Konsolidasyonİşlevi.DISTINCT_COUNT

### **Pivot Tablonun Veri Alanlarına ConsolidationFunction Uygulama**

 Aşağıdaki kod geçerlidir**ORTALAMA** ilk veri alanına (veya değer alanına) konsolidasyon işlevi ve**STD_DEV** ikinci veri alanına (veya değer alanına) konsolidasyon işlevi.

Örnek kodu test etmek için örnek kaynak dosyası ve çıktı dosyaları buradan indirilebilir:

[Kaynak Excel Dosyası](source.xlsx)

[Çıktı Excel Dosyası](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

DistinctCount konsolidasyon işlevi yalnızca Microsoft Excel 2013 tarafından desteklenir.

{{% /alert %}}

