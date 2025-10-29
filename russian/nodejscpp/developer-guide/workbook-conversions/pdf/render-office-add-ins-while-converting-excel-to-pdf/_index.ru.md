---
title: Рендеринг офисных дополнений при преобразовании Excel в PDF с помощью Node.js и C++
linktitle: Рендеринг офисных надстроек при преобразовании Excel в PDF
type: docs
weight: 100
url: /ru/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Возможные сценарии использования**

 Ранее Aspose.Cells не мог рендерить офисные дополнения при сохранении файла Excel в формат PDF. Теперь Aspose.Cells делает это правильно. Вам не нужно использовать никаких специальных методов или свойств для рендеринга офисных дополнений в итоговом PDF. Просто сохраните файл Excel в формат PDF, и он автоматически отобразит офисные дополнения.

## **Рендеринг офисных надстроек при преобразовании Excel в PDF**

Следующий пример кода сохраняет [образец файла Excel](60489769.xlsx), содержащий офисные дополнения. Посмотрите [выводной PDF, созданный с предыдущей версии, то есть 17.11](60489770.pdf) и [выводной PDF, созданный с новой версии, то есть 17.12 и последующие](60489771.pdf). Вывод предыдущей версии — пустой PDF, а новая версия показывает офисное дополнение.

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderOfficeAdd-Ins.xlsx");
// Load the sample Excel file containing Office Add-Ins
const wb = new AsposeCells.Workbook(filePath);

// Save it to Pdf format
wb.save(`output-${AsposeCells.CellsHelper.getVersion()}.pdf`);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
