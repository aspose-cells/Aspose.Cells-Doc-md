---
title: Çalışsayfa Kopyalama ve Taşıma
type: docs
weight: 20
url: /tr/python-java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

Bazen ortak biçimlendirme ve veriye sahip bir dizi çalışma sayfasına ihtiyaç duyarsınız. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalara sahip bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunun bir yolu var: bir sayfa oluşturduktan sonra onu kopyalayarak.

Aspose.Cells, çalışsayfaları arasında veya aralında kopyalama ve taşımayı destekler. Veriler, biçimlendirme, tablolar, matrisler, grafikler, resimler ve diğer nesnelerle birlikte çalışsayfalar, en yüksek derecede doğrulukla kopyalanır.

{{% /alert %}} 
## **Microsoft Excel Kullanarak Sayfaları Taşıma veya Kopyalama**
Çalışbooklar arası veya içinde çalışsayfaları taşıma ve kopyalama içeren adımlar şunları içerir.

1. Levhanın alacağı sayımaları içeren çalışbook'u açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1. **Düzen** menüsünde, **Sayfa Taşı veya Kopyala**'yı tıklayın.
1. Alınacak kitap kutusunda, sayfaları alacak olan çalışma kitabını tıklayın.
1. Seçili sayfaları yeni bir çalışma kitabına taşımak veya kopyalamak için **yeni kitap**'a tıklayın.
1. **Önceki sayfa** kutusunda, taşınan veya kopyalanan sayfaların ekleneceği sayfaya tıklayın.
1. Sayfaları taşımak yerine kopyalamak için **Kopya oluştur** onay kutusunu işaretleyin.
### **Çalışma Kitabı İçinde Çalışma Sayfalarını Kopyalama**
Aspose.Cells, mevcut bir sayfayı kopyalamak için kullanılan [WorksheetCollection.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\)) metodu için aşırı yüklenmiş bir versiyon sağlar. Yöntemin bir versiyonu kaynak sayfa dizinini parametre olarak alır. Diğer versiyon ise kaynak sayfa adını alır.

Aşağıdaki örnek, bir çalışma kitabı içinde mevcut bir çalışma sayfasının nasıl kopyalanacağını gösterir.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **Çalışma Kitapları Arasında Çalışma Sayfalarını Kopyalama**
Aspose.Cells, sayfaları başka çalışma kitaplarına kopyalamak için kullanılan [Worksheet.copy()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\)) metodu sağlar. Bu metod kaynak sayfa nesnesini parametre olarak alır.

Aşağıdaki örnek, bir çalışma kitabından diğer bir çalışma kitabına sayfa kopyalamanın nasıl yapılacağını gösterir.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **Çalışma Kitabı İçinde Sayfaları Taşıma**
Aspose.Cells, aynı elektronik tabloda başka bir konuma bir sayfayı taşımak için kullanılan [Worksheet.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\)) metodu sağlar.

Aşağıdaki örnek, bir çalışma kitabı içinde bir çalışma sayfasının başka bir konuma nasıl taşınacağını gösterir.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
