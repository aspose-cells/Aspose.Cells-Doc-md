---
title: Вставка или удаление строк в рабочем листе Excel
type: docs
weight: 20
url: /ru/net/insert-or-delete-rows-in-an-excel-worksheet/
description: В этой статье приведен код на C#, позволяющий вставлять и удалять строки в рабочем листе Excel.
keywords: c# вставка или удаление строк в рабочем листе Excel, c# вставка или удаление строк в Excel, c# вставка строк в Excel, c# удаление строк в Excel, вставка или удаление строк в рабочем листе Excel с использованием c#, вставка или удаление строк в Excel с использованием c#, вставка строк в Excel с использованием c#, удаление строк в Excel с использованием c#
---

{{% alert color="primary" %}}

При создании нового рабочего листа или работы с существующим листом в Excel вам может понадобиться добавить дополнительные строки или столбцы для размещения данных. В других случаях может потребоваться удалить строки или столбцы из указанных позиций на листе.

{{% /alert %}}

Aspose.Cells предлагает два метода для вставки и удаления строк: [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) и [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). Эти методы оптимизированы для производительности и выполняют работу очень быстро.

Для вставки или удаления нескольких строк рекомендуем всегда использовать методы [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) и [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index), вместо использования методов [**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) или [**DeleteRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow) в цикле.

Aspose.Cells работает так же, как и Microsoft Excel. При добавлении строк или столбцов содержимое рабочего листа сдвигается вниз и вправо. При удалении строк или столбцов содержимое рабочего листа сдвигается вверх или влево. Ссылки в других рабочих листах и ячейках обновляются при добавлении или удалении строк.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
