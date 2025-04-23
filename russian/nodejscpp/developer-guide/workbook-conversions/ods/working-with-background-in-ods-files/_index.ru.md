---  
title: Работа с фоном в файлах ODS с Node.js через C++  
linktitle: Работа с фоном в файлах ODS  
type: docs  
weight: 150  
url: /ru/nodejs-cpp/working-with-background-in-ods-files/  
description: Узнайте, как управлять фонами в файлах ODS с помощью Aspose.Cells for Node.js via C++.  
---  

## **Фон в файлах ODS**  

Фон можно добавлять к листам в файлах ODS. Фон может быть цветным или графическим. Фон не виден при открытии файла, но если файл распечатать в формате PDF, фон будет виден в полученном PDF. Фон также виден в диалоге предварительного просмотра печати.  

Aspose.Cells for Node.js via C++ предоставляет возможность читать информацию о фоне и добавлять фон в файлы ODS.  

## **Чтение информации о фоне из файла ODS**  

Aspose.Cells for Node.js via C++ предоставляет класс [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) для управления фоном в файлах ODS. Следующий пример демонстрирует использование класса [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) для загрузки исходного файла ODS и чтения информации о фоне. Обратите внимание на вывод в консоль, генерируемый этим кодом.  

### **Образец кода**  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load source Excel file
const filePath = path.join(sourceDir, "GraphicBackground.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

const background = worksheet.getPageSetup().getODSPageBackground();

console.log("Background Type: " + background.getType().toString());
console.log("Background Position: " + background.getGraphicPositionType().toString());

// Save background image
const imagePath = outputDir + "background.jpg";
fs.writeFileSync(imagePath, Buffer.from(background.getGraphicData()));
```  

### **Вывод в консоль**  

{{< highlight javascript >}}  
Background Type: Graphic  
Background Position: CenterCenter  
{{< /highlight >}}  

## **Добавить цветной фон в файл ODS**  

Aspose.Cells for Node.js via C++ предоставляет класс [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) для управления фоном в файлах ODS. Следующий пример показывает использование свойства [**OdsPageBackground.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getColor--) для добавления цветового фона в файл ODS. Также смотрите файл [output ODS](90112031.ods), созданный этим кодом.  

### **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 0).putValue(1);
worksheet.getCells().get(1, 0).putValue(2);
worksheet.getCells().get(2, 0).putValue(3);
worksheet.getCells().get(3, 0).putValue(4);
worksheet.getCells().get(4, 0).putValue(5);
worksheet.getCells().get(5, 0).putValue(6);
worksheet.getCells().get(0, 1).putValue(7);
worksheet.getCells().get(1, 1).putValue(8);
worksheet.getCells().get(2, 1).putValue(9);
worksheet.getCells().get(3, 1).putValue(10);
worksheet.getCells().get(4, 1).putValue(11);
worksheet.getCells().get(5, 1).putValue(12);

const background = worksheet.getPageSetup().getODSPageBackground();

background.setColor(AsposeCells.Color.Azure);
background.setType(AsposeCells.OdsPageBackgroundType.Color);

workbook.save(outputDir + "ColoredBackground.ods", AsposeCells.SaveFormat.Ods);
```  

## **Добавить графический фон в файл ODS**  

Aspose.Cells for Node.js via C++ предоставляет класс [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) для управления фоном в файлах ODS. Следующий пример демонстрирует использование свойства [**OdsPageBackground.getGraphicData()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getGraphicData--) для добавления графического фона в файл ODS. Обратите внимание на файл [output ODS](90112030.ods), созданный этим кодом.  

### **Образец кода**  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 0).putValue(1);
worksheet.getCells().get(1, 0).putValue(2);
worksheet.getCells().get(2, 0).putValue(3);
worksheet.getCells().get(3, 0).putValue(4);
worksheet.getCells().get(4, 0).putValue(5);
worksheet.getCells().get(5, 0).putValue(6);
worksheet.getCells().get(0, 1).putValue(7);
worksheet.getCells().get(1, 1).putValue(8);
worksheet.getCells().get(2, 1).putValue(9);
worksheet.getCells().get(3, 1).putValue(10);
worksheet.getCells().get(4, 1).putValue(11);
worksheet.getCells().get(5, 1).putValue(12);

const background = worksheet.getPageSetup().getODSPageBackground();

background.setType(AsposeCells.OdsPageBackgroundType.Graphic);
background.setGraphicData(fs.readFileSync(path.join(sourceDir, "background.jpg")));
background.setGraphicType(AsposeCells.OdsPageBackgroundGraphicType.Area);

workbook.save(outputDir + "GraphicBackground.ods", AsposeCells.SaveFormat.Ods);
```  

