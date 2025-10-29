---  
title: Поддержка немецкой локализации в именованных диапазонах с помощью Node.js через C++  
linktitle: Поддержка немецкой локали в формулах для именованных диапазонов  
type: docs  
weight: 60  
url: /ru/nodejs-cpp/support-for-german-locale-in-named-range-formulae/  
description: Узнайте, как поддерживать немецкую локализацию в именованных диапазонах, используя Aspose.Cells for Node.js via C++.  
---  

Английские формулы записаны в именованные области. Этот файл Excel можно открыть в среде, где настроена немецкая локализация системы, однако английская формула будет переведена на немецкий язык. Ниже приводится пример этой функции; для ее работы необходимо установить Excel на немецком языке и настроить системную локаль на немецкую.  

Образец файла для тестирования этой функции можно загрузить по следующей ссылке:  

[sampleNamedRangeTest.xlsm](73990165.xlsm)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
const fs = require("fs");

const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNamedRangeTest.xlsm");
const outputFilePath = path.join(dataDir, "sampleOutputNamedRangeTest.xlsm");

const wb = new AsposeCells.Workbook();
wb.save(sourceFilePath);

const name = "HasFormula";
const value = "=GET.CELL(48, INDIRECT(\"ZS\",FALSE))";

const wbSource = new AsposeCells.Workbook(sourceFilePath);
const wsCol = wbSource.getWorksheets();

const nameIndex = wsCol.getNames().add(name);
const namedRange = wsCol.getNames().get(nameIndex);
namedRange.setRefersTo(value);

wbSource.save(outputFilePath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
