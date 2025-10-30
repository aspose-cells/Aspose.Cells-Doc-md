---
title: Node.js aracılığıyla C++ kullanarak Değişken Aralığını Döndürmek için AbstractCalculationEngine kullanımı
linktitle: Aspose.Cells kitaplığını kullanarak Microsoft Excel de bir dizi değeri döndüren soyut bir hesaplama motoru tanıtır. Varolan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanarak bir dizi değeri alabiliriz ve sonucu döndürebiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
description: Bu makale, Aspose.Cells kütüphanesini kullanarak Node.js aracılığıyla C++ ile Excel de değerler aralığını döndüren soyut hesaplama motorunu tanıtmaktadır. Bir Excel dosyasını yükleyin veya oluşturun ve değiştirilmiş dosyayı diske kaydedin.
keywords: Aspose.Cells, Excel, değerleri döndüren soyut hesaplama motoru Node.js aracılığıyla C++, özel fonksiyonlar
type: docs
weight: 55
url: /tr/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel tarafından desteklenmeyen kullanıcı tanımlı veya özel işlevleri uygulamak için kullanılan [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) sınıfını sağlar.

Bu makale, [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) aralığındaki değerlerin nasıl döndürüleceğini açıklayacaktır.

{{% /alert %}}

Aşağıdaki kod, [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) sınıfının kullanımını gösterir ve yöntemi aracılığıyla değer aralığını döndürür.

Bir sınıf oluşturun ve bir *calculateCustomFunction* fonksiyonu ekleyin. Bu sınıf [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) uygulamaktadır.

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomFunctionStaticValue extends AsposeCells.AbstractCalculationEngine {
calculate(data) {
data.setCalculatedValue([
[new Date(2015, 5, 12, 10, 6, 30), 2],
[3.0, "Test"]
]);
}
}
```

Şimdi yukarıdaki fonksiyonu programınızda kullanın

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomFunctionStaticValue extends AsposeCells.AbstractCalculationEngine {
calculate(data) {
data.setCalculatedValue([
[new Date(2015, 5, 12, 10, 6, 30), 2],
[3.0, "Test"]
]);
}
}

try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();

// Set formula
const cell = cells.get(0, 0);
cell.setArrayFormula("=MYFUNC()", 2, 2);

const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);

// Set calculation options for formula
const calculationOptions = new AsposeCells.CalculationOptions();
calculationOptions.setCustomEngine(new CustomFunctionStaticValue());
workbook.calculateFormula(calculationOptions);

// Save to xlsx by setting the calc mode to manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);
workbook.save(dataDir + "output_out.xlsx");

// Save to pdf
workbook.save(dataDir + "output_out.pdf");
} catch (error) {
console.error(`Test failed: ${error.message}`);
throw error;
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
