---
title: Экспорт данных из листа в .NET
linktitle: Экспорт данных из листа
type: docs
weight: 180
url: /ru/net/export-data-from-worksheet/
description: В этой статье объясняется, как экспортировать или импортировать данные из листа в объект datatable с использованием C#.
keywords: C# Export Data from Worksheet, C# Export Data to DataTable, Columns Containing Strongly Typed Data, Columns Containing Non Strongly Typed Data, C# Export Range with flag to skip column name, C# How to Export Range with Header.
---

## Обзор

В этой статье объясняется, как экспортировать данные вашего листа в объект DataTable с использованием C#. Она охватывает следующие темы

_Формат_: **Excel**
- [C# Excel в DataTable](#csharp-excel-to-datatable)
- [C# Конвертировать Excel в DataTable](#csharp-convert-excel-to-datatable)
- [C# Импортировать Excel в DataTable](#csharp-import-excel-to-datatable)
- [C# Экспортировать в DataTable из Excel](#csharp-export-to-datatable-from-excel)

_Формат_: **XLS**
- [C# XLS в DataTable](#csharp-xls-to-datatable)
- [C# Конвертировать XLS в DataTable](#csharp-convert-xls-to-datatable)
- [C# Импортировать XLS в DataTable](#csharp-import-xls-to-datatable)
- [C# Экспортировать в DataTable из XLS](#csharp-export-to-datatable-from-xls)

_Формат_: **XLSX**
- [C# XLSX в DataTable](#csharp-xlsx-to-datatable)
- [C# Преобразовать XLSX в DataTable](#csharp-convert-xlsx-to-datatable)
- [C# Импортировать XLSX в DataTable](#csharp-import-xlsx-to-datatable)
- [C# Экспорт в DataTable из XLSX](#csharp-export-to-datatable-from-xlsx)

_Формат_: **ODS**
- [C# ODS в DataTable](#csharp-ods-to-datatable)
- [C# Преобразовать ODS в DataTable](#csharp-convert-ods-to-datatable)
- [C# Импортировать ODS в DataTable](#csharp-import-ods-to-datatable)
- [C# Экспорт в DataTable из ODS](#csharp-export-to-datatable-from-ods)

## **Как экспортировать данные Excel с помощью C#**

{{% alert color="primary" %}}

В этой статье обсуждаются некоторые техники экспорта данных, к которым разработчики имеют доступ через Aspose.Cells.

{{% /alert %}}

## **Как экспортировать данные из листа**

Aspose.Cells не только облегчает своим пользователям импорт данных в листы из внешних источников данных, но также позволяет экспортировать данные своих листов в [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8). Как мы знаем, что [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) является частью ADO.NET и используется для хранения данных. Когда данные хранятся в [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8), их можно использовать любым способом в соответствии с требованиями пользователей. Разработчики также могут непосредственно сохранять эти данные (хранятся в [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)) в базу данных при необходимости. Таким образом, мы видим, что разработчикам становится проще манипулировать данными листа, если они экспортируются в [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **Как экспортировать данные в DataTable с помощью Aspose.Cells**

Разработчики могут легко экспортировать данные своих листов в объект [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8), вызывая либо метод [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index), либо метод [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) класса [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Оба метода используются в различных сценариях, которые подробно обсуждаются ниже.

## **Столбцы, содержащие строго типизированные данные**

Мы знаем, что электронная таблица хранит данные в виде последовательности строк и столбцов. Если все значения в столбцах листа являются строго типизированными (то есть все значения в столбце должны иметь тот же тип данных), то мы можем экспортировать содержимое листа, вызвав метод [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) класса [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Метод [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) принимает следующие параметры для экспорта данных листа в объект [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8):

- **Номер строки**, номер строки первой ячейки данных, которые будут экспортированы.
- **Номер столбца**, номер столбца первой ячейки, из которого будут экспортироваться данные.
- **Количество строк**, количество строк для экспорта.
- **Количество столбцов**, количество столбцов для экспорта.
- **Экспорт имен столбцов**, логическое свойство, указывающее, должны ли данные в первой строке листа быть экспортированы в виде имен столбцов для [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) или нет.

_Шаги: Экспорт данных в DataTable_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Шаги:</em> Excel to DataTable in C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Шаги:</em> XLS to DataTable in C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Шаги:</em> XLSX to DataTable in C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Шаги:</em> ODS to DataTable in C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Шаги:</em> Convert Excel to DataTable in C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Шаги:</em> Convert XLS to DataTable in C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Шаги:</em> Convert XLSX to DataTable in C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Шаги:</em> Convert ODS to DataTable in C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Шаги:</em> Import Excel to DataTable in C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Шаги:</em> Import XLS to DataTable in C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Шаги:</em> Import XLSX to DataTable in C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Шаги:</em> Import ODS to DataTable in C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Шаги:</em> Export to DataTable from Excel in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Шаги:</em> Export to DataTable from XLS in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Шаги:</em> Export to DataTable from XLSX in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Шаги:</em> Export to DataTable from ODS in C#</strong></a>

_Шаги кода:_

1. Загрузите свой файл Excel в объект [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/).
   - Объект [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/) может загружать форматы файлов Excel, например XLS, XLSX, XLSM, ODS и др.
3. Получите доступ к первому [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) в файле Excel.
4. Выберите область экспорта, например 7 строк и 2 столбца, начиная с 1-й ячейки **DataTable**.
5. Используйте метод [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) для экспорта данных в DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **Столбцы, содержащие нестрого типизированные данные**

Если все значения в столбцах рабочего листа не являются явно заданными типами (это означает, что значения в столбце могут иметь разные типы данных), то мы можем экспортировать содержимое рабочего листа, вызвав метод [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) класса [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Метод [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) принимает те же параметры, что и метод [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index), для экспорта данных рабочего листа в объект [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **Как экспортировать диапазон с заголовком**

Данные из диапазона могут быть экспортированы в [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8), где доступен флаг для пропуска заголовочной строки в экспортированных данных. Нижеприведенный код экспортирует диапазон данных в [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) с аргументом [**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions), который содержит флаг [**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname). Он установлен в **true**, если информация о заголовке есть, следовательно, ее не будет включено в данные, и установлен в **false**, если заголовок отсутствует, и все строки должны быть рассмотрены как данные.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **Продвинутые темы**
- [Экспорт данных Excel в DataTable без форматирования](/cells/ru/net/export-excel-data-to-datatable-without-any-formatting/)
- [Экспорт значений HTML-строки ячеек в DataTable](/cells/ru/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Экспорт видимых строк данных из рабочего листа](/cells/ru/net/export-visible-rows-data-from-worksheet/)
- [Игнорировать скрытые столбцы при экспорте данных рабочего листа в таблицу данных](/cells/ru/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Автоматическое переименование дублирующихся столбцов при экспорте данных рабочего листа](/cells/ru/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
