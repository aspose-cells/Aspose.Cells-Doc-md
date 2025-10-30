---
title: Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle
linktitle: Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle
type: docs
weight: 5000
url: /tr/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Aspose.Cells for Node.js via C++ kullanarak boş sütun ve satır silerken diğer çalışma sayfalarındaki referansların nasıl korunacağını öğrenin.
---

{{% alert color="primary" %}}

Çalışma sayfasında boş sütunları ve satırları sildiğinizde, diğer çalışma sayfalarındaki bu sütunların referansları geçersiz hale gelir. Bu davranışı önlemek ve diğer çalışma sayfalarındaki bu çalışma sayfasının referanslarının güncellenmesini istiyorsanız, lütfen [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) özelliğini kullanın ve bunu **true** olarak ayarlayın.

{{% /alert %}}

## **Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle**

Aşağıdaki örnek kod ve konsol çıktısına bakın. İkinci çalışma sayfasındaki E3 hücresinde =Sheet1!C3 formülü var, bu da ilk çalışma sayfasındaki C3 hücresine referans verir. [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) özelliğini **true** olarak ayarlarsanız, bu formül güncellenerek =Sheet1!A1 olur, ilk çalışma sayfasında boş sütunlar ve satırları sildikten sonra. Ancak, [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) özelliğini **false** yaparsanız, ikinci çalışma sayfasındaki E3 hücresindeki formül değişmeden kalır ve geçersiz olur.

### **Programlama Örneği**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();

// Add second sheet with name Sheet2
wb.getWorksheets().add("Sheet2");

// Access first sheet and add some integer value in cell C1
// Also add some value in any cell to increase the number of blank rows and columns
const sht1 = wb.getWorksheets().get(0);
sht1.getCells().get("C1").putValue(4);
sht1.getCells().get("K30").putValue(4);

// Access second sheet and add formula in cell E3 which refers to cell C1 in first sheet
const sht2 = wb.getWorksheets().get(1);
sht2.getCells().get("E3").setFormula("'Sheet1'!C1");

// Calculate formulas of workbook
wb.calculateFormula();

// Print the formula and value of cell E3 in second sheet before deleting blank columns and rows in Sheet1.
console.log("Cell E3 before deleting blank columns and rows in Sheet1.");
console.log("--------------------------------------------------------");
console.log("Cell Formula: " + sht2.getCells().get("E3").getFormula());
console.log("Cell Value: " + sht2.getCells().get("E3").getStringValue());

// If you comment DeleteOptions.UpdateReference property below, then the formula in cell E3 in second sheet will not be updated
const opts = new AsposeCells.DeleteOptions();
opts.setUpdateReference(true);

// Delete all blank rows and columns with delete options
sht1.getCells().deleteBlankColumns(opts);
sht1.getCells().deleteBlankRows(opts);

// Calculate formulas of workbook
wb.calculateFormula();

// Print the formula and value of cell E3 in second sheet after deleting blank columns and rows in Sheet1.
console.log("");
console.log("");
console.log("Cell E3 after deleting blank columns and rows in Sheet1.");
console.log("--------------------------------------------------------");
console.log("Cell Formula: " + sht2.getCells().get("E3").getFormula());
console.log("Cell Value: " + sht2.getCells().get("E3").getStringValue());
```

### **Konsol Çıktısı**

Yukarıdaki örnek kodun, [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) özelliği **true** olarak ayarlandığında çıkan konsol çıktısı.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Yukarıdaki örnek kodun, [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) özelliği **false** olarak ayarlandığında çıkan konsol çıktısı. Gördüğünüz gibi, ikinci çalışma sayfasındaki E3 hücresindeki formül güncellenmedi ve hücre değeri artık 4 yerine 0 oldu, bu da geçersiz.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
