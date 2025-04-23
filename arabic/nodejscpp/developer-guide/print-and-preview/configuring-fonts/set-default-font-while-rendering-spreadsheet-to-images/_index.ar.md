---
title: تعيين الخط الافتراضي أثناء عرض أوراق العمل كصور باستخدام Node.js عبر C++
linktitle: تعيين الخط الافتراضي أثناء تقديم جدول البيانات إلى الصور
type: docs
weight: 360
url: /ar/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: تعلم كيفية تعيين الخط الافتراضي أثناء عرض أوراق العمل كصور باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

يرجى استخدام خاصية [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) لتعيين الخط الافتراضي أثناء تقديم جداول البيانات إلى الصور. ستكون هذه الخاصية فعالة فقط عندما لا يمكن للخط الافتراضي للدفتر تقديم حروفك. يتم استخدام الخط الافتراضي المحدد بواسطة الخاصية [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) لجميع تلك الخلايا التي تحتوي على خطوط غير صحيحة أو غير موجودة.

{{% /alert %}}

## تعيين الخط الافتراضي أثناء تقديم جداول البيانات إلى الصور

ينشئ رمز النموذج التالي دفتر عمل، يضيف نصًا في الخلية A4 من ورقة العمل الأولى، ويضبط خطه إلى خط غير صالح أو غير موجود. ثم، يأخذ صورتين لورقة العمل. الصورة الأولى تم التقاطها بضبط الخاصية [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) إلى *Courier New*، والثانية بضبط الخاصية [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) إلى *Times New Roman*.

هذه هي الصورة الناتجة بعد تعيين الخاصية [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) إلى *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

هذه هي الصورة الناتجة بعد تعيين الخاصية [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) إلى *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## كود عينة

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Set default font of the workbook to none
let s = wb.getDefaultStyle();
s.getFont().setName("");
wb.setDefaultStyle(s);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access cell A4 and add some text inside it.
const cell = ws.getCells().get("A4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell A4 which is unknown.
let st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
st.setIsTextWrapped(true);
cell.setStyle(st);

// Set first column width and fourth column height
ws.getCells().setColumnWidth(0, 80);
ws.getCells().setRowHeight(3, 60);

// Create image or print options.
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);

// Render worksheet image with Courier New as default font.
opts.setDefaultFont("Courier New");
let sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "out_courier_new_out.png");

// Render worksheet image again with Times New Roman as default font.
opts.setDefaultFont("Times New Roman");
sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "times_new_roman_out.png");
```
