---
title: Satır ve Sütunları Kopyalama
type: docs
weight: 40
url: /tr/net/copying-rows-and-columns/
description: Bu makale, Aspose.Cells for .NET API si aracılığıyla Satırları ve Sütunları Kopyalamanın nasıl yapılacağını göstermektedir.
keywords: C# ile Satırları ve Sütunları Kopyalama, C# de Satırları Kopyalama, C# ile Sütunlar Kopyalama, Aspose.Cells for .NET Kullanan Satırlar ve Sütunlar Nasıl Kopyalanır, Birden Fazla Satır ve Sütun Yapıştırma, Tek Satır veya Sütun Nasıl Kopyalanır ve Yapıştırılır.
---

## **Giriş**

Bazen, bir çalışma sayfasında tüm çalışma sayfasını kopyalamadan satır ve sütunları kopyalamanız gerekir. Aspose.Cells ile, çalışma kitapları arasında veya içinde satır ve sütunları kopyalamak mümkündür.
Bir satır (veya sütun) kopyalandığında, içindeki veriler, güncellenmiş referanslarla formülleri - ve değerleri, yorumları, biçimlendirmeyi, gizli hücreleri, görüntüleri ve diğer çizim nesnelerini içeren veriler de kopyalanır.

## **Microsoft Excel ile Satırları ve Sütunları Nasıl Kopyalanır**

1. Kopyalamak istediğiniz satırı veya sütunu seçin.
1. Satır veya sütunları kopyalamak için **Standart** araç çubuğunda **Kopyala**'yı tıklayın veya **CTRL**+**C**'ye basın.
1. Kopyalamak istediğiniz seçimin altında veya sağındaki bir satır veya sütunu seçin.
1. Satır veya sütunları kopyalarken, **Ekle** menüsünde **Kopyalanan Hücreler**'i tıklayın.

{{% alert color="primary" %}}

Hedef hücrelerin içeriği herhangi bir içeriği Çıkar veya tıklamak yerine **Standart** araç çubuğunda **Yapıştır**'ı tıklarsanız değiştirilir.

{{% /alert %}}

## **Microsoft Excel ile Yapıştırma Seçenekleri Kullanarak Satır ve Sütunları Nasıl Yapıştırılır**

1. Kopyalamak istediğiniz veri veya diğer özelliklere sahip hücreleri seçin.
1. Ana sekmede **Kopyala**'yı tıklayın.
1. Kopyaladığınız şeyi yapıştırmak istediğiniz alanın ilk hücresine tıklayın.
1. Ana sekmede **Yapıştır**'ın yanındaki oku tıklayın ve ardından **Yapıştırma**'yı seçin.
1. İstediğiniz **seçenekleri** seçin.

## **Aspose.Cells for .NET Kullanarak Satır ve Sütunları Nasıl Kopyalanır**

## **Tek Satırları Nasıl Kopyalanır**

Aspose.Cells, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıfının [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) yöntemini sağlar. Bu yöntem, formüller, değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri de dahil olmak üzere tüm türde verileri kaynaktan hedefe kopyalar.

[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) yöntemi aşağıdaki parametreleri alır:

- kaynak [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) nesnesi
- kaynak satır dizini, ve
- hedef satır dizini.

Bu yöntemi bir sayfa içinde bir satırı, veya başka bir sayfaya kopyalamak için kullanın. [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) yöntemi, örneğin Microsoft Excel'de olduğu gibi benzer şekilde çalışır. Bu nedenle, örneğin, hedef satırın yüksekliğini açıkça ayarlamanıza gerek yok, o değer de kopyalanır.

Aşağıdaki örnek, bir çalışsayfasında bir satır kopyalamayı gösterir. Bir şablon Microsoft Excel dosyası kullanır ve ikinci satırı (veri, biçimlendirme, yorumlar, resimler vb. ile birlikte) kopyalar ve aynı çalışsayfadaki 12. satıra yapıştırır.

[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) yöntemi kullanarak kaynak satırın yüksekliğini almayı ve ardından hedef satırın yüksekliğini ayarlamayı dikkate almanız gerekmez, çünkü [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) yöntemi otomatik olarak satır yüksekliği hakkında da ilgilenir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

Satırları kopyalarken, ilgili resimler, grafikler veya diğer çizim nesnelerinin Microsoft Excel ile aynı olduğu gibi dikkate alınması önemlidir:

1. Kaynak satır dizini 5 ise, resim, grafik vb., başlangıç satır dizini 4 ve bitiş satır dizini 6 içinde bulunduruluyorsa kopyalanır.
1. Var olan resimler, grafikler vb. hedef satırdan silinmez.

{{% /alert %}}

## **Birden Fazla Satırın Nasıl Kopyalanacağı**

Ayrıca, ek bir tamsayı parametresi alarak yeni bir hedefe birden fazla satır kopyalarken [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) yöntemini de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **Sütunları Kopyalamak**

Aspose.Cells, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıfının [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) yöntemini sağlar, bu yöntem formüller, güncellenmiş referanslar içeren değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm türde verileri kaynaktan hedefe kopyalar.

[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) yöntemi aşağıdaki parametreleri alır:

- kaynak [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) nesnesi
- kaynak sütun indeksi ve
- hedef sütun indeksi.

Bir çalışma sayfası içinde bir sütunu kopyalamak veya başka bir çalışma sayfasına kopyalamak için [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) yöntemini kullanın.

Bu örnek, bir çalışma sayfasından bir sütunu kopyalar ve başka bir iş kitabındaki bir çalışma sayfasına yapıştırır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **Birden Çok Sütun Nasıl Kopyalanır**

[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) yöntemine benzer şekilde, Aspose.Cells API'leri ayrıca birden çok kaynak sütunu yeni bir konuma kopyalamak için [**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index) yöntemini sağlar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **Yapıştırma Seçenekleri ile Satır ve Sütunların Nasıl Yapıştırılacağı**

Aspose.Cells şimdi, [**PasteOptions**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) işlevler [**CopyRows**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) ve [**CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1) kullanırken uygun yapıştırma seçeneğini Excel ile benzer şekilde ayarlamayı sağlar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

