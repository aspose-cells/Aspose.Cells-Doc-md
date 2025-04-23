---
title: Tablolar ve Aralıklar
type: docs
weight: 30
url: /tr/go-cpp/tables-and-ranges/
---

## **Giriş**

Bazen bir tablo oluşturursunuz ve Microsoft Excel'in getirdiği tablo işlevselliğiyle çalışmaya devam etmek istemezsiniz. Bunun yerine, bir tabloya benzeyen bir şey istersiniz. Biçimlendirmeyi kaybetmeden bir tabloda veriyi tutmak için tabloyu düzenli bir veri aralığına dönüştürün. Aspose.Cells, tablolar ve liste nesneleri için Microsoft Excel'in bu özelliğini destekler.

## **Microsoft Excel Kullanımı**

**Dönüştürülecek Aralığı Belirt** özelliğini kullanarak bir tabloyu biçimlendirmeyi kaybetmeden hızlıca bir aralığa dönüştürmek için aşağıdaki adımları izleyin. Microsoft Excel 2007/2010'da:

1. Tablonun herhangi bir yerine tıklayın ve etkin hücrenin bir tablo sütununda olduğundan emin olun.
1. **Tasarım** sekmesinde, **Araçlar** grubunda, **Dönüştür**'ü tıklayın.

{{% alert color="primary" %}}

Tablo özellikleri, tablo bir aralığa dönüştürüldükten sonra artık kullanılamaz. Örneğin, satır başlıkları artık sıralama ve filtre oklarını içermez ve formüllerde kullanılan yapılandırılmış referanslar (tablo adlarını kullanan referanslar), normal hücre referanslarına dönüşür.

{{% /alert %}}

## **Aspose.Cells Kullanımı**

Aşağıdaki kod parçası Aspose.Cells kullanarak aynı işlevselliği göstermektedir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertTableToRange.go" >}}
