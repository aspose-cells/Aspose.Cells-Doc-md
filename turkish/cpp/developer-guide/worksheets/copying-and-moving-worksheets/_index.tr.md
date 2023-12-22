---
title: Çalışma Sayfalarını Kopyalama ve Taşıma
type: docs
weight: 10
url: /tr/cpp/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

Bazen ortak biçimlendirme ve verilere sahip çok sayıda çalışma sayfasına ihtiyaç duyarsınız. Örneğin, üç aylık bütçelerle çalışıyorsanız aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalardan oluşan bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunu yapmanın bir yolu var: Bir sayfa oluşturup onu kopyalayarak.

Aspose.Cells, çalışma kitaplarının içinde veya çalışma kitapları arasında çalışma sayfalarının kopyalanmasını ve taşınmasını destekler. Veriler, biçimlendirme, tablolar, matrisler, grafikler, görüntüler ve diğer nesnelerle dolu bir çalışma sayfası en yüksek hassasiyetle kopyalanır.

{{% /alert %}} 
##  **Microsoft Excel'i kullanarak Sayfaları Taşıma veya Kopyalama**
Aşağıda, Microsoft Excel'deki çalışma kitaplarının içinde veya çalışma kitapları arasında çalışma sayfalarının kopyalanması ve taşınmasıyla ilgili adımlar yer almaktadır.

1. Sayfaları başka bir çalışma kitabına taşımak veya kopyalamak için sayfaları alacak çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1.  Üzerinde**Düzenlemek** menüsünde *Sayfayı Taşı veya Kopyala**'yı tıklayın.
1. İçinde**Kitaba** iletişim kutusunda, sayfaları almak için çalışma kitabını tıklayın.
1. Seçilen sayfaları yeni bir çalışma kitabına taşımak veya kopyalamak için *Yeni Kitap**'ı tıklayın.
1. İçinde**Sayfadan önce** kutusunda, taşınan veya kopyalanan sayfaları önüne eklemek istediğiniz sayfayı tıklayın.
1.  Sayfaları taşımak yerine kopyalamak için**Bir kopya oluştur** onay kutusu.
###  **Aspose.Cells ile Çalışma Kitabındaki Çalışma Sayfalarını Kopyalama**
 Aspose.Cells aşırı yüklenmiş bir yöntem sağlar[AddCopy()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/addcopy/)koleksiyona bir çalışma sayfası eklemek ve mevcut bir çalışma sayfasından verileri kopyalamak için kullanılır. Yöntemin bir sürümü, kaynak çalışma sayfasının dizinini parametre olarak alır. Diğer sürüm kaynak çalışma sayfasının adını alır. Aşağıdaki örnek, mevcut bir çalışma sayfasının çalışma kitabına nasıl kopyalanacağını gösterir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook-new.cpp" >}}
###  **Çalışma Sayfalarını Çalışma Kitabı İçinde Taşıma**
 Aspose.Cells bir yöntem sunuyor[MoveTo()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/moveto/)Bir çalışma sayfasını aynı e-tabloda başka bir konuma taşımak için kullanılır. Yöntem, hedef çalışma sayfası dizinini parametre olarak alır. Aşağıdaki örnek, bir çalışma sayfasının çalışma kitabı içindeki başka bir konuma nasıl taşınacağını gösterir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook-new.cpp" >}}
