---
title: توسيم أنماط عناصر الجدول باستخدام خاصية HtmlSaveOptions.TableCssId في Node.js عبر C++
linktitle: بادئة أنماط عناصر الجدول مع خاصية HtmlSaveOptions.TableCssId
type: docs
weight: 110
url: /ar/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: تعلم كيفية إضافة بادئة لأنماط عناصر الجدول في HTML باستخدام Aspose.Cells for Node.js via C++. 
---

## **سيناريوهات الاستخدام المحتملة**

يسمح Aspose.Cells بتكوين بادئة لأنماط عناصر الجدول باستخدام الخاصية [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--). فترض أن تُعين هذه الخاصية بقيمة مثل **MyTest_TableCssId**، حينها ستجد أن أنماط عناصر الجدول تظهر كما في المثال أدناه:

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

اللقطة الشاشية التالية تظهر تأثير استخدام خاصية [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--) على الإخراج الخاص بـ HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **بادئة أنماط عناصر الجدول باستخدام خاصية HtmlSaveOptions.TableCssId**

يوضح الكود العينة التالي كيفية الاستفادة من خاصية [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--). يرجى التحقق من [إخراج HTML](60489790.zip) الذي تم توليده بواسطة الكود للرجوع إليه.

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - specify table css id
const opts = new AsposeCells.HtmlSaveOptions();
opts.setTableCssId("MyTest_TableCssId");

// Save the workbook in html
wb.save("outputTableCssId.html", opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
