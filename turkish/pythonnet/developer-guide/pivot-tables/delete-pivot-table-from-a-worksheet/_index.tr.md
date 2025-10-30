---
title: Bir Çalışma Sayfasından Pivot Tablosunu Sil
type: docs
weight: 60
url: /tr/python-net/delete-pivot-table-from-a-worksheet/
description: Excel Çalışma Sayfaları İçin Python via .NET Kodunu Kullanarak PivotTablosunu Kaldırma
keywords: Aspose.Cells for Python Excel, Excel Python kütüphanesi, Python via .NET çalışma sayfasından pivot tablosunu kaldırma, Python via .NET çalışma sayfasından pivot tablosunu kaldırma, Python via .NET ile pivot tablosunu nasıl silinir, Python via .NET ile pivot tablosunu silme, pivot tablosunu excel den Python via .NET ile silme, Python via .NET pivot tablosu silme, Python via .NET ile pivot tablosunu kaldırma, pivot tablosunu silme, pivot tablosunu nasıl silinir
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, Çalışma Sayfasından Pivot Tablosunu Silme veya Kaldırma özelliği sağlar. Pivot tablosunu pivot tablo nesnesi veya pivot tablosu konumunu kullanarak silebilirsiniz. Lütfen pivot tablosunu pivot tablo nesnesi kullanarak silmek için [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) yöntemini ve pivot tablosu koleksiyonu içindeki konumunu kullanarak pivot tablosu nesnesini silmek için [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) yöntemini kullanın.

{{% /alert %}}

## **Aspose.Cells for Python Excel Kütüphanesi Kullanarak Çalışma Sayfasından Pivot Tablosunu Nasıl Sileceğiniz**

Aşağıdaki örnek kod, çalışma sayfasından iki pivot tablosunu siler. İlk önce [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) yöntemini kullanarak pivot tablosunu kaldırır, ardından [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) yöntemini kullanarak pivot tablosunu kaldırır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
{{< app/cells/assistant language="python-net" >}}
