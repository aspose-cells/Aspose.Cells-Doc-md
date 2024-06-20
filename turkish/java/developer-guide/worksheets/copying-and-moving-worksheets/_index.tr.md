---
title: Çalışsayfa Kopyalama ve Taşıma
type: docs
weight: 20
url: /tr/java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}}

Bazen ortak biçimlendirme ve veriye sahip bir dizi çalışma sayfasına ihtiyaç duyarsınız. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalara sahip bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunun bir yolu var: bir sayfa oluşturduktan sonra onu kopyalayarak.

Aspose.Cells, çalışma kitapları içinde veya arasında çalışma sayfalarını kopyalama ve taşıma desteği sağlar. Veri, biçimlendirme, tablolar, matrisler, grafikler, görüntüler ve diğer nesnelerle birlikte, en yüksek hassasiyetle kopyalanan çalışma sayfaları.

{{% /alert %}}

## **Microsoft Excel Kullanarak Sayfaları Taşıma veya Kopyalama**

Çalışma kitapları içinde veya arasında çalışma sayfalarını kopyalama ve taşıma adımları aşağıdaki gibidir.

1. Sayfaları başka bir çalışma kitabına taşımak veya kopyalamak için, sayfaları alacak olan çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1. **Düzenle** menüsünde, **Sayfayı Taşı veya Kopyala**'yı tıklayın.
1. Alınacak kitap kutusunda, sayfaları alacak olan çalışma kitabını tıklayın.
1. Seçili sayfaları yeni bir çalışma kitabına taşımak veya kopyalamak için, **yeni kitap**'ı tıklayın.
1. **Önceki sayfa** kutusunda, taşınan veya kopyalanan sayfaların nereden önce ekleneceğini tıklayın.
1. Sayfaları taşımak yerine kopyalamak için **Kopyasını Oluştur** onay kutusunu seçin.

## **Çalışma Kitabı İçinde Çalışma Sayfalarını Kopyalama**

Aspose.Cells, mevcut bir çalışma sayfasından veri kopyalamak için kullanılan ve çalışma sayfasının bir kopyasını eklemek için kullanılan [**WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy(int)) adlı aşırı yüklü bir yöntem sağlar. Yöntemin bir sürümü, kaynak çalışma sayfasının endeksini parametre olarak alır. Diğer sürüm, kaynak çalışma sayfasının adını alır.

Aşağıdaki örnek, bir çalışma kitabı içinde mevcut bir çalışma sayfasının nasıl kopyalanacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **Çalışma Kitapları Arasında Çalışma Sayfalarını Kopyalama**

Aspose.Cells, bir çalışma kitabı içinde veya arasında bir kaynak çalışma sayfasından veri ve biçimlendirmeyi kopyalamak için kullanılan [**Worksheet.copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)) adlı bir yöntem sağlar. Bu yöntem, kaynak çalışma sayfası nesnesini parametre olarak alır.

Aşağıdaki örnek, bir çalışma kitabından diğer bir çalışma kitabına sayfa kopyalamanın nasıl yapılacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

Aşağıdaki örnek, bir çalışma kitabından başka bir çalışma kitabına bir çalışma sayfasını kopyalamayı göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **Çalışma Kitabı İçinde Sayfaları Taşıma**

Aspose.Cells, bir çalışma kitabı içinde bir çalışma sayfasını başka bir konuma taşımak için kullanılan [**Worksheet.moveTo()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo(int)) adlı bir yöntem sağlar.

Aşağıdaki örnek, bir çalışma kitabı içinde bir çalışma sayfasının başka bir konuma nasıl taşınacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
