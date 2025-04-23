---
title: Excel dosyalarına Resimler ve Şekiller Ekleyin.
linktitle: Şekiller
type: docs
weight: 140
url: /tr/python-net/insert-shapes/
description: Resimleri, oleobjectleri ve şekilleri Excel dosyalarına ekleyin.
---

{{% alert color="primary" %}}

Bazen çalışma sayfasına bazı gerekli şekiller eklemeniz gerekebilir. Aynı şekli çalışma sayfasının farklı konumlarına eklemeniz gerekebilir. Veya şekilleri toplu olarak çalışma sayfasına eklemeniz gerekebilir.

Endişelenmeyin! [Aspose.Cells](https://products.aspose.com/cells/), tüm bu operasyonları destekler.

{{% /alert %}}

Bu rehber belgesi, örnek oluşturmak için her türden bir veya iki şekil seçecektir. Bu örnekler aracılığıyla, belirli şekli çalışma sayfasına eklemek için [Aspose.Cells](https://products.aspose.com/cells/) kullanmayı öğreneceksiniz.
- **Resimler**
- **OleObjects**
- **Çizgiler**
- **Dikdörtgenler**
- **Temel Şekiller**
- **Blok Okları**
- **Denklem Şekilleri**
- **Akış Şemaları**
- **Yıldızlar ve Pankartlar**
- **Çağrılar**

Bu rehber doküman, her türden bir veya iki şekil seçecek ve örnekler yapacaktır. Bu örnekler aracılığıyla, [Aspose.Cells](https://products.aspose.com/cells/) kullanarak belirtilen şekli çalışma tablosuna nasıl ekleyeceğinizi öğreneceksiniz.

## **C# ile Excel Çalışma Tablosuna Resim Ekleme**

Bir elektron mikroskobuna resim eklemek çok kolaydır. Sadece birkaç satır kod gerektirir:
Basitçe, [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) noktasal nesnesinde kapsüllenmiş olan [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) nesnesinin [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) metodunu çağırın. [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) metodu aşağıdaki parametreleri alır:

- **üst_sol_satır**, üst sol satırın dizini.
- **üst_sol_sütun**, üst sol sütunun dizini.
- **dosya_adi**, görüntü dosyasının adı, yol dahil.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-Pictures-AddingPictures-1.py" >}}


## **C# ile Excel Çalışma Tablosuna OLE Nesneleri Eklemek**

Aspose.Cells for Python via .NET, OLE nesnelerini çalışma sayfalarına ekleme, çıkarma ve manipüle etme desteği sağlar. Bu nedenle, Aspose.Cells for Python via .NET'de, koleksiyon listesine yeni bir OLE nesnesi eklemek için kullanılan [**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection) sınıfı bulunur. Diğer bir sınıf olan [**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject), bir OLE nesnesini temsil eder. Bazı önemli üyeleri şunlardır:

- [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data) özelliği, ikon olarak gösterilecek görüntü (ikon) verisini bayt dizisi türünde belirtir. Görüntü, çalışsayan elemanı çalışsayan eleman levhasında göstermek için kullanılacaktır.
- [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data) özelliği, bayt dizisi biçimindeki nesne verisini belirtir. Bu veri, çalışsayan eleman simgesine çift tıkladığınızda ilgili programda gösterilecektir.

Aşağıdaki örnek, çalışsayan elemanları çalışsayan eleman(lar)ı çalışsayan eleman yapıştırma.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-OLE-InsertingOLEObjects-1.py" >}}

## **C# ile Excel Çalışma Tablosuna Çizgi Eklemek**

Satırın şekli **çizgiler** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Satırı eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Ardından, 'Son Kullanılan Şekiller' veya 'Çizgiler'den satırı seçin

![](line.png)

***Aspose.Cells for Python via .NET kullanılarak***

Çalışma sayfasına bir satır eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line)

Metod, bir [LineShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) nesnesi döner.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına satır eklemenin nasıl yapılacağını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Line.py" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](line2.png)



## **C# ile Excel Çalışma Kitabına Satır Oku Eklemek**

Satırın oku şekli **Çizgiler** kategorisine aittir. Bu, bir satırın özel bir durumudur.

***Microsoft Excel'de (örneğin 2007):***

- Ok satırını eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Ardından, 'Son Kullanılan Şekiller' veya 'Çizgiler'den ok satırını seçin

![](line_arrow1.png)

***Aspose.Cells for Python via .NET kullanılarak***

Çalışma sayfasına bir ok satırı eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line)

Metod, bir [LineShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) nesnesi döner.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına ok satırı eklemenin nasıl yapılacağını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-LineArrow.py" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](line_arrow2.png)



## **C# ile Excel Çalışma Kitabına Dikdörtgen Eklemek**

Dikdörtgenin şekli **Dikdörtgenler** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Dikdörtgeni eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Ardından, 'Son Kullanılan Şekiller' veya 'Dikdörtgenler'den dikdörtgeni seçin

![](rectangle.png)

***Aspose.Cells for Python via .NET kullanılarak***

Çalışma sayfasına bir dikdörtgen eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**add_rectangle**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_rectangle)

Yöntem, bir [RectangleShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına dikdörtgen nasıl ekleyeceğinizi gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Rectangle.py" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](rectangle2.png)



## **C# ile Excel Çalışma Kitabına Küp Eklemek**

Küpün şekli **Temel Şekiller** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Küpü eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Sonra, **Temel Şekiller**'den Küp'ü seçin

![](cube.png)

***Aspose.Cells for Python via .NET kullanılarak***

Çalışma sayfasına bir küp eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**public Shape add_auto_shape(type, upper_left_row, top, upper_left_column, left, height, width)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

Yöntem, bir [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına küp nasıl ekleyeceğinizi gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Cube.py" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](cube2.png)



## **C# ile Excel Çalışma Sayfasına Çağrı Oku Ok İçin Ekleme**

Çağrı oku dört ok şekli **Bloklı Oklar** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Çağrı ok dört ok eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Sonra, **Bloklı Oklar**'dan çağrı ok dört ok'u seçin

![](callout_quad_arrow.png)

***Aspose.Cells for Python via .NET kullanılarak***

Çalışma sayfasına bir çağrı oku dört ok eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

Yöntem, bir [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına çağrı ok dört ok nasıl ekleyeceğinizi gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.py" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](callout_quad_arrow2.png)



## **C# ile Excel Çalışma Sayfasına Çarpı İşareti Ekleme**

Çarpma işareti şekli **Denklem Şekilleri** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Çarpma işareti eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Sonra, **Denklem Şekilleri**'nden çarpma işaretini seçin

![](multiplication_sign.png)

***Aspose.Cells for Python via .NET kullanılarak***

Çarpma işaretini çalışma sayfasına eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

Yöntem, bir [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına çarpma işareti eklemeyi göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.py" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](multiplication_sign2.png)



## **C# ile Excel Çalışma Sayfasına Çoklu Belge Ekleme**

Çoklu belgenin şekli **FlowCharts** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Çoklu belgeyi eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Sonra, **FlowCharts**'den çoklu belgeyi seçin

![](multidocument.png)

***Aspose.Cells for Python via .NET kullanılarak***

Çalışma sayfasına çoklu belge eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

Yöntem, bir [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına çoklu belge eklemeyi göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Multidocument.py" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](multidocument2.png)



## **C# Dilinde Excel Çalışma Sayfasına Beşgen Yıldız Ekleme**

Beş köşeli yıldızın şekli **Yıldızlar ve Bayraklar** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Beş köşeli yıldızı eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Sonra, **Yıldızlar ve Bayraklar**'dan beş köşeli yıldızı seçin

![](star_5_points.png)

***Aspose.Cells for Python via .NET kullanılarak***

Çalışma sayfasına beş köşeli yıldız eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

Yöntem, bir [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına beş köşeli yıldız eklemeyi göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-FivePointedStar.py" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](star_5_points2.png)



## **C# Dilinde Excel Çalışma Sayfasına Düşünce Balonu Bulutu Ekleme**

Düşünce balonu bulutunun şekli **Çağrılar** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Düşünce balonu bulutu eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Daha sonra, **Araç Çubuğu**'ndan düşünce balonu bulutunu seçin

![](thought_bubble_cloud.png)

***Aspose.Cells for Python via .NET kullanılarak***

Çalışma sayfasına düşünce balonu bulutu eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

Yöntem, bir [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına düşünce balonu bulutu nasıl ekleyeceğinizi gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.py" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](thought_bubble_cloud2.png)

## **Gelişmiş Konular**
- [Şekil Ayar Değerlerini Değiştirme](/cells/tr/python-net/change-adjustment-values-of-the-shape/)
- [Çalışma Sayfaları Arasında Şekilleri Kopyalama](/cells/tr/python-net/copy-shapes-between-worksheets/)
- [İlkel Olmayan Şekildeki Veri](/cells/tr/python-net/data-in-non-primitive-shape/)
- [Çalışma Sayfası İçindeki Şeklin Mutlak Konumunu Bulma](/cells/tr/python-net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Şekilden Bağlantı Noktalarını Al](/cells/tr/python-net/get-connection-points-from-shape/)
- [Denetimleri Yönetme](/cells/tr/python-net/managing-controls/)
- [Çalışma Sayfasına Simgeler Ekleme](/cells/tr/python-net/insert-svg-to-excel/)
- [OLE Nesnelerini Yönetme](/cells/tr/python-net/managing-ole-objects/)
- [Resimleri Yönetme](/cells/tr/python-net/managing-pictures/)
- [Akıllı Sanatı Yönetme](/cells/tr/python-net/managing-smartart/)
- [Metin Kutularını Yönetme](/cells/tr/python-net/managing-textbox-of-excel/)
- [Çalışma Sayfasına WordArt Fili Ekleme](/cells/tr/python-net/add-wordart-watermark-to-worksheet/)
- [Bağlantılı Şekillerin Değerlerini Yenileme](/cells/tr/python-net/refresh-values-of-linked-shapes/)
- [Çalışma Sayfası İçinde Şekil Önüne veya Arkasına Gönderme](/cells/tr/python-net/send-shape-front-or-back-inside-the-worksheet/)
- [Şekil Seçeneklerini Yönetme](/cells/tr/python-net/managing-shape-options/)
- [Şekil Metin Seçeneklerini Yönetme](/cells/tr/python-net/managing-shape-text-options/)
- [Web Uzantıları - Office Eklentileri](/cells/tr/python-net/web-extensions-office-add-ins/)

