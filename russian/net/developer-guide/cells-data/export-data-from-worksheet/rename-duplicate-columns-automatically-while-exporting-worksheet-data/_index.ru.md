---
title: Переименование дублирующихся столбцов автоматически при экспорте данных листа
type: docs
weight: 250
url: /ru/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Узнайте, как автоматически переименовывать дублирующиеся столбцы при экспорте данных листа через API Aspose.Cells for .NET.
keywords: Переименование дублирующихся столбцов при экспорте данных листа, автоматическое переименование дублирующихся столбцов при экспорте данных в DataTable
---

## **Возможные сценарии использования**

Иногда пользователь сталкивается с проблемой дублирующихся столбцов при экспорте данных с листа в таблицу данных. DataTable не может содержать дублирующиеся столбцы, поэтому дублирующиеся столбцы должны быть переименованы перед экспортом данных листа в таблицу данных. Aspose.Cells может автоматически переименовывать дублирующиеся столбцы в соответствии с указанной вами стратегией с использованием свойства [**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy). Если вы укажете [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Digit, столбцы будут переименованы как столбец1, столбец2, столбец3 и т. д., а если вы укажете [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter, то столбцы будут переименованы как столбецA, столбецB, столбецC и т. д.

## **Автоматическое переименование дублирующихся столбцов при экспорте данных рабочего листа**

Приведенный ниже образец кода добавляет некоторые данные в первые три столбца листа, но все столбцы имеют одно и то же название, т. е. *People*. Затем он экспортирует данные с листа в таблицу данных, указывая стратегию [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter. Затем он выводит названия столбцов таблицы данных, сгенерированной Aspose.Cells. Ниже приведен снимок таблицы данных с экспортированными данными визуализатором. Как вы можете видеть, дублирующиеся столбцы были переименованы в PeopleA, PeopleB и т. д.

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **Вывод в консоль**

Вот консольный вывод приведенного выше образца кода для справки.

{{< highlight java >}}

People

PeopleA

PeopleB

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
