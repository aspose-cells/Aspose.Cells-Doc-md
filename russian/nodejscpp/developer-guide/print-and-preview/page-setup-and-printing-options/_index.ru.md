---  
title: Настройка страниц и параметры печати с помощью Node.js через C++  
linktitle: Настройка страницы и параметры печати  
type: docs  
weight: 60  
url: /ru/nodejs-cpp/page-setup-and-printing-options/  
---  

{{% alert color="primary" %}}  
Иногда разработчики нуждаются в настройке страницы и параметров печати для управления процессом печати. Настройки страницы и параметры печати предлагают различные варианты и полностью поддерживаются в Aspose.Cells.  

В этой статье показано, как создать консольное приложение в Node.js через C++, применить настройки страниц и параметры печати к листу с помощью API Aspose.Cells.  
{{% /alert %}}  

## **Работа с настройками страницы и печати**  

Для этого примера мы создали рабочую книгу в Microsoft Excel и использовали Aspose.Cells для установки настроек страницы и параметров печати.  

### **Использование Aspose.Cells для установки параметров настройки страницы**  

Сначала создайте простой лист в Microsoft Excel. Затем примените к нему настройки страницы. При выполнении кода настройки страницы изменяются, как показано на скриншоте ниже.  

|**Выходной файл.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|  

1. Создайте лист с данными в Microsoft Excel:  
   1. Откройте новую книгу в Microsoft Excel.  
   1. Добавьте некоторые данные.  
1. Установите параметры настройки страницы:  
   Примените параметры настройки страницы к файлу. Ниже приведено скриншоты параметров по умолчанию, до применения новых параметров.  

|**Параметры настройки страницы по умолчанию.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|  

1. Скачайте и установите Aspose.Cells:  
   1. [Скачать](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++.  
   1. Установите его на вашем компьютере для разработки.  
      Все компоненты Aspose, установленные, работают в режиме оценки. Режим оценки не имеет ограничения по времени и только внедряет водные знаки в созданные документы.  
1. Создайте проект:  
   1. Запустите вашу среду Node.js.  
   1. Создайте новое консольное приложение.  
      Этот пример покажет консольное приложение Node.js, но вы также можете использовать привязки C++.  
1. Добавьте ссылки:  
   1. В этом примере используется Aspose.Cells, поэтому добавьте ссылку на этот компонент в проект. Например:  
      …\Program Files\Aspose\Aspose.Cells\Bin\Node.js-Cpp\Aspose.Cells.node  
1. Напишите приложение, которое вызывает API:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "CustomerReport.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the orientation to Portrait
worksheet.getPageSetup().setOrientation(AsposeCells.PageOrientationType.Portrait);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Setting the paper size to A4
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Setting the print quality of the worksheet to 1200 dpi
worksheet.getPageSetup().setPrintQuality(1200);

// Setting the first page number of the worksheet pages
worksheet.getPageSetup().setFirstPageNumber(2);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_out.xlsx"));
```  

### **Настройка параметров печати**  

Настройки настройки страницы также предоставляют несколько параметров печати (также называемых параметрами листа), которые позволяют пользователям контролировать печать страниц листа. Они позволяют пользователям:  

- Выбирать конкретную область печати листа.
- Напечатать заголовки.
- Напечатать сетку.
- Печать верхних заголовков строк / столбцов.
- Достичь чернового качества.
- Напечатать примечания.
- Напечатать ошибки ячеек.
- Определить порядок страниц.  

Приведенный ниже пример применяет параметры печати к файлу, созданному в приведенном выше примере (PageSetup.xls). Снимок экрана ниже показывает параметры печати по умолчанию до применения новых параметров.  

|**Входной документ**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|  
Выполнение кода изменяет параметры печати.  

|**Выходной файл**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageSetup.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

const pageSetup = worksheet.getPageSetup();

// Specifying the cells range (from A1 cell to E30 cell) of the print area
pageSetup.setPrintArea("A1:E30");

// Defining column numbers A & E as title columns
pageSetup.setPrintTitleColumns("$A:$E");

// Defining row numbers 1 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_Print_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
