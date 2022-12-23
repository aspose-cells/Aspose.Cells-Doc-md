---
title: Aspose.Cells'de Çalışma Sayfasına Şekiller Ekleyin
type: docs
weight: 5
url: /tr/java/insert-shapes-to-worksheet-in-aspose-cells/
---
{{% alert color="primary" %}}

Bazen çalışma sayfasına bazı gerekli şekilleri eklemeniz gerekir. Aynı şekli çalışma sayfasının farklı konumlarına eklemeniz gerekebilir. Veya çalışma sayfasına toplu olarak şekiller eklemeniz gerekebilir.

 Endişelenme![Aspose.Cells](https://products.aspose.com/cells/)tüm bu işlemleri destekler.

{{% /alert %}}

Excel'deki şekiller temel olarak aşağıdaki türlere ayrılır:
- **çizgiler**
- **dikdörtgenler**
- **Basit şekiller**
- **Blok Okları**
- **Denklem Şekilleri**
- **Akış Şemaları**
- **Yıldızlar ve Afişler**
- **açıklamalar**

 Bu kılavuz belge, numune yapmak için her türden bir veya iki şekil seçecektir. Bu örnekler aracılığıyla, nasıl kullanılacağını öğreneceksiniz.[Aspose.Cells](https://products.aspose.com/cells/) Belirtilen şekli çalışma sayfasına eklemek için.



## **Çalışma Sayfasına Satır Ekleme**

 Çizginin şekli şuna aittir:**çizgiler** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Satırı eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
- Ardından, 'Son Kullanılan Şekiller' veya 'Çizgiler' arasından satırı seçin.

![](line.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına bir satır eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[public Shape addShape(int tipi, int üstSolSatır, int üst, int üstSolSütun, int sol, int yükseklik, int genişlik)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına nasıl satır ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](line2.png)



## **Çalışma Sayfasına çizgi oku ekleme**

 Çizgi okunun şekli şuna aittir:**çizgiler** kategori. Çizginin özel bir halidir.

***Microsoft Excel'de (örneğin 2007):***

- Çizgi okunu eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
- Ardından, 'Son Kullanılan Şekiller' veya 'Çizgiler'den çizgi okunu seçin

![](line_arrow1.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına çizgi oku eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[public Shape addShape(int tipi, int üstSolSatır, int üst, int üstSolSütun, int sol, int yükseklik, int genişlik)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına çizgi okunun nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](line_arrow2.png)



## **Çalışma Sayfasına Dikdörtgen Ekleme**

 Dikdörtgenin şekli şuna aittir:**dikdörtgenler** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Dikdörtgeni eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
- Ardından, "Son Kullanılan Şekiller" veya "Dikdörtgenler" arasından dikdörtgeni seçin.

![](rectangle.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına bir dikdörtgen eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[public Shape addShape(int tipi, int üstSolSatır, int üst, int üstSolSütun, int sol, int yükseklik, int genişlik)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına dikdörtgenin nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](rectangle2.png)



## **Çalışma Sayfasına Küp Ekleme**

Küpün şekli şuna aittir:**Basit şekiller** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Küpü eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
-  Ardından, Küpü seçin**Basit şekiller**

![](cube.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına bir küp eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[public Shape addAutoShape(int tipi, int üstSolSatır, int üst, int üstSolSütun, int sol, int yükseklik, int genişlik)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, küpün bir çalışma sayfasına nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](cube2.png)



## **Çalışma Sayfasına belirtme çizgisi dörtlü ok ekleme**

 Belirtme çizgisi dörtlü okunun şekli şuna aittir:**Blok Okları** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Dörtlü oku belirtme çizgisi eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
-  Ardından, belirtme çizgisi dörtlü okunu seçin.**Blok Okları**

![](callout_quad_arrow.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına bir belirtme çizgisi dörtlü ok eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[public Shape addAutoShape(int tipi, int üstSolSatır, int üst, int üstSolSütun, int sol, int yükseklik, int genişlik)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, belirtme çizgisi dörtlü okunun bir çalışma sayfasına nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](callout_quad_arrow2.png)



## **Çalışma Sayfasına çarpma işareti ekleme**

 Çarpma işaretinin şekli şuna aittir:**Denklem Şekilleri** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Çarpma işaretini eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
-  Ardından, çarpma işaretini seçin**Denklem Şekilleri**

![](multiplication_sign.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına bir çarpma işareti eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[public Shape addAutoShape(int tipi, int üstSolSatır, int üst, int üstSolSütun, int sol, int yükseklik, int genişlik)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına çarpma işaretinin nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](multiplication_sign2.png)



## **Çalışma Sayfasına çoklu belge ekleme**

 Çoklu belgenin şekli şuna aittir:**Akış Şemaları** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Çoklu belgeyi eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
-  Ardından, çoklu belgeyi seçin**Akış Şemaları**

![](multidocument.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına çoklu belge eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[public Shape addAutoShape(int tipi, int üstSolSatır, int üst, int üstSolSütun, int sol, int yükseklik, int genişlik)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, çoklu belgenin bir çalışma sayfasına nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](multidocument2.png)



## **Çalışma Sayfasına Beş Köşeli Yıldız Ekleme**

 Beş köşeli yıldızın şekli,**Yıldızlar ve Afişler** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Beş köşeli yıldızı eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
-  Ardından, beş köşeli yıldızı seçin.**Yıldızlar ve Afişler**

![](star_5_points.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına Beş Köşeli yıldız eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[public Shape addAutoShape(int tipi, int üstSolSatır, int üst, int üstSolSütun, int sol, int yükseklik, int genişlik)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına Beş Köşeli yıldızın nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](star_5_points2.png)



## **Çalışma Sayfasına bir düşünce balonu bulutu ekleme**

 Düşünce baloncuğu bulutunun şekli,**açıklamalar** kategori.

***Microsoft Excel'de (örneğin 2007):***

- Düşünce balonu bulutunu eklemek istediğiniz hücreyi seçin
- Ekle menüsünü tıklayın ve Şekiller'i tıklayın.
-  Ardından, düşünce balonu bulutunu seçin.**açıklamalar**

![](thought_bubble_cloud.png)

***Aspose.Cells'i kullanma***

Çalışma sayfasına bir düşünce balonu bulutu eklemek için aşağıdaki yöntemi kullanabilirsiniz.

{{% alert color="primary" %}}

[public Shape addAutoShape(int tipi, int üstSolSatır, int üst, int üstSolSütun, int sol, int yükseklik, int genişlik)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Yöntem bir döndürür[Şekil](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) nesne.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfasına düşünce balonu bulutunun nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

Yukarıdaki kodu yürütün, aşağıdaki sonuçları alacaksınız:

![](thought_bubble_cloud2.png)
