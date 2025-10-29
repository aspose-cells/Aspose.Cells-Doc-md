---
title: Назначение макроса элементу управления формы с Node.js через C++
linktitle: Назначить макрос на элемент управления формы
type: docs
weight: 60
url: /ru/nodejs-cpp/assign-macro-to-form-control/
description: Узнайте, как назначить макросный код на элемент управления формой, например на кнопку, используя Aspose.Cells for Node.js via C++. 
keywords: Назначение макроса элементу управления формой Node.js через C++, Код макроса для элемента управления формой Node.js через C++, Интегрированный макрос в XLSM Node.js через C++
---

{{% alert color="primary" %}}

Aspose.Cells позволяет назначить код макроса элементу управления формы, такому как кнопка. Используйте свойство [**Shape.getMacroName()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getMacroName--), чтобы назначить новый код макроса элементу управления формы внутри книги.

{{% /alert %}}

Следующий пример создает новую рабочую книгу, назначает код макроса на кнопку формы и сохраняет результат в формате XLSM. После открытия файла XLSM в Microsoft Excel вы увидите следующий код макроса.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Назначить макрос на элемент управления формы в Node.js**

Вот пример кода для генерации выходного файла XLSM с макросным кодом.

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
