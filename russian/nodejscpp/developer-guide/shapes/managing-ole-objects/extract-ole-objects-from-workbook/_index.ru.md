---  
title: Извлечение OLE объектов из рабочей книги с помощью Node.js через C++  
linktitle: Извлечение объектов OLE из книги  
type: docs  
weight: 110  
url: /ru/nodejs-cpp/extract-ole-objects-from-workbook/  
---  

{{% alert color="primary" %}}  
Иногда необходимо извлечь OLE объекты из рабочей книги. Aspose.Cells поддерживает извлечение и сохранение этих OLE объектов.

Эта статья показывает, как создать консольное приложение на Node.js через C++ и извлечь разные OLE объекты из рабочей книги с помощью нескольких простых строк кода.  
{{% /alert %}}  

## **Извлечение объектов OLE из книги**  

### **Создание шаблонной книги Excel**  

1. Создайте рабочую книгу в Microsoft Excel.  
1. Добавьте документ Microsoft Word, рабочую книгу Excel и PDF-документ как OLE объекты на первый лист.  

|**Образец документа с объектами OLE (OleFile.xls)**|  
| :- |  
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|  

Затем извлеките OLE объекты и сохраните их на жесткий диск с их соответствующими типами файлов.  

### **Загрузите и установите Aspose.Cells**  

1. [Скачайте Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Установите его на вашем компьютере для разработки.  

Все компоненты Aspose, установленные, работают в режиме оценки. Режим оценки не имеет ограничения по времени и только внедряет водные знаки в созданные документы.  

### **Создайте проект**  

Запустите **Node.js** и создайте новое консольное приложение. Этот пример покажет консольное приложение Node.js, но вы также можете использовать любую среду, совместимую с JavaScript.  

1. Добавьте зависимости  
   1. Добавьте ссылку на компонент Aspose.Cells в ваш проект, например, включите пакет с помощью функции `require`:  
   ```javascript  
   const { Cells } = require("aspose.cells");  
   ```

### **Извлечение объектов OLE**  

Следующий код выполняет фактическую работу по поиску и извлечению объектов OLE. Объекты OLE (DOC, XLS и PDF файлы) сохраняются на диск.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "oleFile.xlsx"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object in the worksheet.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);
// Specify the output filename.
let fileName = path.join(dataDir, "outOle" + i + ".");
// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Excel97To2003:
fileName += "Xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "Ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "Pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "Jpg";
break;
default:
//........
break;
}
// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = Buffer.from(ole.getObjectData());
if (ole.getObjectData() != null) {
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, "outOle" + i + ".out.xlsx"));
}
} else {
if (ole.getObjectData() != null) {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
