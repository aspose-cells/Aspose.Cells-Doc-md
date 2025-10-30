---
title: Golang ile C++ kullanarak Aspose.Cells’in Varsayılan Hesaplama Motorunu genişletmek için Özel Hesaplama Motoru uygulama
linktitle: Özel Hesaplama Motoru Uygula
description: Bu makale, Golang ile C++ kullanarak Aspose.Cells kütüphanesi ile özel bir hesaplama motoru uygulayarak varsayılan hesaplama motorunu genişletmenin nasıl yapıldığını anlatmaktadır. Var olan bir Excel dosyasını yükleyerek veya yeni bir tane oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanarak özel bir hesaplama motoru uygulayabilir ve sonuçları alabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, Özel Hesaplama Motoru, varsayılan hesaplama motorunu genişletir, C++
type: docs
weight: 80
url: /tr/go-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Özel Hesaplama Motorunu Uygulama**

Aspose.Cells'in neredeyse tüm Microsoft Excel formüllerini hesaplayabilen güçlü bir hesaplama motoru bulunmaktadır. Bununla birlikte, varsayılan hesaplama motorunu genişletmenize olanak tanır ve size daha fazla güç ve esneklik sağlar.

Bu özellik uygulamada kullanılan özellik ve sınıflar.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/go-cpp/calculationdata/)

Aşağıdaki kod, Özel Hesaplama Motorunu uygular. Bu, bir [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) arayüzünü uygular ve içinde bir [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/) yöntemi bulunmaktadır. Bu yöntem, tüm formüllerinize karşı çağrılır. Bu yöntemin içinde **TODAY** işlevini yakalar ve sistem tarihine bir gün ekler. Dolayısıyla, mevcut tarih 27/07/2023 ise, özel motor, TODAY() işlemini 28/07/2023 olarak hesaplar.

### **Programlama Örneği**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCustomCalculationEngineToExtendTheDefaultCalculationEngineOfAsposeCells.go" >}}
### **Sonuç**

Lütfen yukarıdaki örnek kodun konsol çıktısını kontrol edin, özel motor ile A1'in değeri (tarih saati) motor olmadan sonuçtan bir gün sonraki olmalıdır.

### **İlgili Makale**

{{% alert color="primary" %}}

[Özel fonksiyonun worksheet'e yazmadan doğrudan hesaplanması](/cells/tr/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
