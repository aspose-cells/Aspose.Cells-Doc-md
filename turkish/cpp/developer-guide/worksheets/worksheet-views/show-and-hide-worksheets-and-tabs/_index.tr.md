---
title: Çalışma Sayfaları ve Sekmeleri Göster ve Gizle ile C++
linktitle: Sayfaları ve Tabları Gösterme ve Gizleme
type: docs
weight: 10
url: /tr/cpp/show-and-hide-worksheets-and-tabs/
description: Bu makale, C++ API veya Kütüphane kullanarak bir Excel çalışma sayfasını programlı olarak gösterip gizleme örnek kodu sağlar. Ayrıca, Excel çalışma kitabı sekmelerinin nasıl gösterilip gizleneceğini anlatır.
---

{{% alert color="primary" %}}

Aspose.Cells kullanıcının çalışma sayfalarını ve sekmelerini gösterebilmesine ve gizleyebilmesine olanak tanır.

{{% /alert %}}

## **Bir Çalışma Sayfasını Gösterme ve Gizleme**

Bir Excel dosyasında bir veya birden fazla çalışma sayfası olabilir. Excel dosyası oluşturduğumuzda, içinde çalıştığımız Excel dosyasına çalışma sayfaları ekleriz. Bir Excel dosyasındaki her çalışma sayfası kendi veri ve biçimlendirme ayarları gibi diğer çalışma sayfalarından bağımsızdır. Bazı durumlarda, geliştiriciler kendi ilgileri için Excel dosyalarındaki birkaç çalışma sayfasını gizlemek ve diğerlerini göstermek isteyebilirler. **Aspose.Cells** bu nedenle geliştiricilere Excel dosyalarında çalışma sayfalarının görünürlüğünü kontrol etme imkanı sunar.

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışma sayfalarını yönetmek için geniş özellikler ve yöntemler sunar. Bir çalışma sayfasının görünürlüğünü kontrol etmek için, [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) özelliğini [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının kullanın. [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) bir Boolean özelliğidir, bu da yalnızca **doğru** veya **yanlış** değerleri depolayabilir.

### **Bir Çalışma Sayfasını Görünür Yapma**

Bir çalışma sayfasını görünür yapmak için [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) özelliğini **true** olarak ayarlayın.

### **Bir Çalışsayıyı Gizleme**

Bir çalışma sayfasını gizlemek için [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) özelliğini **false** olarak ayarlayın.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the first worksheet of the Excel file
    worksheet.SetIsVisible(false);

    // Save the modified Excel file in default (Excel 2003) format
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Worksheet hidden and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Tabları Gösterme ve Gizleme**

Microsoft Excel dosyasının alt kısmına dikkatlice baktığınızda, bir dizi kontrolü göreceksiniz. Bunlar şunları içerir:

- Sayfa sekmeleri.
- Sekme kaydırma düğmeleri.

Sayfa sekmeleri, Excel dosyasındaki çalışma sayfalarını temsil eder. Herhangi bir sekmeye tıklayarak o çalışma sayfasına geçebilirsiniz. Çalışma kitabında daha fazla çalışma sayfası olduğunda, daha fazla sayfa sekmesi olacaktır. İyi bir sayıda çalışma sayfasının olduğu Excel dosyasında bunları dolaşmak için düğmeler kullanmanız gerekebilir. Bu nedenle, Microsoft Excel, sayfa sekmeleri ve sekmeler arasında kaydırmak için düğmeler sağlar.

Aspose.Cells kullanarak geliştiriciler Excel dosyalarında sayfa sekmelerinin ve sekmelerin kaydırma düğmelerinin görünürlüğünü kontrol edebilirler.

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, bir Excel dosyasını yönetmek için geniş bir özellik ve yöntem yelpazesi sunar. Bir Excel dosyasındaki sekmelerin görünürlüğünü kontrol etmek için geliştiriciler [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfının [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) özelliğini kullanabilirler. [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) Boolean bir özelliktir, bu da sadece **true** veya **false** değeri depolayabileceği anlamına gelir.

### **Sekmeleri Görünür Yapma**

Sekmeleri görünür yapmak için [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfının [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) özelliğini **true** yapın.

### **Sekmeleri Gizleme**

Bir Excel dosyasında sekmeleri gizlemek için [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfının [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) özelliğini **false** yapın.

Aşağıda, bir Excel dosyasını (book1.xls) açan, sekmelerini gizleyen ve değiştirilmiş dosyayı output.xls olarak kaydeden tam bir örnek bulunmaktadır. Kodun çalıştırılmasından sonra çalışma kitabının sekmelerinin gizlendiğini göreceksiniz.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Hiding the tabs of the Excel file
    settings.SetShowTabs(false);

    // Shows the tabs of the Excel file
    // settings.SetShowTabs(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Sekme Çubuğu Genişliğini Kontrol Etme**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Show tabs in the Excel file
    settings.SetShowTabs(true);

    // Adjust the sheet tab bar width
    settings.SetSheetTabBarWidth(800);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
