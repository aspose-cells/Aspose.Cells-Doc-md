---
title: Cell'den Tabloya Erişmek ve Satır ve Sütun Ofsetlerini Kullanarak İçerisine Değerler Eklemek
type: docs
weight: 230
url: /tr/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 Normal olarak, Tablo veya Liste Nesnesinin içindeki değerleri şunu kullanarak eklersiniz:[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)yöntem. Ancak bazen, satır ve sütun uzaklıklarını kullanarak Tablo veya Liste Nesnesi içine değerler eklemeniz gerekebilir.

Bir hücreden Tablo veya Liste Nesnesine erişmek için,[**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) yöntem. Satır ve sütun ofsetlerini kullanarak içine değerler eklemek için[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) yöntem.

{{% /alert %}}

 Aşağıdaki ekran görüntüsü, kodun içinde kullanılan kaynak Excel dosyasını göstermektedir. Boş tabloyu içerir ve tablonun içinde bulunan D5 hücresini vurgular. Bu tabloya D5 hücresinden şunu kullanarak erişeceğiz:[**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) yöntemini kullanın ve ardından her ikisini de kullanarak içindeki değerleri ekleyin.[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) ve[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue)yöntemler.

## Örnek vermek

### Kaynak ve çıktı dosyalarını karşılaştıran ekran görüntüleri

|![yapılacaklar:resim_alternatif_metin](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
|:- |

Aşağıdaki ekran görüntüsü, kod tarafından oluşturulan çıktı Excel dosyasını gösterir. Görüldüğü gibi D5 hücresi bir değere sahiptir ve tablonun 2,2 konumunda bulunan F6 hücresi bir değere sahiptir.

|![yapılacaklar:resim_alternatif_metin](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
|:- |

### C# kodu, hücreden tabloya erişmek ve satır ve sütun ofsetlerini kullanarak içine değerler eklemek için

Aşağıdaki örnek kod, yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükler ve tablonun içindeki değerleri ekler ve yukarıda gösterildiği gibi çıktı Excel dosyasını oluşturur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
