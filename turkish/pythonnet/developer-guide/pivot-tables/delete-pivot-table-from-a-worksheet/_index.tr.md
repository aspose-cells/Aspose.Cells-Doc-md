---
title: Pivot Tabloyu Çalışma Sayfasından Silme
type: docs
weight: 60
url: /tr/python-net/delete-pivot-table-from-a-worksheet/
description: Python via .NET Excel Çalışma Sayfaları için PivotTable'ı kaldırma kodu
keywords: Python via .NET remove pivot table from worksheet, Python via .NET remove pivot table from excel, how to delete pivot table with Python via .NET, delete pivot table with Python via .NET, delete pivot table from excel with Python via .NET, Python via .NET delete pivot table, Python via .NET remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET, Özet Tabloyu Çalışma Sayfasından silme veya kaldırma özelliği sağlar. Pivot tablo nesnesini veya pivot tablo konumunu kullanarak pivot tabloyu silebilirsiniz. Lütfen şunu kullanın:[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) Pivot tablo nesnesini kullanarak pivot tabloyu silme yöntemi ve[**Worksheet.pivot_tables.remove_at(dizin, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)Pivot tablo koleksiyonu içindeki konumunu kullanarak pivot tablo nesnesini silme yöntemi.

{{% /alert %}}

 Aşağıdaki örnek kod, çalışma sayfasından iki pivot tabloyu siler. İlk önce pivot tabloyu kullanarak kaldırır[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) yöntemini kullanır ve ardından pivot tabloyu kullanarak kaldırır[**Worksheet.pivot_tables.remove_at(dizin, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) yöntem

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
