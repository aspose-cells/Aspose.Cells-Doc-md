---
title: Satırları ve Sütunları Kopyalama
type: docs
weight: 20
url: /tr/cpp/copying-rows-and-columns/
---
##  **giriiş**
Bazen çalışma sayfasının tamamını kopyalamadan, çalışma sayfasındaki satırları ve sütunları kopyalamanız gerekir. Aspose.Cells ile çalışma kitaplarının içinde veya arasında satır ve sütun kopyalamak mümkündür.
Bir satır (veya sütun) kopyalandığında, güncellenmiş referanslarla birlikte formüller ve değerler, yorumlar, biçimlendirme, gizli hücreler, resimler ve diğer çizim nesneleri de dahil olmak üzere satır (veya sütun) içindeki veriler de kopyalanır.
##  **Microsoft Excel ile Satır ve Sütunların Kopyalanması**
1. Kopyalamak istediğiniz satırı veya sütunu seçin.
1.  Satırları veya sütunları kopyalamak için**Kopyala** üzerinde**Standart** araç çubuğuna basın veya**CTRL**+*C**.
1. Seçiminizi kopyalamak istediğiniz yerin altından veya sağından bir satır veya sütun seçin.
1.  Satırları veya sütunları kopyalarken**Kopyalandı Cells** üzerinde**Sokmak** Menü.

{{% alert color="primary" %}} 

 Eğer tıklarsan**Yapıştırmak** üzerinde**Standart** araç çubuğuna veya tuşuna basın**CTRL**+****Ekle'deki bir komuta tıklamak yerine V**** Menüde, hedef hücrelerin içeriği değiştirilir.

{{% /alert %}} 
##  **Aspose.Cells'i kullanma**
###  **Satırları Kopyalama**
Aspose.Cells, Aspose::Cells::ICells sınıfının CopyRow yöntemini sağlar. Bu yöntem, formüller, değerler, yorumlar, hücre formatları, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere her türlü veriyi kaynak satırdan hedef satıra kopyalar.

CopyRow yöntemi aşağıdaki parametreleri alır:

- kaynak Cells nesnesi,
- kaynak satır dizini ve
- hedef satır dizini.

Bir sayfanın içindeki bir satırı veya başka bir sayfaya kopyalamak için bu yöntemi kullanın. CopyRow yöntemi Microsoft Excel'e benzer şekilde çalışır. Yani örneğin hedef satırın yüksekliğini açıkça ayarlamanıza gerek yok, o değer de kopyalanır.

Aşağıdaki örnek, çalışma sayfasındaki bir satırın nasıl kopyalanacağını gösterir. Bir şablon Microsoft Excel dosyası kullanır ve ikinci satırı (veriler, biçimlendirme, yorumlar, resimler vb. ile birlikte) kopyalar ve aynı çalışma sayfasının 12. satırına yapıştırır.

 kullanarak kaynak satır yüksekliğini elde eden adımı atlayabilirsiniz.**GetRowHeigh** yöntemini kullanın ve ardından hedef satır yüksekliğini kullanarak**Satır Yüksekliğini Ayarla** olarak yöntem**Kopyalama Satırı** yöntemi otomatik olarak satır yüksekliğini dikkate alır.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows-new.cpp" >}}

{{% alert color="primary" %}} 

Satırları kopyalarken, ilgili görselleri, grafikleri veya diğer çizim nesnelerini not etmek önemlidir; çünkü bu, Microsoft Excel'de de aynıdır:

1. Kaynak satır dizini 5 ise, resim, grafik vb. üç satırda yer alıyorsa kopyalanır (başlangıç satır dizini 4 ve bitiş satır dizini 6'dır).
1. Hedef satırdaki mevcut görseller, grafikler vb. kaldırılmayacaktır.

{{% /alert %}} 
###  **Sütunları Kopyalama**
Aspose.Cells, Aspose::Cells::ICells sınıfının CopyColumn yöntemini sağlar; bu yöntem, güncelleştirilmiş referanslarla birlikte formüller ve değerler, yorumlar, hücre formatları, gizli hücreler, görüntüler ve diğer çizim nesneleri de dahil olmak üzere tüm veri türlerini kaynaktan kopyalar. sütununu hedef sütuna taşıyın.

CopyColumn yöntemi aşağıdaki parametreleri alır:

- kaynak Cells nesnesi,
- kaynak sütun dizini ve
- hedef sütun dizini.

Bir sayfanın içindeki bir sütunu veya başka bir sayfaya kopyalamak için CopyColumn yöntemini kullanın.

Bu örnek, bir çalışma sayfasından bir sütunu kopyalayıp başka bir çalışma kitabındaki bir çalışma sayfasına yapıştırır.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns-new.cpp" >}}
