---
title: Excel Çalışma Sayfasının Saydam Görüntüsünü Oluşturun
type: docs
weight: 80
url: /tr/java/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

 Bazen, çalışma sayfanızın görüntüsünü şeffaf bir görüntü olarak oluşturmanız gerekir. Dolgu renkleri olmayan tüm hücrelere saydamlık uygulamak istiyorsunuz. Aspose.Cells şunları sağlar:[**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) çalışma sayfası görüntüsüne saydamlık uygulama özelliği. Bu özellik ne zaman**YANLIŞ** , daha sonra dolgu renkleri olmayan hücreler beyaz renkle çizilir ve**doğru**, dolgu renkleri olmayan hücreler saydam olarak çizilir.

{{% /alert %}}

Aşağıdaki çalışma sayfası görüntüsünde saydamlık uygulanmamıştır. Dolgu renkleri olmayan hücreler beyaz olarak çizilir.

**Saydamlık uygulamadan çalışma sayfası görüntüsü**

![yapılacaklar:resim_alternatif_metin](create-transparent-image-of-excel-worksheet_1.png)

Aşağıdaki çalışma sayfası görüntüsünde ise şeffaflık uygulanmıştır. Dolgu rengi olmayan hücreler şeffaftır.

**Saydamlık uygulandıktan sonra çalışma sayfası görüntüsü**

![yapılacaklar:resim_alternatif_metin](create-transparent-image-of-excel-worksheet_2.png)

Excel çalışma sayfanızın saydam bir görüntüsünü oluşturmak için aşağıdaki örnek kodu kullanabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
