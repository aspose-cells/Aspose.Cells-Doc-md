---
title: Çalışma Kitapları Arasında ve İçinde Çalışma Sayfalarını Kopyalayın ve Taşıyın
type: docs
weight: 80
url: /tr/python-net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

Bazen, ortak biçimlendirme ve veri girişi gerektiren sayısız çalışma sayfasına ihtiyacınız olabilir. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfaları olan bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunu yapmanın bir yolu vardır: bir sayfa oluşturarak ve ardından bunu üç kez kopyalayarak.

Aspose.Cells for Python via .NET, çalışma sayfalarını veya çalışma kitapları içinde veya arasında kopyalamayı veya hareket ettirmeyi destekler. Sayfalar, veri, biçimlendirme, tablolar, matrisler, grafikler, resimler ve diğer nesneleri yüksek doğruluk oranıyla kopyalanır.

{{% /alert %}}

## **Çalışma Sayfalarını Kopyalama ve Taşıma**

### **Bir Çalışma Sayfasını Bir Çalışma Kitabı İçinde Kopyalama**

Tüm örnekler için ilk adımlar aynıdır.

1. Microsoft Excel'de bazı veriler içeren iki çalış kitabı oluşturun. Bu örneğin amaçları için, Microsoft Excel'de iki yeni çalışma kitabı oluşturduk ve çalışma sayfalarına bazı veriler girdik.

- İlkÇalışmaKitabı.xlsx (3 çalışsayfası).
- İkinciÇalışmaKitabı.xlsx (1 çalışsayfası).

1. Aspose.Cells for Python via .NET'yi indirin ve kurun:
   1. [Aspose.Cells for Python via .NET indir](https://downloads.aspose.com/cells/python-net).
   1. Geliştirme bilgisayarınıza kurun.
      Tüm [Aspose](http://www.aspose.com/) bileşenleri yüklendiğinde değerlendirme modunda çalışır. Değerlendirme modunun bir zaman limiti yoktur ve yalnızca üretilen belgelere filigran enjekte eder.
1. Bir proje oluşturun ve referanslara ekleyin:   
1. Bir çalışma kitabı içindeki çalışsayfayı kopyalama
   İlk örnek, İlkÇalışmaKitabı.xlsx içindeki ilk çalışsayfayı (Kopya) kopyalar.

Kod çalıştırıldığında, Kopya adlı çalışsayfa, İlkÇalışmaKitabı.xlsx içinde Last Sheet adıyla kopyalanır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheets.py" >}}

### **Bir Çalışma Kitabı içinde bir Çalışsayfayı Taşıma**

Aşağıdaki kod, bir çalışma kitabı içindeki bir çalışsayfayı bir konumdan başka bir konuma taşımanın nasıl yapıldığını gösterir. Kod çalıştırıldığında, İlkÇalışmaKitabı.xlsx içindeki İndex 1'de Move olarak adlandırılan çalışsayfa, İndex 2'ye taşınır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheets.py" >}}

### **Çalışma Kitapları Arasında Bir Çalışma Sayfası Kopylama**

Kod çalıştırıldığında, Kopya adlı çalışsayfa, İkinciÇalışmaKitabı.xlsx içine Sheet2 adıyla kopyalanır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.py" >}}

### **Çalışma Kitapları Arasında Bir Çalışma Sayfası Taşıma**

Kod çalıştırıldığında, İlkÇalışmaKitabı.xlsx içindeki Move adlı çalışsayfa, İkinciÇalışmaKitabı.xlsx içine Sheet3 adıyla taşınır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.py" >}}
