---
title: Sayfa Ayarları Özellikleri ile C++
linktitle: Sayfa Ayarı Özellikleri
type: docs
weight: 60
url: /tr/cpp/page-setup-features/
description: Excel dosyalarında sayfa ayarlarını yapılandırmak için Aspose.Cells ile C++ kullanma hakkında bilgi edinin.
---

## **Sayfa Ayarı Özellikleri**

Aspose.Cells, Excel dosyaları için sayfa ayar seçeneklerini yapılandırmak üzere kapsamlı özellikler sunar. Bu özellikler, kenar boşlukları, yönlendirme, kağıt boyutu ve daha fazlasını kontrol etmenizi sağlar.

### **Sayfa Kenar Boşluklarını Ayarlama**

Bir çalışma sayfasının kenar boşluklarını `PageSetup` sınıfını kullanarak ayarlayabilirsiniz. Aşağıdaki örnek, üst, alt, sol ve sağ kenar boşluklarını nasıl ayarlayacağınızı gösterir.

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageMargins() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set page margins
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetTopMargin(1.0);
    pageSetup.SetBottomMargin(1.0);
    pageSetup.SetLeftMargin(0.75);
    pageSetup.SetRightMargin(0.75);

    // Save the workbook
    workbook.Save("PageMargins.xlsx");
}
```

### **Sayfa Yönlendirmesini Ayarlama**

Sayfa yönlendirmesini portre veya manzara olarak ayarlayabilirsiniz. Aşağıdaki örnek, sayfa yönlendirmesini manzara şeklinde ayarlamayı gösterir.

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageOrientation() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    workbook.Save("PageOrientation.xlsx");
}
```

### **Kağıt Boyutunu Ayarlama**

Yazdırma için kağıt boyutunu `PageSetup` sınıfını kullanarak ayarlayabilirsiniz. Aşağıdaki örnek, kağıt boyutunu A4 olarak ayarlamayı gösterir.

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPaperSize() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    workbook.Save("PaperSize.xlsx");
}
```

### **Yazdırma Alanını Ayarlama**

Belirli bir hücre aralığını yazdırmak için `PageSetup` sınıfını kullanabilirsiniz. Aşağıdaki örnek, yazdırma alanını nasıl ayarlayacağınızı gösterir.

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintArea() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea("A1:D10");

    // Save the workbook
    workbook.Save("PrintArea.xlsx");
}
```

### **Sayfa Ağır İhlalleri Ayarlama**

Bir çalışma sayfasına sayfa sonlarını ekleyebilir, sayfaların nerede sona erdiğini ve yeni sayfaların nereden başladığını kontrol edebilirsiniz. Aşağıdaki örnek yatay sayfa sonu eklemeyi göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageBreaks() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a horizontal page break at row 10
    worksheet.GetHorizontalPageBreaks().Add("A10");

    // Save the workbook
    workbook.Save("PageBreaks.xlsx");
}
```

### **Başlık ve Altbilgi Ayarlama**

Bir çalışma sayfasının başlık ve altbilgisini `PageSetup` sınıfını kullanarak özelleştirebilirsiniz. Aşağıdaki örnek özel başlık ve altbilgi ayarlamayı göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetHeaderFooter() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set custom header and footer
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&CHeader Text");
    pageSetup.SetFooter(0, "&CFooter Text");

    // Save the workbook
    workbook.Save("HeaderFooter.xlsx");
}
```

### **Yazdırma Başlıklarını Ayarlama**

Her yazdırılan sayfada tekrar edilmesi gereken satır veya sütunları `PageSetup` sınıfını kullanarak belirtebilirsiniz. Aşağıdaki örnek yazdırma başlıklarını ayarlamayı göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintTitles() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print titles
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows("$1:$1");
    pageSetup.SetPrintTitleColumns("$A:$A");

    // Save the workbook
    workbook.Save("PrintTitles.xlsx");
}
```

### **Yazdırma Kalitesini Ayarlama**

Bir çalışma sayfasının yazdırma kalitesini `PageSetup` sınıfını kullanarak ayarlayabilirsiniz. Aşağıdaki örnek yazdırma kalitesini ayarlamayı göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintQuality() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print quality
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintQuality(600);

    // Save the workbook
    workbook.Save("PrintQuality.xlsx");
}
```

### **Yazdırma Sırasını Ayarlama**

Bir çalışma sayfasının yazdırma sırasını `PageSetup` sınıfını kullanarak ayarlayabilirsiniz. Aşağıdaki örnek sıralamayı "Önce Yukarı, sonra Aşağı" olarak ayarlamayı göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintOrder() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrder(PrintOrderType::OverThenDown);
    workbook.Save("PrintOrder.xlsx");
}
```

### **Yazdırma Kılavuz Çizgilerini Ayarlama**

Kılavuz çizgilerinin yazdırılıp yazdırılmayacağını `PageSetup` sınıfını kullanarak kontrol edebilirsiniz. Aşağıdaki örnek kılavuz çizgilerinin yazdırılmasını etkinleştirmeyi göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintGridlines() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of gridlines
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintGridlines(true);

    // Save the workbook
    workbook.Save("PrintGridlines.xlsx");
}
```

### **Başlıkları Yazdırmayı Ayarlama**

Satır ve sütun başlıklarının yazdırılıp yazdırılmayacağını `PageSetup` sınıfını kullanarak kontrol edebilirsiniz. Aşağıdaki örnek başlıkların yazdırılmasını etkinleştirmeyi göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintHeadings() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of headings
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintHeadings(true);

    // Save the workbook
    workbook.Save("PrintHeadings.xlsx");
}
```

### **Siyah-Beyaz Yazdırmayı Ayarlama**

Çalışma sayfasının siyah-beyaz olarak yazdırılıp yazdırılmayacağını `PageSetup` sınıfını kullanarak kontrol edebilirsiniz. Aşağıdaki örnek siyah-beyaz yazdırmayı etkinleştirmeyi göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintBlackAndWhite() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable black and white printing
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetBlackAndWhite(true);

    // Save the workbook
    workbook.Save("PrintBlackAndWhite.xlsx");
}
```

### **Taslak Modunda Yazdırmayı Ayarlama**

Çalışma sayfasının taslak kalitede yazdırılıp yazdırılmayacağını `PageSetup` sınıfını kullanarak kontrol edebilirsiniz. Aşağıdaki örnek taslak kalitede yazdırmayı etkinleştirmeyi göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintDraft() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintDraft(true);
    workbook.Save("PrintDraft.xlsx");
}
```

### **Yorumları Yazdırmayı Ayarlama**

Yorumların yazdırılıp yazdırılmayacağını `PageSetup` sınıfını kullanarak kontrol edebilirsiniz. Aşağıdaki örnek yorumların yazdırılmasını etkinleştirmeyi göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintComments() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);
    workbook.Save("PrintComments.xlsx");
}
```

### **Hataları Yazdırmayı Ayarlama**

Hata mesajlarının nasıl yazdırılacağını `PageSetup` sınıfını kullanarak kontrol edebilirsiniz. Aşağıdaki örnek hata yazdırma seçeneğini ayarlamayı göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintErrors() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsBlank);
    workbook.Save("PrintErrors.xlsx");
}
```

### **Yazdırma Alanını Sayfa Sayısına Uydurma**

Yazdırma alanının belirli sayfa sayısına sığacak şekilde ölçeklendirilip ölçeklenmeyeceğini `PageSetup` sınıfını kullanarak kontrol edebilirsiniz. Aşağıdaki örnek yazdırma alanını bir genişlikte ve bir yükseklikte sayfaya uydurmayı göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintAreaFitToPages() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area to fit to one page wide and one page tall
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the workbook
    workbook.Save("PrintAreaFitToPages.xlsx");
}
```

### **Yazdırma Ölçeğini Ayarlama**

Bir çalışma sayfası için yazdırma ölçek ayarını `PageSetup` sınıfını kullanarak belirleyebilirsiniz. Aşağıdaki örnek yazdırma ölçek ayarını %50 yapmayı göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintScale() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print scale to 50%
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetZoom(50);

    // Save the workbook
    workbook.Save("PrintScale.xlsx");
}
```

### **Yatay ve Dikey Yazdırma Merkezini Ayarlama**

Yazdırılan sayfada çalışma sayfasının yatay ve dikey olarak ortalanıp ortalanmayacağını `PageSetup` sınıfını kullanarak kontrol edebilirsiniz. Aşağıdaki örnek çalışma sayfasını yatay ve dikey olarak ortalamayı göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintCenterHorizontallyAndVertically() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Center the worksheet horizontally and vertically
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the workbook
    workbook.Save("PrintCenterHorizontallyAndVertically.xlsx");
}
```

### **İlk Sayfa Numarasını Ayarlama**

Yazdırma için ilk sayfa numarasını `PageSetup` sınıfını kullanarak belirleyebilirsiniz. Aşağıdaki örnek ilk sayfa numarasını ayarlamayı göstermektedir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintFirstPageNumber() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the first page number
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save("PrintFirstPageNumber.xlsx");
}
```

### **Yazdırma Sayfa Numarasını Ayarlama**

Sayfanın numarasının yazdırılmasını kontrol etmek için `PageSetup` sınıfını kullanabilirsiniz. Aşağıdaki örnek, sayfa numarasının yazdırılmasını nasıl etkinleştireceğinizi gösterir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPrintPageNumber() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&P");
    workbook.Save("PrintPageNumber.xlsx");
}
```

### **Yazdırma Sayfa Sırasını Ayarlama**

Sayfaların yazdırılma sırasını `PageSetup` sınıfını kullanarak ayarlayabilirsiniz. Aşağıdaki örnek, sayfa sırasını "İlk aşağı sonra yatay" olarak ayarlamayı gösterir:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPageOrder() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the page order to "Down, then Over"
    PageSetup
{{< app/cells/assistant language="cpp" >}}
