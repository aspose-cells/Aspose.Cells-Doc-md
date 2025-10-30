---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /tr/python-net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Bazen, çalışma sayfanızın şeffaf bir resim olarak üretilmesini istersiniz. Tüm hücrelere şeffaflık uygulamak istersiniz, dolgu rengi olmayan hücreler dahil. Aspose.Cells for Python via .NET, şeffaflık uygulamak için [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent) özelliği sağlar. Bu özellik **false** ise, dolgusu olmayan hücreler beyaz renkte çizilir, **true** ise, şeffaf olarak çizilir.

{{% /alert %}} 

Aşağıdaki çalışma sayfası görüntüsünde şeffaflık uygulanmamıştır. Dolgu rengi olmayan hücreler beyaz olarak çizilmiştir.

|**Şeffaflık olmadan çıktı: hücre arka planı beyazdır**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

Ancak aşağıdaki çalışma sayfası görüntüsünde şeffaflık uygulanmıştır. Dolgu rengi olmayan hücreler şeffaf olarak çizilmiştir.

|**Şeffaflık etkinleştirilmiş çıktı**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

Aşağıdaki örnek kod, bir Excel çalışma sayfasından şeffaf bir görüntü oluşturur.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-CreateTransparentImage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
