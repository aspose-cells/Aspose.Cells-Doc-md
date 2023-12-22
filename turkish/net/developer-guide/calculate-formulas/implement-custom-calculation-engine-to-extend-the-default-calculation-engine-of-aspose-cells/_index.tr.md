---
title: Aspose.Cells Varsayılan Hesaplama Motorunu genişletmek için Özel Hesaplama Motorunu uygulayın
description: Bu makalede, Aspose.Cells kitaplığını kullanarak özel bir hesaplama motoru uygulayarak varsayılan hesaplama motorunun nasıl genişletileceği açıklanmaktadır. Mevcut bir Excel dosyasını yükleyerek veya yeni bir dosya oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanarak özel bir hesaplama motoru uygulayabilir ve sonuçları alabiliriz. Son olarak değiştirdiğimiz Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, Custom Calculation Engine, extends the default calculation engine
type: docs
weight: 80
url: /tr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
##  **Özel Hesaplama Motorunu Uygulama**

Aspose.Cells, Microsoft Excel formüllerinin neredeyse tamamını hesaplayabilen güçlü bir hesaplama motoruna sahiptir. Buna rağmen, size daha fazla güç ve esneklik sağlayan varsayılan hesaplama motorunu genişletmenize de olanak tanır.

Bu özelliğin uygulanmasında aşağıdaki özellik ve sınıflar kullanılır.

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[CalculationData](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

Aşağıdaki kod Özel Hesaplama Motorunu uygular. Arayüzü uygular**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** hangisi var**[Hesapla(CalculationData data)](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** yöntem. Bu yöntem tüm formüllerinize karşı çağrılır. Bu yöntemin içinde şunları yakalarız:**TODAY** işlevini kullanın ve sistem tarihine bir gün ekleyin. Dolayısıyla, geçerli tarih 27/07/2023 ise özel motor TODAY() işlevini 28/07/2023 olarak hesaplayacaktır.

###  **Programlama Örneği**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

###  **Sonuç**

Lütfen yukarıdaki örnek kodun konsol çıktısını kontrol edin; özel motorla A1'in değeri (tarih saat), özel motor olmadan sonuçtan bir gün sonra olmalıdır.

###  **İlgili Makale**

{{% alert color="primary" %}}

[Özel işlevin çalışma sayfasına yazmadan doğrudan hesaplanması](/cells/tr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
