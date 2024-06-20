---
title: Bir Çalışma Sayfasından Pivot Tablosunu Sil
type: docs
weight: 60
url: /tr/net/delete-pivot-table-from-a-worksheet/
description: Excel Çalışma Sayfaları için PivotTablo nun kaldırılması için C# kodu
keywords: c# çalışma sayfasından pivot tablosu kaldır, c# excel den pivot tablosu kaldır, c# ile pivot tablosu nasıl silinir, c# ile pivot tablosunu sil, excel den c# ile pivot tablosu silme, c# pivot tablosunu silme, c# pivot tablosu kaldırma, pivot tablosunu silme, pivot tablosunu silme
---

{{% alert color="primary" %}}

Aspose.Cells, bir Çalışma Sayfasından Pivot Tablosunu silme veya kaldırma özelliği sağlar. Pivot tablosu nesnesini veya pivot tablosu pozisyonunu kullanarak pivot tablosunu silebilirsiniz. Pivot tablosunu nesnesini kullanarak pivot tablosunu silmek için lütfen [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) yöntemini ve pivot tablosu koleksiyonundaki pozisyonunu kullanarak pivot tablosunu silme yöntemi [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) kullanın.

{{% /alert %}}

Aşağıdaki örnek kod, çalışma sayfasından iki pivot tablosunu siler. İlk önce [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) yöntemini kullanarak pivot tablosunu kaldırır, ardından [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) yöntemini kullanarak pivot tablosunu kaldırır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}
