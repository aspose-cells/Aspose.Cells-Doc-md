---
title: Ana Pivot Tablosunun İçindeki Yerleşik veya Çocuk Pivot Tablolarını Bul ve Yenile
type: docs
weight: 60
url: /tr/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Ebeveyn Pivota Tablosunun gömülü veya alt Pivota Tablolarını bulma ve yenileme Aspose.Cells for Python via .NET ile nasıl yapılır.
keywords: Python Excel Kütüphanesi Aspose.Cells, Ana Özet Tablosunun İçerisindeki veya Alt Tablolarını Bulma ve Yenileme
---

## **Olası Kullanım Senaryoları**

Bazı durumlarda, bir pivot tablosu diğer bir pivot tablosunu veri kaynağı olarak kullandığı için buna çocuk pivot tablosu veya yerleşik pivot tablosu denir. [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#) yöntemi kullanarak bir ana pivot tablosunun çocuk pivot tablolarını bulabilirsiniz.

## **Ana Özet Tablosunun İçerisindeki veya Alt Tablolarını Bulma ve Yenileme**

Aşağıdaki örnek kod, üç pivot tablosunu içeren [örnek Excel dosyasını](61767747.xlsx) yükler. Alt iki pivot tablosu yukarıdaki pivot tablosunun alt pivot tablolarıdır ve bu ekran görüntüsünde gösterildiği gibi. Kod, [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#) yöntemini kullanarak alt pivot tablosunu bulur ve ardından birer birer yeniler.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}
