---
title: 通过Node.js的C++将宏分配给表单控件
linktitle: 给窗体控件分配宏
type: docs
weight: 60
url: /zh/nodejs-cpp/assign-macro-to-form-control/
description: 了解如何使用Aspose.Cells for Node.js via C++将宏代码分配给如按钮等表单控件。 
keywords: 通过Node.js的C++将宏分配给表单控件，表单控件的宏代码，集成宏在XLSM中通过Node.js的C++
---

{{% alert color="primary" %}}

Aspose.Cells允许您向按钮等窗体控件分配宏代码。请使用[**Shape.getMacroName()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getMacroName--)属性将新的宏代码分配给工作簿内的窗体控件。

{{% /alert %}}

以下示例创建一个新工作簿，将宏代码分配给表单按钮，并以XLSM格式保存。当在Microsoft Excel中打开该文件时，将看到如下宏代码。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **在Node.js中将宏分配给表单控件**

这是生成带有宏代码的XLSM文件的示例代码。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);

const moduleIdx = workbook.getVbaProject().getModules().add(sheet);
const module = workbook.getVbaProject().getModules().get(moduleIdx);
module.setCodes(
"Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub"
);

const button = sheet.getShapes().addButton(2, 0, 2, 0, 28, 80);
button.setPlacement(AsposeCells.PlacementType.FreeFloating);
button.getFont().setName("Tahoma");
button.getFont().setIsBold(true);
button.getFont().setColor(AsposeCells.Color.Blue);
button.setText("Aspose");

button.setMacroName(sheet.getName() + ".ShowMessage");

const outputFilePath = path.join(dataDir, "Output.out.xlsm");
workbook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
