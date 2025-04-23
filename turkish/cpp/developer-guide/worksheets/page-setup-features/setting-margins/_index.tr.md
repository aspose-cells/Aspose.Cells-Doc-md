---
title: Kenar Boşluklarını C++ ile Ayarlama
linktitle: Kenar Boşlukları Ayarlama
type: docs
weight: 20
url: /tr/cpp/setting-margins/
description: Excel çalışma sayfasının kenar boşluklarını C++ kullanarak nasıl ayarlayacağınızı öğrenin. Bu kılavuz, sayfa kenar boşluklarını ayarlama, içeriği ortalama ve başlık ve alt bilgi kenar boşluklarını programlama yoluyla yapılandırmayı kapsar Aspose.Cells for C++ ile.
keywords: Excel çalışma sayfası kenar boşluklarını merkeze ayarla c++, çalışma sayfası başlığı ve altbilgi kenar boşluklarını ayarla c++
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel'in sayfa düzeni seçeneklerini tamamen destekler. Geliştiriciler, baskı işlemini kontrol etmek için çalışma sayfaları için sayfa düzeni ayarlarını yapılandırabilirler. Bu konu, Aspose.Cells'ı kullanarak sayfa kenar boşluklarını yapılandırmanın nasıl yapıldığını tartışmaktadır.

{{% /alert %}}

## **Kenar Boşlukları Ayarlama**

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı ile temsil edilir.

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, bir çalışma sayfası için sayfa düzeni seçeneklerini ayarlamak amacıyla kullanılan [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) özelliği sağlar. [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) niteliği, geliştiricilerin yazdırılan çalışma sayfası için farklı sayfa düzeni seçenekleri belirlemesine olanak tanıyan [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) sınıfının bir nesnesidir. [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) sınıfı, sayfa düzeni ayarlarını yapmak için kullanılan çeşitli özellikler ve metodlar sağlar.

### **Sayfa Kenar Boşlukları**

Sayfa kenar boşluklarını (sol, sağ, üst, alt) [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) sınıf üyelerini kullanarak belirleyin. İşte sayfa kenar boşluklarını belirtmek için kullanılan birkaç metod:

- [**GetLeftMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getleftmargin/)
- [**GetRightMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getrightmargin/)
- [**GetTopMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/gettopmargin/)
- [**GetBottomMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getbottommargin/)

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set bottom, left, right, and top page margins
    pageSetup.SetBottomMargin(2);
    pageSetup.SetLeftMargin(1);
    pageSetup.SetRightMargin(1);
    pageSetup.SetTopMargin(3);

    // Save the Workbook
    workbook.Save(outDir + u"SetMargins_out.xls");

    std::cout << "Margins set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Sayfa Üzerinde Ortala**

Bir şeyi yatay ve dikey olarak sayfada ortalayabilirsiniz. Bunun için [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) sınıfının, [**GetCenterHorizontally()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcenterhorizontally/) ve [**GetCenterVertically()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcentervertically/) üyeleri bazı kullanışlıdır.

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Center on page Horizontally and Vertically
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered page setup!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Üst Bilgi ve Alt Bilgi Kenar Boşlukları**

Başlık ve altbilgi kenar boşluklarını [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) sınıf üyeleri olan [**GetHeaderMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheadermargin/) ve [**GetFooterMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfootermargin/) kullanarak ayarla.

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Header / Footer margins
    pageSetup.SetHeaderMargin(2);
    pageSetup.SetFooterMargin(2);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered header and footer margins!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
