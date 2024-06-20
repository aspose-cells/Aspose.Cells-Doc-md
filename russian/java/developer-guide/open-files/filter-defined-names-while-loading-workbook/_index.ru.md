---
title: Фильтрация заданных имен при загрузке рабочей книги
type: docs
weight: 50
url: /ru/java/filter-defined-names-while-loading-workbook/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет фильтровать или удалять заданные имена, присутствующие внутри рабочей книги. Пожалуйста, используйте [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) для загрузки заданных имен и ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) для их удаления при загрузке рабочей книги. Обратите внимание, что если вы удалите заданные имена, то формулы внутри рабочей книги могут перестать работать.

## **Фильтрация заданных имен при загрузке рабочей книги**

Приведенный ниже образец кода загружает [образец Excel-файла](61767873.xlsx), в котором в ячейке C1 содержится формула, содержащая заданные имена, т. е. *=SUM(MyName1, MyName2)*. Поскольку мы используем ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) для удаления заданных имен при загрузке рабочей книги, формула в ячейке C1 в [конечном Excel-файле](61767872.xlsx) перестает работать и вы видите *#NAME?* вместо этого. Пожалуйста, обратите внимание на следующий скриншот, который показывает эффект кода на пример Excel-файла.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
