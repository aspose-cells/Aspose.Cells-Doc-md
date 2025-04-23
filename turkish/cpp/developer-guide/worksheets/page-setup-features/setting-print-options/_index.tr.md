---
title: Yazdırma Seçeneklerini C++ ile Ayarlama
linktitle: Baskı Seçeneklerini Ayarlama
type: docs
weight: 40
url: /tr/cpp/setting-print-options/
description: Bu makale, C++ API ve Kütüphanesi kullanarak Excel Sayfası Ayarları nın Yazdırma Seçeneklerini programlı olarak ayarlama adımlarını gösterir. Yazdırma Alanı, Yazdır Başlıkları ve Sayfa Sırası ayarlanabilir.
keywords: Excel yazdırma alanını c++, yazdırma başlıklarını c++, sayfa sırasını c++ ile ayarla
---

{{% alert color="primary" %}}

Microsoft Excel'in sayfa düzeni ayarları, kullanıcıların çalışma sayfalarının nasıl basılacağını kontrol etmelerini sağlayan birkaç baskı seçeneği (ayrıca sayfa seçenekleri olarak da adlandırılır) sunar.

{{% /alert %}}

## **Baskı Seçeneklerini Ayarlama**

Bu baskı seçenekleri, kullanıcıların şunları yapmalarını sağlar:

- Çalışma sayfasında belirli bir baskı alanı seçin.
- Başlıkları yazdırın.
- Izgaraları yazdırın.
- Satır/sütun başlıklarını yazdırın.
- Taslak kalitesine ulaşın.
- Yorumları yazdırın.
- Hücre hatalarını yazdırın.
- Sayfa sıralamasını tanımlayın.

Aspose.Cells, Microsoft Excel tarafından sunulan tüm yazdırma seçeneklerini destekler ve geliştiriciler bu seçenekleri [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) sınıfı tarafından sunulan özellikleri kullanarak kolayca yapılandırabilir. Bu özelliklerin nasıl kullanılacağı aşağıda daha detaylı olarak anlatılmıştır.

### **Baskı Alanı Belirle**

Varsayılan olarak, baskı alanı veri içeren çalışma sayfasının tüm alanlarını içerir. Geliştiriciler, çalışma sayfasının belirli bir baskı alanını belirleyebilirler.

Belirli bir baskı alanı seçmek için, [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) sınıfının [**GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) özelliğini kullanın. Bu özelliğe, baskı alanını tanımlayan bir hücre aralığı atayın.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set the print area to the range A1:T35
    pageSetup.SetPrintArea(u"A1:T35");

    // Save the workbook
    workbook.Save(outDir + u"SetPrintArea_out.xls");

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Başlıkları Yazdırma**

Aspose.Cells, basılı bir çalışma sayfasının tüm sayfalarında tekrar edecek şekilde satır ve sütun başlıklarını belirlemenize olanak tanır. Bunu yapmak için [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) sınıfının [**GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) ve [**GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) özelliklerini kullanın.

Tekrar edilecek satırlar veya sütunlar, satır veya sütun numaralarını geçirerek tanımlanır. Örneğin satırlar $1:$2 ve sütunlar $A:$B olarak tanımlanır.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of output excel file
    U16String outputFilePath = outDir + u"SetPrintTitle_out.xls";

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Define column numbers A & B as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$B");

    // Define row numbers 1 & 2 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Diğer Yazdırma Seçeneklerini Belirleme**

[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) sınıfı ayrıca aşağıdaki gibi genel yazdırma seçeneklerini ayarlamak için birkaç başka özellik sunar:

- [**GetPrintGridlines()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintgridlines/): bir Boolean özellik olup, ızgaraları yazdırıp yazdırmama durumunu belirler.
- [**GetPrintHeadings()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintheadings/): Satır ve sütun başlıklarını yazdırmak veya yazdırmamak konusunda tanımlı olan bir Boolean özelliği.
- [**GetBlackAndWhite()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getblackandwhite/): Çalışsayıyı siyah-beyaz moda yazdırmak veya yazdırmamak konusunda tanımlı olan bir Boolean özelliği.
- [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/): Çalışma sayfasındaki yazdırma yorumlarını veya çalışma sayfasının sonunda yer alan yorumları gösterip göstermemeyi tanımlar.
- [**GetPrintDraft()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintdraft/): bir boolean özellik olup, sayfayı grafik olmadan yazdırıp yazdırmama durumunu belirler.
- [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/): hücre hatalarını görüntülenen şekilde, boş, çizgi veya N/A olarak yazdırıp yazdırmayacağını tanımlar.

[**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) ve [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/) özelliklerini ayarlamak için Aspose.Cells ayrıca önceden tanımlı değerlere sahip [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) ve [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) adında iki enum sağlar; bunlar sırasıyla [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) ve [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/) özelliklerine atanır.

[**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) numaralamasındaki önceden tanımlanmış değerler aşağıda açıklamalarıyla listelenmiştir.

|**Yazdırma Yorumları Türleri**|**Açıklama**|
| :- | :- |
|PrintInPlace| Çalışma sayfasında görüntülenen yorumları yazdırmayı belirtir.
|PrintNoComments| Yorumları yazdırmamayı belirtir.
|PrintSheetEnd| Yorumları çalışma sayfasının sonunda yazdırmayı belirtir.

[**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) numaralamasındaki önceden tanımlanmış değerler aşağıda açıklamalarıyla listelenmiştir.

|**Yazdırma Hataları Türleri**|**Açıklama**|
| :- | :- |
|PrintErrorsBlank| Hataları yazdırmamayı belirtir.
|PrintErrorsDash| Hataları "--" olarak yazdırmayı belirtir.
|PrintErrorsDisplayed| Hataları görüntülendiği gibi yazdırmayı belirtir.
|PrintErrorsNA| Hataları "#N/A" olarak yazdırmayı belirtir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set print options
    pageSetup.SetPrintGridlines(true);  // Allow printing gridlines
    pageSetup.SetPrintHeadings(true);   // Allow printing row/column headings
    pageSetup.SetBlackAndWhite(true);   // Allow printing in black & white mode
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);  // Print comments as displayed
    pageSetup.SetPrintDraft(true);      // Print with draft quality
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);  // Print cell errors as N/A

    // Save the workbook
    U16String outputPath = outDir + u"OtherPrintOptions_out.xls";
    workbook.Save(outputPath);

    std::cout << "Workbook saved with print options successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Sayfa Sırasını Belirleme**

[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) sınıfı, çalışma sayfasının birden fazla sayfasını yazdırmak için kullanılan [**GetOrder()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getorder/) özelliğini sağlar. Sayfaların sıralaması aşağıdaki gibi iki olasılığı sağlar.

- **Aşağıdan önce ardından:** herhangi bir sayfayı sağa yazdırmadan önce tüm sayfaları aşağıya yazdırır.
- **Ardından aşağıdan önce:** sayfaları aşağıya yazdırmadan önce soldan sağa doğru sayfaları yazdırır.

Aspose.Cells, tüm önceden tanımlanmış sıralama tiplerini içeren [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) numaralaması sağlar.

[**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) numaralamasındaki önceden tanımlanmış değerler aşağıda listelenmiştir.

|**Yazdırma Sıralama Türleri**|**Açıklama**|
| :- | :- |
|DownThenOver|Aşağıdan önce ardından sıralama temsil eder.
|OverThenDown|Ardından aşağıdan önce sıralama temsil eder.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

    // Set the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outDir + u"SetPageOrder_out.xls");

    std::cout << "Page order set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
