---
title: Golang ile C++ aracılığıyla Konsolidasyon Fonksiyonu
linktitle: Konsolidasyon Fonksiyonu
type: docs
weight: 20
url: /tr/go-cpp/consolidation-function/
description: Aspose.Cells kullanarak Golang ile C++ aracılığıyla Pivot Tablo uygulama ve Pivot Grafikler oluşturmayı öğrenin.
---

## **Konsolidasyon fonksiyonu**

Aspose.Cells, Pivot tablosunun veri alanlarına (veya değer alanlarına) KonsolidasyonFonksiyonu uygulamak için kullanılabilir. Microsoft Excel'de, değer alanına sağ tıkladıktan sonra **Değer Alanı Ayarları...** seçeneğini seçebilir ve ardından **Değerleri Nasıl Özetleyeceğinizi Seçin** sekmesini seçebilirsiniz. Oradan, Sum, Count, Average, Max, Min, Product, DistinctCount vb. gibi istediğiniz herhangi bir KonsolidasyonFonksiyonunu seçebilirsiniz.

Aspose.Cells, aşağıdaki konsolidasyon işlevlerini desteklemek için [**ConsolidationFunction**](https://reference.aspose.com/cells/go-cpp/consolidationfunction/) numaralı sıralamayı sağlamaktadır.

- ConsolidationFunction::Ortalama
- ConsolidationFunction::Say
- ConsolidationFunction::SayNumaraları
- ConsolidationFunction::FarklıSayım
- ConsolidationFunction::Maksimum
- ConsolidationFunction::Minimum
- ConsolidationFunction::Çarpım
- ConsolidationFunction::StdSapma
- ConsolidationFunction::StdSapp
- ConsolidationFunction::Toplam
- ConsolidationFunction::Varyans
- ConsolidationFunction::Varyansp

### **Döndürme Tablosunun Veri Alanlarına Konsolidasyon İşlevi Uygulama**

Aşağıdaki kod **Ortalama** konsolidasyon fonksiyonunu birinci veri alanına (veya değer alanına) ve ikinci veri alanına (veya değer alanına) **FarklıSayıyıSay** konsolidasyon fonksiyonunu uygular.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConsolidationFunction.go" >}}
{{% alert color="primary" %}}

Farklı Sayı Sayımı konsolidasyon işlevi sadece Microsoft Excel 2013 tarafından desteklenmektedir.

{{% /alert %}}
