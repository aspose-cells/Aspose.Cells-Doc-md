---
title: Tablolar ve Aralıklar
type: docs
weight: 30
url: /tr/cpp/tables-and-ranges/
---
##  **giriiş**
Bazen Microsoft Excel'de bir tablo oluşturursunuz ve birlikte gelen tablo işleviyle çalışmaya devam etmek istemezsiniz. Bunun yerine masaya benzeyen bir şey istiyorsunuz. Biçimlendirmeyi kaybetmeden verileri bir tabloda tutmak için tabloyu normal bir veri aralığına dönüştürün. Aspose.Cells, tablolar ve liste nesneleri için Microsoft Excel'in bu özelliğini desteklemektedir.
##  **Microsoft Excel'i kullanma**
 Kullan**Aralığa Dönüştür** Bir tabloyu biçimlendirmeyi kaybetmeden hızla bir aralığa dönüştürme özelliği. Microsoft Excel 2007/2010'da:

1. Etkin hücrenin bir tablo sütununda olduğundan emin olmak için tabloda herhangi bir yeri tıklayın.
1.  Üzerinde**Tasarım** sekmesinde**Aletler** grubunda *Aralığa Dönüştür**'e tıklayın.

{{% alert color="primary" %}} 

Tablo bir aralığa dönüştürüldükten sonra tablo özellikleri artık kullanılamaz. Örneğin, satır başlıkları artık sıralama ve filtre oklarını içermiyor ve formüllerde kullanılan yapılandırılmış başvurular (tablo adlarını kullanan başvurular) normal hücre başvurularına dönüşüyor.

{{% /alert %}} 
##  **Aspose.Cells'i kullanma**
Aşağıdaki kod parçacığı, Aspose.Cells kullanılarak aynı işlevselliği göstermektedir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange-new.cpp" >}}
