---
title: Çalışma Sayfalarını Kopyalama ve Taşıma
type: docs
weight: 10
url: /tr/net/copying-and-moving-worksheets/
description: Bu makale örnek kod içerir ve C# API veya .NET Kitaplığı kullanılarak çalışma sayfalarının hem bir Excel çalışma kitabında hem de Excel çalışma kitaplarında programlı olarak nasıl kopyalanıp taşınacağını açıklar.
keywords: copy worksheet c#, move worksheet c#
---
{{% alert color="primary" %}}

Bazen, ortak biçimlendirme ve verilere sahip bir dizi çalışma sayfasına ihtiyacınız olur. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalardan oluşan bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunu yapmanın bir yolu var: bir sayfa oluşturup onu kopyalayarak.

Aspose.Cells, çalışma kitaplarının içinde veya arasında çalışma sayfalarının kopyalanmasını ve taşınmasını destekler. Veriler, biçimlendirme, tablolar, matrisler, çizelgeler, resimler ve diğer nesnelerle birlikte çalışma sayfası en yüksek hassasiyetle kopyalanır.

{{% /alert %}}

##  **Microsoft Excel kullanarak Sayfaları Taşıma veya Kopyalama**

Microsoft Excel'de çalışma sayfalarını çalışma kitaplarının içinde veya arasında kopyalamak ve taşımak için gereken adımlar aşağıdadır.

1. Sayfaları başka bir çalışma kitabına taşımak veya kopyalamak için, sayfaları alacak olan çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1.  Üzerinde**Düzenlemek** menüsünde *Taşı veya Sayfayı Kopyala**'yı tıklayın.
1.  İçinde**Kitaba** iletişim kutusunda, sayfaları almak için çalışma kitabına tıklayın.
1. Seçilen sayfaları yeni bir çalışma kitabına taşımak veya kopyalamak için *Yeni Kitap**'ı tıklayın.
1.  İçinde**sayfadan önce** kutusunda, taşınan veya kopyalanan sayfaları eklemek istediğiniz sayfayı tıklayın.
1.  Sayfaları taşımak yerine kopyalamak için**Bir kopya oluştur** onay kutusu.

###  **Aspose.Cells ile Çalışma Kitabındaki Çalışma Sayfalarını Kopyalayın**

 Aspose.Cells, aşırı yüklenmiş bir yöntem sağlar,[**Aspose.Cells.WorksheetCollection.AddCopy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/addcopy/index)koleksiyona bir çalışma sayfası eklemek ve mevcut bir çalışma sayfasından veri kopyalamak için kullanılır. Yöntemin bir sürümü, kaynak çalışma sayfasının dizinini parametre olarak alır. Diğer sürüm, kaynak çalışma sayfasının adını alır.

Aşağıdaki örnek, bir çalışma kitabı içinde varolan bir çalışma sayfasının nasıl kopyalanacağını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWithinWorkbook-1.cs" >}}

###  **Çalışma Sayfalarını Çalışma Kitapları Arasında Kopyalama**

 Aspose.Cells bir yöntem sağlar,[**Aspose.Cells.Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)çalışma kitapları içinde veya arasında bir kaynak çalışma sayfasından başka bir çalışma sayfasına veri ve biçimlendirmeyi kopyalamak için kullanılır. Yöntem, kaynak çalışma sayfası nesnesini parametre olarak alır.

Aşağıdaki örnek, çalışma sayfasının bir çalışma kitabından başka bir çalışma kitabına nasıl kopyalanacağını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.cs" >}}

Aşağıdaki örnek, bir çalışma sayfasının bir çalışma kitabından diğerine nasıl kopyalanacağını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.cs" >}}

###  **Çalışma Sayfalarını Çalışma Kitabı İçinde Taşıma**

 Aspose.Cells bir yöntem sağlar[**Aspose.Cells.Worksheet.MoveTo()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/moveto)bir çalışma sayfasını aynı elektronik tabloda başka bir konuma taşımak için kullanılır. Yöntem, hedef çalışma sayfası dizinini parametre olarak alır.

Aşağıdaki örnek, bir çalışma sayfasının çalışma kitabı içinde başka bir konuma nasıl taşınacağını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-MoveWorksheet-1.cs" >}}
