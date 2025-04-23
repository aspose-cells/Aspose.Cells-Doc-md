---
title: Aspose.Cells in Varsayılan Hesaplama Motorunu Genişletmek
type: docs
weight: 590
url: /tr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells'in neredeyse tüm Microsoft Excel formüllerini hesaplayabilen güçlü bir hesaplama motoru bulunmaktadır. Bununla birlikte, varsayılan hesaplama motorunu genişletmenize olanak tanır ve size daha fazla güç ve esneklik sağlar.

Bu özellik uygulamada kullanılan özellik ve sınıflar.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [CalculationData](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **Özel Hesaplama Motorunu Uygulama**
Aşağıdaki kod, Özelleştirilmiş Hesaplama Motorunu uygular. Sadece bir yöntemi olan [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) arayüzünü uygular, bu metod [calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate-com.aspose.cells.CalculationData-)dır. Bu yöntem, formüllerinizin tümüne karşı çağrılır. Bu yöntem içinde, **BUGÜN** (TODAY) fonksiyonunu yakalıyor ve sistem tarihine bir gün ekliyoruz. Yani, şu anki tarih 27/07/2023 ise, özel motor BUGÜN() fonksiyonunu 28/07/2023 olarak hesaplar.

### **Programlama Örneği**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

### **Sonuç**

Lütfen yukarıdaki örnek kodun konsol çıktısını kontrol edin, özel motor ile A1'in değeri (tarih saati) motor olmadan sonuçtan bir gün sonraki olmalıdır.

### **İlgili Makale**
{{% alert color="primary" %}} 

- [Özel işlevin çalışma tablosuna yazılmadan doğrudan hesaplanması](/cells/tr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
