---
title: Cell'den Tabloya Erişmek ve Satır ve Sütun Ofsetlerini Kullanarak İçerisine Değerler Eklemek
type: docs
weight: 110
url: /tr/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 Normal olarak, Tablo veya Liste Nesnesinin içindeki değerleri şunu kullanarak eklersiniz:[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)) yöntem. Ancak bazen, satır ve sütun uzaklıklarını kullanarak Tablo veya Liste Nesnesi içine değerler eklemeniz gerekebilir.

Bir hücreden Tablo veya Liste Nesnesine erişmek için,[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) yöntem. Satır ve sütun ofsetlerini kullanarak içine değerler eklemek için[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) yöntem.

{{% /alert %}}

## Örnek vermek

### Kaynak ve çıktı dosyalarını karşılaştıran ekran görüntüleri

 Aşağıdaki ekran görüntüsü, kodun içinde kullanılan kaynak Excel dosyasını göstermektedir. Boş tabloyu içerir ve tablonun içinde bulunan D5 hücresini vurgular. Bu tabloya D5 hücresinden şunu kullanarak erişeceğiz:[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) yöntemi ve ardından her ikisini de kullanarak içindeki değerleri ekleyin[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean) ) ve[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) yöntemler.

![yapılacaklar:resim_alternatif_metin](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

Aşağıdaki ekran görüntüsü, kod tarafından oluşturulan çıktı Excel dosyasını gösterir. Görüldüğü gibi D5 hücresi bir değere sahiptir ve tablonun 2,2 konumunda bulunan F6 hücresi bir değere sahiptir.

![yapılacaklar:resim_alternatif_metin](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Java kodu, hücreden tabloya erişmek ve satır ve sütun ofsetlerini kullanarak içine değerler eklemek için

Aşağıdaki örnek kod, yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükler ve tablonun içindeki değerleri ekler ve yukarıda gösterildiği gibi çıktı Excel dosyasını oluşturur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
