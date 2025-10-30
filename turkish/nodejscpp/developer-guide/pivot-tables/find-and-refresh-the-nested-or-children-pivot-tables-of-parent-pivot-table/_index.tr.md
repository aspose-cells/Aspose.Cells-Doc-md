---
title: Ana Pivot Tablosunun İçindeki Yerleşik veya Çocuk Pivot Tablolarını Bul ve Yenile
type: docs
weight: 60
url: /tr/nodejs-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Aspose.Cells for Node.js via C++ ile ana pivot tablonun gömülü veya alt pivot tablolarını nasıl bulunur ve yenilerim.
keywords: Aspose.Cells for Node.js Excel, Excel Node.js kütüphanesi, Aspose.Cells for Node.js Excel Kütüphanesini Kullanarak Ana Pivot Tablosunun Gömülü veya Alt Pivot Tablolarını Bulma ve Yenileme.
---

## **Olası Kullanım Senaryoları**

Bazı durumlarda, bir pivot tablosu diğer bir pivot tablosunu veri kaynağı olarak kullandığı için buna çocuk pivot tablosu veya yerleşik pivot tablosu denir. [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--) yöntemi kullanarak bir ana pivot tablosunun çocuk pivot tablolarını bulabilirsiniz.

## **Ana Özet Tablosunun İçerisindeki veya Alt Tablolarını Bulma ve Yenileme**

Aşağıdaki örnek kod, üç pivot tablosunu içeren [örnek Excel dosyasını](61767747.xlsx) yükler. Alt iki pivot tablosu yukarıdaki pivot tablosunun alt pivot tablolarıdır ve bu ekran görüntüsünde gösterildiği gibi. Kod, [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--) yöntemini kullanarak alt pivot tablosunu bulur ve ardından birer birer yeniler.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
