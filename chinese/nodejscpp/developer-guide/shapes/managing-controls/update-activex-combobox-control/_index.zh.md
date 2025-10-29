---
title: 通过C++和Node.js更新ActiveX组合框控件
linktitle: 更新ActiveX组合框控件
type: docs
weight: 170
url: /zh/nodejs-cpp/update-activex-combobox-control/
description: 学习如何使用Aspose.Cells for Node.js via C++读取和写入ActiveX组合框控件的值。 
---

## **可能的使用场景**
您可以使用Aspose.Cells for Node.js via C++读取或写入ActiveX组合框控件的值。请通过[Shape.getActiveXControl()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--)属性访问ActiveX控件，并通过[ActiveXControlBase.getType()](https://reference.aspose.com/cells/nodejs-cpp/activexcontrolbase/#getType--)属性检查其类型，类型应返回[ControlType.ComboBox](https://reference.aspose.com/cells/nodejs-cpp/controltype/)，然后将其类型转换为[ComboBoxActiveXControl](https://reference.aspose.com/cells/nodejs-cpp/comboboxactivexcontrol/)对象，并读取或修改其各种属性。

请下载以下示例代码中使用的 [示例 Excel 文件](5115124.xlsx)。
## **更新ActiveX ComboBox控件**
以下截图显示了样本代码对 [样本excel文件](5115124.xlsx) 的效果。正如你所看到的，活动X组合框的值已更新为"This is combo box control"。

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **示例代码**
以下样本代码更新了 [样本excel文件](5115124.xlsx) 中存在的活动X组合框控件的值。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SourceFile_activex.xlsx");
// Create a workbook
const wb = new AsposeCells.Workbook(filePath);

// Access first shape from first worksheet
const shape = wb.getWorksheets().get(0).getShapes().get(0);

// Access ActiveX ComboBox Control and update its value
if (shape.getActiveXControl() != null)
{
// Access Shape ActiveX Control
const c = shape.getActiveXControl();

if (c instanceof AsposeCells.ComboBoxActiveXControl)
{
// Type cast ActiveXControl into ComboBoxActiveXControl and change its value
const comboBoxActiveX = new AsposeCells.ComboBoxActiveXControl(c);
comboBoxActiveX.setValue("This is combo box control with updated value.");

}

}

// Save the workbook
const outputFilePath = path.join(dataDir, "OutputFile_out.xlsx");
wb.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
