---
title: Автоматическое переименование повторяющихся столбцов при экспорте данных листа
type: docs
weight: 250
url: /ru/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
---
## **Возможные сценарии использования**

Иногда пользователь сталкивается с проблемой дублирования столбцов при экспорте данных из рабочего листа в таблицу данных. DataTable не может иметь повторяющихся столбцов, поэтому повторяющиеся столбцы необходимо переименовать, прежде чем вы сможете экспортировать данные рабочего листа в таблицу данных. Aspose.Cells может автоматически переименовывать повторяющиеся столбцы в соответствии со стратегией, указанной вами с помощью[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) имущество. Если вы укажете[**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) .Digit, столбцы будут переименованы как столбец1, столбец2, столбец3 и т. д., и если вы укажете[**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter, тогда столбцы будут переименованы как столбец A, столбец B, столбец C и т. д.

## **Автоматическое переименование повторяющихся столбцов при экспорте данных листа**

 Следующий пример кода добавляет некоторые данные в первые три столбца рабочего листа, но все столбцы имеют одинаковое имя, т.е.*Люди* . Затем он экспортирует данные из рабочего листа в таблицу данных, указав[**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Письмо стратегии. Затем он печатает имена столбцов таблицы данных, сгенерированной Aspose.Cells. На следующем снимке экрана показана таблица данных с экспортированными данными в визуализаторе. Как видите, повторяющиеся столбцы были переименованы в PeopleA, PeopleB и т. д.

![дело:изображение_альтернативный_текст](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **Консольный вывод**

Вот вывод консоли приведенного выше примера кода для справки.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
