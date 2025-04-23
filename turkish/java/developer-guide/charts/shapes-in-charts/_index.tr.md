---
title: Grafiklerde Kontroller
linktitle: Grafikte Şekiller
type: docs
weight: 60
url: /tr/java/controls-in-charts/
---

{{% alert color="primary" %}}

Bazen bir grafik içine etiketler, metin kutuları, resimler ve benzeri çizim nesneleri eklemeniz gerekebilir. Aspose.Cells, çalışma zamanında bir grafiğe denetim ekleyebilir.

{{% /alert %}}

## **Grafiğe Etiket Denetimi Ekleme**

Etiketler, bir elektronik tablonun içeriği hakkında kullanıcılara bilgi vermenin bir yolunu sağlar. Aspose.Cells, etiketleri hatta grafiklere bile eklemenize ve bunları manipüle etmenize olanak sağlar.

 [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) sınıfı, bir etiket kontrolü eklemek için kullanılan [**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart-int-int-int-int-) adında bir yöntem sağlar. Aşağıda bu yöntem için kullanılan parametrelerin bir listesi bulunmaktadır:

- **üst** – etiketin sol üst köşesinden dikey ofset (1/4000 biriminde grafik alanı).
- **sol** – etiketin sol üst köşesinden yatay ofset (1/4000 biriminde grafik alanı).
- **yükseklik** – etiketin yüksekliği, grafik alanının 1/4000 biriminde.
- **Genişlik** – etiketin genişliği, birim olarak 1/4000'lik chart alanının birimleri.

Yöntem, [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) sınıfının bir nesnesini döndürür, burada [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) sınıfı, tabloda bir etiketi temsil eder. Aşağıda bununla ilgili bazı önemli üyeler bulunmaktadır:

- [**Text**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text) özelliği bir etiketin başlık dizesini belirtir.
- [**Fill**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) özelliği doldurma renk özelliklerini belirtir.

Aşağıdaki örnek, bir etiketi tabloya eklemenin nasıl yapıldığını göstermektedir. Örnek, bir grafik içeren bir tasarımcı dosyasını kullanır. Bu dosyayı bir etiketi grifiğe eklemek için kullanırız.

Aşağıda tasarımcı dosyasının ekran görüntüsü bulunmaktadır.

**Tasarımcı grafik**

![todo:image_alt_text](controls-in-charts_1.png)

Aşağıda, grafik üzerine bir etiket eklemek için orijinal kod bulunmaktadır. Kodu çalıştırdığınızda aşağıdaki çıktı oluşturulur.

**Bir etiket grafik üzerine eklenir**

![todo:image_alt_text](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **Grafiğe TextBox Kontrolü Ekleme**

Bir raporda önemli bilgileri vurgulamanın bir yolu, bir metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya en yüksek satış yapılan coğrafi bölgeyi belirtmek için metin girin. [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) sınıfı, grafiğe bir metin kutusu denetimi eklemek için kullanılan [**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart-int-int-int-int-) adında bir yöntem sağlar. Aşağıdaki parametre listesi, yöntem için kullanılan parametreleri gösterir:

- **top** – metin kutusunun grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **sol** – metin kutusunun grafik alanının sol üst köşesinden yatay ofseti, 1/4000 birim olarak.
- **height** – metin kutusunun yüksekliği, grafik alanının 1/4000 biriminde.
- **width** – metin kutusunun genişliği, grafik alanının 1/4000 biriminde.

Yöntem, bir [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) sınıfının nesnesini döndürür. [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) sınıfı, grafikte bir metin kutusunu temsil eder.

Aşağıdaki örnek, bir metin kutusunu bir grafik üzerine nasıl ekleyeceğinizi göstermektedir. Örnek, içinde grafik bulunan önceki tasarımcı dosyasını kullanır. Bu dosyayı kullanarak grafiğe bir metin kutusu ekleriz.

Grafik üzerine bir metin kutusu eklemek için orijinal kod aşağıda verilmektedir. Kodu çalıştırdığınızda aşağıdaki çıktı oluşturulur.

**Bir metin kutusu grafik üzerine eklenir**

![todo:image_alt_text](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **Grafiğe Resim Ekleme**

Aspose.Cells, bir grafiğe resim eklemenize olanak tanır. Örneğin, bir resim ekleyerek bir grafiği vurgulamak veya anlamını artırmak veya bir marka resim dosyası eklemek.

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) sınıfı, grafiğe bir resim nesnesi eklemek için kullanılan [**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart-int-int-java.io.InputStream-int-int-) adında bir yöntem sağlar. Aşağıdaki parametre listesi, yöntem için kullanılan parametreleri gösterir:

- **top** – resmin, grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **left** – resmin, grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **stream** – resim verisini içeren bir akım nesnesi.
- **widthScale** – resmin genişlik ölçeği, yüzde değeri.
- **heightScale** – resmin yükseklik ölçeği, yüzde değeri.

Yöntem, [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) sınıfının bir nesnesini döndürür. [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) sınıfı, grafikte bir resim nesnesini temsil eder.

Aşağıdaki örnek, bir resmi bir grafik üzerine nasıl ekleyeceğinizi göstermektedir. Örnek, içinde grafik bulunan önceki tasarımcı dosyasını kullanır. Bu dosyayı kullanarak grafiğe bir resim ekleriz.

Aşağıda, grafik üzerine bir resim eklemek için orijinal kod bulunmaktadır. Kodu çalıştırdığınızda aşağıdaki çıktı oluşturulur.

**Bir resim grafik içine eklenir**

![todo:image_alt_text](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **Grafiğe Onay Kutusu Ekleme**

Aspose.Cells, [**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType) numaralandırmasını kullanarak bir grafik sayfasına onay kutuları eklemenize olanak tanır. Aşağıdaki örnek, bir grafik sayfasına bir onay kutusu eklemenin nasıl yapılacağını göstermektedir.

Aşağıdaki resim, çıktı dosyasındaki grafik tablosunu içeren onay kutusu göstermektedir.

![todo:image_alt_text](controls-in-charts_5.jpg)

Aşağıdaki kod parçası tarafından oluşturulan [çıktı dosyası](InsertCheckboxInChartSheet_out.xlsx) ekli olarak sunulmuştur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
{{< app/cells/assistant language="java" >}}
