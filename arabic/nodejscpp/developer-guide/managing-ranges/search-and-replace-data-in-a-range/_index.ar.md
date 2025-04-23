---
title: البحث واستبدال البيانات في نطاق باستخدام Node.js عبر C++
linktitle: البحث واستبدال البيانات في نطاق
type: docs
weight: 170
url: /ar/nodejs-cpp/search-and-replace-data-in-a-range/
description: توضح هذه المقالة كيفية البحث واستبدال البيانات في نطاق في Excel باستخدام Node.js عبر كود C++.
keywords: البحث والاستبدال البيانات في إكسل باستخدام Node.js، البحث عن البيانات واستبدالها في حسابات، البحث في نطاق، البحث عن البيانات في نطاق باستخدام Node.js، البحث عن البيانات في إكسل باستخدام Node.js، البحث في نطاق، البحث عن البيانات في إكسل، البحث في نطاق، البحث عن واستبدال البيانات في إكسل باستخدام Node.js، البحث عن واستبدال البيانات في نطاق باستخدام Node.js، البحث عن واستبدال البيانات في نطاق باستخدام Node.js
---

{{% alert color="primary" %}}

أحيانًا تحتاج إلى البحث عن واستبدال بيانات محددة في نطاق مع تجاهل أي قيم خلايا خارج النطاق المطلوب. يتيح لك Aspose.Cells for Node.js via C++ تقييد البحث على نطاق معين. تشرح هذه المقالة كيفية ذلك.

{{% /alert %}}

يوفر Aspose.Cells for Node.js via C++ طريقة [**FindOptions.setRange(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setRange-cellarea-) لتحديد نطاق عند البحث عن بيانات. يوضح رمز المثال أدناه البحث واستبدال البيانات في النطاق.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

const area = AsposeCells.CellArea.createCellArea("E9", "H15");

const opts = new AsposeCells.FindOptions();
opts.setLookInType(AsposeCells.LookInType.Values);
opts.setLookAtType(AsposeCells.LookAtType.EntireContent);
opts.setRange(area);

let cell = null;

do {
cell = worksheet.getCells().find("search", cell, opts);
if (cell === null || cell.isNull()) {
break;
}
cell.putValue("replace");
} while (true);

workbook.save(path.join(dataDir, "output.out.xlsx"));
```
