---
title: Grafiklerdeki Kontroller
linktitle: Grafikteki Şekiller
type: docs
weight: 60
url: /tr/java/controls-in-charts/
---
{{% alert color="primary" %}}

Bazen bir grafiğe etiketler, metin kutuları, resimler vb. gibi çizim nesneleri eklemeniz gerekir. Aspose.Cells, kontrolleri çalışma zamanında bir grafiğe ekleyebilir.

{{% /alert %}}

## **Grafiğe Etiket Kontrolü Ekleme**

Etiketler, kullanıcılara elektronik tablonun içeriği hakkında bilgi vermek için bir araç sağlar. Aspose.Cells, grafiklere bile etiket eklemenize ve değiştirmenize olanak tanır.

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) sınıf adlı bir yöntem sağlar[**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart(int,%20int,%20int,%20int)), bir grafiğe bir etiket kontrolü eklemek için kullanılır. Yöntem için kullanılan parametrelerin listesi aşağıdadır:

- **tepe** – grafik alanının 1/4000'lik birimlerinde sol üst köşeden etiketin dikey ofseti.
- **sol** – grafik alanının 1/4000'lik birimlerinde sol üst köşeden etiketin dikey ofseti.
- **boy uzunluğu** – grafik alanının 1/4000 birimi cinsinden etiketin yüksekliği.
- **Genişlik** – grafik alanının 1/4000'lik birimlerinde etiketin genişliği.

 Yöntem, bir nesne döndürür[**Etiket**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) sınıf, nerede[**Etiket**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)class grafikte bir etiketi temsil eder. Aşağıda ayrıntıları verilen bazı önemli üyeleri vardır:

- [**Metin**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text)özelliği, bir etiketin başlık dizesini belirtir.
- [**Doldurmak**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) özelliği, dolgu rengi niteliklerini belirtir.

Aşağıdaki örnek, grafiğe nasıl etiket ekleneceğini gösterir. Örnek, içinde grafik bulunan bir tasarımcı dosyası kullanır. Grafiğe bir etiket eklemek için bu dosyayı kullanıyoruz.

Aşağıda, tasarımcı dosyasının bir ekran görüntüsü bulunmaktadır.

**tasarımcı grafiği**

![yapılacaklar:resim_alternatif_metin](controls-in-charts_1.png)

Grafiğe etiket eklemek için orijinal kod aşağıdadır. Kod yürütülürken aşağıdaki çıktı oluşturulur.

**Grafiğe bir etiket eklendi**

![yapılacaklar:resim_alternatif_metin](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **Grafiğe Metin Kutusu Denetimi Ekleme**

 Bir rapordaki önemli bilgileri vurgulamanın bir yolu, bir metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya en yüksek satışa sahip coğrafi bölgeyi belirtmek için metin girin. bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) sınıf adlı bir yöntem sağlar[**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart(int,%20int,%20int,%20int)), bir grafiğe bir metin kutusu denetimi eklemek için kullanılır. Yöntem için kullanılan parametre listesi aşağıdadır:

- **tepe** – grafik alanının 1/4000 biriminde metin kutusunun sol üst köşeden dikey uzaklığı.
- **sol** – grafik alanının 1/4000 biriminde metin kutusunun sol üst köşeden dikey uzaklığı.
- **boy uzunluğu**– grafik alanının 1/4000'lik birimlerinde metin kutusunun yüksekliği.
- **Genişlik** – grafik alanının 1/4000'lik birimleri cinsinden metin kutusunun genişliği.

 Yöntem, bir nesne döndürür[**Metin kutusu**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) sınıf nerede[**Metin kutusu**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)class, grafikte bir metin kutusunu temsil eder.

Aşağıdaki örnek, bir grafiğe nasıl metin kutusu ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki tasarımcı dosyasını kullanır. Grafik başlığını göstermek için grafiğe bir metin kutusu eklemek için bu dosyayı kullanıyoruz.

Grafiğe bir metin kutusu eklemek için orijinal kod aşağıdadır. Kod yürütülürken aşağıdaki çıktı oluşturulur.

**Grafiğe bir metin kutusu eklenir**

![yapılacaklar:resim_alternatif_metin](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **Grafiğe Resim Ekleme**

Aspose.Cells, bir grafiğe resim eklemenizi sağlar. Örneğin, bir grafiği veya içeriğini vurgulamak veya daha fazla anlam vermek için bir resim ekleyin veya bir marka görsel dosyası ekleyin.

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) sınıf adlı bir yöntem sağlar[**ResimInChart'a ekle**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart(int,%20int,%20java.io.InputStream,%20int,%20int)), grafiğe bir resim nesnesi eklemek için kullanılır. Yöntem için kullanılan parametre listesi aşağıdadır:

- **tepe**– tablo alanının 1/4000 biriminde resmin sol üst köşeden dikey kayması.
- **sol**– tablo alanının 1/4000 biriminde resmin sol üst köşeden dikey kayması.
- **aktarım** – görüntü verilerini içeren bir akış nesnesi.
- **genişlikÖlçeği** – görüntü genişliği ölçeği, bir yüzde değeri.
- **yükseklikÖlçek** – görüntü yüksekliği ölçeği, bir yüzde değeri.

 Yöntem, bir nesne döndürür[**Resim**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) sınıf nerede[**Resim**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)class, grafikteki bir resim nesnesini temsil eder.

Aşağıdaki örnek, grafiğe nasıl resim ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki tasarımcı dosyasını kullanır. Bu dosyayı grafiğe bir resim eklemek için kullanıyoruz.

Grafiğe resim eklemek için orijinal kod aşağıdadır. Kod yürütülürken aşağıdaki çıktı üretilir

**Grafiğe bir resim eklenir**

![yapılacaklar:resim_alternatif_metin](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **Grafiğe Onay Kutusu Ekleme**

Aspose.Cells kullanarak bir grafik sayfasına onay kutuları eklemenizi sağlar.[**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType) numaralandırma. Aşağıdaki örnek, bir grafik sayfasına bir onay kutusu eklemeyi gösterir.

Aşağıdaki resimde, çıktı dosyasında onay kutusu bulunan grafik sayfası gösterilmektedir.

![yapılacaklar:resim_alternatif_metin](controls-in-charts_5.jpg)

bu[çıktı dosyası](InsertCheckboxInChartSheet_out.xlsx)aşağıdaki kod parçacığı tarafından oluşturulan referans için eklenmiştir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
