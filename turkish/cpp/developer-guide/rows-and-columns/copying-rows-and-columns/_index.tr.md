---
title: Satır ve Sütunları Kopyalama
type: docs
weight: 20
url: /tr/cpp/copying-rows-and-columns/
---

## **Giriş**
Bazen çalışma sayfasındaki tüm çalışma sayfasını kopyalamadan satır ve sütunları kopyalamanız gerekebilir. Aspose.Cells ile, satırları ve sütunları çalışma kitabı içinde veya arasında kopyalamak mümkündür.
Bir satır (veya sütun) kopyalandığında, içerdiği veriler, güncellenmiş referanslarla formulalar ve değerler, yorumlar, biçimlendirme, gizli hücreler, görüntüler ve diğer çizim nesneleri de kopyalanır.
## **Microsoft Excel ile Satır ve Sütunları Kopyalama**
1. Kopyalamak istediğiniz satırı veya sütunu seçin.
1. Satır veya sütunları kopyalamak için **Standart** araç çubuğunda **Kopyala**'yı tıklayın veya **CTRL**+**C**'ye basın.
1. Kopyalamak istediğiniz seçimin altında veya sağındaki bir satır veya sütunu seçin.
1. Satır veya sütunları kopyalarken, **Ekle** menüsünde **Kopyalanan Hücreler**'i tıklayın.

{{% alert color="primary" %}} 

**Insert** menüsünde bir komut üzerine tıklamak yerine **Standart** araç çubuğundaki **Yapıştır**'a tıklarsanız veya **CTRL**+**V** tuşlarına basarsanız, hedef hücrelerin içeriği değiştirilir.

{{% /alert %}} 
## **Aspose.Cells Kullanımı**
### **Satırları Kopyalama**
Aspose.Cells, Aspose::Cells::ICells sınıfının CopyRow yöntemini sağlar. Bu yöntem, kaynak satırdan hedef satıra formülleri, değerleri, yorumları, hücre biçimlerini, gizli hücreleri, görüntüleri ve diğer çizim nesnelerini de içeren tüm veri türlerini kopyalar.

CopyRow yöntemi aşağıdaki parametreleri alır:

- kaynak Cells nesnesi,
- kaynak satır dizini, ve
- hedef satır dizini.

Bu yöntemi, bir çalışma sayfası içinde veya başka bir sayfaya bir satır kopyalamak için kullanabilirsiniz. CopyRow yöntemi, Microsoft Excel ile benzer şekilde çalışır. Örneğin, hedef satırın yüksekliğini ayrıca ayarlamanıza gerek yoktur, o değer de kopyalanır.

Aşağıdaki örnek, bir çalışma sayfasında bir satırı nasıl kopyalayacağınızı göstermektedir. Bir şablon Microsoft Excel dosyası kullanır ve ikinci satırı (veriler, biçimlendirme, yorumlar, görüntüler vb. ile birlikte) kopyalar ve aynı çalışma sayfasındaki 12. satıra yapıştırır.

**GetRowHeigh** yöntemi ile kaynak satırın yüksekliğini almak ve ardından **SetRowHeight** yöntemini kullanarak hedef satır yüksekliğini ayarlayan adımı atlayabilirsiniz, çünkü **CopyRow** yöntemi otomatik olarak satır yüksekliğiyle ilgilenir.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows-new.cpp" >}}

{{% alert color="primary" %}} 

Satırları kopyalarken, bu, Microsoft Excel ile aynı olan ilgili resimler, grafikler veya diğer çizim nesnelerinin dikkate alınması önemlidir:

1. Kaynak satır dizini 5 ise, resim, grafik vb. 4 ve 6 olan üç satırlarda kapsanmışsa kopyalanır (başlangıç satır dizini 4 ve bitiş satır dizini 6).
1. Hedef satırdaki mevcut resimler, grafikler vb. kaldırılmaz.

{{% /alert %}} 
### **Sütunları Kopyalama**
Aspose.Cells, Aspose::Cells::ICells sınıfının CopyColumn yöntemini sağlar, bu yöntem, kaynaktan hedefe sütun endeksine formülleri - güncellenmiş referanslarla - ve değerleri, yorumları, hücre biçimlerini, gizli hücreleri, görüntüleri ve diğer çizim nesnelerini de içeren tüm veri türlerini kopyalar.

CopyColumn yöntemi aşağıdaki parametreleri alır:

- kaynak Cells nesnesi,
- kaynak sütun indeksi ve
- hedef sütun indeksi.

Bir sayfa içindeki bir sütunu kopyalamak veya başka bir sayfaya yapıştırmak için CopyColumn yöntemini kullanın.

Bu örnek, bir çalışma sayfasından bir sütunu kopyalar ve başka bir iş kitabındaki bir çalışma sayfasına yapıştırır.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns-new.cpp" >}}
