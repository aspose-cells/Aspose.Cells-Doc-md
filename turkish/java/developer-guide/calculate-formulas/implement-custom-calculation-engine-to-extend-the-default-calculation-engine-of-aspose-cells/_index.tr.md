---
title: Aspose.Cells Varsayılan Hesaplama Motorunu genişletmek için Özel Hesaplama Motorunu uygulayın
type: docs
weight: 590
url: /tr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells, Microsoft Excel formüllerinin neredeyse tamamını hesaplayabilen güçlü bir hesaplama motoruna sahiptir. Buna rağmen, size daha fazla güç ve esneklik sağlayan varsayılan hesaplama motorunu genişletmenize de olanak tanır.

Bu özelliğin uygulanmasında aşağıdaki özellik ve sınıflar kullanılır.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [ÖzetHesaplamaMotoru](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [HesaplamaVerileri](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
##  **Özel Hesaplama Motorunu Uygulama**
Aşağıdaki kod Özel Hesaplama Motorunu uygular. Arayüzü uygular[ÖzetHesaplamaMotoru](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) tek bir yöntemi olan[calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Bu yöntem tüm formüllerinize karşı çağrılır. Bu yöntemin içinde şunları yakalarız:**TODAY** işlevini kullanın ve sistem tarihine bir gün ekleyin. Dolayısıyla, geçerli tarih 27/07/2023 ise özel motor TODAY() işlevini 28/07/2023 olarak hesaplayacaktır.

###  **Programlama Örneği**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

###  **Sonuç**

Lütfen yukarıdaki örnek kodun konsol çıktısını kontrol edin; özel motorla A1'in değeri (tarih saat), özel motor olmadan sonuçtan bir gün sonra olmalıdır.

###  **İlgili Makale**
{{% alert color="primary" %}} 

- [Özel işlevin çalışma sayfasına yazmadan doğrudan hesaplanması](/cells/tr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
