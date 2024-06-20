---
title: Excel Tablosunu Veri Aralığına Dönüştür
type: docs
weight: 10
url: /tr/python-java/convert-an-excel-table-to-a-range-of-data/
---

## **Excel Tablosunu Veri Aralığına Dönüştür**
Aspose.Cells for Python via Java, Excel tablosunu bir veri aralığına dönüştürme seçeneği sunar. Bunun için API, [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) yöntemini sağlar. Aşağıdaki kod parçası, [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) yöntemini kullanarak bir Excel tablosunu bir veri aralığına dönüştürmenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Excel Tablosunu Bir Seçenekle Veri Aralığına Dönüştür**
Bir tabloyu bir veri aralığına dönüştürürken, [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) sınıfını kullanarak ek seçenekler sağlayabilirsiniz. Ek seçenekleri belirtmek için [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) sınıfının bir örneğini [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) yöntemine iletebilirsiniz. Aşağıdaki kod parçası, [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) sınıfını kullanarak tablonun son satır endeksini belirlemek için nasıl kullanıldığını göstermektedir. Tablo formatlaması belirtilen satır endeksine kadar korunur ve geri kalan formatlama kaldırılır.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
