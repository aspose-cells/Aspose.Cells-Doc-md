---
title: Excel Tablosunu Veri Aralığına Dönüştürme
type: docs
weight: 10
url: /tr/python-java/convert-an-excel-table-to-a-range-of-data/
---
## **Excel Tablosunu Veri Aralığına Dönüştürme**
Aspose.Cells for Python via Java, Excel Tablosunu bir veri aralığına dönüştürme seçeneği sunar. Bunun için API,[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\) ) yöntem. Aşağıdaki kod parçacığı, kullanımını gösterir[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) bir Excel tablosunu bir veri aralığına dönüştürme yöntemi.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Bir Excel Tablosunu Seçeneklerle Aralığa Dönüştürme**
Bir tabloyu aralığa dönüştürürken ek seçenekler sağlayabilirsiniz.[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) sınıf. örneğini iletebilirsiniz[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)sınıfa[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) ek seçenekleri belirtmek için yöntem. Aşağıdaki kod parçacığı,[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)tablonun son satır dizinini ayarlamak için sınıf. Tablo biçimlendirmesi, belirtilen satır dizinine kadar korunacak ve biçimlendirmenin geri kalanı kaldırılacaktır.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
