---
title: Excel Tablosunu Veri Aralığına Dönüştürme
type: docs
weight: 10
url: /tr/java/convert-an-excel-table-to-a-range-of-data/
---
{{% alert color="primary" %}}

Bazen Microsoft Excel'de bir tablo oluşturursunuz ve beraberinde gelen tablo işleviyle çalışmaya devam etmek istemezsiniz. Bunun yerine, masaya benzeyen bir şey istiyorsunuz. Biçimlendirmeyi kaybetmeden verileri bir tabloda tutmak için tabloyu normal bir veri aralığına dönüştürün.

Aspose.Cells, tablolar ve liste nesneleri için Microsoft Excel'in bu özelliğini destekler.

{{% /alert %}}

## **Microsoft Excel'i kullanma**

 Kullan**Aralığa Dönüştür** biçimlendirmeyi kaybetmeden bir tabloyu hızla bir aralığa dönüştürme özelliği. Microsoft Excel 2007/2010'da:

1. Aktif hücrenin bir tablo sütununda olduğundan emin olmak için tabloda herhangi bir yeri tıklayın.

![yapılacaklar:resim_alternatif_metin](convert-an-excel-table-to-a-range-of-data_1.gif)

1.  Üzerinde**Tasarım** sekmesinde, içinde**Araçlar** grup, tıklayın**Aralığa Dönüştür**.

![yapılacaklar:resim_alternatif_metin](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

Tablo bir aralığa dönüştürüldükten sonra tablo özellikleri artık kullanılamaz. Örneğin, satır başlıkları artık sıralama ve filtre oklarını içermez ve formüllerde kullanılan yapılandırılmış başvurular (tablo adlarını kullanan başvurular), normal hücre başvurularına dönüşür.

{{% /alert %}}

## **Aspose.Cells'i kullanma**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **Seçeneklerle Tabloyu Aralığa Dönüştür**

Aspose.Cells, Tabloyu Aralığa dönüştürürken ek seçenekler sunar.[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)sınıf. bu[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)sınıf sağlar[**Son Sıra**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow)tablo satırının son dizinini ayarlamanıza izin veren özellik. Tablo biçimlendirmesi, belirtilen satır dizinine kadar korunacak ve biçimlendirmenin geri kalanı kaldırılacaktır.

Aşağıda verilen örnek kod,[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)sınıf.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
