---
title: تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل
linktitle: تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل
type: docs
weight: 5000
url: /ar/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: تعلم كيفية الحفاظ على المراجع في أوراق عمل أخرى عند حذف الأعمدة والصفوف الفارغة في ورقة عمل باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

عند حذف الأعمدة والصفوف الفارغة في ورقة العمل، تصبح مراجعها في ورقات العمل الأخرى غير صالحة. إذا كنت ترغب في تجنب هذا السلوك وتريد تحديث تلك المراجع لورقة العمل الحالية في ورقات العمل الأخرى أيضًا، يرجى استخدام الخاصية [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) وتعيينها على **صحيح**.

{{% /alert %}}

## **تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل**

 يرجى الاطلاع على رمز العينة التالي وإخراجه في وحدة التحكم. تتضمن الخلية E3 في ورقة العمل الثانية صيغة =Sheet1!C3 والتي تشير إلى الخلية C3 في ورقة العمل الأولى. إذا قمت بضبط خاصية [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) على **صحيح**، سيتم تحديث هذه الصيغة وتحويلها إلى =Sheet1!A1 عند حذف الأعمدة والصفوف الفارغة في ورقة العمل الأولى. ومع ذلك، إذا قمت بضبط خاصية [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) على **خطأ**، فستظل الصيغة في الخلية E3 في ورقة العمل الثانية =Sheet1!C3 وتصبح غير صالحة.

### **نموذج برمجة**

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

### **مخرجات الوحدة**

هذه هي مخرجات وحدة التحكم للرمز النموذجي أعلاه عند تعيين خاصية [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) على **صحيح**.

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

هذه هي مخرجات وحدة التحكم للرمز النموذجي أعلاه عند تعيين خاصية [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) على **خطأ**. كما ترى، فإن الصيغة في الخلية E3 في ورقة العمل الثانية لم يتم تحديثها، وأصبح قيمة خليةها الآن 0 بدلاً من 4، وهذا غير صالح.

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
