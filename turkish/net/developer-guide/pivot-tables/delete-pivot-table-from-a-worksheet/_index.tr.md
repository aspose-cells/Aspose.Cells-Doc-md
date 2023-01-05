---
title: Pivot Tabloyu Çalışma Sayfasından Silme
type: docs
weight: 60
url: /tr/net/delete-pivot-table-from-a-worksheet/
description: Excel Çalışma Sayfaları için PivotTable'ı kaldırmak için C# kodu
keywords: c# remove pivot table from worksheet, c# remove pivot table from excel, how to delete pivot table with c#, delete pivot table with c#, delete pivot table from excel with c#, c# delete pivot table, c# remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---
{{% alert color="primary" %}}

 Aspose.Cells, Pivot Tabloyu bir Çalışma Sayfasından silmek veya kaldırmak için bir özellik sağlar. Pivot tablo nesnesini veya pivot tablo konumunu kullanarak pivot tabloyu silebilirsiniz. lütfen[**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) pivot tablo nesnesini kullanarak pivot tabloyu silme yöntemi ve[**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) pivot tablo koleksiyonu içindeki konumunu kullanarak pivot tablo nesnesini silme yöntemi.

{{% /alert %}}

 Aşağıdaki örnek kod, çalışma sayfasından iki pivot tabloyu siler. İlk önce pivot tabloyu kullanarak kaldırır[**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) yöntemini kullanır ve ardından pivot tabloyu kullanarak kaldırır[**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) yöntem

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}
