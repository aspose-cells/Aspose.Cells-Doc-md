---
title: Grafiklerdeki Şekiller
description: Microsoft Excel'de denetim eklemek ve grafikleri özelleştirmek için Aspose.Cells for .NET'i nasıl kullanacağınızı öğrenin. Kılavuzumuz grafik öğelerini nasıl değiştireceğinizi, biçimlendirmeyi nasıl ayarlayacağınızı ve grafiklerinizin genel görünümünü ve kullanılabilirliğini nasıl geliştireceğinizi gösterecektir.
keywords: Aspose.Cells for .NET, Chart Controls, Chart Customization, Microsoft Excel, Chart Elements, Formatting.
type: docs
weight: 70
url: /tr/net/controls-in-charts/
---
{{% alert color="primary" %}}

Bazen etiketler, metin kutuları, resimler vb. gibi çizim nesnelerini bir grafiğe eklemeniz gerekir. Aspose.Cells, çalışma zamanında kontrolleri bir grafiğe ekleyebilir.

{{% /alert %}}

##  **Grafiğe Etiket Kontrolü Ekleme**

Etiketler, kullanıcılara bir e-tablonun içeriği hakkında bilgi vermek için bir araç sağlar.
Aspose.Cells, grafiklere bile etiket eklemenizi ve değiştirmenizi sağlar.

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart), bir grafiğe etiket denetimi eklemek için kullanılır. Yöntem için kullanılan parametrelerin listesi aşağıda verilmiştir:

- **tepe**– grafik alanının 1/4000'i birimlerinde etiketin sol üst köşeden dikey uzaklığı.
- **sol**– grafik alanının 1/4000'i birimlerinde etiketin sol üst köşeden dikey uzaklığı.
- **yükseklik** – grafik alanının 1/4000'lik birimleri cinsinden etiketin yüksekliği.
- **Genişlik** – grafik alanının 1/4000'i birimlerinde etiketin genişliği.

 Yöntem geri döner[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)nesne.[**Etiket**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) class grafikteki bir etiketi temsil eder. Bazı önemli üyeleri var:

- [**Metin**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)(özellik) – bir etiketin başlık dizesini belirtir.
- [**Doldurmak**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (özellik) – dolgu rengi niteliklerini belirtir.

Aşağıdaki örnek, grafiğe nasıl etiket ekleneceğini gösterir. Örnekte, içinde grafik bulunan bir tasarımcı dosyası (**exp_piechart.xls**) kullanılıyor. Grafiğe etiket eklemek için bu dosyayı kullanıyoruz. Grafiğe etiket eklemeye yönelik orijinal kod aşağıdadır. Kod çalıştırıldığında aşağıdaki çıktı elde edilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

##  **Grafiğe TextBox Denetimi Ekleme**

Bir rapordaki önemli bilgileri vurgulamanın bir yolu metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya satışların en yüksek olduğu coğrafi bölgeyi belirtmek için metin girin.[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart), bir grafiğe metin kutusu denetimi eklemek için kullanılır. Yöntem için kullanılan parametreler listesi aşağıdadır:

- **tepe** – grafik alanının 1/4000'i birimlerinde metin kutusunun sol üst köşeden dikey uzaklığı.
- **sol** – grafik alanının 1/4000'i birimlerinde metin kutusunun sol üst köşeden dikey uzaklığı.
- **yükseklik** – metin kutusunun yüksekliği, grafik alanının 1/4000'i biriminde.
- **Genişlik** – metin kutusunun genişliği, grafik alanının 1/4000'i biriminde.

 Yöntem geri döner[**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) nesne.[**Metin kutusu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)class grafikteki bir metin kutusunu temsil eder.

Aşağıdaki örnek, bir grafiğe metin kutusunun nasıl ekleneceğini gösterir. Örnek, içinde grafik bulunan önceki tasarımcı dosyasını (**exp_piechart.xls**) kullanıyor. Bu dosyayı, grafiğin başlığını göstermek üzere grafiğe bir metin kutusu eklemek için kullanırız. Grafiğe metin kutusu eklemenin orijinal kodu aşağıdadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

##  **Grafiğe Resim Ekleme**

Aspose.Cells, bir grafiğe resim eklemenizi sağlar. Örneğin, bir grafiği veya içeriğini vurgulamak veya daha fazla anlam vermek için bir resim ekleyin veya bir marka görseli dosyası ekleyin.

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**Grafikteki Resim Ekle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart)Grafiğe bir resim nesnesi eklemek için kullanılır. Yöntem için kullanılan parametreler listesi aşağıdadır:

- **tepe** – grafik alanının 1/4000'lik birimlerinde resmin sol üst köşeden dikey uzaklığı.
- **sol** – grafik alanının 1/4000'lik birimlerinde resmin sol üst köşeden dikey uzaklığı.
- **aktarım** – görüntü verilerini içeren bir akış nesnesi.
- **genişlikÖlçek** – görüntü genişliğinin ölçeği, bir yüzde değeri.
- **yükseklikÖlçek** – görüntü yüksekliğinin ölçeği, bir yüzde değeri.

 Yöntem bir döndürür[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) nesne.[**Resim**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)sınıf grafikteki bir resim nesnesini temsil eder.

Aşağıdaki örnek, grafiğe nasıl resim ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki tasarımcı dosyasını (**exp_piechart.xls**) kullanıyor. Grafiğe resim eklemek için bu dosyayı kullanıyoruz. Grafiğe resim eklemek için orijinal kod aşağıdadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

##  **Grafiğe Onay Kutusu Ekleme**

 Aspose.Cells, kullanarak bir grafik sayfasına onay kutuları eklemenizi sağlar[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) numaralandırma. Aşağıdaki örnek, bir grafik sayfasına onay kutusu eklemeyi gösterir.

Aşağıdaki resimde, çıktı dosyasındaki onay kutusunun bulunduğu grafik sayfası gösterilmektedir.

![yapılacak şey:image_alt_text](controls-in-charts_1.jpg)

[çıktı dosyası](101089316.xlsx) Aşağıdaki kod pasajı tarafından oluşturulan kod referansınız için eklenmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

##  **İleri konular**
- [Grafiğe WordArt Filigranı Ekleme](/cells/tr/net/add-wordart-watermark-to-chart/)
