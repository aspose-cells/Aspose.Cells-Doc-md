---  
title: Форматирование среза с помощью Node.js через C++  
linktitle: Форматирование фильтра  
type: docs  
weight: 20  
url: /ru/nodejs-cpp/formatting-slicer/  
---  

## **Возможные сценарии использования**  

Вы можете форматировать срез в Microsoft Excel, задавая количество колонок или стиль и др. Aspose.Cells for Node.js via C++ также позволяет делать это с помощью свойств [**Slicer.getNumberOfColumns()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getNumberOfColumns--) и [**Slicer.getStyleType()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getStyleType--).  

## **Форматирование фильтра**  

Пожалуйста, ознакомьтесь с следующим кодом. Он загружает [образец файла Excel](67338473.xlsx), содержащий срезку. Он получает доступ к срезке, задает количество столбцов и тип стиля, а затем сохраняет его как [файл Excel вывода](67338474.xlsx). На скриншоте показано, как выглядит срезка после выполнения образца кода.  

![todo:image_alt_text](formatting-slicer_1.png)  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFormattingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Set the number of columns of the slicer.
slicer.setNumberOfColumns(2);

// Set the type of slicer style.
slicer.setStyleType(AsposeCells.SlicerStyleType.SlicerStyleLight6);

// Save the workbook in output XLSX format.
wb.save("outputFormattingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
