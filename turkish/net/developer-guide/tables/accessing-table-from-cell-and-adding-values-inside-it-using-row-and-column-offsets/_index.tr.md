---
title: Hücreden Tablo Erişimi ve Satır ve Sütun Ofsetleri Kullanarak Değerler Eklemek
type: docs
weight: 230
url: /tr/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalde, Tablo veya List Objesi içine değerleri [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) yöntemini kullanarak eklersiniz. Ancak bazen, Tablo veya List Objesi içine değerleri satır ve sütun ofsetleri kullanarak eklemeniz gerekebilir.

Hücreden Tablo veya List Objesine erişmek için [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) yöntemini kullanın. Satır ve sütun ofsetleri kullanarak içine değerler eklemek için [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) yöntemini kullanın.

{{% /alert %}}

Aşağıdaki ekran görüntüsü, koddaki kullanılan kaynak Excel dosyasını gösterir. Boş tabloyu içerir ve tablonun içinde bulunan D5 hücresini vurgular. Bu tabloya D5 hücresinden [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) yöntemini kullanarak erişeceğiz ve ardından [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) ve [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) yöntemlerini kullanarak içine değerler ekleyeceğiz.

## Örnek

### Kaynak ve çıktı dosyalarını karşılaştıran ekran görüntüleri

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

Aşağıdaki ekran görüntüsü, kod tarafından oluşturulan çıktı Excel dosyasını göstermektedir. D5 hücresinin bir değeri olduğunu ve tablonun 2,2 ofsetindeki F6 hücresinin bir değeri olduğunu görebilirsiniz.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### Hücreden tabloya erişme ve satır ve sütun ofsetleri kullanarak içine değer eklemek için C# kodu

Yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükleyen ve tablo içine değer ekleyen ve yukarıda gösterilen çıktı Excel dosyasını oluşturan aşağıdaki örnek kod verilmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
{{< app/cells/assistant language="csharp" >}}
