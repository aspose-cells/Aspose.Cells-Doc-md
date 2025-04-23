---  
title: Управление объектами OLE с помощью Node.js через C++  
linktitle: Управление объектами OLE  
type: docs  
weight: 50  
url: /ru/nodejs-cpp/managing-ole-objects/  
description: Узнайте, как управлять объектами OLE в Aspose.Cells for Node.js via C++. Добавляйте, извлекайте и манипулируйте объектами OLE внутри листов.  
---  

## **Введение**  

OLE (Object Linking and Embedding) — это платформа для технологии составных документов. Вкратце, составной документ — это что-то вроде рабочего стола, который может содержать визуальные и информационные объекты всех видов: текст, календари, анимации, звук, движущееся видео, 3D, постоянно обновляемые новости, элементы управления и т.д. Каждый объект рабочего стола — это независимый программный элемент, который может взаимодействовать с пользователем и также обмениваться данными с другими объектами на рабочем столе.  

OLE поддерживается многими программами и используется для обеспечения совместного использования контента, созданного в одной программе, в другой. Например, вы можете вставить документ Microsoft Word в Microsoft Excel. Чтобы посмотреть, какие типы контента можно вставлять, нажмите **Объект** в меню **Вставка**. В списке **Тип объекта** отображаются только программы, установленные на компьютере и поддерживающие объекты OLE.  

### **Вставка объектов OLE в лист**  

Aspose.Cells for Node.js via C++ поддерживает добавление, извлечение и манипуляцию объектами OLE в листах. По этой причине Aspose.Cells содержит класс [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection), используемый для добавления нового объекта OLE в коллекцию. Другой класс, [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), представляет объект OLE. Он содержит некоторые важные члены:  

- Свойство [**getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) задает изображение (иконку) в виде массива байтов. Это изображение отображается для отображения OLE-объекта в листе.  
- Свойство [**getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) задает данные объекта в виде массива байтов. Эти данные будут отображаться в соответствующей программе при двойном щелчке по иконке OLE-объекта.  

Нижеприведенный пример показывает, как добавить объект(ы) OLE в лист Excel.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const filePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(filePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Извлечение объектов OLE в книге**  

В следующем примере показано, как извлекать объекты OLE в книге. Пример получает различные объекты OLE из существующего файла XLS и сохраняет различные файлы (DOC, XLS, PPT, PDF и т. д.) на основе типа формата файла объекта OLE.  

После выполнения кода мы можем сохранить разные файлы на основе их соответствующих типов формата объектов OLE.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);

// Specify the output filename.
let fileName = path.join(dataDir, `ole_${i}.`);

// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Xlsx:
fileName += "xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "jpg";
break;
default:
//........
break;
}

// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = new Uint8Array(ole.getObjectData());
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, `Excel_File${i}.out.xlsx`));
}

// Create the files based on the oleobject format types.
else {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
```  

### **Извлечение встроенного файла MOL**  

Aspose.Cells for Node.js via C++ поддерживает извлечение объектов необычных типов, таких как MOL (файл молекулярных данных, содержащий информацию о атомах и связях). Следующий пример демонстрирует извлечение встроенного файла MOL и сохранение его на диск с помощью этого [пример файла excel](94896196.xlsx).  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "EmbeddedMolSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
let index = 1;

const worksheets = workbook.getWorksheets();
const sheetCount = worksheets.getCount();
for (let i = 0; i < sheetCount; i++) {
const sheet = worksheets.get(i);
const oles = sheet.getOleObjects();
const oleCount = oles.getCount();
for (let j = 0; j < oleCount; j++) {
const ole = oles.get(j);
const fileName = path.join(outputDir, `OleObject${index}.mol`);
const fileStream = fs.createWriteStream(fileName);
fileStream.write(Buffer.from(ole.getObjectData()));
fileStream.end();
index++;
}
}
```  

## **Продвинутые темы**  
- [Доступ и изменение отображаемой метки связанного объекта OLE](/cells/ru/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [Автоматическое обновление объекта OLE через Microsoft Excel с помощью Aspose.Cells](/cells/ru/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [Извлечение объектов OLE из книги](/cells/ru/nodejs-cpp/extract-ole-objects-from-workbook/)  
- [Получение или установка идентификатора класса встроенного объекта OLE](/cells/ru/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Вставка файла WAV в качестве объекта OLE](/cells/ru/nodejs-cpp/inserting-a-wav-file-as-an-ole-object/)  


