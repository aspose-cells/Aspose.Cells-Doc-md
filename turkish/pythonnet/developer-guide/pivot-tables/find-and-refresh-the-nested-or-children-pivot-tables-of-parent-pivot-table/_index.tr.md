---
title: Ana Pivot Tablonun Yuvalanmış veya Alt Pivot Tablolarını Bulma ve Yenileme
type: docs
weight: 60
url: /tr/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Aspose.Cells for Python via .NET ile ana Pivot Tablonun yuvalanmış veya alt Pivot Tabloları nasıl bulunur ve yenilenir.
keywords: Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table.
---
##  **Olası Kullanım Senaryoları**

Bazen bir pivot tablo, veri kaynağı olarak başka bir pivot tabloyu kullanır; bu nedenle buna alt pivot tablo veya iç içe geçmiş pivot tablo adı verilir. Bir ana pivot tablonun alt pivot tablolarını aşağıdakileri kullanarak bulabilirsiniz:[**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)yöntem.

##  **Ana Pivot Tablonun Yuvalanmış veya Alt Pivot Tablolarını Bulma ve Yenileme**

 Aşağıdaki örnek kod,[örnek Excel dosyası](61767747.xlsx) üç pivot tablo içerir. Alttaki iki pivot tablo, bu ekran görüntüsünde gösterildiği gibi yukarıdaki pivot tablonun çocuklarıdır. Kod, aşağıdakileri kullanarak çocuk pivot tablosunu bulur:[**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)yöntemini kullanır ve ardından bunları birer birer yeniler.

![yapılacak şey:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

##  **Basit kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}
