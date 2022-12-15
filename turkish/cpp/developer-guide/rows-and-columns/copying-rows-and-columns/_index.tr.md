---
title: Satırları ve Sütunları Kopyalama
type: docs
weight: 20
url: /tr/cpp/copying-rows-and-columns/
---
## **giriiş**
Bazen tüm çalışma sayfasını kopyalamadan çalışma sayfasındaki satırları ve sütunları kopyalamanız gerekir. Aspose.Cells ile çalışma kitaplarının içinde veya arasında satır ve sütun kopyalamak mümkündür.
Bir satır (veya sütun) kopyalandığında, güncellenmiş referanslara sahip formüller ve değerler, yorumlar, biçimlendirme, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere içerdiği veriler de kopyalanır.
## **Microsoft Excel ile Satırları ve Sütunları Kopyalama**
1. Kopyalamak istediğiniz satırı veya sütunu seçin.
1.  Satırları veya sütunları kopyalamak için tıklayın**kopyala** üzerinde**Standart** araç çubuğu veya tuşuna basın**CTRL**+**C**.
1. Seçiminizi kopyalamak istediğiniz yerin altından veya sağından bir satır veya sütun seçin.
1.  Satırları veya sütunları kopyalarken,**Cells kopyalandı** üzerinde**Sokmak** Menü.

{{% alert color="primary" %}} 

 eğer tıklarsan**Yapıştırmak** üzerinde**Standart** araç çubuğu veya basın**CTRL**+** üzerindeki bir komuta tıklamak yerine V****Ekle** menüsü, hedef hücrelerin içeriği değiştirilir.

{{% /alert %}} 
## **Aspose.Cells'i kullanma**
### **Satırları Kopyalama**
Aspose.Cells, Aspose::Cells::ICells sınıfının CopyRow yöntemini sağlar. Bu yöntem, formüller, değerler, yorumlar, hücre formatları, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kaynak satırdan hedef satıra kopyalar.

CopyRow yöntemi aşağıdaki parametreleri alır:

- kaynak Cells nesnesi,
- kaynak satır dizini ve
- hedef satır dizini.

Bir sayfadaki bir satırı veya başka bir sayfaya kopyalamak için bu yöntemi kullanın. CopyRow yöntemi, Microsoft Excel'e benzer şekilde çalışır. Yani, örneğin, hedef satırın yüksekliğini açıkça ayarlamanıza gerek yoktur, o değer de kopyalanır.

Aşağıdaki örnek, çalışma sayfasındaki bir satırın nasıl kopyalanacağını gösterir. Bir şablon Microsoft Excel dosyası kullanır ve ikinci satırı (veriler, biçimlendirme, yorumlar, resimler vb. İle birlikte) kopyalar ve aynı çalışma sayfasında 12. satıra yapıştırır.

 kullanarak kaynak satır yüksekliğini alan adımı atlayabilirsiniz.**GetRowHeigh** yöntemini kullanarak hedef satır yüksekliğini ayarlar ve ardından**Satır Yüksekliğini Ayarla** yöntem olarak**Satırı Kopyala** method otomatik olarak satır yüksekliği ile ilgilenir.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows.cpp" >}}

{{% alert color="primary" %}} 

Satırları kopyalarken, Microsoft Excel'de olduğu gibi ilgili resimleri, çizelgeleri veya diğer çizim nesnelerini not etmek önemlidir:

1. Kaynak satır dizini 5 ise resim, grafik vb. üç satırda yer alıyorsa kopyalanır (başlangıç satır dizini 4 ve bitiş satır dizini 6'dır).
1. Hedef satırdaki mevcut resimler, çizelgeler vb. kaldırılmayacaktır.

{{% /alert %}} 
### **Sütunları Kopyalama**
Aspose.Cells, Aspose::Cells::ICells sınıfının CopyColumn yöntemini sağlar; bu yöntem, formüller - güncellenmiş referanslarla - ve değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kaynaktan kopyalar sütundan hedef sütuna.

CopyColumn yöntemi aşağıdaki parametreleri alır:

- kaynak Cells nesnesi,
- kaynak sütun dizini ve
- hedef sütun dizini.

Bir sayfadaki bir sütunu veya başka bir sayfaya kopyalamak için CopyColumn yöntemini kullanın.

Bu örnek, bir çalışma sayfasındaki bir sütunu kopyalar ve başka bir çalışma kitabındaki bir çalışma sayfasına yapıştırır.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns.cpp" >}}
