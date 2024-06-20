---
title: Bir Çalışma Sayfasında Değerlerin Yerine Formülleri Göster
type: docs
weight: 100
url: /tr/java/show-formulas-instead-of-values-in-a-worksheet/
---

{{% alert color="primary" %}}

Microsoft Excel'de formülleri hesaplanmış değerlerin yerine göstermek mümkündür. Bu, **Formüller** sekmesindeki *Formülleri Göster* seçeneğini kullanarak yapılır. Formüller gösterildiğinde, Microsoft Excel, çalışma sayfasında formülleri görüntüler. Aynı şeyi Aspose.Cells kullanarak da yapabilirsiniz.

{{% /alert %}} 

Aspose.Cells, bir [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) özelliği sağlar. Bu özelliği **true** olarak ayarlayarak Microsoft Excel'in formüllerini göstermesini sağlayabilirsiniz.

Aşağıdaki görüntü, A3 hücresinde =Sum(A1:A2) formülü olan çalışma sayfasını göstermektedir.

**A3 hücresinde formül olan çalışma sayfası**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_1.png)

Aşağıdaki görüntü, [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) özelliğini **true** olarak ayarlayarak hesaplanmış değer yerine formülü gösteren çalışma sayfasını göstermektedir.

**Çalışma sayfası artık hesaplanmış değer yerine formülü gösteriyor**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
