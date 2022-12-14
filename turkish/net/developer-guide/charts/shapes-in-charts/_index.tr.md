---
title: Grafiklerdeki Şekiller
type: docs
weight: 70
url: /tr/net/controls-in-charts/
---
{{% alert color="primary" %}}

Bazen bir grafiğe etiketler, metin kutuları, resimler vb. gibi çizim nesneleri eklemeniz gerekir. Aspose.Cells, kontrolleri çalışma zamanında bir grafiğe ekleyebilir.

{{% /alert %}}

## **Grafiğe Etiket Kontrolü Ekleme**

Etiketler, kullanıcılara elektronik tablonun içeriği hakkında bilgi vermek için bir araç sağlar.
Aspose.Cells, grafiklere bile etiket eklemenize ve değiştirmenize olanak tanır.

bu[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart), bir grafiğe etiket denetimi eklemek için kullanılır. Yöntem için kullanılan parametrelerin listesi aşağıdadır:

- **tepe** – grafik alanının 1/4000'lik birimlerinde sol üst köşeden etiketin dikey ofseti.
- **ayrıldı** – grafik alanının 1/4000'lik birimlerinde sol üst köşeden etiketin dikey ofseti.
- **yükseklik** – grafik alanının 1/4000 birimi cinsinden etiketin yüksekliği.
- **Genişlik** – grafik alanının 1/4000'lik birimleri cinsinden etiket genişliği.

 Yöntem döndürür[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)nesne. bu[**Etiket**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) class grafikte bir etiketi temsil eder. Bazı önemli üyeleri vardır:

- [**Metin**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)(özellik) – bir etiketin başlık dizesini belirtir.
- [**Doldurmak**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (özellik) – dolgu rengi niteliklerini belirtir.

Aşağıdaki örnek, grafiğe nasıl etiket ekleneceğini gösterir. Örnek bir tasarımcı dosyası kullanır (**exp_piecart.xls**) içinde bir grafik var. Grafiğe bir etiket eklemek için bu dosyayı kullanıyoruz. Grafiğe etiket eklemek için orijinal kod aşağıdadır. Kod yürütülürken aşağıdaki çıktı oluşturulur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

## **Grafiğe Metin Kutusu Denetimi Ekleme**

 Bir rapordaki önemli bilgileri vurgulamanın bir yolu, bir metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya en yüksek satışa sahip coğrafi bölgeyi belirtmek için metin girin. bu[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart)bir grafiğe bir metin kutusu denetimi eklemek için kullanılır. Yöntem için kullanılan parametre listesi aşağıdadır:

- **tepe** – grafik alanının 1/4000 biriminde metin kutusunun sol üst köşeden dikey uzaklığı.
- **ayrıldı** – grafik alanının 1/4000 biriminde metin kutusunun sol üst köşeden dikey uzaklığı.
- **yükseklik**– grafik alanının 1/4000'lik birimlerinde metin kutusunun yüksekliği.
- **Genişlik** – grafik alanının 1/4000'lik birimleri cinsinden metin kutusunun genişliği.

 Yöntem döndürür[**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) nesne. bu[**Metin kutusu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)class, grafikte bir metin kutusunu temsil eder.

Aşağıdaki örnek, bir grafiğe nasıl metin kutusu ekleneceğini gösterir. Örnek, önceki tasarımcı dosyasını kullanır (**exp_piecart.xls**) içinde bir grafik var. Grafik başlığını göstermek için grafiğe bir metin kutusu eklemek için bu dosyayı kullanıyoruz. Grafiğe metin kutusu eklemek için orijinal kod aşağıdadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **Grafiğe Resim Ekleme**

Aspose.Cells, bir grafiğe resim eklemenizi sağlar. Örneğin, bir grafiği veya içeriğini vurgulamak veya daha fazla anlam vermek için bir resim ekleyin veya bir marka görsel dosyası ekleyin.

 bu[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**Grafikte Resim Ekle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart)grafiğe bir resim nesnesi eklemek için kullanılır. Yöntem için kullanılan parametre listesi aşağıdadır:

- **tepe**– tablo alanının 1/4000 biriminde resmin sol üst köşeden dikey kayması.
- **ayrıldı**– tablo alanının 1/4000 biriminde resmin sol üst köşeden dikey kayması.
- **aktarım** – görüntü verilerini içeren bir akış nesnesi.
- **genişlikÖlçeği** – görüntü genişliği ölçeği, bir yüzde değeri.
- **yükseklikÖlçek** – görüntü yüksekliği ölçeği, bir yüzde değeri.

 Yöntem bir döndürür[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) nesne. bu[**Resim**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)class, grafikteki bir resim nesnesini temsil eder.

Aşağıdaki örnek, grafiğe nasıl resim ekleneceğini gösterir. Örnek, önceki tasarımcı dosyasını kullanır (**exp_piecart.xls**) içinde bir grafik var. Bu dosyayı grafiğe bir resim eklemek için kullanıyoruz. Grafiğe resim eklemek için orijinal kod aşağıdadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **Grafiğe Onay Kutusu Ekleme**

 Aspose.Cells kullanarak bir grafik sayfasına onay kutuları eklemenizi sağlar.[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) numaralandırma. Aşağıdaki örnek, bir grafik sayfasına bir onay kutusu eklemeyi gösterir.

Aşağıdaki resimde, çıktı dosyasında onay kutusu bulunan grafik sayfası gösterilmektedir.

![yapılacaklar:resim_alternatif_Metin](controls-in-charts_1.jpg)

 bu[çıktı dosyası](101089316.xlsx)aşağıdaki kod parçacığı tarafından oluşturulan referans için eklenmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **ileri konular**
- [Grafiğe WordArt Filigranı Ekleme](/cells/tr/net/add-wordart-watermark-to-chart/)
