---
title: Pivot Tablo Oluşturma
type: docs
weight: 10
url: /tr/python-java/create-a-pivot-table/
---
## **Pivot Tablo Oluşturma**
Java üzerinden Python için Aspose.Cells, pivot tablolar oluşturma özelliği sağlar. Aspose.Cells kullanarak bir pivot tablo oluşturmak için lütfen aşağıdaki adımları izleyin:

1. kullanarak çalışma sayfası hücrelerine bazı veriler ekleyin.[Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell)nesnenin[değer ayarla](https://reference.aspose.com/cells/python/asposecells.api/cell#Value)Emlak. Bu veriler, pivot tablo için bir veri kaynağı olarak kullanılacaktır.
1. Çağırarak çalışma sayfasına bir pivot tablo ekleyin.[Özet Tablo Koleksiyonu](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)[Ekle](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)) yöntemi, kapsüllenmiş[Çalışma kağıdı](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)nesne.
1. Erişmek[Pivot tablo](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)gelen nesne[Özet Tablo Koleksiyonu](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)geçerek[Pivot tablo](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)dizin.
1. Kapsüllenmiş pivot tablo nesnelerinden (yukarıda açıklanmıştır) herhangi birini kullanın.[Özet Tablo Koleksiyonu](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)pivot tabloyu yönetmek için nesne.

Aşağıdaki kod parçacığı, Aspose.Cells API ile bir pivot tablo oluşturmayı gösterir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
