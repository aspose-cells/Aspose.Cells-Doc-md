---
title: Настройка заголовков и нижних колонтитулов с помощью Node.js через C++
linktitle: Установка заголовков и нижних колонтитулов
type: docs
weight: 30
url: /ru/nodejs-cpp/setting-headers-and-footers/
description: В этой статье объясняется, как программно вставить изображение в заголовок и нижний колонтитул листов Excel с помощью Aspose.Cells for Node.js via C++. 
keywords: вставить изображение в заголовок и нижний колонтитул Excel Node.js через C++, задать команды скрипта заголовка и нижнего колонтитула Excel Node.js через C++
---

{{% alert color="primary" %}}

Заголовки и нижние колонтитулы - это строки текста, отображаемые ниже верхнего поля или выше нижнего поля соответственно. Также возможно добавить заголовки и нижние колонтитулы к листам. Заголовки и нижние колонтитулы могут использоваться для отображения полезной информации, такой как номер страницы, имя автора, название темы или дата и время. Заголовки и нижние колонтитулы управляются с использованием настроек разметки страницы.

{{% /alert %}}

## **Настройка колонтитулов и подвалов**

Aspose.Cells for Node.js via C++ позволяет добавлять заголовки и нижние колонтитулы в листы во время выполнения, но мы рекомендуем вручную настраивать заголовки и нижние колонтитулы в предварительно оформленном файле для печати. Вы можете использовать Microsoft Excel как инструмент пользовательского интерфейса для установки заголовков и нижних колонтитулов, чтобы сэкономить время и усилия. Aspose.Cells может импортировать файл и сохранять настройки.

Чтобы добавить верхние и нижние колонтитулы во время выполнения, Aspose.Cells предоставляет специальные вызовы API и команды сценариев для форматирования верхних и нижних колонтитулов.

### **Скриптовые команды**

Команды сценариев - это специальные команды, которые позволяют задавать форматирование верхних и нижних колонтитулов.

|**Сценарные команды**|**Описание**|
| :- | :- |
|&P|Текущий номер страницы|
|&G|Картинка|
|&N|Общее количество страниц|
|&D|Текущая дата|
|&T|Текущее время|
|&A|Имя листа|
|&F|Имя файла без пути|
|&&Text|Показывает &Text. Например: &&WO будет отображаться как &WO|
|&"\<FontName>"|Представляет имя шрифта. Например: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Представляет имя шрифта со стилем. Например: &"Arial,Bold"|
|&\<FontSize>|Представляет размер шрифта. Например: “&14abc”. Однако, если за этой командой следует обычное число для печати в заголовке, его следует отделить пробелом от размера шрифта. Например: “&14 123”.

### **Установить заголовки и нижние колонтитулы**

Класс [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) предоставляет два метода, [**setHeader(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeader-number-string-) и [**setFooter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooter-number-string-), используемые для добавления заголовка и нижнего колонтитула к листу. Эти методы принимают только два параметра:

- **Раздел** - раздел, куда следует поместить заголовок или колонтитул. Существуют три раздела: слева, по центру и справа, представленные соответственно 0, 1 и 2.
- **Сценарий** - сценарий, используемый для заголовка или колонтитула. В этом сценарии содержатся команды сценариев для форматирования заголовков или колонтитулов.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const excel = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = excel.getWorksheets().get(0).getPageSetup();

// Setting worksheet name at the left section of the header
pageSetup.setHeader(0, "&A");

// Setting current date and current time at the central section of the header
// and changing the font of the header
pageSetup.setHeader(1, "&\"Times New Roman,Bold\"&D-&T");

// Setting current file name at the right section of the header and changing the
// font of the header
pageSetup.setHeader(2, "&\"Times New Roman,Bold\"&12&F");

// Setting a string at the left section of the footer and changing the font
// of a part of this string ("123")
pageSetup.setFooter(0, "Hello World! &\"Courier New\"&14 123");

// Setting the current page number at the central section of the footer
pageSetup.setFooter(1, "&P");

// Setting page count at the right section of footer
pageSetup.setFooter(2, "&N");

// Save the Workbook.
excel.save("SetHeadersAndFooters_out.xls");
```

### **Вставка изображения в заголовок или колонтитул**

Класс [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) имеет два дополнительных метода, [**setHeaderPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeaderPicture-number-numberarray-) и [**setFooterPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooterPicture-number-numberarray-), используемых для вставки изображений в заголовок и нижний колонтитул. Эти методы принимают параметры:

- **Секция** - раздел заголовка или колонтитула, в который будет помещено изображение. Существуют три секции: слева, по центру и справа, представленные значениями 0, 1 и 2 соответственно.
- **Массив байтов** - графические данные (двоичные данные должны быть записаны в буфер массива байтов).

После выполнения нижеприведенного кода и открытия файла проверьте заголовок листа:

1. На меню **Файл** выберите **Настройка страницы**. Будет отображено диалоговое окно.
1. Выберите вкладку **Шапка/Нижний колонтитул**.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a Workbook object
const workbook = new AsposeCells.Workbook();

// Creating a string variable to store the url of the logo/picture
const logoUrl = path.join(dataDir, "aspose-logo.jpg");

// Declaring a byte array
const binaryData = fs.readFileSync(logoUrl);

// Creating a PageSetup object to get the page settings of the first worksheet of the workbook
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the logo/picture in the central section of the page header
pageSetup.setHeaderPicture(1, binaryData);

// Setting the script for the logo/picture
pageSetup.setHeader(1, "&G");

// Setting the Sheet's name in the right section of the page header with the script
pageSetup.setHeader(2, "&A");

// Saving the workbook
workbook.save(path.join(dataDir, "InsertImageInHeaderFooter_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
