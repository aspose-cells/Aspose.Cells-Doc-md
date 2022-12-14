---
title: Фильтровать определенные имена при загрузке книги
type: docs
weight: 50
url: /ru/java/filter-defined-names-while-loading-workbook/
---
## **Возможные сценарии использования**

Aspose.Cells позволяет фильтровать или удалять определенные имена, присутствующие в книге. Пожалуйста, используйте[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)для загрузки определенных имен и использования ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)чтобы удалить их при загрузке книги. Обратите внимание: если вы удалите определенные имена, формулы внутри рабочей книги могут разбиться.

## **Фильтровать определенные имена при загрузке книги**

Следующий пример кода загружает[образец файла Excel](61767873.xlsx)который имеет формулу в ячейке C1, содержащую определенные имена, т.е.*=СУММ(МоеИмя1, МоеИмя2)*. Так как мы используем ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)чтобы удалить определенные имена при загрузке книги, формула в ячейке C1 в[выходной файл Excel](61767872.xlsx)расстается и ты увидишь*#NAME?*вместо. См. следующий снимок экрана, на котором показано влияние кода на пример файла Excel.

![дело:изображение_альтернативный_текст](filter-defined-names-while-loading-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
