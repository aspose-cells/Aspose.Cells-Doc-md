---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /ru/net/spreadsheetml-xlsx-xml/
---
## **О SpreadsheetML**
SpreadsheetML — это название семейства форматов электронных таблиц на основе XML. Существует несколько версий SpreadsheetML:

1. SpreadsheetML версия 2003 была введена в Microsoft Word 2003. SpreadsheetML стала важным шагом Microsoft к тому, чтобы сделать формат документа открытым.
1. [Офис OpenXML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML) — это новый формат на основе XML, представленный в Microsoft приложениях Office 2007. Office Open XML — это контейнерный формат для нескольких специализированных языков разметки на основе XML. SpreadsheetML версии 2007 — это язык разметки, используемый Microsoft Office Excel 2007 для хранения документов.
1. Microsoft Excel 2010 хранит документы в версии SpreadsheetML 2010, как определено в обновленном стандарте OOXML.
## **SpreadsheetML в Aspose.Cells**
Доступны три «версии» SpreadsheetML:

|**SpreadsheetML «Версия»**|**Применимый стандарт/спецификация**|**Поддерживается в Aspose.Cells for .NET**|
|:- |:- |:- |
|Microsoft Excel 2003|[Microsoft Excel 2003 XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|Да|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|Да|
|Microsoft Excel 2010|OOXML ISO/IEC DIS 29500|Да|
|Microsoft Excel 2013|OOXML ISO/IEC DIS 29500|Да|
Документы OOXML SpreadsheetML чаще всего представляют собой файлы XLSX, которые представляют собой ZIP-пакеты. В дополнение к XLSX. Aspose.Cells предоставляет обширную поддержку для загрузки, сохранения и преобразования SpreadsheetML документов. Такая всеобъемлющая реализация возможна, потому что Aspose.Cells был разработан с учетом структуры Microsoft документов Excel (и известно, что SpreadsheetML имитирует внутреннее представление Microsoft документов Excel).
### **OOXML открыт, зачем использовать Aspose.Cells?**
Это правда, что технология Office Open XML позволяет создавать приложения для обработки и создания документов, используя только классы XML, не полагаясь на сторонние библиотеки, такие как Aspose.Cells. работать с документами OOXML, а не через XML или другие библиотеки.

Спецификация OOXML состоит из нескольких тысяч страниц. Быть открытым и стандартным не означает быть простым. Чтобы правильно обрабатывать или генерировать документы OOXML, необходимо хорошо изучить формат.

Помимо упрощения правильной обработки и создания действительных документов, Aspose.Cells предоставляет следующие важные функции, которые недоступны при работе с файлами OOXML напрямую через XML или другие сторонние библиотеки:

- Качественные преобразования между многими популярными форматами Excel, включая преобразование в PDF, HTML, TIFF и печать.
- Возможность построения документов из фрагментов, из одного или нескольких документов, при этом автоматически объединяя данные по стилистическому форматированию, диаграммам и графикам.
- Функции высокого уровня, такие как импорт данных из различных источников данных, включая Array, ArrayList, DataTable, DataColumn, DataGrid, DataView и DataReader, или экспорт данных для заполнения DataTable или Array всего одной строкой кода.
- Надежный механизм расчета формул, который поддерживает почти все стандартные и расширенные функции Excel Microsoft.

Рассмотрим следующий пример. Некоторые ячейки содержат текст «Hello World», выделенный жирным шрифтом. Теперь представьте, что вам нужно написать программу, которая ищет все фразы «Hello World» на листе и заменяет их на «До свидания, Земля».
### **Фрагмент документа Office Open XML**
**XML**

{{< highlight "csharp" >}}

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


Реализовать даже простую операцию поиска и замены в документе Office Open XML сложно. Наш совет: помните, что открытый и стандартный не значит простой, и звоните по телефону Aspose.Cells.
