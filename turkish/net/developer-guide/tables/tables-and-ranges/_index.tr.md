---
title: Tablolar ve Aralıklar
type: docs
weight: 50
url: /tr/net/tables-and-ranges/
---
## **Giriş**

Bazen Microsoft Excel'de bir tablo oluşturursunuz ve beraberinde gelen tablo işleviyle çalışmaya devam etmek istemezsiniz. Bunun yerine, masaya benzeyen bir şey istiyorsunuz. Biçimlendirmeyi kaybetmeden verileri bir tabloda tutmak için tabloyu normal bir veri aralığına dönüştürün.
Aspose.Cells, tablolar ve liste nesneleri için Microsoft Excel'in bu özelliğini destekler.

## **Microsoft Excel'i kullanma**

 Kullan**Aralığa Dönüştür** biçimlendirmeyi kaybetmeden bir tabloyu hızla bir aralığa dönüştürme özelliği. Microsoft Excel 2007/2010'da:

1. Aktif hücrenin bir tablo sütununda olduğundan emin olmak için tabloda herhangi bir yeri tıklayın.
1.  Üzerinde**Tasarım** sekmesinde, içinde**Araçlar** grup, tıklayın**Aralığa Dönüştür**.

## **Aspose.Cells'i kullanma**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

Tablo bir aralığa dönüştürüldükten sonra tablo özellikleri artık kullanılamaz. Örneğin, satır başlıkları artık sıralama ve filtre oklarını içermez ve formüllerde kullanılan yapılandırılmış başvurular (tablo adlarını kullanan başvurular), normal hücre başvurularına dönüşür.

{{% /alert %}}

## **Seçeneklerle Tabloyu Aralığa Dönüştür**

Aspose.Cells, Tabloyu Aralığa dönüştürürken ek seçenekler sunar.[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) sınıf. bu[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)sınıf sağlar[**Son Sıra**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow)tablo satırının son dizinini ayarlamanıza izin veren özellik. Tablo biçimlendirmesi, belirtilen satır dizinine kadar korunacak ve biçimlendirmenin geri kalanı kaldırılacaktır.

Aşağıda verilen örnek kod,[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)sınıf.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}
