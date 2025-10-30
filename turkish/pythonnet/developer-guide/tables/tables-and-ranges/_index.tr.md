---
title: Tablolar ve Aralıklar
type: docs
weight: 50
url: /tr/python-net/tables-and-ranges/
---

## **Giriş**

Bazen Microsoft Excel'de bir tablo oluşturursunuz ve onunla gelen tablo işlevleriyle çalışmak istemezsiniz. Bunun yerine, bir tablo gibi görünen bir şey istersiniz. Biçimlendirmeyi kaybetmeden bir tabloda veri tutmak için tabloyu normal bir veri aralığına dönüştürün.
Aspose.Cells for Python via .NET, Microsoft Excel'in tablo ve liste nesneleri özelliğini destekler.

## **Microsoft Excel Kullanımı**

**Dönüştürülecek Aralığı Belirt** özelliğini kullanarak bir tabloyu biçimlendirmeyi kaybetmeden hızlıca bir aralığa dönüştürmek için aşağıdaki adımları izleyin. Microsoft Excel 2007/2010'da:

1. Tablonun herhangi bir yerine tıklayın ve etkin hücrenin bir tablo sütununda olduğundan emin olun.
1. **Tasarım** sekmesinde, **Araçlar** grubunda, **Dönüştür**'ü tıklayın.

## **Aspose.Cells for Python via .NET Kullanılarak**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRange-1.py" >}}

{{% alert color="primary" %}}

Tablo özellikleri, tablo bir aralığa dönüştürüldükten sonra artık kullanılamaz. Örneğin, satır başlıkları artık sıralama ve filtre oklarını içermez ve formüllerde kullanılan yapılandırılmış referanslar (tablo adlarını kullanan referanslar), normal hücre referanslarına dönüşür.

{{% /alert %}}

## **Tablo, Aralığı Seçenekleri ile Aralığı Dönüştürme**

Aspose.Cells for Python via .NET, Tabloyu Aralığa dönüştürürken ek seçenekler sağlar; [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions) sınıfı aracılığıyla yapılabilir. [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions) sınıfı, [**last_row**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions/last_row/) özelliğiyle tablonun son satırını belirlemenize izin verir. Bu ayar ile formatlama, belirlenen satıra kadar korunur ve kalan formatlama kaldırılır.

Aşağıda verilen örnek kod, [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions) sınıfının kullanımını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRangeWithOptions-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
