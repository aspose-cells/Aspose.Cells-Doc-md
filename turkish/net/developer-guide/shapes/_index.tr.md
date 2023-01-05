---
title: Excel dosyalarının Resimlerini ve Şekillerini ekleyin.
linktitle: şekiller
type: docs
weight: 140
url: /tr/net/insert-shapes/
description: Resimleri, oleobject'i, şekilleri Excel dosyalarına dönüştürün.
---
{{% alert color="primary" %}}

Bazen çalışma sayfasına bazı gerekli şekilleri eklemeniz gerekir. Aynı şekli çalışma sayfasının farklı konumlarına eklemeniz gerekebilir. Veya çalışma sayfasına toplu olarak şekiller eklemeniz gerekebilir.

 Endişelenme![Aspose.Cells](https://products.aspose.com/cells/)tüm bu işlemleri destekler.

{{% /alert %}}

Excel'deki şekiller temel olarak aşağıdaki türlere ayrılır:
- **resimler**
- **Ole Nesneleri**
- **çizgiler**
- **dikdörtgenler**
- **Basit şekiller**
- **Blok Okları**
- **Denklem Şekilleri**
- **Akış Şemaları**
- **Yıldızlar ve Afişler**
- **açıklamalar**

 Bu kılavuz belge, numune yapmak için her türden bir veya iki şekil seçecektir. Bu örnekler aracılığıyla, nasıl kullanılacağını öğreneceksiniz.[Aspose.Cells](https://products.aspose.com/cells/) Belirtilen şekli çalışma sayfasına eklemek için.

## **C#'de Excel Çalışma Sayfasına Resim Ekleme**

Bir e-tabloya resim eklemek çok kolaydır. Yalnızca birkaç satır kod alır:
 basitçe[**Eklemek**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) yöntemi[**resimler**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) koleksiyon (kapsüllenmiş[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nesne). bu[**Eklemek**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)yöntem aşağıdaki parametreleri alır:

- **Sol üst sıra dizini**, sol üst satırın dizini.
- **Sol üst sütun dizini**, sol üst sütunun dizini.
- **Resim dosyası adı**, resim dosyasının adı, yol ile tamamlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **C#'de OLE Nesnelerini Excel Çalışma Sayfasına Ekleme**

Aspose.Cells, çalışma sayfalarına OLE nesneleri eklemeyi, ayıklamayı ve değiştirmeyi destekler. Bu nedenle Aspose.Cells,[**OleNesne Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) toplama listesine yeni bir OLE Nesnesi eklemek için kullanılan sınıf. Başka bir sınıf,[**Ole nesnesi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), bir OLE Nesnesini temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Görüntü Verileri**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)özelliği, bayt dizisi türündeki görüntü (simge) verilerini belirtir. Görüntü, çalışma sayfasında OLE Nesnesini göstermek için görüntülenecektir.
-  bu[**Nesne Verileri**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)özelliği, nesne verilerini bir bayt dizisi biçiminde belirtir. OLE Object ikonuna çift tıkladığınızda bu veriler ilgili programda gösterilecektir.

Aşağıdaki örnek, bir OLE Nesnesinin/Nesnelerinin bir çalışma sayfasına nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **C#'de Excel Çalışma Sayfasına Satır Ekleme**

 Çizginin şekli şuna aittir:**çizgiler** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Satırı eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
- Ardından, 'Son Kullanılan Şekiller' veya 'Çizgiler' arasından satırı seçin.

![](line.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına bir satır eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[genel LineShape AddLine(
 int üstSolSatır,
 üst,
 int üstSol Sütun,
 int sola,
 yükseklik,
 int genişliği
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 Yöntem bir döndürür[Çizgi Şekli](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) nesne.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına nasıl satır ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](line2.png)



## **C#'de Excel Çalışma Sayfasına bir çizgi oku ekleme**

 Çizgi okunun şekli şuna aittir:**çizgiler** kategori. Çizginin özel bir halidir.

***Microsoft Excel'de (örneğin 2007):***

- Çizgi okunu eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
- Ardından, 'Son Kullanılan Şekiller' veya 'Çizgiler'den çizgi okunu seçin

![](line_arrow1.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına çizgi oku eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[genel LineShape AddLine(
 int üstSolSatır,
 üst,
 int üstSol Sütun,
 int sola,
 yükseklik,
 int genişliği
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 Yöntem bir döndürür[Çizgi Şekli](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) nesne.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına çizgi okunun nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](line_arrow2.png)



## **C#'de Excel Çalışma Sayfasına Dikdörtgen Ekleme**

 Dikdörtgenin şekli şuna aittir:**dikdörtgenler** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Dikdörtgeni eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
- Ardından, "Son Kullanılan Şekiller" veya "Dikdörtgenler" arasından dikdörtgeni seçin.

![](rectangle.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına bir dikdörtgen eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[genel RectangleShape AddRectangle(
 int üstSolSatır,
 üst,
 int üstSol Sütun,
 int sola,
 yükseklik,
 int genişliği
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

 Yöntem bir döndürür[Dikdörtgen şekil](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) nesne.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına dikdörtgenin nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](rectangle2.png)



## **C#'de Excel Çalışma Sayfasına Küp Ekleme**

Küpün şekli şuna aittir:**Basit şekiller** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Küpü eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
-  Ardından, Küpü seçin**Basit şekiller**

![](cube.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına bir küp eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[genel Shape AddAutoShape(
 AutoShapeType türü,
 int üstSolSatır,
 üst,
 int üstSol Sütun,
 int sola,
 yükseklik,
 int genişliği
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, küpün bir çalışma sayfasına nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](cube2.png)



## **C#'de Excel Çalışma Sayfasına belirtme çizgisi dörtlü ok ekleme**

 Belirtme çizgisi dörtlü okunun şekli şuna aittir:**Blok Okları** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Dörtlü oku belirtme çizgisi eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
-  Ardından, belirtme çizgisi dörtlü okunu seçin.**Blok Okları**

![](callout_quad_arrow.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına bir belirtme çizgisi dörtlü ok eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[genel Shape AddAutoShape(
 AutoShapeType türü,
 int üstSolSatır,
 üst,
 int üstSol Sütun,
 int sola,
 yükseklik,
 int genişliği
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, belirtme çizgisi dörtlü okunun bir çalışma sayfasına nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](callout_quad_arrow2.png)



## **C#'de Excel Çalışma Sayfasına çarpma işareti ekleme**

 Çarpma işaretinin şekli şuna aittir:**Denklem Şekilleri** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Çarpma işaretini eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
-  Ardından, çarpma işaretini seçin**Denklem Şekilleri**

![](multiplication_sign.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına bir çarpma işareti eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[genel Shape AddAutoShape(
 AutoShapeType türü,
 int üstSolSatır,
 üst,
 int üstSol Sütun,
 int sola,
 yükseklik,
 int genişliği
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına çarpma işaretinin nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](multiplication_sign2.png)



## **C#'de Excel Çalışma Sayfasına çoklu belge ekleme**

 Çoklu belgenin şekli şuna aittir:**Akış Şemaları** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Çoklu belgeyi eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
-  Ardından, çoklu belgeyi seçin**Akış Şemaları**

![](multidocument.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına çoklu belge eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[genel Shape AddAutoShape(
 AutoShapeType türü,
 int üstSolSatır,
 üst,
 int üstSol Sütun,
 int sola,
 yükseklik,
 int genişliği
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, çoklu belgenin bir çalışma sayfasına nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](multidocument2.png)



## **C#'de Excel Çalışma Sayfasına Beş Köşeli Yıldız Ekleme**

 Beş köşeli yıldızın şekli,**Yıldızlar ve Afişler** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Beş köşeli yıldızı eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
-  Ardından, beş köşeli yıldızı seçin.**Yıldızlar ve Afişler**

![](star_5_points.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına Beş Köşeli yıldız eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[genel Shape AddAutoShape(
 AutoShapeType türü,
 int üstSolSatır,
 üst,
 int üstSol Sütun,
 int sola,
 yükseklik,
 int genişliği
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına Beş Köşeli yıldızın nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](star_5_points2.png)



## **C#'de Excel Çalışma Sayfasına bir düşünce balonu bulutu ekleme**

 Düşünce baloncuğu bulutunun şekli,**açıklamalar** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Düşünce balonu bulutunu eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
-  Ardından, düşünce balonu bulutunu seçin.**açıklamalar**

![](thought_bubble_cloud.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına bir düşünce balonu bulutu eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[genel Shape AddAutoShape(
 AutoShapeType türü,
 int üstSolSatır,
 üst,
 int üstSol Sütun,
 int sola,
 yükseklik,
 int genişliği
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına düşünce balonu bulutunun nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](thought_bubble_cloud2.png)

## **ileri konular**
- [Şeklin Ayarlama Değerlerini Değiştirme](/cells/tr/net/change-adjustment-values-of-the-shape/)
- [Çalışma Sayfaları Arasında Şekilleri Kopyalama](/cells/tr/net/copy-shapes-between-worksheets/)
- [İlkel Olmayan Şekildeki Veriler](/cells/tr/net/data-in-non-primitive-shape/)
- [Çalışma Sayfası İçinde Şeklin Mutlak Konumunu Bulma](/cells/tr/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Şekilden Bağlantı noktalarını alın](/cells/tr/net/get-connection-points-from-shape/)
- [Kontrolleri Yönetme](/cells/tr/net/managing-controls/)
- [Çalışma Sayfasına Simgeler Ekle](/cells/tr/net/insert-svg-to-excel/)
- [OLE Nesnelerini Yönetme](/cells/tr/net/managing-ole-objects/)
- [Resimleri Yönetme](/cells/tr/net/managing-pictures/)
- [Akıllı Sanatı Yönet](/cells/tr/net/managing-smartart/)
- [Metin Kutusunu Yönetme](/cells/tr/net/managing-textbox-of-excel/)
- [Çalışma Sayfasına WordArt Filigranı Ekleme](/cells/tr/net/add-wordart-watermark-to-worksheet/)
- [Bağlantılı Şekillerin Değerlerini Yenile](/cells/tr/net/refresh-values-of-linked-shapes/)
- [Şekli Çalışma Sayfasının Önüne veya Arkasına Gönder](/cells/tr/net/send-shape-front-or-back-inside-the-worksheet/)
- [Şekil Seçeneklerini Yönet](/cells/tr/net/managing-shape-options/)
- [Şekil Metni Seçeneklerini Yönetin](/cells/tr/net/managing-shape-text-options/)
- [Web Uzantıları - Office Eklentileri](/cells/tr/net/web-extensions-office-add-ins/)

