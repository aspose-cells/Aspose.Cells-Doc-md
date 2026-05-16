---
title: Licensing
type: docs
weight: 120
url: /nodejs-cpp/licensing/
description: Aspose.Cells for Node.js via C++ provides different plans for purchase or offers a Free Trial and a 30-day Temporary License for evaluation using Licensing and Subscription policies.
keywords: Node.js Apply License from Disk, Set License in Aspose.Cells for Node.js via C++
---

## How to Apply a License in Aspose.Cells for Node.js via C++

The license is a plain text XML file that contains details such as the product name, number of developers it is licensed to, subscription expiry date and so on. The file is digitally signed, so don't modify the file. Even inadvertent addition of an extra line break into the file will invalidate it.

You need to set a license before utilizing Aspose.Cells if you want to avoid its evaluation limitation. It is only required to set a license once per application (or process).

### How to Apply a License from Disk

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const licensePath = path.join(dataDir, "Aspose.Cells.lic");

try {
    const license = new AsposeCells.License();
    license.setLicense(licensePath);
} catch (ex) {
    console.log(ex.message);
}

const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cell = sheet.getCells().get("A1");
cell.putValue("Hello World!");
wb.save(path.join(dataDir, "MyBook_out.xlsx"));

```
{{% alert color="primary" %}}

When you call the SetLicense method, the license name should be same as that of your license file name. For example, you may change the license file name to Aspose.Cells.lic.xml. Then in your code, you should use the modified license name (Aspose.Cells.lic.xml) for the SetLicense method.

{{% /alert %}}