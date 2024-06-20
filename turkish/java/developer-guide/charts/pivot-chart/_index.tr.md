---
title: Aspose.Cells Kullanarak Bir PivotChart Nasıl Eklenir
linktitle: Pivot Grafik
type: docs
weight: 100
url: /tr/java/how-to-add-pivot-chart/
description: Aspose.Cells ı Kullanarak Bir PivotChart Nasıl Eklenir.
keywords: PivotChart
---
## PivotChart Nedir

Excel'de bir PivotChart, bir PivotTable'dan oluşturulan verilerin grafiksel bir temsilidir. Kullanıcılara verileri dinamik olarak görselleştirmelerine ve analiz etmelerine olanak tanır. Veriyi özetleyerek ve bilgileri grafik formunda göstererek PivotChart'lar etkileşimlidir ve verinin farklı perspektiflerini göstermek için kolayca değiştirilebilir, bu da Excel'de veri analizi ve sunum için güçlü bir araç yapar.

## Aspose.Cells kullanarak PivotChart ekleme
### **Pivot Tablosu Oluşturma**

Aspose.Cells kullanarak bir pivot tablosu oluşturmak için:

1. Bir Hücre nesnesi'nin PutValue/setValue yöntemini kullanarak bir çalışma sayfasındaki hücrelere bazı veriler ekleyin. Ayrıca zaten verilerle doldurulmuş bir şablon dosyası kullanabilirsiniz. Veriler, pivot tablosunun veri kaynağı olarak kullanılacaktır.
1. PivotTables koleksiyonunun add yöntemini (Worksheet nesnesinde kapsüllenmiş) çağırarak çalışma sayfasına bir pivot tablosu ekleyin.
1. PivotTables koleksiyonundan yeni PivotTable nesnesine geçerek indeksini iletebilirsiniz.
1. Tabloyu yönetmek için PivotTable nesnesinde kapsüllenmiş herhangi bir pivot tablo nesnesini kullanın.

Aşağıda bileşen tarafından görevin tamamlanması için kullanılan kod örneği bulunmaktadır. Kodu çalıştırmak yeni bir dosya oluşturur: pivotTable_test.xls.

**Giriş verisi** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**Çıktı pivot tablosu**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Pivot Tablosuna Dayalı Pivot Çizelgesi Oluşturma**

Aspose.Cells kullanarak bir pivot çizelgesi oluşturmak için:

1. Bir grafik ekleyin.
1. Grafik PivotSource'unu elektronik tabloda zaten mevcut bir pivot çizelgesine atıf yapacak şekilde ayarlayın.
1. Diğer özellikleri ayarlayın.

Görevi gerçekleştirmek için bileşen tarafından kullanılan kod aşağıda verilmiştir. Kodu çalıştırmak yeni bir dosya oluşturur: pivotChart_test.xls.

**Pivot çizelgesi sayfası**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Bu makale Aspose.Cells kullanarak pivot tabloları ve pivot çizelgeleri oluşturmayı göstermektedir. Umarız kendi senaryolarınızda bu özellikleri kullanmanıza yardımcı olur.

Aspose.Cells yılların araştırması, tasarımı ve dikkatli ayarlamasından faydalanmıştır.

[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9) adresindeki sorularınızı, yorumlarınızı ve önerilerinizi bekliyoruz. Hızlı bir yanıt garantisi veriyoruz.

{{% /alert %}}
