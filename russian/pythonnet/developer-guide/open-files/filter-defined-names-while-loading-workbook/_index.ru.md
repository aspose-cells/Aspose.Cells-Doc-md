---
title: Фильтрация заданных имен при загрузке рабочей книги
type: docs
weight: 50
url: /ru/python-net/filter-defined-names-while-loading-workbook/
---

## **Возможные сценарии использования**

Aspose.Cells для Python via .NET позволяет фильтровать или удалять определённые имена, присутствующие внутри рабочей книги. Используйте [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) для загрузки определённых имён и ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) для их удаления при загрузке книги. Обратите внимание, что удаление определённых имён может привести к нарушению формул внутри книги.

## **Фильтрация заданных имен при загрузке рабочей книги**

Приведенный ниже образец кода загружает [образец файла Excel](61767860.xlsx), в котором в клетке **C1** содержится формула с определенными именами, т. е. *=SUM(MyName1, MyName2)*. Поскольку мы используем ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) для удаления определенных имен при загрузке книги Excel, формула в клетке C1 в [выходном файле Excel](61767861.xlsx) распадается, и вы видите *#NAME?* вместо нее. Пожалуйста, ознакомьтесь со следующим снимком экрана, который показывает влияние кода на образец файла Excel.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDefinedNamesWhileLoadingWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
