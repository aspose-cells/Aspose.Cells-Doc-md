---
title: Просмотры листов с Node.js через C++
linktitle: Представления листа
type: docs
weight: 40
url: /ru/nodejs-cpp/worksheet-views/
description: Эта статья опишет, как использовать Node.js и API Node.js для взаимодействия с предварительным просмотром разрывов страниц книги Excel и листов. Работайте с разделенными панелями, зафиксированными панелями и коэффициентом масштабирования.
---

## **Предпросмотр разрывов страниц**

Все листы могут быть просмотрены в двух режимах:

- Обычный вид.
- Предварительный просмотр разрыва страницы.

Обычно вид — это стандартный режим просмотра листа. Предварительный просмотр разрывов страниц — это режим редактирования, который отображает лист так, как он будет напечатан. Предварительный просмотр показывает, какая часть данных попадет на каждую страницу, чтобы вы могли настроить область печати и разрывы страниц. Используя Aspose.Cells for Node.js via C++, разработчики могут включать режим нормы или предварительного просмотра разрывов страниц.

### **Управление режимами просмотра**

Aspose.Cells предоставляет класс, который представляет файл Microsoft Excel. Класс содержит коллекцию, которая позволяет получить доступ к каждой таблице в файле Excel.

Таблица представлена классом. Класс предоставляет широкий спектр свойств и методов для управления таблицами. Чтобы включить обычный или режим предварительного просмотра разрыва страницы, используйте свойство класса. Это логическое свойство, которое может хранить только значение **true** или **false**.

#### **Включение нормального режима**

Установите таблицу в обычный вид, установив свойство класса в **false**.

#### **Включение предварительного просмотра разрывов страниц**

Установите любую таблицу в режим предварительного просмотра разрыва страницы, установив свойство класса в **true**. Таким образом, таблица переключится из обычного вида в режим предварительного просмотра разрыва страницы.

Приведен полный пример ниже, демонстрирующий, как использовать свойство для включения режима просмотра предварительного просмотра разрыва страницы для первой таблицы файла Excel.

Файл book1.xls открывается созданием экземпляра класса. Просмотр переключается на предварительный просмотр разрыва страницы для первой таблицы, установив свойство в **true**. Измененный файл сохраняется как output.xls.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");


// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Displaying the worksheet in page break preview
worksheet.setIsPageBreakPreview(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Коэффициент масштабирования**

### **Использование Microsoft Excel**

Microsoft Excel предоставляет возможность установить коэффициент масштабирования листа. Эта функция помогает пользователям просматривать содержимое листа в уменьшенном или увеличенном виде. Пользователи могут установить коэффициент масштабирования на любое значение.

### **Aspose.Cells и коэффициент увеличения**

Aspose.Cells позволяет разработчикам установить коэффициент увеличения таблицы.
Aspose.Cells предоставляет класс, который представляет файл Microsoft Excel. Класс содержит коллекцию, которая позволяет получить доступ к каждой таблице в файле Excel.

Таблица представлена классом. Класс предоставляет широкий спектр свойств и методов для управления таблицами. Чтобы установить коэффициент увеличения таблицы, используйте свойство класса. Коэффициент увеличения устанавливается путем назначения числового (целочисленного) значения свойству.

Ниже приведен полный пример, демонстрирующий, как использовать свойство [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) для установки коэффициента масштабирования первого листа файла Excel.

Файл book1.xls открывается путем создания экземпляра класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Коэффициент масштабирования первого листа устанавливается на 75, и измененный файл сохраняется как output.xls.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the zoom factor of the worksheet to 75
worksheet.setZoom(75);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Закрепить области**

### **Использование Microsoft Excel**

Закрепление области экрана - это функция, предоставляемая Microsoft Excel. Закрепление области экрана позволяет выбрать данные, которые останутся видимыми при прокрутке на листе.

### **Aspose.Cells и заморозка панелей**

Aspose.Cells позволяет разработчикам применять замороженные панели к листам во время выполнения.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет широкий диапазон свойств и методов для управления листами. Чтобы настроить закрепление панелей, вызовите метод [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) класса Worksheet. Метод [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) принимает следующие параметры:

- **Строка**, индекс строки, с которой начнется закрепление.
- **Столбец**, индекс столбца, с которого начнется закрепление.
- **Закрепленные строки**, количество видимых строк в верхней панели.
- **Закрепленные столбцы** — количество видимых столбцов в левой панели.

Файл book1.xls открывается путем вызова конструктора класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) при его создании, и в первом листе замораживается несколько строк и столбцов. Измененный файл сохраняется как output.xls.

Ниже приведен полный пример, показывающий, как использовать метод [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) для замораживания строк и столбцов (начиная с C4, представленного 4-й строкой и 3-й колонкой, где строки и столбцы начинаются с индекса 0) первого листа файла Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Applying freeze panes settings
worksheet.freezePanes(3, 2, 3, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));

// The file stream will be automatically closed after saving
```

## **Разделение областей экрана**

Если вам нужно разделить экран для получения двух разных представлений на одном листе, используйте разделение областей экрана. Microsoft Excel предлагает очень удобную функцию, которая позволяет просматривать более одной копии вашего листа и прокручивать каждую область листа независимо: разделение областей экрана.

Разделы работают одновременно. Если вы внесете изменение в один, изменение одновременно появится в другом. Aspose.Cells предоставляет функцию разделения панелей для пользователей.

### **Применение и удаление разделенных панелей**

#### **Разделение панелей**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) , который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) предоставляет широкий спектр свойств и методов для управления файлом Excel. Чтобы реализовать разделенные виды, используйте метод [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) класса [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--). Чтобы удалить разделение панелей, используйте метод [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--).

В примере мы используем простой шаблонный файл, который загружается, затем устанавливается функция разделенных панелей для ячейки на первом листе. Обновленный файл сохраняется.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const book = new AsposeCells.Workbook(filePath);

// Set the active cell
book.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
book.getWorksheets().get(0).split();

// Save the excel file
book.save(path.join(dataDir, "output.xls"));
```

После выполнения вышеуказанного кода сгенерированный файл будет иметь разделенный вид.

#### **Удаление панелей**

Удаление разделенных панелей с использованием метода [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const workbook = new AsposeCells.Workbook(filePath);

// Set the active cell
workbook.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
workbook.getWorksheets().get(0).removeSplit();

// Save the excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Продвинутые темы**
- [Скрытие отображения нулевых значений в таблице](/cells/ru/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Установить цвет вкладки листа](/cells/ru/nodejs-cpp/set-worksheet-tab-color/)
- [Показывать и скрывать линии сетки и заголовки строк и столбцов](/cells/ru/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [Показывать и скрывать строки, столбцы и полосы прокрутки](/cells/ru/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [Показать и скрыть листы и вкладки](/cells/ru/nodejs-cpp/show-and-hide-worksheets-and-tabs/)
- [Показывать формулы вместо значений в листе](/cells/ru/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [Использовать параметры проверки ошибок](/cells/ru/nodejs-cpp/use-error-checking-options/)

