---
title: Bir çalışma sayfasına yazmadan özel işlevin doğrudan hesaplanması
type: docs
weight: 650
url: /tr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
{{% alert color="primary" %}} 

 Bu makalede, özel işlevlerinizi önce bir çalışma sayfasına yazmadan doğrudan nasıl hesaplayabileceğiniz açıklanmaktadır. lütfen[Worksheet.calculateFormula(dize formülü, CalculationOptions tercihleri)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) yöntemi bu amaç için.

{{% /alert %}} 
## **Bir çalışma sayfasına yazmadan özel işlevin doğrudan hesaplanması**
Lütfen bu yöntemin kullanımını gösteren aşağıdaki örnek koda bakın. adlı özel bir işlev kullandık.*MyCompany.CustomFunction()*ve değerini "Aspose.Cells" olarak hesaplıyoruz. bu değer otomatik olarak A1 hücresinin "Hoş Geldiniz" değeri ile hesaplama motoru tarafından birleştirilir ve hesaplanan son değer "Aspose.Cells'e Hoş Geldiniz" olarak döner. Görüldüğü gibi bir çalışma tablosunda herhangi bir yere özel fonksiyonumuzu yazmadığımız ve doğrudan kendi özel mantığımızla hesaplanan bir koddur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **Konsol Çıkışı**
Aşağıda, yukarıdaki örnek kodun konsol çıktısı bulunmaktadır.

{{< highlight "java" >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **İlgili Makale**
{{% alert color="primary" %}} 

- [Aspose.Cells Varsayılan Hesaplama Motorunu genişletmek için Özel Hesaplama Motorunu uygulayın](/cells/tr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
