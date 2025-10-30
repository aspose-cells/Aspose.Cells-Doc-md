---
title: Hücreden Tablo Erişimi ve Satır ve Sütun Ofsetleri Kullanarak Değerler Eklemek
type: docs
weight: 230
url: /tr/python-net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalde, Tablo veya List Objesi içine değerleri [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool) yöntemini kullanarak eklersiniz. Ancak bazen, Tablo veya List Objesi içine değerleri satır ve sütun ofsetleri kullanarak eklemeniz gerekebilir.

Hücreden Tablo veya List Objesine erişmek için [**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#) yöntemini kullanın. Satır ve sütun ofsetleri kullanarak içine değerler eklemek için [**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any) yöntemini kullanın.

{{% /alert %}}

Aşağıdaki ekran görüntüsü, koddaki kullanılan kaynak Excel dosyasını gösterir. Boş tabloyu içerir ve tablonun içinde bulunan D5 hücresini vurgular. Bu tabloya D5 hücresinden [**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#) yöntemini kullanarak erişeceğiz ve ardından [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool) ve [**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any) yöntemlerini kullanarak içine değerler ekleyeceğiz.

## Örnek

### Kaynak ve çıktı dosyalarını karşılaştıran ekran görüntüleri

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

Aşağıdaki ekran görüntüsü, kod tarafından oluşturulan çıktı Excel dosyasını göstermektedir. D5 hücresinin bir değeri olduğunu ve tablonun 2,2 ofsetindeki F6 hücresinin bir değeri olduğunu görebilirsiniz.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### Hücreden tabloya erişmek ve satır ve sütun kaydırmaları kullanarak içine değerler eklemek için Python kodu

Yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükleyen ve tablo içine değer ekleyen ve yukarıda gösterilen çıktı Excel dosyasını oluşturan aşağıdaki örnek kod verilmiştir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-AccessTableFromCellAndAddValue.py" >}}
{{< app/cells/assistant language="python-net" >}}
