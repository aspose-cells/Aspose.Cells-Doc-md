---
title: Eğitim tablosuna yazmadan özel bir fonksiyonun doğrudan hesaplanması
type: docs
weight: 650
url: /tr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

{{% alert color="primary" %}} 

Bu makale, özel işlevlerinizi önce bir çalışma sayfasına yazmadan doğrudan nasıl hesaplayabileceğinizi açıklamaktadır. Bu amaçla [Worksheet.calculateFormula(string formula, CalculationOptions opts)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) yöntemini kullanabilirsiniz.

{{% /alert %}} 
## **Özel işlevin çalışma tablosuna yazılmadan doğrudan hesaplanması**
Lütfen aşağıdaki örnek kodu inceleyin. Kendi özel mantığımızla hesapladığımız *MyCompany.CustomFunction()* adında özel bir fonksiyon kullandık ve bu fonksiyonun değerini *"Aspose.Cells."* olarak hesapladık ve ardından bu değer, *"Welcome to "* olan A1 hücresinin değeriyle otomatik olarak birleştirildi ve son hesaplanmış değer *"Welcome to Aspose.Cells."* olarak döndü. Kodda görebileceğiniz gibi özel işlevimizi hiçbir çalışma sayfasına yazmadık ve bu doğrudan kendi özel mantığımızla hesaplandı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun konsol çıktısı aşağıdaki gibidir.

{{< highlight java >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **İlgili Makale**
{{% alert color="primary" %}} 

- [Aspose.Cells'in Varsayılan Hesaplama Motorunu Genişletmek için Özel Hesaplama Motoru Uygulamak](/cells/tr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
