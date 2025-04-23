---
title: Обновление элемента управления ComboBox ActiveX с помощью Node.js через C++
linktitle: Обновить элемент управления ActiveX ComboBox
type: docs
weight: 170
url: /ru/nodejs-cpp/update-activex-combobox-control/
description: Узнайте, как читать и записывать значения элемента управления ComboBox ActiveX с помощью Aspose.Cells for Node.js via C++. 
---

## **Возможные сценарии использования**
Вы можете читать или записывать значения элемента управления ComboBox ActiveX, используя Aspose.Cells for Node.js via C++. Обратитесь к ActiveX Control через свойство [Shape.getActiveXControl()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) и проверьте его тип через свойство [ActiveXControlBase.getType()](https://reference.aspose.com/cells/nodejs-cpp/activexcontrolbase/#getType--), оно должно возвращать значение [ControlType.ComboBox](https://reference.aspose.com/cells/nodejs-cpp/controltype/) и затем привести его к объекту [ComboBoxActiveXControl](https://reference.aspose.com/cells/nodejs-cpp/comboboxactivexcontrol/) для чтения или изменения различных свойств.

Пожалуйста, загрузите [образец файла Excel](5115124.xlsx), используемый в следующем примере кода.
## **Обновление элемента управления ComboBox ActiveX**
На следующем скриншоте показан эффект примера кода на [образец файла Excel](5115124.xlsx). Как видно, значение элемента управления ActiveX ComboBox было обновлено на "This is combo box control".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Образец кода**
Следующий образец кода обновляет значение элемента управления ActiveX ComboBox, находящегося внутри [образца файла Excel](5115124.xlsx).

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
