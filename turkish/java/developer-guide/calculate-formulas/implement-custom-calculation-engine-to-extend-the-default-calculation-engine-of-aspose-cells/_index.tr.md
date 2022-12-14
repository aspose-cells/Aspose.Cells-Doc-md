---
title: Aspose.Cells Varsayılan Hesaplama Motorunu genişletmek için Özel Hesaplama Motorunu uygulayın
type: docs
weight: 590
url: /tr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells, Microsoft Excel formüllerinin neredeyse tamamını hesaplayabilen güçlü bir hesaplama motoruna sahiptir. Buna rağmen, size daha fazla güç ve esneklik sağlayan varsayılan hesaplama motorunu genişletmenize de izin verir.

Bu özelliğin uygulanmasında aşağıdaki özellik ve sınıflar kullanılır.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [SoyutHesaplamaMotoru](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [Hesaplama Verileri](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **Özel Hesaplama Motorunu Uygulayın**
Aşağıdaki kod, Özel Hesaplama Motorunu uygular. Arayüzü uygular[SoyutHesaplamaMotoru](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) tek bir yöntemi olan[hesapla(HesaplamaVeri verileri)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Bu yöntem, tüm formüllerinize karşı çağrılır. Bu yöntemin içinde,**TOPLAM** formülünü kullanır ve değerini 30 artırır. Yani Aspose.Cells hesaplanan değer 20 ise özel motorumuz 30 ekleyerek 50 yapar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}
## **Konsol Çıkışı**
İşte yukarıdaki örnek kodun konsol çıktısı.

{{< highlight "java" >}}

 Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}
## **İlgili Makale**
{{% alert color="primary" %}} 

- [Bir çalışma sayfasına yazmadan özel işlevin doğrudan hesaplanması](/cells/tr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
