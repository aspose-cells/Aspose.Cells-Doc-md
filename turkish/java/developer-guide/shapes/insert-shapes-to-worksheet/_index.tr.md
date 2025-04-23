---
title: Aspose.Cells te Çalışma Sayfasına Şekiller Ekleyin
type: docs
weight: 5
url: /tr/java/insert-shapes-to-worksheet-in-aspose-cells/
---


{{% alert color="primary" %}}

Bazen çalışma sayfasına bazı gerekli şekiller eklemeniz gerekebilir. Aynı şekli çalışma sayfasının farklı konumlarına eklemeniz gerekebilir. Veya şekilleri toplu olarak çalışma sayfasına eklemeniz gerekebilir.

Endişelenmeyin! [Aspose.Cells](https://products.aspose.com/cells/), tüm bu operasyonları destekler.

{{% /alert %}}

Bu rehber belgesi, örnek oluşturmak için her türden bir veya iki şekil seçecektir. Bu örnekler aracılığıyla, belirli şekli çalışma sayfasına eklemek için [Aspose.Cells](https://products.aspose.com/cells/) kullanmayı öğreneceksiniz.
- **Çizgiler**
- **Dikdörtgenler**
- **Temel Şekiller**
- **Blok Okları**
- **Denklem Şekilleri**
- **Akış Şemaları**
- **Yıldızlar ve Pankartlar**
- **Çağrılar**

Bu rehber doküman, her türden bir veya iki şekil seçecek ve örnekler yapacaktır. Bu örnekler aracılığıyla, [Aspose.Cells](https://products.aspose.com/cells/) kullanarak belirtilen şekli çalışma tablosuna nasıl ekleyeceğinizi öğreneceksiniz.



## **Çalışma Sayfasına Satır Ekleme**

Satırın şekli **çizgiler** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Satırı eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Ardından, 'Son Kullanılan Şekiller' veya 'Çizgiler'den satırı seçin

![](line.png)

***Aspose.Cells Kullanarak***

Çalışma sayfasına bir satır eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-)

Bu yöntem bir [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına satır eklemenin nasıl yapılacağını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](line2.png)



## **Çalışma Sayfasına Satır Oku Eklemek**

Satırın oku şekli **Çizgiler** kategorisine aittir. Bu, bir satırın özel bir durumudur.

***Microsoft Excel'de (örneğin 2007):***

- Ok satırını eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Ardından, 'Son Kullanılan Şekiller' veya 'Çizgiler'den ok satırını seçin

![](line_arrow1.png)

***Aspose.Cells Kullanarak***

Çalışma sayfasına bir ok satırı eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-)

Bu yöntem bir [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına ok satırı eklemenin nasıl yapılacağını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](line_arrow2.png)



## **Çalışma Sayfasına Dikdörtgen Ekleme**

Dikdörtgenin şekli **Dikdörtgenler** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Dikdörtgeni eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Ardından, 'Son Kullanılan Şekiller' veya 'Dikdörtgenler'den dikdörtgeni seçin

![](rectangle.png)

***Aspose.Cells Kullanarak***

Çalışma sayfasına bir dikdörtgen eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-)

Bu yöntem bir [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına dikdörtgen nasıl ekleyeceğinizi gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](rectangle2.png)



## **Çarpan bir Küp Eklemek**

Küpün şekli **Temel Şekiller** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Küpü eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Sonra, **Temel Şekiller**'den Küp'ü seçin

![](cube.png)

***Aspose.Cells Kullanarak***

Çalışma sayfasına bir küp eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Bu yöntem bir [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına küp nasıl ekleyeceğinizi gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](cube2.png)



## **Çağrı oku dört oklu bir ok ekleniyor**

Çağrı oku dört ok şekli **Bloklı Oklar** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Çağrı ok dört ok eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Sonra, **Bloklı Oklar**'dan çağrı ok dört ok'u seçin

![](callout_quad_arrow.png)

***Aspose.Cells Kullanarak***

Çalışma sayfasına bir çağrı oku dört ok eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Bu yöntem bir [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına çağrı ok dört ok nasıl ekleyeceğinizi gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](callout_quad_arrow2.png)



## **Çarpma işareti ekleniyor**

Çarpma işareti şekli **Denklem Şekilleri** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Çarpma işareti eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Sonra, **Denklem Şekilleri**'nden çarpma işaretini seçin

![](multiplication_sign.png)

***Aspose.Cells Kullanarak***

Çarpma işaretini çalışma sayfasına eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Bu yöntem bir [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına çarpma işareti eklemeyi göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](multiplication_sign2.png)



## **Çoklu belgeyi Çalışma Sayfasına Ekleme**

Çoklu belgenin şekli **FlowCharts** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Çoklu belgeyi eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Sonra, **FlowCharts**'den çoklu belgeyi seçin

![](multidocument.png)

***Aspose.Cells Kullanarak***

Çalışma sayfasına çoklu belge eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Bu yöntem bir [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına çoklu belge eklemeyi göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](multidocument2.png)



## **Beş köşeli yıldızı Çalışma Sayfasına Ekleme**

Beş köşeli yıldızın şekli **Yıldızlar ve Bayraklar** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Beş köşeli yıldızı eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Sonra, **Yıldızlar ve Bayraklar**'dan beş köşeli yıldızı seçin

![](star_5_points.png)

***Aspose.Cells Kullanarak***

Çalışma sayfasına beş köşeli yıldız eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Bu yöntem bir [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına beş köşeli yıldız eklemeyi göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](star_5_points2.png)



## **Düşünce balonu bulutunu Çalışma Sayfasına Ekleme**

Düşünce balonu bulutunun şekli **Çağrılar** kategorisine aittir.

***Microsoft Excel'de (örneğin 2007):***

- Düşünce balonu bulutu eklemek istediğiniz hücreyi seçin
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.
- Daha sonra, **Araç Çubuğu**'ndan düşünce balonu bulutunu seçin

![](thought_bubble_cloud.png)

***Aspose.Cells Kullanarak***

Çalışma sayfasına düşünce balonu bulutu eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Bu yöntem bir [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesnesi döndürür.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına düşünce balonu bulutu nasıl ekleyeceğinizi gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:

![](thought_bubble_cloud2.png)
{{< app/cells/assistant language="java" >}}
