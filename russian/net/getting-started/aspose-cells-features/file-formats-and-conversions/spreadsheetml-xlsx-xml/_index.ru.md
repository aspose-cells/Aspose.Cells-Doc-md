---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /ru/net/spreadsheetml-xlsx-xml/
---

## **О SpreadsheetML**
SpreadsheetML - это название семейства форматов на основе XML для документов электронных таблиц. Существует несколько версий SpreadsheetML:

1. Версия SpreadsheetML 2003 была введена в Microsoft Word 2003. SpreadsheetML был значительным шагом Microsoft в направлении открытости формата документа.
1. [Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML) - новый формат на основе XML, введенный в приложения Microsoft Office 2007. Office Open XML - это контейнерный формат для нескольких специализированных языков разметки на основе XML. Версия SpreadsheetML 2007 - это язык разметки, используемый Microsoft Office Excel 2007 для хранения своих документов.
1. Microsoft Excel 2010 сохраняет документы в версии SpreadsheetML 2010, как определено в обновленном стандарте OOXML.
## **SpreadsheetML в Aspose.Cells**
Доступно три «версии» формата SpreadsheetML:

|**Версия SpreadsheetML**|**Применимый стандарт/спецификация**|**Поддерживается в Aspose.Cells for .NET**|
| :- | :- | :- |
|Microsoft Excel 2003|[Microsoft Excel 2003 XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|Да|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|Да|
|Microsoft Excel 2010|OOXML ISO/IEC DIS 29500|Да|
|Microsoft Excel 2013|OOXML ISO/IEC DIS 29500|Да|
Документы OOXML SpreadsheetML чаще всего поставляются в виде файлов XLSX, которые являются ZIP-архивами. Кроме XLSX. Aspose.Cells обеспечивает обширную поддержку загрузки, сохранения и преобразования документов SpreadsheetML. Такая всеобъемлющая реализация возможна, поскольку Aspose.Cells был разработан с учетом структуры документов Microsoft Excel (а SpreadsheetML известен своими внутренними представлениями документов Microsoft Excel).
### **OOXML - открытый формат, зачем использовать Aspose.Cells?**
Действительно, технология Office Open XML позволяет создавать приложения для обработки и генерации документов с использованием только классов XML без привлечения сторонних библиотек, таких как Aspose.Cells. Однако мы настоятельно рекомендуем всё же использовать Aspose.Cells при работе с документами OOXML, вместо работы через XML или другие библиотеки.

Спецификация OOXML содержит несколько тысяч страниц. Открытость и стандартизация не означают простоты. Для корректной обработки или генерации документов OOXML необходимо тщательно изучить формат.

Помимо упрощения корректной обработки и создания допустимых документов, Aspose.Cells предоставляет следующие важные функции, которых у вас не будет при работе с файлами OOXML непосредственно через XML или другие сторонние библиотеки:

- Качественные преобразования между многими популярными форматами Excel, включая преобразование в PDF, HTML, TIFF и печать.
- Возможность создания документов из фрагментов, из одного или нескольких документов, автоматическое слияние данных по стилистическому форматированию, диаграммам и графикам.
- Функции высокого уровня, такие как, импорт данных из различных источников данных, включая массив, ArrayList, DataTable, DataColumn, DataGrid, DataView и DataReader, или экспорт данных для заполнения DataTable или массива всего одной строкой кода.
- Надежный расчетный движок формул, поддерживающий практически все стандартные и продвинутые функции Microsoft Excel.

Рассмотрим следующий пример. Некоторые ячейки содержат текст «Привет, мир» жирным шрифтом. Теперь представьте, что вам необходимо написать программу, которая ищет все фразы «Привет, мир» в таблице и заменяет их на «До свидания, Земля».
### **Фрагмент документа Office Open XML**
**XML**

{{< highlight csharp >}}

 <?xml version="1.0" encoding="UTF-8" standalone="yes" ?>

\- <worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">

  <dimension ref="A1:M184" />

\- <sheetViews>

\- <sheetView tabSelected="1" workbookViewId="0">

  <selection activeCell="H27" sqref="H27" />

  </sheetView>

  </sheetViews>

  <sheetFormatPr defaultRowHeight="15" />

\- <sheetData>

\- <row r="1" spans="1:7">

\- <c r="A1" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="11" spans="1:7">

\- <c r="D11" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="15" spans="1:7">

\- <c r="G15" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="21" spans="2:7">

\- <c r="G21" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="25" spans="2:7">

\- <c r="F25" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="31" spans="2:7">

\- <c r="B31" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="34" spans="6:13">

\- <c r="M34" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="38" spans="6:13">

\- <c r="F38" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="117" spans="8:8">

\- <c r="H117" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="184" spans="8:8">

\- <c r="H184" s="1" t="s">

  <v>0</v>

  </c>

  </row>

  </sheetData>

  <pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3" />

</worksheet>



{{< /highlight >}}


Реализация даже простой операции поиска и замены в документе Office Open XML затруднительна. Наш совет: помните, что открытое и стандартное не означает простое, используйте Aspose.Cells.
{{< app/cells/assistant language="csharp" >}}
