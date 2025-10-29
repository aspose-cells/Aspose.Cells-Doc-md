---
title: Автоматическая подгонка высоты строк при загрузке файла с помощью Node.js через C++
linktitle: Автоматическое подгонение высоты строки при загрузке файла
type: docs
weight: 120
url: /ru/nodejs-cpp/autofit-row-height/
description: Узнайте, как подогнать высоту строк, которые не настроены вручную, при загрузке файла с помощью Aspose.Cells for Node.js via C++.
keywords: Автоматическая подгонка высоты строк при загрузке файла Node.js через C++, автоматическая регулировка высоты строки при открытии файла Excel Node.js через C++ 
---

## **Возможные сценарии использования**
Высота строки автоматически соответствует размеру шрифта содержимого, но когда высота кешированной строки не совпадает с высотой содержимого файла, MS Excel автоматически подгоняет высоту строки при загрузке файла, в то время как Aspose.Cells for Node.js via C++ этого не делает для повышения производительности. Если необходимо использовать программу Aspose.Cells для автоматического совпадения высоты строк при загрузке файлов, это можно сделать через параметр [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) в вашем коде.

Пожалуйста, ознакомьтесь с изображением ниже. Наблюдается, что кешированная высота строки в строке 11 составляет 15, но Excel автоматически подогнал высоту строки при загрузке файла.
<br>
<img src="1.png" width=70% />

## **Регулировка высоты строки с помощью Aspose.Cells for Node.js via C++**
Если вы напрямую загрузите файл и сохраните его как PDF, данные не будут полностью отображаться в PDF, поскольку кешированная высота строки равна только 15.
<br>
<img src="2.png" width=70% />
<br>
Если при загрузке файла в параметре [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) установить значение true, тогда Aspose.Cells автоматически скорректирует высоту строки. Таким образом, высота строки будет соответствовать требованиям отображения текста.
<br>
<img src="3.png" width=70% />

## **Пример кода Node.js**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
workbook.save(path.join(dataDir, "out.pdf"));

const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setAutoFitterOptions(new AsposeCells.AutoFitterOptions());
loadOptions.getAutoFitterOptions().setOnlyAuto(true);
const book = new AsposeCells.Workbook(filePath, loadOptions);
book.save(path.join(dataDir, "out2.pdf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
