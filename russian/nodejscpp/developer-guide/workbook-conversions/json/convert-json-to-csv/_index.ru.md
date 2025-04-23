---  
title: Конвертировать JSON в CSV с помощью Node.js через C++  
linktitle: Конвертировать JSON в CSV  
type: docs  
weight: 210  
url: /ru/nodejs-cpp/convert-json-to-csv/  
description: Узнайте, как преобразовать JSON данные в CSV с помощью Aspose.Cells for Node.js via C++.  
---  

## **Преобразовать JSON в CSV**  

Aspose.Cells поддерживает преобразование простого и вложенного JSON в CSV. Для этого API предоставляет [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) и [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) классы. Класс [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) предоставляет параметры для раскладки JSON, такие как [**JsonLayoutOptions.getArrayAsTable()**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions/#getArrayAsTable--) (обрабатывает массив как таблицу). Класс [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) обрабатывает JSON с использованием настроек раскладки, задаваемых классом [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions).  

Следующий пример демонстрирует использование классов [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) и [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) для загрузки [исходного JSON файла](104398869.json) и генерации [выходного CSV файла](104398870.csv).  

### **Образец кода**  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");


// Create sample JSON if missing
const jsonPath = path.join(sourceDir, "SampleJson.json");

// Read JSON file
const str = fs.readFileSync(jsonPath, "utf-8");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();

// Set JsonLayoutOptions
const importOptions = new AsposeCells.JsonLayoutOptions();
importOptions.setConvertNumericOrDate(true);
importOptions.setArrayAsTable(true);
importOptions.setIgnoreTitle(true);
AsposeCells.JsonUtility.importData(str, cells, 0, 0, importOptions);

// Save Workbook
workbook.save(outputDir + "SampleJson_out.csv");
```  

