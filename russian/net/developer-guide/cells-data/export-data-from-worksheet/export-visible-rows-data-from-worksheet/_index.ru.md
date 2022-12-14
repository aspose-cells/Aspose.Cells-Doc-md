---
title: Экспорт данных видимых строк из рабочего листа
type: docs
weight: 10
url: /ru/net/export-visible-rows-data-from-worksheet/
---
{{% alert color="primary" %}}

 Вы можете экспортировать данные из рабочих листов в таблицы данных, используя Aspose.Cells. Иногда вам нужно экспортировать данные только видимых строк. Aspose.Cells предоставляет способ добиться этого. Использовать[**Экспорттаблеоптионс.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows) чтобы указать, что вы хотите экспортировать только данные видимых строк.

{{% /alert %}}

В этом примере показано, как экспортировать данные из следующего рабочего листа. Ряды 5, 6 и 7 скрыты.

|**Пример данных на листе, строки 5, 6 и 7 скрыты**|
|:- |
|![дело:изображение_альтернативный_текст](export-visible-rows-data-from-worksheet_1.png)|

После экспорта данных в таблицу данных с помощью[**Рабочий лист.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) метод с[**Экспорттаблеоптионс.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)вариант, это будет выглядеть так. Скрытые строки отображаются как пустые строки

|**Скрытые строки экспортируются в таблицу данных как пустые строки.**|
|:- |
|![дело:изображение_альтернативный_текст](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
