---
title: Konsolidasyon Fonksiyonu
type: docs
weight: 20
url: /tr/python-net/consolidation-function/
description: Aspose.Cells for Python via .NET ile Pivot Tablonun Veri Alanlarına Konsolidasyon İşlevi nasıl uygulanır.
keywords: ConsolidationFunction to Data Fields of Pivot Table.
---
##  **Konsolidasyon işlevi**

 Aspose.Cells for Python via .NET, ConsolidationFunction'ı pivot tablonun veri alanlarına (veya değer alanlarına) uygulamak için kullanılabilir. Microsoft Excel'de değer alanına sağ tıklayıp ardından öğesini seçebilirsiniz.**Değer Alanı Ayarları...** seçeneğini seçin ve ardından *Değerleri Şuna Göre Özetle** sekmesini seçin. Buradan, Toplam, Sayım, Ortalama, Maks, Min, Çarpım, Farklı Sayım vb. gibi seçtiğiniz herhangi bir Konsolidasyon İşlevini seçebilirsiniz.

 Aspose.Cells for Python via .NET sağlar[**Konsolidasyon Fonksiyonu**](https://reference.aspose.com/cells/python-net/aspose.cells/consolidationfunction/) Aşağıdaki birleştirme işlevlerini desteklemek için numaralandırma.

- KonsolidasyonFonksiyonu.ORTALAMA
- KonsolidasyonFonksiyonu.COUNT
- Konsolidasyonİşlevi.COUNT_NUMS
- KonsolidasyonFonksiyonu.DISTINCT_COUNT
- KonsolidasyonFunction.MAX
- KonsolidasyonFonksiyonu.MIN
- KonsolidasyonFonksiyonu.ÜRÜN
- KonsolidasyonFonksiyonu.STD_DEV
- KonsolidasyonFonksiyonu.STD_DEVP
- KonsolidasyonFunction.SUM
- KonsolidasyonFonksiyonu.VAR
- KonsolidasyonFonksiyonu.VARP

###  **Pivot Tablonun Veri Alanlarına Konsolidasyon Fonksiyonunu Uygulama**

 Aşağıdaki kod geçerlidir**AVERAGE** ilk veri alanına (veya değer alanına) birleştirme işlevi ve**DISTINCT_COUNT** ikinci veri alanına (veya değer alanına) birleştirme işlevi.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ConsolidationFunctions-1.py" >}}

{{% alert color="primary" %}}

DISTINCT_COUNT birleştirme işlevi yalnızca Microsoft Excel 2013 tarafından desteklenir.

{{% /alert %}}
