---
title: Çalışma Sayfalarını Çalışma Kitapları İçinde ve Çalışma Kitapları Arasında Kopyalama ve Taşıma
type: docs
weight: 80
url: /tr/net/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

Bazen, ortak biçimlendirme ve veri girişi içeren bir dizi çalışma sayfasına ihtiyacınız olur. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalardan oluşan bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunu yapmanın bir yolu var: bir sayfa oluşturup ardından onu üç kez kopyalayarak.

Aspose.Cells, çalışma kitaplarının içinde veya arasında çalışma sayfalarının kopyalanmasını veya taşınmasını destekler. Veriler, biçimlendirme, tablolar, matrisler, çizelgeler, resimler ve diğer nesneleri içeren çalışma sayfaları en yüksek hassasiyetle kopyalanır.

{{% /alert %}}

## **Çalışma Sayfalarını Kopyalama ve Taşıma**

### **Çalışma Kitabındaki Çalışma Sayfasını Kopyalama**

İlk adımlar tüm örnekler için aynıdır.

1. Microsoft Excel'de bazı verilerle iki çalışma kitabı oluşturun. Bu örneğin amaçları doğrultusunda, Microsoft Excel'de iki yeni çalışma kitabı oluşturduk ve çalışma sayfalarına bazı veriler girdik.

- FirstWorkbook.xlsx (3 çalışma sayfası).
- SecondWorkbook.xlsx (1 çalışma sayfası).

1. Aspose.Cells'i indirin ve yükleyin:
   1. [İndir Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. Geliştirme bilgisayarınıza kurun.
 Herşey[Aspose](http://www.aspose.com/) bileşenler kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca üretilen belgelere filigran ekler.
1. Bir proje oluşturun:
 1. Visual Studio.Net'i başlatın.
 1. Yeni bir konsol uygulaması oluşturun.
1. Referans ekle:
 1. Projeye Aspose.Cells'e bir referans ekleyin.
 Örneğin, ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll dosyasına bir başvuru ekleyin.
1. Çalışma sayfasını çalışma kitabına kopyalama
 İlk örnek, FirstWorkbook.xlsx içindeki ilk çalışma sayfasını kopyalar (Kopyala).

Kod çalıştırılırken FirstWorkbook.xlsx içerisinde Copy adlı çalışma sayfası Last Sheet adıyla kopyalanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **Bir Çalışma Kitabını Çalışma Kitabı İçinde Taşıma**

Aşağıdaki kod, bir çalışma sayfasının çalışma kitabındaki bir konumdan diğerine nasıl taşınacağını gösterir. Kodun çalıştırılması, FirstWorkbook.xlsx'te Dizin 1'den dizin 2'ye Taşı adlı çalışma sayfasını taşır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **Çalışma Kitapları Arasında Çalışma Sayfası Kopyalama**

Kodun çalıştırılması, Copy is adlı çalışma sayfasını Sheet2 adıyla SecondWorkbook.xlsx dosyasına kopyalar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **Çalışma Sayfasını Çalışma Kitapları Arasında Taşıma**

Kodun çalıştırılması, Move adlı çalışma sayfasını FirstWorkbook.xlsx'ten Sheet3 adlı SecondWorkbook.xlsx'e taşır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}
