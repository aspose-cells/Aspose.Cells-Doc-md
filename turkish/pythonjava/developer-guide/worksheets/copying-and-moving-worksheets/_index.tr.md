---
title: Çalışma Sayfalarını Kopyalama ve Taşıma
type: docs
weight: 20
url: /tr/python-java/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

Bazen, ortak biçimlendirme ve verilere sahip bir dizi çalışma sayfasına ihtiyacınız olur. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalardan oluşan bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunu yapmanın bir yolu var: bir sayfa oluşturup onu kopyalayarak.

Aspose.Cells, çalışma kitaplarının içinde veya arasında çalışma sayfalarının kopyalanmasını ve taşınmasını destekler. Veriler, biçimlendirme, tablolar, matrisler, çizelgeler, resimler ve diğer nesnelerle birlikte çalışma sayfaları en yüksek hassasiyetle kopyalanır.

{{% /alert %}} 
## **Microsoft Excel kullanarak Sayfaları Taşıma veya Kopyalama**
Aşağıda, çalışma sayfalarının çalışma kitaplarının içinde veya arasında kopyalanması ve taşınmasıyla ilgili adımlar yer almaktadır.

1. Sayfaları alacak çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1. Üzerinde**Düzenlemek**menü, tıklayın**Sayfayı Taşı veya Kopyala**.
1. Kitaba kutusunda, sayfaları almak için çalışma kitabına tıklayın.
1. Seçilen sayfaları yeni bir çalışma kitabına taşımak veya kopyalamak için**yeni kitap**.
1. İçinde**sayfadan önce**kutusunda, taşınan veya kopyalanan sayfaları eklemek istediğiniz sayfayı tıklayın.
1. Sayfaları taşımak yerine kopyalamak için**Bir kopya oluştur**onay kutusu.
### **Çalışma Kitabındaki Çalışma Sayfalarını Kopyalama**
Aspose.Cells aşırı yükleme sağlar[WorksheetCollection.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\)) varolan bir çalışma sayfasını kopyalamak için kullanılan yöntem. Yöntemin bir sürümü, kaynak çalışma sayfasının dizinini parametre olarak alır. Diğer sürüm, kaynak çalışma sayfasının adını alır.

Aşağıdaki örnek, bir çalışma kitabı içinde varolan bir çalışma sayfasının nasıl kopyalanacağını gösterir.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **Çalışma Sayfalarını Çalışma Kitapları Arasında Kopyalama**
Aspose.Cells şunları sağlar:[Çalışma sayfası.kopya()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\)) çalışma sayfalarını diğer çalışma kitaplarına kopyalamak için kullanılan yöntem. Yöntem, kaynak çalışma sayfası nesnesini parametre olarak alır.

Aşağıdaki örnek, çalışma sayfasının bir çalışma kitabından başka bir çalışma kitabına nasıl kopyalanacağını gösterir.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **Çalışma Sayfalarını Çalışma Kitabı İçinde Taşıma**
Aspose.Cells şunları sağlar:[Worksheet.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\)) bir çalışma sayfasını aynı elektronik tabloda başka bir konuma taşımak için kullanılan yöntem.

Aşağıdaki örnek, bir çalışma sayfasının çalışma kitabı içinde başka bir konuma nasıl taşınacağını gösterir.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
