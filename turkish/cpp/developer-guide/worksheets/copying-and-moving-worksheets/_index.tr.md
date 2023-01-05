---
title: Çalışma Sayfalarını Kopyalama ve Taşıma
type: docs
weight: 10
url: /tr/cpp/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

Bazen, ortak biçimlendirme ve verilere sahip bir dizi çalışma sayfasına ihtiyacınız olur. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalardan oluşan bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunu yapmanın bir yolu var: bir sayfa oluşturup onu kopyalayarak.

Aspose.Cells, çalışma kitaplarının içinde veya arasında çalışma sayfalarının kopyalanmasını ve taşınmasını destekler. Veriler, biçimlendirme, tablolar, matrisler, çizelgeler, resimler ve diğer nesnelerle eksiksiz bir çalışma sayfası en yüksek hassasiyetle kopyalanır.

{{% /alert %}} 
## **Microsoft Excel kullanarak Sayfaları Taşıma veya Kopyalama**
Aşağıda, Microsoft Excel'de çalışma sayfalarının çalışma kitaplarının içinde veya arasında kopyalanması ve taşınmasıyla ilgili adımlar yer almaktadır.

1. Sayfaları başka bir çalışma kitabına taşımak veya kopyalamak için, sayfaları alacak olan çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1.  Üzerinde**Düzenlemek** menü, tıklayın**Sayfayı Taşı veya Kopyala**.
1.  İçinde**Kitaba** iletişim kutusunda, sayfaları almak için çalışma kitabına tıklayın.
1.  Seçilen sayfaları yeni bir çalışma kitabına taşımak veya kopyalamak için**Yeni kitap**.
1.  İçinde**sayfadan önce** kutusunda, taşınan veya kopyalanan sayfaları eklemek istediğiniz sayfayı tıklayın.
1.  Sayfaları taşımak yerine kopyalamak için**Bir kopya oluştur** onay kutusu.
### **Aspose.Cells ile Çalışma Kitabındaki Çalışma Sayfalarını Kopyalayın**
 Aspose.Cells, aşırı yüklenmiş bir yöntem sağlar[Kopya Ekle()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa1e73c54ea19bb7aa0f9f197c2baa5ba)koleksiyona bir çalışma sayfası eklemek ve mevcut bir çalışma sayfasından veri kopyalamak için kullanılır. Yöntemin bir sürümü, kaynak çalışma sayfasının dizinini parametre olarak alır. Diğer sürüm, kaynak çalışma sayfasının adını alır. Aşağıdaki örnek, bir çalışma kitabı içinde varolan bir çalışma sayfasının nasıl kopyalanacağını gösterir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook.cpp" >}}
### **Çalışma Sayfalarını Çalışma Kitabı İçinde Taşıma**
 Aspose.Cells bir yöntem sağlar[Taşınmak()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a240bf1d3d52ea8c8bfd54ffa320921b7)bir çalışma sayfasını aynı elektronik tabloda başka bir konuma taşımak için kullanılır. Yöntem, hedef çalışma sayfası dizinini parametre olarak alır. Aşağıdaki örnek, bir çalışma sayfasının çalışma kitabı içinde başka bir konuma nasıl taşınacağını gösterir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook.cpp" >}}
