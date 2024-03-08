---
title: Aspose.Cells kullanarak PivotChart nasıl eklenir?
linktitle: Pivot Grafik
type: docs
weight: 100
url: /tr/java/how-to-add-pivot-chart/
description: Aspose.Cells'i kullanarak PivotChart nasıl eklenir?
keywords: PivotChart
---
##  PivotChart Nedir?

Excel'deki PivotChart, PivotTable'dan oluşturulan verilerin grafiksel temsilidir. Bilgileri grafik biçiminde özetleyip görüntüleyerek kullanıcıların verileri dinamik olarak görselleştirmelerine ve analiz etmelerine olanak tanır. PivotChart'lar etkileşimlidir ve verilerin farklı perspektiflerini gösterecek şekilde kolayca değiştirilebilir; bu da onu Excel'de veri analizi ve sunumu için güçlü bir araç haline getirir.

##  Aspose.Cells kullanarak PivotChart nasıl eklenir?
###  **Pivot Tablo Oluşturma**

Aspose.Cells'i kullanarak bir pivot tablo oluşturmak için:

1. Cell nesnesinin PutValue/setValue yöntemini kullanarak çalışma sayfası hücrelerine bazı veriler ekleyin. Ayrıca halihazırda verilerle doldurulmuş bir şablon dosyası da kullanırsınız. Veriler pivot tablonun veri kaynağı olarak kullanılacaktır.
1. PivotTables koleksiyonunun ekleme yöntemini (Çalışma Sayfası nesnesinde kapsüllenmiş) çağırarak çalışma sayfasına bir pivot tablo ekleyin.
1. Dizinini ileterek PivotTable koleksiyonundan yeni PivotTable nesnesine erişin.
1. Tabloyu yönetmek için PivotTable nesnesinde kapsüllenmiş pivot tablo nesnelerinden herhangi birini kullanın.

Aşağıda bir kod örneği verilmiştir. Kodun yürütülmesi yeni bir dosya oluşturur: pivotTable_test.xls.

**Giriş verileri** 

![yapılacak şey:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**Çıkış pivot tablosu**

![yapılacak şey:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

###  **Pivot Tabloyu Temel Alan Pivot Grafik Oluşturma**

Aspose.Cells'i kullanarak pivot grafik oluşturmak için:

1. Bir grafik ekleyin.
1. Grafiğin PivotSource'unu e-tablodaki mevcut bir pivot tabloya başvuracak şekilde ayarlayın.
1. Diğer nitelikleri ayarlayın.

Aşağıda, bileşenin görevi gerçekleştirmek için kullandığı kod bulunmaktadır. Kodun yürütülmesi yeni bir dosya oluşturur: pivotChart_test.xls.

**Pivot grafik sayfası**

![yapılacak şey:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Bu makale, Aspose.Cells'i kullanarak pivot tabloların ve pivot grafiklerin nasıl oluşturulacağını gösterir. Umarız bu özellikleri kendi senaryolarınızda kullanmanıza yardımcı olur.

Aspose.Cells yıllarca süren araştırma, tasarım ve dikkatli ayarlamalardan yararlanmıştır.

 Soru, görüş ve önerilerinizi şu adrese bekliyoruz:[Aspose.Cells Forumu](https://forum.aspose.com/c/cells/9). Hızlı yanıt garantisi veriyoruz.

{{% /alert %}}
