---  
title: Показать и скрывать листы и вкладки с помощью Node.js через C++  
linktitle: Показывать и скрывать рабочие листы и вкладки  
type: docs  
weight: 10  
url: /ru/nodejs-cpp/show-and-hide-worksheets-and-tabs/  
description: В этой статье представлен пример кода для использования API Node.js или библиотеки Node.js для программного отображения и скрытия листа Excel. Также показано, как показывать и скрывать вкладки рабочей книги Excel.  
---  

{{% alert color="primary" %}}  
Aspose.Cells позволяет пользователю показывать и скрывать элементы книги, включая рабочие листы и вкладки.  
{{% /alert %}}  

## **Показать и скрыть лист**  

Файл Excel может содержать один или более листов. Всякий раз, когда мы создаем файл Excel, мы добавляем листы в файл Excel, в котором работаем. Каждый лист в файле Excel независим от другого листа и имеет свои собственные данные и настройки форматирования и т. д. Иногда разработчики могут захотеть скрыть несколько листов и сделать другие видимыми в файле Excel по своему усмотрению. Таким образом, **Aspose.Cells** позволяет разработчикам контролировать видимость листов в их файлах Excel.  

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), для доступа к каждому листу файла Excel.  

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет широкий набор свойств и методов для управления листами. Для управления видимостью листа используйте свойство [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) класса [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) — логическое свойство, которое может хранить только значение **true** или **false**.  

### **Сделать лист видимым**  

Сделать лист видимым, установив свойство [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) класса [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) в **true**.  

### **Скрыть лист**  

Скрыть лист, установив свойство [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) класса [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) в **false**.  

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object with opening the Excel file through the file stream
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(chunks)); // Fixed from stream to Blob

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the first worksheet of the Excel file
worksheet.setIsVisible(false);

// Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

## **Показывать и скрывать вкладки**  

Если вы внимательно посмотрите внизу файла Microsoft Excel, вы увидите ряд элементов управления. Среди них:  

- Вкладки листов.  
- Кнопки прокрутки вкладок.  

Вкладки представляют листы Excel-файла. Щелкните на любой вкладке, чтобы переключиться на этот лист. Чем больше листов в книге Excel, тем больше вкладок. Если в Excel-файле большое количество листов, вам понадобятся кнопки для перемещения по ним. Поэтому Microsoft Excel предоставляет кнопки прокрутки вкладок для прокрутки по вкладкам.  

С помощью Aspose.Cells разработчики могут контролировать видимость вкладок листов и кнопок прокрутки в файле Excel.  

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) предлагает широкий набор свойств и методов для управления файлом Excel. Для управления видимостью вкладок в файле Excel разработчики могут использовать свойство [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) — логическое свойство, которое может хранить только значение **true** или **false**.  

### **Отображение вкладок**  

Сделайте вкладки видимыми, установив свойство [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) в **true**.  

### **Скрытие вкладок**  

Скрыть вкладки в файле Excel, установив свойство [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) в **false**.  

Ниже приведен полный пример, который открывает файл Excel (book1.xls), скрывает его вкладки и сохраняет измененный файл как output.xls. После выполнения кода вы увидите, что вкладки книги скрыты.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(false);

// Shows the tabs of the Excel file
// workbook.getSettings().setShowTabs(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

### **Управление Шириной Панели Вкладок**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Loading the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(true);

// Adjusting the sheet tab bar width
workbook.getSettings().setSheetTabBarWidth(800);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
