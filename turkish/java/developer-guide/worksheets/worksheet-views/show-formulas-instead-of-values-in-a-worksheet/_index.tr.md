---
title: Çalışma Sayfasında Değerler Yerine Formülleri Gösterme
type: docs
weight: 100
url: /tr/java/show-formulas-instead-of-values-in-a-worksheet/
---
{{% alert color="primary" %}}

t kullanarak Microsoft Excel'de hesaplanan değerler yerine formülleri göstermek mümkündür.*Formülleri Göster* seçeneği**formüller**kurdele. Formüller gösterildiğinde, Microsoft Excel formülleri çalışma sayfasında görüntüler. Aynı şeyi Aspose.Cells'i kullanarak da elde edebilirsiniz.

{{% /alert %}} 

Aspose.Cells bir sağlar[**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) Emlak. Bunu şuna ayarla:**doğru**Microsoft Excel'i formülleri gösterecek şekilde ayarlamak için.

Aşağıdaki resimde, A3 hücresinde bir formül bulunan çalışma sayfası gösterilmektedir: =Toplam(A1:A2).

**A3 hücresinde formül bulunan çalışma sayfası**

![yapılacaklar:resim_alternatif_metin](show-formulas-instead-of-values-in-a-worksheet_1.png)

 Aşağıdaki resimde, hesaplanan değer yerine ayarlanarak etkinleştirilen formül gösterilmektedir.[**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) mülkiyet**doğru** Aspose.Cells ile.

**Çalışma sayfası artık hesaplanan değer yerine formülü gösteriyor**

![yapılacaklar:resim_alternatif_metin](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
