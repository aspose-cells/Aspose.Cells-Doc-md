---
title: Çalışma Kitapları Arasında ve İçinde Çalışma Sayfalarını Kopyalayın ve Taşıyın
type: docs
weight: 80
url: /tr/net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

Bazen, ortak biçimlendirme ve veri girişi gerektiren sayısız çalışma sayfasına ihtiyacınız olabilir. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfaları olan bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunu yapmanın bir yolu vardır: bir sayfa oluşturarak ve ardından bunu üç kez kopyalayarak.

Aspose.Cells, çalışma kitapları arasında veya içinde çalışma sayfalarını kopyalama veya taşımayı destekler. Veri, biçimlendirme, tablolar, matrisler, grafikler, resimler ve diğer nesnelerin yanı sıra sayfalar en yüksek hassasiyetle kopyalanır.

{{% /alert %}}

## **Çalışma Sayfalarını Kopyalama ve Taşıma**

### **Bir Çalışma Sayfasını Bir Çalışma Kitabı İçinde Kopyalama**

Tüm örnekler için ilk adımlar aynıdır.

1. Microsoft Excel'de bazı veriler içeren iki çalış kitabı oluşturun. Bu örneğin amaçları için, Microsoft Excel'de iki yeni çalışma kitabı oluşturduk ve çalışma sayfalarına bazı veriler girdik.

- İlkÇalışmaKitabı.xlsx (3 çalışsayfası).
- İkinciÇalışmaKitabı.xlsx (1 çalışsayfası).

1. Aspose.Cells'i indirin ve kurun:
   1. [Aspose.Cells for .NET'i İndir](https://downloads.aspose.com/cells/net).
   1. Geliştirme bilgisayarınıza kurun.
      Tüm [Aspose](http://www.aspose.com/) bileşenleri yüklendiğinde değerlendirme modunda çalışır. Değerlendirme modunun bir zaman limiti yoktur ve yalnızca üretilen belgelere filigran enjekte eder.
1. Bir proje oluşturun:
   1. Visual Studio.Net'i başlatın.
   1. Yeni bir konsol uygulaması oluşturun.
1. Referanslar ekleyin:
   1. Projeye Aspose.Cells'e bir başvuru ekleyin.
      Örneğin, bir başvuru ekleyin...\Program Dosyaları\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Bir çalışma kitabı içindeki çalışsayfayı kopyalama
   İlk örnek, İlkÇalışmaKitabı.xlsx içindeki ilk çalışsayfayı (Kopya) kopyalar.

Kod çalıştırıldığında, Kopya adlı çalışsayfa, İlkÇalışmaKitabı.xlsx içinde Last Sheet adıyla kopyalanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **Bir Çalışma Kitabı içinde bir Çalışsayfayı Taşıma**

Aşağıdaki kod, bir çalışma kitabı içindeki bir çalışsayfayı bir konumdan başka bir konuma taşımanın nasıl yapıldığını gösterir. Kod çalıştırıldığında, İlkÇalışmaKitabı.xlsx içindeki İndex 1'de Move olarak adlandırılan çalışsayfa, İndex 2'ye taşınır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **Çalışma Kitapları Arasında Bir Çalışma Sayfası Kopylama**

Kod çalıştırıldığında, Kopya adlı çalışsayfa, İkinciÇalışmaKitabı.xlsx içine Sheet2 adıyla kopyalanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **Çalışma Kitapları Arasında Bir Çalışma Sayfası Taşıma**

Kod çalıştırıldığında, İlkÇalışmaKitabı.xlsx içindeki Move adlı çalışsayfa, İkinciÇalışmaKitabı.xlsx içine Sheet3 adıyla taşınır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}
{{< app/cells/assistant language="csharp" >}}
