---
title: Фильтровать определенные имена при загрузке книги
type: docs
weight: 50
url: /ru/net/filter-defined-names-while-loading-workbook/
---
## **Возможные сценарии использования**

Aspose.Cells позволяет фильтровать или удалять определенные имена, присутствующие в книге. Пожалуйста, используйте[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)для загрузки определенных имен и использования ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)чтобы удалить их при загрузке книги. Обратите внимание: если вы удалите определенные имена, формулы внутри рабочей книги могут разбиться.

## **Фильтровать определенные имена при загрузке книги**

 Следующий пример кода загружает[образец файла Excel](61767860.xlsx) у которого есть формула в ячейке**С1** содержащие определенные имена, т.е.*=СУММ(МоеИмя1, МоеИмя2)*. Поскольку мы используем ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) чтобы удалить определенные имена при загрузке книги, формула в ячейке C1 в[выходной файл Excel](61767861.xlsx) расстается и ты увидишь*#NAME?*вместо. См. следующий снимок экрана, на котором показано влияние кода на пример файла Excel.

![дело:изображение_альтернативный_текст](filter-defined-names-while-loading-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
