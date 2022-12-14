---
title: Ebeveyn Pivot Tablosunun İç İçe veya Alt Pivot Tablolarını Bulun ve Yenileyin
type: docs
weight: 60
url: /tr/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---
## **Olası Kullanım Senaryoları**

Bazen bir pivot tablo, veri kaynağı olarak başka bir pivot tablo kullanır, bu nedenle buna alt pivot tablo veya iç içe pivot tablo denir. Bir üst pivot tablonun alt pivot tablolarını,[**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)yöntem.

## **Ebeveyn Pivot Tablosunun İç İçe veya Alt Pivot Tablolarını Bulun ve Yenileyin**

 Aşağıdaki örnek kod,[örnek excel dosyası](61767747.xlsx) üç pivot tablo içerir. Alttaki iki pivot tablo, bu ekran görüntüsünde gösterildiği gibi yukarıdaki pivot tablonun çocuklarıdır. Kod, şunu kullanarak alt pivot tabloyu bulur:[**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)yöntemini kullanır ve ardından bunları birer birer yeniler.

![yapılacaklar:resim_alternatif_Metin](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}
