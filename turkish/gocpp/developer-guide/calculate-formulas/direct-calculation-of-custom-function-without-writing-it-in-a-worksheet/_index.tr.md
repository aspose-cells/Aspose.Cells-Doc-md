---
title: Golang ile C++ kullanarak Worksheet’e yazmadan özel fonksiyonun doğrudan hesaplanması
linktitle: Özel Fonksiyonun Doğrudan Hesaplanması
description: Bu makale, Aspose.Cells kütüphanesini kullanarak Microsoft Excel de özel fonksiyonları çalışma tablosuna yazmadan doğrudan nasıl hesaplacağınızı tanıtıyor. Mevcut bir Excel dosyası yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanabilir ve özel fonksiyonu hesaplayabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, özel fonksiyonlar, doğrudan hesaplamalar, yazma ihtiyacı yok, çalışma tabloları
type: docs
weight: 90
url: /tr/go-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Worksheet'e Yazmadan Özel Fonksiyonun Doğrudan Hesaplanması**

Bu konu, özel fonksiyonlarınızı öncelikle çalışma sayfasına yazmadan doğrudan nasıl hesaplayabileceğinizi açıklar. Lütfen bu amaçla [**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula_string/) metodunu kullanın.

Lütfen aşağıdaki örnek kodu inceleyin, bu metodun kullanımını gösterir. MyCompany::CustomFunction() adında bir özel fonksiyon kullandık ve değeri "Aspose.Cells." olarak hesapladık. Bu değer otomatik olarak hesaplama motoru tarafından hücre A1'in değeri olan "Welcome to " ile birleştirilir ve nihai hesaplanan değer "Welcome to Aspose.Cells." olur. Koddaki gibi, özel fonksiyonumuzu herhangi bir worksheet'e yazmadık ve tamamen kendi özel mantığımızla hesaplandı.

### **Programlama Örneği**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DirectCalculationOfCustomFunctionWithoutWritingItInAWorksheet.go" >}}
### **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı aşağıdaki gibidir.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **İlgili Makale**

{{% alert color="primary" %}}

[Özel Hesaplama Motoru Uygula ve Aspose.Cells'in Varsayılan Hesaplama Motorunu Geliştir](/cells/tr/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
