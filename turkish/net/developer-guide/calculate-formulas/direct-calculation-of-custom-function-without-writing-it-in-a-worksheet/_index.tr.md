---
title: Bir çalışma sayfasına yazmadan özel işlevin doğrudan hesaplanması
type: docs
weight: 90
url: /tr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
## **Bir çalışma sayfasına yazmadan özel işlevin doğrudan hesaplanması**

 Bu konuda, özel işlevlerinizi önce bir çalışma sayfasına yazmadan doğrudan nasıl hesaplayabileceğiniz açıklanmaktadır. lütfen[**Worksheet.CalculateFormula(dize formülü, CalculationOptions tercihleri)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)Bu amaç için yöntem.

Lütfen bu yöntemin kullanımını gösteren aşağıdaki örnek koda bakın. MyCompany.CustomFunction() adlı özel bir işlev kullandık ve değerini "Aspose.Cells" olarak hesapladık. bu değer otomatik olarak A1 hücresinin değeri olan "Welcome to" ile hesaplama motoru tarafından birleştirilir ve hesaplanan son değer "Welcome to Aspose.Cells" olarak döner. özel fonksiyonumuzu bir çalışma sayfasında herhangi bir yere yazmaz ve doğrudan kendi özel mantığımızla hesaplanır.

### **Programlama Örneği**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Konsol Çıkışı**

Aşağıda, yukarıdaki örnek kodun konsol çıktısı bulunmaktadır.

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **İlgili Makale**

{{% alert color="primary" %}}

[Aspose.Cells Varsayılan Hesaplama Motorunu genişletmek için Özel Hesaplama Motorunu uygulayın](/cells/tr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
