---
title: تحميل أوراق عمل محددة في دفتر العمل باستخدام Node.js عبر C++
linktitle: تحميل الأوراق العمل المحددة في كتيب عمل
type: docs
weight: 100
url: /ar/nodejs-cpp/load-specific-worksheets-in-a-workbook/
description: تعلم كيفية تحميل أوراق عمل محددة في دفتر العمل باستخدام Aspose.Cells for Node.js via C++. حسن الأداء وقلل استهلاك الذاكرة.
---

{{% alert color="primary" %}}

بشكل افتراضي، تحمل Aspose.Cells الجدول بأكمله إلى الذاكرة. من الممكن تحميل ورقات محددة فقط. يمكن أن يُحسِن هذا الأداء ويستهلك أقل كمية من الذاكرة. هذا النهج مفيد عند العمل مع دفتر عمل كبير يتكون من العديد من ورقات العمل.

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define a new Workbook.
let workbook;

// Load the workbook with the specified worksheet only.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
loadOptions.setLoadFilter(new CustomLoad());

// Create the workbook.
workbook = new AsposeCells.Workbook(path.join(dataDir, "TestData.xlsx"), loadOptions);

// Perform your desired task.

// Save the workbook.
workbook.save(path.join(dataDir, "outputFile.out.xlsx"));
```

إليك تنفيذ فئة CustomLoad.

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoad extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "Sheet2") {
// Load everything from worksheet "Sheet2"
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.All);
} else {
// Load nothing
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.Structure);
}
}
}
```


{{< app/cells/assistant language="nodejs-cpp" >}}
