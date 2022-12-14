---
title: Aspose.Cells Varsayılan Hesaplama Motorunu genişletmek için Özel Hesaplama Motorunu uygulayın
type: docs
weight: 80
url: /tr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
## **Özel Hesaplama Motorunu Uygulayın**

Aspose.Cells, Microsoft Excel formüllerinin neredeyse tamamını hesaplayabilen güçlü bir hesaplama motoruna sahiptir. Buna rağmen, size daha fazla güç ve esneklik sağlayan varsayılan hesaplama motorunu genişletmenize de izin verir.

Bu özelliğin uygulanmasında aşağıdaki özellik ve sınıflar kullanılır.

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[Soyut Hesaplama Motoru](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[CalculationData](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

Aşağıdaki kod, Özel Hesaplama Motorunu uygular. Arayüzü uygular**[Soyut Hesaplama Motoru](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** olan bir**[Hesapla(CalculationData data)](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** yöntem. Bu yöntem, tüm formüllerinize karşı çağrılır. Bu yöntemin içinde,**toplam** formülünü kullanır ve değerini 30 artırır. Yani Aspose.Cells hesaplanan değer 20 ise özel motorumuz 30 ekleyerek 50 yapar.

### **Programlama Örneği**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Konsol Çıkışı**

İşte yukarıdaki örnek kodun konsol çıktısı.

{{< highlight "java" >}}

Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}

### **İlgili Makale**

{{% alert color="primary" %}}

[Bir çalışma sayfasına yazmadan özel işlevin doğrudan hesaplanması](/cells/tr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
