---  
title: Показать и скрыть сетку и заголовки строк и столбцов с помощью Node.js через C++  
linktitle: Показывать и скрывать сетку и заголовки строк и столбцов  
type: docs  
weight: 30  
url: /ru/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/  
description: В этой статье представлен пример кода для использования API Node.js через C++ для программного скрытия или отображения сетки, заголовков строк и столбцов листа Excel.  
---  

{{% alert color="primary" %}}  
Aspose.Cells поддерживает скрытие и показ сетки листа Excel, которая обычно видна. Он также обеспечивает контроль видимости заголовков строк и столбцов листа.  
{{% /alert %}}  

## **Отображение и скрытие линий сетки**  

Все листы Excel по умолчанию имеют сетку. Они помогают выделять клетки для удобства ввода данных. Сетка позволяет нам просматривать лист как коллекцию клеток, каждая клетка легко идентифицируется.  

### **Управление видимостью сетки**  

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет разработчикам получать доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет широкий спектр свойств и методов для управления листом. Чтобы управлять видимостью линий сетки, используйте свойство [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--). [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) — логическое свойство, означающее, что оно может хранить только значение **true** или **false**.  

#### **Отображение линий сетки**  

Делайте линии сетки видимыми, установив свойство [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) в значение **true**.  

#### **Скрытие линий сетки**  

Спрячьте линии сетки, установив свойство [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) в значение **false**.  

Полный пример приведен ниже, он демонстрирует использование свойства [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) путем открытия файла Excel (book1.xls), скрытия линий сетки на первом листе и сохранения измененного файла как output.xls.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileData = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file data
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the grid lines of the first worksheet of the Excel file
worksheet.setIsGridlinesVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Показывать и скрывать заголовки строк и столбцов**  

Все листы Excel состоят из клеток, расположенных в строках и столбцах. Все строки и столбцы имеют уникальные значения, которые используются для их идентификации и для идентификации отдельных клеток. Например, строки нумеруются - 1, 2, 3, 4 и т. д., а столбцы упорядочены по алфавиту - A, B, C, D и т. д. Значения строк и столбцов отображаются в заголовках. С помощью Aspose.Cells разработчики могут управлять видимостью этих заголовков строк и столбцов.  

### **Управление видимостью листов**  

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет разработчикам получать доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет широкий спектр свойств и методов для управления листом. Чтобы управлять видимостью заголовков строк и столбцов, используйте свойство [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--). [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) — логическое свойство, означающее, что оно может хранить только значение **true** или **false**.  

#### **Отображение заголовков строк/столбцов**  

Делайте заголовки строк и столбцов видимыми, установив свойство [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) в значение **true**.  

#### **Скрытие заголовков строк/столбцов**  

Спрячьте заголовки строк и столбцов, установив свойство [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) в значение **false**.  

Полный пример приведен ниже, он показывает, как использовать свойство [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) путем открытия файла Excel (book1.xls), скрытия заголовков строк и столбцов на первом листе и сохранения измененного файла как output.xls.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file path
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the headers of rows and columns
worksheet.setIsRowColumnHeadersVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
Также возможно использовать методы [**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) и [**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) класса [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) для отображения нескольких строк и столбцов.  
{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
