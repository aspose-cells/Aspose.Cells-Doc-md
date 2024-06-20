---
title: Фильтрация заданных имен при загрузке рабочей книги
type: docs
weight: 50
url: /ru/net/filter-defined-names-while-loading-workbook/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет фильтровать или удалять заданные имена, присутствующие внутри рабочей книги. Пожалуйста, используйте [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) для загрузки заданных имен и ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) для их удаления при загрузке рабочей книги. Обратите внимание, что если вы удалите заданные имена, то формулы внутри рабочей книги могут перестать работать.

## **Фильтрация заданных имен при загрузке рабочей книги**

Приведенный ниже образец кода загружает [образец файла Excel](61767860.xlsx), в котором в клетке **C1** содержится формула с определенными именами, т. е. *=SUM(MyName1, MyName2)*. Поскольку мы используем ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) для удаления определенных имен при загрузке книги Excel, формула в клетке C1 в [выходном файле Excel](61767861.xlsx) распадается, и вы видите *#NAME?* вместо нее. Пожалуйста, ознакомьтесь со следующим снимком экрана, который показывает влияние кода на образец файла Excel.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
