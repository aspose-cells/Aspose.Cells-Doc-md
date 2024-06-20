---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /tr/net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Bazen çalışma sayfanızın görüntüsünü şeffaf bir görüntü olarak oluşturmanız gerekebilir. Dolgu renkleri olmayan tüm hücrelere şeffaflık uygulamak istersiniz. Aspose.Cells, çalışma sayfasına şeffaflık uygulamak için [**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent) özelliğini sağlar. Bu özellik **false** olduğunda, dolgu renkleri olmayan hücreler beyaz renkle çizilir ve **true** olduğunda, dolgu renkleri olmayan hücreler şeffaf şekilde çizilir.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
