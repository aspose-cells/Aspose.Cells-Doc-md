---
title: Çalışma Sayfalarını Kopyalama ve Taşıma
type: docs
weight: 20
url: /tr/java/copying-and-moving-worksheets/
---
{{% alert color="primary" %}}

Bazen, ortak biçimlendirme ve verilere sahip bir dizi çalışma sayfasına ihtiyacınız olur. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalardan oluşan bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunu yapmanın bir yolu var: bir sayfa oluşturup onu kopyalayarak.

Aspose.Cells, çalışma kitaplarının içinde veya arasında çalışma sayfalarının kopyalanmasını ve taşınmasını destekler. Veriler, biçimlendirme, tablolar, matrisler, çizelgeler, resimler ve diğer nesnelerle birlikte çalışma sayfası en yüksek hassasiyetle kopyalanır.

{{% /alert %}}

## **Microsoft Excel kullanarak Sayfaları Taşıma veya Kopyalama**

Çalışma sayfalarını çalışma kitaplarının içinde veya arasında kopyalamak ve taşımak için gereken adımlar aşağıdadır.

1. Sayfaları başka bir çalışma kitabına taşımak veya kopyalamak için, sayfaları alacak olan çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1.  Üzerinde**Düzenlemek** menü, tıklayın**Sayfayı Taşı veya Kopyala**.
1. Kitaba kutusunda, sayfaları almak için çalışma kitabına tıklayın.
1.  Seçilen sayfaları yeni bir çalışma kitabına taşımak veya kopyalamak için**yeni kitap**.
1.  İçinde**sayfadan önce** kutusunda, taşınan veya kopyalanan sayfaları eklemek istediğiniz sayfayı tıklayın.
1.  Sayfaları taşımak yerine kopyalamak için**Bir kopya oluştur** onay kutusu.

## **Çalışma Kitabındaki Çalışma Sayfalarını Kopyalama**

 Aspose.Cells, aşırı yüklenmiş bir yöntem sağlar,[**WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy(int)), koleksiyona bir çalışma sayfası eklemek ve mevcut bir çalışma sayfasından verileri kopyalamak için kullanılır. Yöntemin bir sürümü, kaynak çalışma sayfasının dizinini parametre olarak alır. Diğer sürüm, kaynak çalışma sayfasının adını alır.

Aşağıdaki örnek, bir çalışma kitabı içinde varolan bir çalışma sayfasının nasıl kopyalanacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **Çalışma Sayfalarını Çalışma Kitapları Arasında Kopyalama**

 Aspose.Cells bir yöntem sağlar,[**Çalışma sayfası.kopya()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)), çalışma kitaplarının içinde veya arasında bir kaynak çalışma sayfasından başka bir çalışma sayfasına verileri ve biçimlendirmeyi kopyalamak için kullanılır. Yöntem, kaynak çalışma sayfası nesnesini parametre olarak alır.

Aşağıdaki örnek, çalışma sayfasının bir çalışma kitabından başka bir çalışma kitabına nasıl kopyalanacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

Aşağıdaki örnek, bir çalışma sayfasının bir çalışma kitabından diğerine nasıl kopyalanacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **Çalışma Sayfalarını Çalışma Kitabı İçinde Taşıma**

 Aspose.Cells bir yöntem sağlar,[**Worksheet.moveTo()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo(int)), bir çalışma sayfasını aynı elektronik tabloda başka bir konuma taşımak için kullanılır.

Aşağıdaki örnek, bir çalışma sayfasının çalışma kitabı içinde başka bir konuma nasıl taşınacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
