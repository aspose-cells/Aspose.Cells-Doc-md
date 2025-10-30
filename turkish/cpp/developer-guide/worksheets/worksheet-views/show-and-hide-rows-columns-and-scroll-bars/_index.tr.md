---
title: C++ ile Satır, Sütun ve Kaydırma Çubuklarını Göster/Gizle
linktitle: Satır, Sütun ve Kaydırma Çubuklarını Göster ve Gizle
type: docs
weight: 20
url: /tr/cpp/show-and-hide-rows-columns-and-scroll-bars/
description: Bu makale, C++ dili ve Aspose.Cells API kullanarak Excel çalışma sayfası satırları ve sütunlarını programlama yoluyla nasıl gösterip gizleyeceğinizi gösterir. Kaydırma çubuklarının görünürlüğü ayarlanabilir, ve birkaç satır ile sütun gizlenebilir.
---

{{% alert color="primary" %}}

Aspose.Cells, bir çalışma sayfasının satır, sütun ve kaydırma çubuklarının görünürlüğünü kontrol etme yolları sunar.

{{% /alert %}}

## **Satır ve Sütunları Göster ve Gizle**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine olanak tanıyan [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunu sağlar. [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu, çalışma sayfasındaki satır veya sütunları yönetmek için birkaç yöntem sunar. Bunlardan bazıları aşağıda tartışılmıştır.

### **Satır ve Sütunları Göster**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) ve [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) metodlarını sırasıyla çağırarak herhangi bir gizli satır veya sütunu gösterebilirler. Her iki yöntem de iki parametre alır:

- **Satır veya sütun dizini** - belirli bir satır veya sütunun gösterilmesi için kullanılan dizin.
- **Satır yüksekliği veya sütun genişliği** - gizlendikten sonra atanan satır yüksekliği veya sütun genişliği.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhiding the 3rd row and setting its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhiding the 2nd column and setting its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Gizli bir sütunu görünür yapmak istiyorsanız, daha önce atanan genişliğe veya orijinal genişliğe geri yüklemek için negatif genişlik ile gizlenmiş sütunu açınız. Örneğin: `worksheet->GetCells()->UnhideColumn(5, -1)`.

{{% /alert %}}

### **Satır ve Sütunları Gizle**

Geliştiriciler, belirli bir satır veya sütunu gizlemek için sırasıyla [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) ve [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) metodlarını çağırabilirler. Her iki yöntem de gizlenmek istenen satır ve sütun indekslerini parametre olarak alır.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Bir satır veya sütunu sıfır genişliğine ayarlayarak bir satır veya sütunu gizlemek de mümkündür.

{{% /alert %}}

### **Birden Fazla Satır ve Sütunu Gizleme**

Geliştiriciler, aynı anda birden fazla satır veya sütunu gizlemek için sırasıyla [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) ve [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) metodlarını çağırabilirler. Her iki yöntem de gizlenecek başlangıç satırı veya sütunu indeksi ve satır veya sütun sayısı parametreleri olarak alır.

```c++
#include <iostream>
#include <memory>
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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Kaydırma Çubuklarını Göster ve Gizle**

Kaydırma çubukları, herhangi bir dosyanın içeriğini gezinmek için kullanılır. Genellikle iki tür kaydırma çubuğu bulunur:

- Dikey kaydırma çubukları
- Yatay kaydırma çubukları

Microsoft Excel ayrıca yatay ve dikey kaydırma çubukları sağlar böylece kullanıcılar çalışma sayfası içeriğinde kaydırma yapabilirler. Aspose.Cells kullanarak geliştiriciler Excel dosyalarında her iki türde de kaydırma çubuklarının görünürlüğünü kontrol edebilirler.

### **Kaydırma Çubuklarının Görünürlüğünü Kontrol Etmek**

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, bir Excel dosyasını yönetmek için geniş özellikler ve metodlar sağlar. Kaydırma çubuklarının görünürlüğünü kontrol etmek için, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfının [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) ve [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) özelliklerini kullanın. [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) ve [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) Boolean özellikleridir, yani yalnızca **true** veya **false** değerleri depolayabilirler.

#### **Kaydırma Çubuklarını Görünür Yapma**

Kaydırma çubuklarını görünür hale getirmek için [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfının [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) veya [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) özelliğini **true** olarak ayarlayın.

#### **Kaydırma çubuklarını gizleme**

Kaydırma çubuklarını gizlemek için [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfının [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) veya [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) özelliğini **false** olarak ayarlayın.

**Örnek Kod**

Aşağıda, bir Excel dosyasını açıp, hem kaydırma çubuklarını gizleyen hem de değiştirilmiş dosyayı `output.xls` olarak kaydeden tam bir kod bulunmaktadır.

```c++
#include <iostream>
#include <fstream>
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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Hide the vertical scroll bar of the Excel file
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Hide the horizontal scroll bar of the Excel file
    workbook.GetSettings().SetIsHScrollBarVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Scroll bars hidden successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
