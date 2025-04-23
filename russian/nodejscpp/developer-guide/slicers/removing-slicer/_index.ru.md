---
title: Удаление сегментатора с помощью Node.js через C++
linktitle: Удаление срезки
type: docs
weight: 30
url: /ru/nodejs-cpp/removing-slicer/
---

## **Возможные сценарии использования**

Если вы хотите удалить сегментатор в Excel, просто выберите его и нажмите кнопку *Delete*. Аналогично, чтобы удалить его программным путём через API Aspose.Cells, используйте метод [**SlicerCollection.remove(Slicer)**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#remove-slicer-). Он удалит сегментатор с листа.

## **Удаление срезки**

Следующий пример кода загружает [пример файла Excel](67338478.xlsx), содержащий существующий сегментатор. Он обращается к сегментаторам, затем удаляет его и сохраняет книгу как [выходной файл Excel](67338477.xlsx). На изображении ниже показан сегментатор, который будет удалён после выполнения примера.

![todo:image_alt_text](removing-slicer_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRemovingSlicer.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Remove slicer.
worksheet.getSlicers().remove(slicer);

// Save the workbook in output XLSX format.
workbook.save("outputRemovingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```
