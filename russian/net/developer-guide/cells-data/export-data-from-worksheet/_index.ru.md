---
title: Экспорт данных из рабочего листа в .NET
linktitle: Экспорт данных из рабочего листа
type: docs
weight: 180
url: /ru/net/export-data-from-worksheet/
description: В этой статье объясняется, как экспортировать или импортировать данные из рабочего листа в таблицу данных с помощью C#.
---
## Обзор

В этой статье объясняется, как экспортировать данные рабочего листа в DataTable с помощью C#. В ней рассматриваются следующие темы.

_Формат_: **Excel**
- [C# Excel в DataTable](#csharp-excel-to-datatable)
- [C# Преобразовать Excel в DataTable](#csharp-convert-excel-to-datatable)
- [C# Импорт Excel в DataTable](#csharp-import-excel-to-datatable)
- [C# Экспорт в DataTable из Excel](#csharp-export-to-datatable-from-excel)

_Формат_: **XLS**
- [C# XLS в DataTable](#csharp-xls-to-datatable)
- [C# Преобразование XLS в DataTable](#csharp-convert-xls-to-datatable)
- [C# Импорт XLS в DataTable](#csharp-import-xls-to-datatable)
- [C# Экспорт в DataTable из XLS](#csharp-export-to-datatable-from-xls)

_Формат_: **XLSX**
- [C# XLSX в DataTable](#csharp-xlsx-to-datatable)
- [C# Преобразование XLSX в DataTable](#csharp-convert-xlsx-to-datatable)
- [C# Импорт XLSX в DataTable](#csharp-import-xlsx-to-datatable)
- [C# Экспорт в DataTable из XLSX](#csharp-export-to-datatable-from-xlsx)

_Формат_: **ODS**
- [C# ODS в DataTable](#csharp-ods-to-datatable)
- [C# Преобразование ODS в DataTable](#csharp-convert-ods-to-datatable)
- [C# Импорт ODS в DataTable](#csharp-import-ods-to-datatable)
- [C# Экспорт в DataTable из ODS](#csharp-export-to-datatable-from-ods)

## **C# Экспорт данных Excel**

{{% alert color="primary" %}}

В этой статье обсуждаются некоторые методы экспорта данных, к которым у разработчиков есть доступ по номеру Aspose.Cells.

{{% /alert %}}

## **Экспорт данных из рабочего листа**

 Aspose.Cells не только облегчает пользователям импорт данных в рабочие листы из внешних источников данных, но также позволяет им экспортировать данные своих рабочих листов в[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) . Как мы знаем, что[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) является частью ADO.NET и используется для хранения данных. Как только данные сохраняются в[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) , его можно использовать любым способом в соответствии с требованиями пользователей. Разработчики также могут хранить эти данные (хранятся в[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ) непосредственно в базу данных, если они того пожелают. Итак, мы видим, что разработчикам становится проще манипулировать данными рабочего листа, если они экспортируются в[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **Экспорт данных в DataTable с помощью Aspose.Cells**

 Разработчики могут легко экспортировать данные своих рабочих листов в[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) объект, вызвав либо[**Таблица ЭкспортДанных**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) или же[**Экспортдататаблеасстринг**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)учебный класс. Оба метода используются в разных сценариях, которые более подробно обсуждаются ниже.

## **Столбцы, содержащие строго типизированные данные**

Мы знаем, что электронная таблица хранит данные в виде последовательности строк и столбцов. Если все значения в столбцах рабочего листа строго типизированы (это означает, что все значения в столбце должны иметь один и тот же тип данных), мы можем экспортировать содержимое рабочего листа, вызвав метод[**Таблица ЭкспортДанных**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) учебный класс.[**Таблица ЭкспортДанных**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) метод принимает следующие параметры для экспорта данных листа как[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)объект:

- **Номер строки**, номер строки данных первой ячейки будет экспортирован.
- **Номер столбца**, номер столбца первой ячейки, из которой будут экспортированы данные.
- **Количество рядов**, количество строк для экспорта.
- **Число столбцов**, количество столбцов для экспорта.
- **Экспорт имен столбцов** , логическое свойство, указывающее, следует ли экспортировать данные в первой строке рабочего листа в виде имен столбцов таблицы.[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)или не.

_Шаги: экспорт данных в DataTable_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Шаги:</em> Excel в DataTable в C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Шаги:</em> XLS в DataTable в C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Шаги:</em> XLSX в DataTable в C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Шаги:</em> ODS в DataTable в C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Шаги:</em> Преобразование Excel в DataTable в C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Шаги:</em>Преобразование XLS в DataTable в C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Шаги:</em>Преобразование XLSX в DataTable в C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Шаги:</em>Преобразование ODS в DataTable в C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Шаги:</em> Импорт Excel в DataTable по номеру C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Шаги:</em> Импорт XLS в DataTable в C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Шаги:</em> Импорт XLSX в DataTable в C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Шаги:</em> Импорт ODS в DataTable в C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Шаги:</em> Экспорт в DataTable из Excel по номеру C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Шаги:</em> Экспорт в DataTable из XLS в C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Шаги:</em> Экспорт в DataTable из XLSX в C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Шаги:</em> Экспорт в DataTable из ODS в C#</strong></a>

_Шаги кода:_

1.  Загрузите файл Excel в[Рабочая тетрадь](https://reference.aspose.com/cells/net/aspose.cells/workbook/) объект.
   - [Рабочая тетрадь](https://reference.aspose.com/cells/net/aspose.cells/workbook/) объект может загружать форматы файлов Excel, например, XLS, XLSX, XLSM, ODS и т. д.
 3. Доступ к первому[Рабочий лист](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) в файле Excel.
 4. Выберите область экспорта, например, 7 строк и 2 столбца, начиная с 1-й ячейки**Таблица данных**.
 5. Используйте[Таблица ЭкспортДанных](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) способ экспорта данных в DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **Столбцы, содержащие не строго типизированные данные**

 Если все значения в столбцах рабочего листа не являются строго типизированными (это означает, что значения в столбце могут иметь разные типы данных), мы можем экспортировать содержимое рабочего листа, вызвав метод[**Экспортдататаблеасстринг**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) учебный класс.[**Экспортдататаблеасстринг**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)метод принимает тот же набор параметров, что и метод[**Таблица ЭкспортДанных**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)способ экспорта данных рабочего листа в виде[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)объект.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **Экспортировать диапазон с флагом, чтобы пропустить имя столбца**

Данные из диапазона можно экспортировать в[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) где доступен флаг для пропуска строки заголовка в экспортируемых данных. Следующий код экспортирует диапазон данных в[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) с аргументом[**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) который содержит[**ИмяЭкспортКолонки**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) флаг. Он настроен на**истинный** если информация заголовка есть, следовательно, она не будет включена в данные и установлена на**ЛОЖЬ** если нет заголовка и все строки должны рассматриваться как данные.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **Предварительные темы**
- [Экспорт данных Excel в DataTable без форматирования](/cells/ru/net/export-excel-data-to-datatable-without-any-formatting/)
- [Экспорт HTML строкового значения Cells в DataTable](/cells/ru/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Экспорт данных видимых строк из рабочего листа](/cells/ru/net/export-visible-rows-data-from-worksheet/)
- [Игнорировать скрытые столбцы при экспорте данных рабочего листа в таблицу данных](/cells/ru/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Автоматическое переименование повторяющихся столбцов при экспорте данных листа](/cells/ru/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
