---
title: Özel işlevin çalışma sayfasına yazmadan doğrudan hesaplanması
description: Bu makalede, Aspose.Cells Excel'deki özel işlevleri, işlevi bir çalışma sayfasına yazmadan doğrudan hesaplamak için Aspose.Cells kitaplığının nasıl kullanılacağı anlatılmaktadır. Mevcut bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells'in sağladığı yöntemleri kullanarak özel işlevi hesaplayabilir ve sonucu alabiliriz. Son olarak değiştirdiğimiz Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, custom functions, direct calculations, no need to write, worksheets
type: docs
weight: 90
url: /tr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
##  **Özel işlevin çalışma sayfasına yazmadan doğrudan hesaplanması**

 Bu konu, özel işlevlerinizi önce bir çalışma sayfasına yazmadan doğrudan nasıl hesaplayabileceğinizi açıklamaktadır. Lütfen şunu kullanın:[**Worksheet.CalculateFormula(dize formülü, CalculationOptions tercihleri)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)Bu amaç için yöntem.

Lütfen bu yöntemin kullanımını gösteren aşağıdaki örnek koda bakın. MyCompany.CustomFunction() adında özel bir işlev kullandık ve değerini "Aspose.Cells" olarak hesapladık. Kendimiz tarafından bu değer otomatik olarak A1 hücresinin "Welcome to" değeri ile hesaplama motoru tarafından birleştirilir ve hesaplanan son değer "Welcome to Aspose.Cells." olarak geri döner. özel fonksiyonumuz çalışma sayfasının herhangi bir yerine yazılmaz ve doğrudan kendi özel mantığımızla hesaplanır.

###  **Programlama Örneği**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

###  **Konsol Çıkışı**

Yukarıdaki örnek kodun konsol çıktısı aşağıdadır.

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

###  **İlgili Makale**

{{% alert color="primary" %}}

[Aspose.Cells Varsayılan Hesaplama Motorunu genişletmek için Özel Hesaplama Motorunu uygulayın](/cells/tr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
