---
title: Экспорт данных из листа в .NET
linktitle: Экспорт данных из листа
type: docs
weight: 180
url: /ru/net/export-data-from-worksheet/
description: В этой статье объясняется, как экспортировать или импортировать данные из листа в таблицу данных с помощью C#.
keywords: C# Export Data from Worksheet, C# Export Data to DataTable, Columns Containing Strongly Typed Data, Columns Containing Non-Strongly Typed Data, C# Export Range with flag to skip column name
---
##  Обзор

В этой статье объясняется, как экспортировать данные рабочего листа в DataTable с помощью C#. В ней рассматриваются следующие темы.

 _Формат_:**Эксель**
- [C# Excel в таблицу данных](#csharp-excel-to-datatable)
- [C# Преобразование Excel в DataTable](#csharp-convert-excel-to-datatable)
- [C# Импорт Excel в DataTable](#csharp-import-excel-to-datatable)
- [C# Экспорт в DataTable из Excel](#csharp-export-to-datatable-from-excel)

 _Формат_:**XLS**
- [C# XLS в таблицу данных](#csharp-xls-to-datatable)
- [C# Преобразовать XLS в DataTable](#csharp-convert-xls-to-datatable)
- [C# Импортировать XLS в DataTable.](#csharp-import-xls-to-datatable)
- [C# Экспорт в DataTable из XLS](#csharp-export-to-datatable-from-xls)

 _Формат_:**XLSX**
- [C# XLSX в таблицу данных](#csharp-xlsx-to-datatable)
- [C# Преобразовать XLSX в DataTable](#csharp-convert-xlsx-to-datatable)
- [C# Импортировать XLSX в DataTable.](#csharp-import-xlsx-to-datatable)
- [C# Экспорт в DataTable из XLSX](#csharp-export-to-datatable-from-xlsx)

 _Формат_:**ODS**
- [C# ODS в таблицу данных](#csharp-ods-to-datatable)
- [C# Преобразовать ODS в DataTable](#csharp-convert-ods-to-datatable)
- [C# Импортировать ODS в DataTable.](#csharp-import-ods-to-datatable)
- [C# Экспорт в DataTable из ODS](#csharp-export-to-datatable-from-ods)

##  **Как экспортировать данные Excel с помощью C#**

{{% alert color="primary" %}}

В этой статье обсуждаются некоторые методы экспорта данных, к которым разработчики имеют доступ по номеру Aspose.Cells.

{{% /alert %}}

##  **Как экспортировать данные из листа**

 Aspose.Cells не только позволяет пользователям импортировать данные в рабочие листы из внешних источников данных, но также позволяет им экспортировать данные своих рабочих листов в файл.[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) . Поскольку мы знаем, что[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) является частью ADO.NET и используется для хранения данных. Как только данные сохраняются в[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) , его можно использовать любым способом в соответствии с требованиями пользователей. Разработчики также могут хранить эти данные (хранятся в[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ) непосредственно в базу данных, если захотят. Итак, мы видим, что разработчикам становится проще манипулировать данными рабочего листа, если они экспортированы в файл.[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

##  **Как экспортировать данные в DataTable с помощью Aspose.Cells**

 Разработчики могут легко экспортировать данные своих рабочих листов в[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) объект, вызвав либо[**Экспортдататабле**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) или[**Экспортдататаблеасстринг**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)сорт. Оба метода используются в разных сценариях, которые более подробно обсуждаются ниже.

##  **Столбцы, содержащие строго типизированные данные**

 Мы знаем, что электронная таблица хранит данные в виде последовательности строк и столбцов. Если все значения в столбцах листа строго типизированы (это означает, что все значения в столбце должны иметь один и тот же тип данных), то мы можем экспортировать содержимое листа, вызвав метод[**Экспортдататабле**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) сорт.[**Экспортдататабле**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) метод принимает следующие параметры для экспорта данных рабочего листа в виде[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)объект:

- *Номер строки**: номер строки данных первой ячейки, из которой будут экспортированы данные.
- *Номер столбца**: номер столбца первой ячейки, из которой будут экспортированы данные.
- *Количество строк** — количество строк для экспорта.
- *Количество столбцов** — количество экспортируемых столбцов.
- *Экспортировать имена столбцов** — логическое свойство, указывающее, следует ли экспортировать данные в первой строке листа как имена столбцов[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)или нет.

_Шаги: экспорт данных в DataTable_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Шаги:</em> Excel в DataTable в C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Шаги:</em> XLS в DataTable в C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Шаги:</em> XLSX в DataTable в C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Шаги:</em> ODS в DataTable в C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Шаги:</em> Преобразование Excel в DataTable в C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Шаги:</em> Преобразуйте XLS в DataTable в C#.</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Шаги:</em> Преобразуйте XLSX в DataTable в C#.</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Шаги:</em> Преобразуйте ODS в DataTable в C#.</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Шаги:</em> Импортируйте Excel в DataTable в C#.</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Шаги:</em> Импортируйте XLS в DataTable в C#.</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Шаги:</em> Импортируйте XLSX в DataTable в C#.</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Шаги:</em> Импортируйте ODS в DataTable в C#.</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Шаги:</em> Экспорт в DataTable из Excel в C#.</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Шаги:</em> Экспорт в DataTable из XLS в C#.</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Шаги:</em> Экспорт в DataTable из XLSX в C#.</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Шаги:</em> Экспорт в DataTable из ODS в C#.</strong></a>

_Шаги кода:_

1.  Загрузите файл Excel в[Рабочая тетрадь](https://reference.aspose.com/cells/net/aspose.cells/workbook/) объект.
   - [Рабочая тетрадь](https://reference.aspose.com/cells/net/aspose.cells/workbook/) Объект может загружать форматы файлов Excel, например XLS, XLSX, XLSM, ODS и т. д.
 3. Доступ к первому[Рабочий лист](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) в файле Excel.
4. Выберите область экспорта, например 7 строк и 2 столбца, начиная с 1-й ячейки *DataTable**.
 5. Используйте[Экспортдататабле](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) метод для экспорта данных в DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

##  **Столбцы, содержащие нестрого типизированные данные**

 Если все значения в столбцах листа не являются строго типизированными (это означает, что значения в столбце могут иметь разные типы данных), мы можем экспортировать содержимое листа, вызвав метод[**Экспортдататаблеасстринг**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) сорт.[**Экспортдататаблеасстринг**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)метод принимает тот же набор параметров, что и метод[**Экспортдататабле**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)метод экспорта данных рабочего листа в виде[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)объект.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

##  **Как экспортировать диапазон с флагом пропуска имени столбца**

 Данные из диапазона можно экспортировать в[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) где доступен флаг для пропуска строки заголовка в экспортируемых данных. Следующий код экспортирует ряд данных в[**Таблица данных**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) с аргументом[**Экспорттаблеопции**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) который содержит[**ИмяЭкспортКолонки**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) флаг. Он установлен на**истинный** если информация заголовка присутствует, следовательно, она не будет включена в данные и ей будет присвоено значение**ЛОЖЬ** если заголовка нет и все строки следует рассматривать как данные.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

##  **Предварительные темы**
- [Экспорт данных Excel в DataTable без форматирования](/cells/ru/net/export-excel-data-to-datatable-without-any-formatting/)
- [Экспортировать строковое значение HTML из Cells в DataTable.](/cells/ru/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Экспорт данных видимых строк из листа](/cells/ru/net/export-visible-rows-data-from-worksheet/)
- [Игнорировать скрытые столбцы при экспорте данных рабочего листа в таблицу данных](/cells/ru/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Автоматическое переименование повторяющихся столбцов при экспорте данных листа](/cells/ru/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
