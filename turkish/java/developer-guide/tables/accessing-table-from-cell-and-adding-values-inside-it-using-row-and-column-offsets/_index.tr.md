---
title: Hücreden Tablo Erişimi ve Satır ve Sütun Ofsetleri Kullanarak Değerler Eklemek
type: docs
weight: 110
url: /tr/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalde, Tablo veya List Objesi içine değerleri [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue-boolean-) yöntemini kullanarak eklersiniz. Ancak bazen, Tablo veya List Objesi içine değerleri satır ve sütun ofsetleri kullanarak eklemeniz gerekebilir.

Bir hücreden Tablo veya Liste Nesnesine erişmek için [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--) yöntemini kullanın. Ve satır ve sütun konumları kullanarak değer eklemek için [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue-int-int-java.lang.Object-) yöntemini kullanın.

{{% /alert %}}

## Örnek

### Kaynak ve çıktı dosyalarını karşılaştıran ekran görüntüleri

Aşağıdaki ekran görüntüsü, koddaki kullanılan kaynak Excel dosyasını gösterir. Boş tabloyu içerir ve tablonun içinde bulunan D5 hücresini vurgular. Bu tabloya D5 hücresinden [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--) yöntemini kullanarak erişeceğiz ve ardından [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue-boolean-) ve [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue-int-int-java.lang.Object-) yöntemlerini kullanarak içine değerler ekleyeceğiz.

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

Aşağıdaki ekran görüntüsü, kod tarafından oluşturulan çıktı Excel dosyasını göstermektedir. D5 hücresinin bir değeri olduğunu ve tablonun 2,2 ofsetindeki F6 hücresinin bir değeri olduğunu görebilirsiniz.

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Hücreden tabloya erişmek ve içine değer eklemek için Java kodu

Yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükleyen ve tablo içine değer ekleyen ve yukarıda gösterilen çıktı Excel dosyasını oluşturan aşağıdaki örnek kod verilmiştir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
{{< app/cells/assistant language="java" >}}
