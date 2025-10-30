---
title: GlobalizationSettings Sınıfı Kullanarak Özel Alt Toplam Etiketleri ve Pasta Grafik Diğer Etiketleri ile Node.js ve C++
linktitle: Özel Alt Toplam Etiketleri ve Pasta Grafiği Diğer Etiketleri İçin GlobalizationSettings Sınıfını Kullanma
type: docs
weight: 70
url: /tr/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Aspose.Cells for Node.js via C++ kullanarak GlobalizationSettings sınıfı ile pasta grafiklerinin alt toplam etiketleri ve diğer etiketlerini nasıl özelleştireceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells API'leri, kullanıcının bir hesap tablosunda özel alt toplamlar için etiketler kullanmak istediği durumları yönetmek amacıyla [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) sınıfını açtı. Ayrıca, [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) sınıfı, hesaplandırmayı yaparken **Diğer** etiketi için de kullanılabilir.

## **GlobalizationSettings Sınıfı Tanıtımı**

[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) sınıfı şu anda, istenen alt toplam etiketlerini almak veya **Diğer** etiketi için özel metinler render etmek için geçersiz kılınabilecek 3 metot sunar.

1. [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-): Fonksiyonun toplam ismini alır.
1. [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-): Fonksiyonun genel toplam ismini alır.


### **Alt toplamlar için özel etiketler**

[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) sınıfı, aşağıda gösterildiği gibi [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-) ve [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-) metodlarını geçersiz kılarak Alt Toplam etiketlerini özelleştirmek için kullanılabilir.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Defines a custom class derived from GlobalizationSettings class
class CustomSettings extends AsposeCells.GlobalizationSettings {
// Overrides the GetTotalName method
getTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "AVG";
// Handle other cases as per requirement
default:
return super.getTotalName(functionType);
}
}

// Overrides the GetGrandTotalName method
getGrandTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "GRD AVG";
// Handle other cases as per requirement
default:
return super.getGrandTotalName(functionType);
}
}
}
```

Özel etiketleri enjekte etmek için, yukarıda tanımlanan **CustomSettings** sınıfına ait bir örneğe [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--) özelliği atanmalı ve ardından çalışma sayfasına alt toplamlar eklenmelidir.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// Defines a custom class derived from GlobalizationSettings class
class CustomSettings extends AsposeCells.GlobalizationSettings {
// Overrides the GetTotalName method
getTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "AVG";
// Handle other cases as per requirement
default:
return super.getTotalName(functionType);
}
}

// Overrides the GetGrandTotalName method
getGrandTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "GRD AVG";
// Handle other cases as per requirement
default:
return super.getGrandTotalName(functionType);
}
}
}

try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads an existing spreadsheet containing some data
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Assigns the GlobalizationSettings property of the WorkbookSettings class to a custom class created
workbook.getSettings().setGlobalizationSettings(new CustomSettings());

// Accesses the 1st worksheet from the collection which contains data that resides in the cell range A2:B9
const sheet = workbook.getWorksheets().get(0);

// Adds Subtotal of type Average to the worksheet
sheet.getCells().subtotal(AsposeCells.CellArea.createCellArea("A2", "B9"), 0, AsposeCells.ConsolidationFunction.Average, [1]);

// Calculates Formulas
workbook.calculateFormula();

// Auto fits all columns
sheet.autoFitColumns();

// Saves the workbook on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
} catch (error) {
console.error(`Test failed: ${error.message}`);
throw error;
}
```

{{% alert color="primary" %}}

[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) sınıfı yalnızca yeni Alt Toplamlar eklemek için çalışır. Eğer bir çalışma kitabında zaten Alt Toplamlar varsa, bunların etiketleri değiştirilemez.

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
