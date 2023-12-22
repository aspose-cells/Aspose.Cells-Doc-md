---
title: Satırları ve Sütunları Kopyalama
type: docs
weight: 40
url: /tr/net/copying-rows-and-columns/
description: Bu makalede, Aspose.Cells for .NET API aracılığıyla Satırların ve Sütunların nasıl kopyalanacağı gösterilmektedir.
keywords: C# How to Copy Rows and Columns, Copy Rows in C#, Copy Columns using C#, How to Paste Rows and Columns using Aspose.Cells for .NET, Paste multiple rows and columns, How to Copy and paste Single Row or Column.
---
##  **giriiş**

Bazen çalışma sayfasının tamamını kopyalamadan, çalışma sayfasındaki satırları ve sütunları kopyalamanız gerekir. Aspose.Cells ile çalışma kitaplarının içinde veya arasında satır ve sütun kopyalamak mümkündür.
Bir satır (veya sütun) kopyalandığında, güncelleştirilmiş referanslarla birlikte formüller ve değerler, yorumlar, biçimlendirme, gizli hücreler, resimler ve diğer çizim nesneleri de dahil olmak üzere satır (veya sütun) içindeki veriler de kopyalanır.

##  **Microsoft Excel ile Satır ve Sütunlar Nasıl Kopyalanır?**

1. Kopyalamak istediğiniz satırı veya sütunu seçin.
1.  Satırları veya sütunları kopyalamak için**Kopyala** üzerinde**Standart** araç çubuğuna basın veya**CTRL**+*C**.
1. Seçiminizi kopyalamak istediğiniz yerin altından veya sağından bir satır veya sütun seçin.
1.  Satırları veya sütunları kopyalarken**Kopyalandı Cells** üzerinde**Sokmak** Menü.

{{% alert color="primary" %}}

 Eğer tıklarsan**Yapıştırmak** üzerinde**Standart** araç çubuğuna veya tuşuna basın**CTRL**+****Ekle'deki bir komuta tıklamak yerine V****Menüde, hedef hücrelerin tüm içerikleri değiştirilir.

{{% /alert %}}

##  **Microsoft Excel ile Yapıştırma Seçeneklerini Kullanarak Satırları ve Sütunları Yapıştırma**

1. Kopyalamak istediğiniz verileri veya diğer nitelikleri içeren hücreleri seçin.
1. Giriş sekmesinde *Kopyala**'yı tıklayın.
1.  İstediğiniz alandaki ilk hücreye tıklayın**yapıştırmak** ne kopyaladın
1.  Giriş sekmesinde, yanındaki oka tıklayın.**Yapıştır**'ı ve ardından **Yapıştır'ı seçin** Özel.
1.  Şunu seçin:**seçenekler** İstediğiniz.

##  **Aspose.Cells for .NET Kullanılarak Satır ve Sütunlar Nasıl Kopyalanır?**

##  **Tek Satır Nasıl Kopyalanır**

 Aspose.Cells şunları sağlar[**Kopyalama Satırı**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)sınıf. Bu yöntem, formüller, değerler, yorumlar, hücre formatları, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere her türlü veriyi kaynak satırdan hedef satıra kopyalar.

[**Kopyalama Satırı**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)yöntem aşağıdaki parametreleri alır:

-  kaynak[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)nesne,
- kaynak satır dizini ve
- hedef satır dizini.

 Bir sayfanın içindeki bir satırı veya başka bir sayfaya kopyalamak için bu yöntemi kullanın.[**Kopyalama Satırı**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)yöntem Microsoft Excel'e benzer şekilde çalışır. Yani örneğin hedef satırın yüksekliğini açıkça ayarlamanıza gerek yok, o değer de kopyalanır.

Aşağıdaki örnek, çalışma sayfasındaki bir satırın nasıl kopyalanacağını gösterir. Bir şablon Microsoft Excel dosyası kullanır ve ikinci satırı (veriler, biçimlendirme, yorumlar, resimler vb. ile birlikte) kopyalar ve aynı çalışma sayfasının 12. satırına yapıştırır.

 kullanarak kaynak satır yüksekliğini elde eden adımı atlayabilirsiniz.[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) yöntemini kullanın ve ardından hedef satır yüksekliğini kullanarak[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) olarak yöntem[**Kopyalama Satırı**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)yöntemi otomatik olarak satır yüksekliğini dikkate alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

Satırları kopyalarken ilgili görselleri, grafikleri veya diğer çizim nesnelerini not etmek önemlidir çünkü bu, Microsoft Excel'de de aynıdır:

1. Kaynak satır dizini 5 ise resim, grafik vb. üç satırda yer alıyorsa kopyalanır (başlangıç satır dizini 4 ve bitiş satır dizini 6'dır).
1. Hedef satırdaki mevcut görseller, grafikler vb. kaldırılmayacaktır.

{{% /alert %}}

##  **Birden Çok Satır Nasıl Kopyalanır**

Ayrıca birden fazla satırı yeni bir hedefe kopyalayabilirsiniz.[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)kopyalanacak kaynak satırların sayısını belirtmek için tamsayı türünde ek bir parametre alan yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


##  **Sütunlar Nasıl Kopyalanır?**

 Aspose.Cells şunları sağlar[**Sütunu Kopyala**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)sınıfında, bu yöntem, güncellenmiş referanslarla birlikte formüller ve değerler, yorumlar, hücre formatları, gizli hücreler, görüntüler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kaynak sütundan hedef sütuna kopyalar.

[**Sütunu Kopyala**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)yöntem aşağıdaki parametreleri alır:

-  kaynak[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)nesne,
- kaynak sütun dizini ve
- hedef sütun dizini.

 Kullan[**Sütunu Kopyala**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)Bir sayfanın içindeki bir sütunu veya başka bir sayfaya kopyalama yöntemi.

Bu örnek, bir çalışma sayfasından bir sütunu kopyalayıp başka bir çalışma kitabındaki bir çalışma sayfasına yapıştırır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

##  **Birden Çok Sütun Nasıl Kopyalanır**

 Benzer[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) yöntemi, Aspose.Cells API'leri ayrıca şunları da sağlar:[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)Birden fazla kaynak sütununu yeni bir konuma kopyalamak için yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


##  **Yapıştırma Seçenekleri ile Satır ve Sütunlar Nasıl Yapıştırılır**

 Aspose.Cells şimdi sağlıyor[**YapıştırSeçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) fonksiyonları kullanırken[**Satırları Kopyala**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) Ve[**Sütunları Kopyala**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Excel'e benzer uygun yapıştırma seçeneğinin ayarlanmasına olanak tanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

