---
title: Ana Pivot Tablosunun İçindeki Yerleşik veya Çocuk Pivot Tablolarını Bul ve Yenile
type: docs
weight: 60
url: /tr/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **Olası Kullanım Senaryoları**

Bazı durumlarda, bir pivot tablosu diğer bir pivot tablosunu veri kaynağı olarak kullandığı için buna çocuk pivot tablosu veya yerleşik pivot tablosu denir. [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren) yöntemi kullanarak bir ana pivot tablosunun çocuk pivot tablolarını bulabilirsiniz.

## **Ana Pivot Tablosunun İçindeki Yerleşik veya Çocuk Pivot Tablolarını Bul ve Yenile**

Aşağıdaki örnek kod, üç pivot tablosunu içeren [örnek Excel dosyasını](61767747.xlsx) yükler. Alt iki pivot tablosu yukarıdaki pivot tablosunun alt pivot tablolarıdır ve bu ekran görüntüsünde gösterildiği gibi. Kod, [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren) yöntemini kullanarak alt pivot tablosunu bulur ve ardından birer birer yeniler.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}
