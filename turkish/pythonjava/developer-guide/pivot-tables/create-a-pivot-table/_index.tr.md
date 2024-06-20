---
title: Pivot Tablo Oluşturma
type: docs
weight: 10
url: /tr/python-java/create-a-pivot-table/
---

## **Pivot Tablo Oluşturma**
Aspose.Cells for Python via Java, pivot tablolar oluşturma özelliği sunar. Aspose.Cells kullanarak pivot tablosu oluşturmak için lütfen aşağıdaki adımları izleyin:

1. Pivot tablo için veri kaynağı olarak kullanılacak verileri elektronik tablonun hücrelerine [Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell) nesnesinin [setValue](https://reference.aspose.com/cells/python/asposecells.api/cell#Value) özelliğini kullanarak ekleyin.
1. [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) içinde bulunan [Worksheet](https://reference.aspose.com/cells/python/asposecells.api/Worksheet) nesnesinin çağrılı [add](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)) yöntemini kullanarak elektronik tabloya pivot tablo ekleyin.
1. [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) içinden [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable) nesnesine, [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable) indeksini geçirerek erişin.
1. Yönetim için pivot tablo nesnelerinden herhangi birini (yukarıda açıklandığı gibi) [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) nesnesinin içine yerleştirin.

Aşağıdaki kod satırı, Aspose.Cells API ile pivot tablosu oluşturmayı gösterir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
