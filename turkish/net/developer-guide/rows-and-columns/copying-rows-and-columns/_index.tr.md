---
title: Satırları ve Sütunları Kopyalama
type: docs
weight: 40
url: /tr/net/copying-rows-and-columns/
---
## **giriiş**

Bazen, tüm çalışma sayfasını kopyalamadan çalışma sayfasındaki satırları ve sütunları kopyalamanız gerekir. Aspose.Cells ile çalışma kitaplarının içinde veya arasında satır ve sütun kopyalamak mümkündür.
Bir satır (veya sütun) kopyalandığında, güncellenmiş referanslara sahip formüller ve değerler, yorumlar, biçimlendirme, gizli hücreler, resimler ve diğer çizim nesneleri de dahil olmak üzere içerdiği veriler de kopyalanır.

## **Microsoft Excel ile Satırları ve Sütunları Kopyalama**

1. Kopyalamak istediğiniz satırı veya sütunu seçin.
1.  Satırları veya sütunları kopyalamak için tıklayın**Kopyala** üzerinde**Standart** araç çubuğu veya tuşuna basın**CTRL**+**C**.
1. Seçiminizi kopyalamak istediğiniz yerin altından veya sağından bir satır veya sütun seçin.
1.  Satırları veya sütunları kopyalarken,**Cells kopyalandı** üzerinde**Sokmak** Menü.

{{% alert color="primary" %}}

 eğer tıklarsan**Yapıştırmak** üzerinde**Standart** araç çubuğu veya basın**CTRL**+** üzerindeki bir komuta tıklamak yerine V****Ekle** menüsünde, hedef hücrelerin içeriği değiştirilir.

{{% /alert %}}

## **Microsoft Excel ile Yapıştırma Seçeneklerini Kullanarak Satırları ve Sütunları Yapıştırma**

1. Kopyalamak istediğiniz verileri veya diğer öznitelikleri içeren hücreleri seçin.
1.  Giriş sekmesinde,**Kopyala**.
1.  İstediğiniz alandaki ilk hücreye tıklayın.**yapıştırmak** ne kopyaladın
1.  Giriş sekmesinde, yanındaki oka tıklayın.**Yapıştırmak** ve ardından seçin**Yapıştırmak** Özel.
1.  seçin**seçenekler** İstediğiniz.

## **Aspose.Cells'i kullanma**

## **Tek Satırları Kopyalama**

 Aspose.Cells şunları sağlar:[**Satırı Kopyala**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)sınıf. Bu yöntem, formüller, değerler, yorumlar, hücre formatları, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kaynak satırdan hedef satıra kopyalar.

 bu[**Satırı Kopyala**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)yöntem aşağıdaki parametreleri alır:

-  kaynak[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)nesne,
- kaynak satır dizini ve
- hedef satır dizini.

 Bir sayfadaki bir satırı veya başka bir sayfaya kopyalamak için bu yöntemi kullanın. bu[**Satırı Kopyala**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)yöntem Microsoft Excel'e benzer şekilde çalışır. Yani, örneğin, hedef satırın yüksekliğini açıkça ayarlamanıza gerek yoktur, o değer de kopyalanır.

Aşağıdaki örnek, çalışma sayfasındaki bir satırın nasıl kopyalanacağını gösterir. Bir şablon Microsoft Excel dosyası kullanır ve ikinci satırı kopyalar (veriler, biçimlendirme, yorumlar, resimler vb. İle birlikte) ve aynı çalışma sayfasındaki 12. satıra yapıştırır.

 kullanarak kaynak satır yüksekliğini alan adımı atlayabilirsiniz.[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) yöntemini kullanarak hedef satır yüksekliğini ayarlar ve ardından[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) yöntem olarak[**Satırı Kopyala**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)method otomatik olarak satır yüksekliği ile ilgilenir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

Microsoft Excel'de olduğu gibi, satırları kopyalarken ilgili resimleri, çizelgeleri veya diğer çizim nesnelerini not etmek önemlidir:

1. Kaynak satır dizini 5 ise, resim, grafik vb. üç satırda bulunuyorsa kopyalanır (başlangıç satır dizini 4 ve bitiş satır dizini 6'dır).
1. Hedef satırdaki mevcut resimler, çizelgeler vb. kaldırılmayacaktır.

{{% /alert %}}

## **Birden Çok Satırı Kopyalama**

kullanırken birden çok satırı yeni bir hedefe de kopyalayabilirsiniz.[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)kopyalanacak kaynak satır sayısını belirtmek için tamsayı türünde ek bir parametre alan yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **Sütunları Kopyalama**

 Aspose.Cells şunları sağlar:[**Sütunu Kopyala**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Bu yöntem, güncellenmiş referanslarla formüller ve değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kaynak sütundan hedef sütuna kopyalar.

 bu[**Sütunu Kopyala**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)yöntem aşağıdaki parametreleri alır:

-  kaynak[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)nesne,
- kaynak sütun dizini ve
- hedef sütun dizini.

 Kullan[**Sütunu Kopyala**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)bir sayfadaki bir sütunu veya başka bir sayfaya kopyalama yöntemi.

Bu örnek, bir çalışma sayfasındaki bir sütunu kopyalar ve başka bir çalışma kitabındaki bir çalışma sayfasına yapıştırır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **Birden Çok Sütunu Kopyalama**

 Benzer[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) yöntemi, Aspose.Cells API'leri ayrıca şunları sağlar:[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)yöntemi, birden çok kaynak sütunu yeni bir konuma kopyalamak için kullanılır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **Yapıştırma Seçenekleriyle Satırları/Sütunları Yapıştırma**

 Aspose.Cells şimdi sağlıyor[**Seçenekleri Yapıştır**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) fonksiyonları kullanırken[**Satırları Kopyala**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) ve[**Sütunları Kopyala**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Excel'e benzer uygun yapıştırma seçeneğinin ayarlanmasına izin verir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

