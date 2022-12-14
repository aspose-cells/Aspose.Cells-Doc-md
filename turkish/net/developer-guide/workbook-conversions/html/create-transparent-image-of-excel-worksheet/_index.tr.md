---
title: Excel Çalışma Sayfasının Saydam Görüntüsünü Oluşturun
type: docs
weight: 170
url: /tr/net/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

 Bazen, çalışma sayfanızın görüntüsünü şeffaf bir görüntü olarak oluşturmanız gerekir. Dolgu renkleri olmayan tüm hücrelere saydamlık uygulamak istiyorsunuz. Aspose.Cells şunları sağlar:[**ImageOrPrintOptions.Şeffaf**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)çalışma sayfası görüntüsüne saydamlık uygulama özelliği. Bu özellik ne zaman**yanlış** , daha sonra dolgu renkleri olmayan hücreler beyaz renkle çizilir ve**doğru**, dolgu renkleri olmayan hücreler saydam olarak çizilir.

{{% /alert %}} 

Aşağıdaki çalışma sayfası görüntüsünde saydamlık uygulanmamıştır. Dolgu renkleri olmayan hücreler beyaz olarak çizilir.

|**Şeffaflık olmadan çıktı: hücre arka planı beyazdır**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](create-transparent-image-of-excel-worksheet_1.png)|

Aşağıdaki çalışma sayfası görüntüsünde ise şeffaflık uygulanmıştır. Dolgu rengi olmayan hücreler şeffaftır.

|**Şeffaflık etkinleştirilmiş çıktı**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](create-transparent-image-of-excel-worksheet_2.png)|

Aşağıdaki örnek kod, bir Excel çalışma sayfasından saydam bir görüntü oluşturur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
