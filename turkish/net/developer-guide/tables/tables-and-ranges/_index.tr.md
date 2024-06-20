---
title: Tablolar ve Aralıklar
type: docs
weight: 50
url: /tr/net/tables-and-ranges/
---

## **Giriş**

Bazen Microsoft Excel'de bir tablo oluşturursunuz ve onunla gelen tablo işlevleriyle çalışmak istemezsiniz. Bunun yerine, bir tablo gibi görünen bir şey istersiniz. Biçimlendirmeyi kaybetmeden bir tabloda veri tutmak için tabloyu normal bir veri aralığına dönüştürün.
Aspose.Cells, Microsoft Excel'in tablo ve liste nesneleri için bu özelliği destekler.

## **Microsoft Excel Kullanımı**

**Dönüştürülecek Aralığı Belirt** özelliğini kullanarak bir tabloyu biçimlendirmeyi kaybetmeden hızlıca bir aralığa dönüştürmek için aşağıdaki adımları izleyin. Microsoft Excel 2007/2010'da:

1. Tablonun herhangi bir yerine tıklayın ve etkin hücrenin bir tablo sütununda olduğundan emin olun.
1. **Tasarım** sekmesinde, **Araçlar** grubunda, **Dönüştür**'ü tıklayın.

## **Aspose.Cells Kullanımı**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

Tablo özellikleri, tablo bir aralığa dönüştürüldükten sonra artık kullanılamaz. Örneğin, satır başlıkları artık sıralama ve filtre oklarını içermez ve formüllerde kullanılan yapılandırılmış referanslar (tablo adlarını kullanan referanslar), normal hücre referanslarına dönüşür.

{{% /alert %}}

## **Tablo, Aralığı Seçenekleri ile Aralığı Dönüştürme**

Aspose.Cells, [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) sınıfı aracılığıyla Tablo'yu Aralığa dönüştürürken ek seçenekler sağlar. [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) sınıfı, belirtilen satır dizinine kadar tablo biçimlendirmesini korumanızı ve geri kalan biçimlendirmeyi kaldırmanızı sağlayan [**LastRow**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow) özelliğini sağlar.

Aşağıda verilen örnek kod, [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) sınıfının kullanımını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}
