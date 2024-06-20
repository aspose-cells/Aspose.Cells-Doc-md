---
title: Excel Tablosunu Veri Aralığına Dönüştür
type: docs
weight: 10
url: /tr/java/convert-an-excel-table-to-a-range-of-data/
---

{{% alert color="primary" %}}

Bazen Microsoft Excel'de bir tablo oluşturursunuz ve onunla gelen tablo işlevleriyle çalışmak istemezsiniz. Bunun yerine, bir tablo gibi görünen bir şey istersiniz. Biçimlendirmeyi kaybetmeden bir tabloda veri tutmak için tabloyu normal bir veri aralığına dönüştürün.

Aspose.Cells, Microsoft Excel'in tablo ve liste nesneleri için bu özelliği destekler.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

**Dönüştürülecek Aralığı Belirt** özelliğini kullanarak bir tabloyu biçimlendirmeyi kaybetmeden hızlıca bir aralığa dönüştürmek için aşağıdaki adımları izleyin. Microsoft Excel 2007/2010'da:

1. Tablonun herhangi bir yerine tıklayın ve etkin hücrenin bir tablo sütununda olduğundan emin olun.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_1.gif)

1. **Tasarım** sekmesinde, **Araçlar** grubunda, **Dönüştür**'ü tıklayın.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

Tablo özellikleri, tablo bir aralığa dönüştürüldükten sonra artık kullanılamaz. Örneğin, satır başlıkları artık sıralama ve filtre oklarını içermez ve formüllerde kullanılan yapılandırılmış referanslar (tablo adlarını kullanan referanslar), normal hücre referanslarına dönüşür.

{{% /alert %}}

## **Aspose.Cells Kullanımı**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **Tablo, Aralığı Seçenekleri ile Aralığı Dönüştürme**

Aspose.Cells, [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions) sınıfı aracılığıyla Tabloyu Veri Aralığına dönüştürürken ek seçenekler sağlar. [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions) sınıfı, belirli bir satırın son indeksini ayarlamanıza olanak tanıyan [**LastRow**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow) özelliğini sağlar. Tablo biçimlendirmesi belirtilen satır indeksine kadar korunacak ve geri kalan biçimlendirme kaldırılacaktır.

Aşağıda verilen örnek kod, [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions) sınıfının kullanımını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
