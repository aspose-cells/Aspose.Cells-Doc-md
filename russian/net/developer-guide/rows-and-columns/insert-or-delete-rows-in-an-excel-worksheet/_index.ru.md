---
title: Вставка или удаление строк на листе Excel
type: docs
weight: 20
url: /ru/net/insert-or-delete-rows-in-an-excel-worksheet/
description: В этой статье представлен код C# для вставки и удаления строк на листе Excel.
keywords: c# insert or delete rows in excel worksheet, c# insert or delete rows in excel, c# insert rows in excel, c# delete rows in excel, insert or delete rows in excel worksheet with c#, insert or delete rows in excel with c#, insert rows in excel with c#, delete rows in excel with c#
---
{{% alert color="primary" %}}

При создании нового листа или работе с существующим листом может потребоваться добавить дополнительные строки или столбцы для размещения данных. В других случаях может потребоваться удалить строки или столбцы из указанных позиций на листе.

{{% /alert %}}

 Aspose.Cells предлагает два метода вставки и удаления строк:[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) и[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). Эти методы оптимизированы для производительности и делают работу очень быстро.

 Чтобы вставить или удалить несколько строк, мы рекомендуем всегда использовать[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) и[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) методы вместо использования[**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) или же[**УдалитьРов**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow)методы в цикле.

Aspose.Cells работает так же, как Microsoft Excel. При добавлении строк или столбцов содержимое рабочего листа смещается вниз и вправо. При удалении строк или столбцов содержимое рабочего листа сдвигается вверх или влево. Любые ссылки на других листах и ячейках обновляются при добавлении или удалении строк.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
