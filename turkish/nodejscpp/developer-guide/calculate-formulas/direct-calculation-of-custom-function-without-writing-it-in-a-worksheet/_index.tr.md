---
title: Özel fonksiyonun doğrudan hesaplanması, çalışma sayfasına yazmadan Node.js aracılığıyla C++
linktitle: Eğitim tablosuna yazmadan özel bir fonksiyonun doğrudan hesaplanması
description: Bu makale, Aspose.Cells kütüphanesini kullanarak, fonksiyonu bir çalışma sayfasına yazmadan özel fonksiyonların doğrudan nasıl hesaplanacağını anlatmaktadır. Mevcut bir Excel dosyasını yükleyin veya yeni bir tane oluşturun, özel fonksiyonu hesaplayın ve değiştirilen dosyayı kaydedin.
keywords: Aspose.Cells, Excel, özel fonksiyonlar, doğrudan hesaplamalar, Node.js aracılığıyla C++, yazmaya gerek yok, çalışma sayfaları
type: docs
weight: 90
url: /tr/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Özel işlevin çalışma tablosuna yazılmadan doğrudan hesaplanması**

Bu konu, özel fonksiyonlarınızı öncelikle çalışma sayfasına yazmadan doğrudan nasıl hesaplayabileceğinizi açıklar. Lütfen bu amaçla [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-CalculationOptions-) metodunu kullanın.

Bu metodu kullanımını gösteren aşağıdaki örnek kodu inceleyin. MyCompany.CustomFunction() adında özel bir işlev kullandık ve bu işlevin değerini "Aspose.Cells." olarak kendimiz hesapladık ve bu değer otomatik olarak hesaplama motoru tarafından "Hoş geldiniz " olan A1 hücresinin değeri ile birleştirildi ve son hesaplanmış değer olarak "Hoş geldiniz Aspose.Cells." olarak döndü. Kodun içinde özel bir işlevimizi çalıştırmadığımızı ve bunun yerine, özel mantığımızla doğrudan hesaplandığını görebilirsiniz.

### **Programlama Örneği**

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomEngine extends AsposeCells.AbstractCalculationEngine {
// Override the Calculate method with custom logic
calculate(data) {
// Check the formula name and calculate it yourself
if (data.getFunctionName() === "MyCompany.CustomFunction") {
// This is our calculated value
data.setCalculatedValue("Aspose.Cells.");
}
}
}

class ImplementDirectCalculationOfCustomFunction {
static run() {
// Create a workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add some text in cell A1
ws.getCells().get("A1").putValue("Welcome to ");

// Create a calculation options with custom engine
const opts = new AsposeCells.CalculationOptions();
opts.setCustomEngine(new CustomEngine());

// This line shows how you can call your own custom function without
// a need to write it in any worksheet cell
// After the execution of this line, it will return
// Welcome to Aspose.Cells.
const ret = ws.calculateFormula("=A1 & MyCompany.CustomFunction()", opts);

// Print the calculated value
console.log("Calculated Value: " + ret);
}
}

// Example invocation
ImplementDirectCalculationOfCustomFunction.run();
```

### **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı aşağıdaki gibidir.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **İlgili Makale**

{{% alert color="primary" %}}

[Özel Hesaplama Motoru Uygulaması ve Aspose.Cells'in Varsayılan Hesaplama Motorunu Geliştirme](/cells/tr/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
