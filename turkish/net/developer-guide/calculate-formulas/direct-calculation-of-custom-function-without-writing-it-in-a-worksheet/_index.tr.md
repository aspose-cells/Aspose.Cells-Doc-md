---
title: Eğitim tablosuna yazmadan özel bir fonksiyonun doğrudan hesaplanması
description: Bu makale, Aspose.Cells kütüphanesini kullanarak Microsoft Excel de özel fonksiyonları çalışma tablosuna yazmadan doğrudan nasıl hesaplacağınızı tanıtıyor. Mevcut bir Excel dosyası yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanabilir ve özel fonksiyonu hesaplayabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, özel fonksiyonlar, doğrudan hesaplamalar, yazma ihtiyacı yok, çalışma tabloları
type: docs
weight: 90
url: /tr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Özel işlevin çalışma tablosuna yazılmadan doğrudan hesaplanması**

Bu konu, bir elektronik tabloda öncelikle onları yazmadan özel işlevlerinizi doğrudan nasıl hesaplayabileceğinizi açıklar. Bu amacı için [**Worksheet.CalculateFormula(string formula, CalculationOptions opts)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) yöntemini kullanın.

Bu metodu kullanımını gösteren aşağıdaki örnek kodu inceleyin. MyCompany.CustomFunction() adında özel bir işlev kullandık ve bu işlevin değerini "Aspose.Cells." olarak kendimiz hesapladık ve bu değer otomatik olarak hesaplama motoru tarafından "Hoş geldiniz " olan A1 hücresinin değeri ile birleştirildi ve son hesaplanmış değer olarak "Hoş geldiniz Aspose.Cells." olarak döndü. Kodun içinde özel bir işlevimizi çalıştırmadığımızı ve bunun yerine, özel mantığımızla doğrudan hesaplandığını görebilirsiniz.

### **Programlama Örneği**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı aşağıdaki gibidir.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **İlgili Makale**

{{% alert color="primary" %}}

Aspose.Cells'in Varsayılan Hesaplama Motorunu Genişletmek için Özel Hesaplama Motoru Uygulama

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
