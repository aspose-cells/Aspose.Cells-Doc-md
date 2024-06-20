---
title: Aspose.Cells in Varsayılan Hesaplama Motorunu Genişletmek
description: Bu makale, Aspose.Cells kitaplığını kullanarak özel bir hesaplama motorunu uygulayarak varsayılan hesaplama motorunu genişletme sürecini açıklar. Varolan bir Excel dosyasını yükleyerek veya yeni bir tane oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanarak özel bir hesaplama motorunu uygulayabilir ve sonuçları alabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, Özel Hesaplama Motoru, varsayılan hesaplama motorunu genişletir
type: docs
weight: 80
url: /tr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Özel Hesaplama Motorunu Uygulama**

Aspose.Cells'in neredeyse tüm Microsoft Excel formüllerini hesaplayabilen güçlü bir hesaplama motoru bulunmaktadır. Bununla birlikte, varsayılan hesaplama motorunu genişletmenize olanak tanır ve size daha fazla güç ve esneklik sağlar.

Bu özellik uygulamada kullanılan özellik ve sınıflar.

- [**CalculationOptions.CustomEngine**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)

Aşağıdaki kod, Özel Hesaplama Motorunu uygular. Bu, bir [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) arayüzünü uygular ve içinde bir [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate) yöntemi bulunmaktadır. Bu yöntem, tüm formüllerinize karşı çağrılır. Bu yöntemin içinde **TODAY** işlevini yakalar ve sistem tarihine bir gün ekler. Dolayısıyla, mevcut tarih 27/07/2023 ise, özel motor, TODAY() işlemini 28/07/2023 olarak hesaplar.

### **Programlama Örneği**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Sonuç**

Lütfen yukarıdaki örnek kodun konsol çıktısını kontrol edin, özel motor ile A1'in değeri (tarih saati) motor olmadan sonuçtan bir gün sonraki olmalıdır.

### **İlgili Makale**

{{% alert color="primary" %}}

Çalışma sayfasına yazmadan özel işlevi doğrudan hesaplama

{{% /alert %}}
