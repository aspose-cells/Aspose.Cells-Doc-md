---
title: Node.js aracılığıyla C++ kullanarak Aspose.Cells ile Varsayılan Hesaplama Motorunu Geliştirmek için Özel Hesaplama Motoru Uygulama
linktitle: Aspose.Cells in Varsayılan Hesaplama Motorunu Genişletmek
description: Bu makale, Node.js de Aspose.Cells kütüphanesi kullanılarak varsayılan hesaplama motorunu genişletmek amacıyla özel bir hesaplama motoru uygulamayı anlatmaktadır. Mevcut bir Excel dosyasını yükleyin veya yeni oluşturun, sağlanan yöntemleri kullanın ve düzenlenmiş Excel dosyasını kaydedin.
keywords: Aspose.Cells, Excel, Özel Hesaplama Motoru, Node.js aracılığıyla C++
type: docs
weight: 80
url: /tr/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Özel Hesaplama Motorunu Uygulama**

Aspose.Cells'in neredeyse tüm Microsoft Excel formüllerini hesaplayabilen güçlü bir hesaplama motoru bulunmaktadır. Bununla birlikte, varsayılan hesaplama motorunu genişletmenize olanak tanır ve size daha fazla güç ve esneklik sağlar.

Bu özellik uygulamada kullanılan özellik ve sınıflar.

- [**CalculationOptions.getCustomEngine()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getCustomEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/nodejs-cpp/calculationdata)

Aşağıdaki kod, Özel Hesaplama Motorunu uygular. [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) arayüzünü uygular ve [**calculate(CalculationData data)**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine/#calculate-calculationdata-) yöntemine sahiptir. Bu yöntem, tüm formülleriniz üzerinde çağrılır. Bu yöntemde, **BUGÜN** fonksiyonunu yakalar ve sistem tarihine bir gün ekleriz. Eğer şu anki tarih 27/07/2023 ise, özel motor **BUGÜN()** fonksiyonunu 28/07/2023 olarak hesaplar.

### **Programlama Örneği**

```javascript
const AsposeCells = require("aspose.cells.node");

// Create a new class derived from AbstractCalculationEngine
class CustomEngine extends AsposeCells.AbstractCalculationEngine {
// Override the Calculate method with custom logic
calculate(data) {
// Check the formula name and change the implementation
if (data.getFunctionName().toUpperCase() === "TODAY") {
// Assign the CalculationData.CalculatedValue: add one day offset for the date
data.setCalculatedValue(AsposeCells.CellsHelper.getDoubleFromDateTime(new Date(), false) + 1.0);
}
}
getProcessBuiltInFunctions() {
return true;
}
}

class ImplementCustomCalculationEngine {
static run() {
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook();

// Access first Worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Access Cell A1 and put a formula to sum values of B1 to B2
const a1 = sheet.getCells().get("A1");
const style = a1.getStyle();
style.setNumber(14);
a1.setStyle(style);

a1.setFormula("=TODAY()");

// Calculate all formulas in the Workbook 
workbook.calculateFormula();

// The result of A1 should be 20 as per default calculation engine
console.log("The value of A1 with default calculation engine: " + a1.getStringValue());

// Create an instance of CustomEngine
const engine = new CustomEngine();

// Create an instance of CalculationOptions
const opts = new AsposeCells.CalculationOptions();

// Assign the CalculationOptions.CustomEngine property to the instance of CustomEngine
opts.setCustomEngine(engine);

// Recalculate all formulas in Workbook using the custom calculation engine
workbook.calculateFormula(opts);

// The result of A1 will be 50 as per custom calculation engine
console.log("The value of A1 with custom calculation engine: " + a1.getStringValue());

console.log("Press any key to continue...");
}
}

// Call the run method to execute the example
ImplementCustomCalculationEngine.run();
```

### **Sonuç**

Lütfen yukarıdaki örnek kodun konsol çıktısını kontrol edin; özel motor ile A1 hücresinin değeri (tarih ve saat), motor kullanılmadan sonucu ise en az bir gün farklı olmalıdır.

### **İlgili Makale**

{{% alert color="primary" %}}

[Özel Fonksiyonun Doğrudan Hesaplanması, çalışma sayfasına yazmadan](/cells/tr/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
