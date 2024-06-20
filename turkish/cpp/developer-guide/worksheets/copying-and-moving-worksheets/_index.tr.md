---
title: Çalışsayfa Kopyalama ve Taşıma
type: docs
weight: 10
url: /tr/cpp/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

Bazen ortak biçimlendirme ve veriye sahip bir dizi çalışma sayfasına ihtiyaç duyarsınız. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalara sahip bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunun bir yolu var: bir sayfa oluşturduktan sonra onu kopyalayarak.

Aspose.Cells, çalışma kitapları içinde veya arasında çalışma sayfalarını kopyalama ve taşımayı destekler. Bir çalışma sayfası, veri, biçimlendirme, tablolar, matrisler, grafikler, resimler ve diğer nesnelerle birlikte en yüksek hassasiyetle kopyalanır.

{{% /alert %}} 
## **Microsoft Excel Kullanarak Sayfaları Taşıma veya Kopyalama**
Microsoft Excel'de çalışma kitapları içinde veya arasında çalışma sayfalarını kopyalama ve taşımanın dahil olduğu adımlar aşağıda verilmiştir.

1. Sayfaları başka bir çalışma kitabına taşımak veya kopyalamak için, sayfaları alacak olan çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1. **Düzenle** menüsünde, **Sayfayı Taşı veya Kopyala**'yı tıklayın.
1. **Kitapçığa** iletişim kutusunda, sayfaların alınacağı çalışma kitabını tıklayın.
1. Seçili sayfaları yeni bir kitapçığa taşımak veya kopyalamak için **Yeni Kitap**'a tıklayın.
1. **Önceki sayfa** kutusunda, taşınan veya kopyalanan sayfaların nereden önce ekleneceğini tıklayın.
1. Sayfaları taşımak yerine kopyalamak için **Kopyasını Oluştur** onay kutusunu seçin.
### **Aspose.Cells ile Bir Çalışma Kitabı İçinde Çalışma Sayfalarını Kopyalama**
Aspose.Cells, koleksiyona bir çalışma sayfası eklemek ve mevcut bir çalışma sayfasından veri kopyalamak için kullanılan [AddCopy()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/addcopy/) adlı aşırı yüklenmiş bir yöntem sağlar. Yöntemin bir versiyonu kaynak çalışma sayfasının endeksini parametre olarak alır. Diğer versiyon ise kaynak çalışma sayfasının adını alır. Aşağıdaki örnek, bir çalışma kitabı içinde mevcut bir çalışma sayfasını kopyalamanın nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook-new.cpp" >}}
### **Çalışma Kitabı İçinde Sayfaları Taşıma**
Aspose.Cells, aynı elektronik tablo içinde bir çalışma sayfasını başka bir konuma taşımak için kullanılan [MoveTo()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/moveto/) adlı bir yöntem sağlar. Yöntem hedef çalışma sayfası indeksini parametre olarak alır. Aşağıdaki örnek, bir çalışma sayfasını çalışma kitabı içinde başka bir konuma taşımanın nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook-new.cpp" >}}
