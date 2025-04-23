---
title: C++ ile Satır ve Sütunları Gizleme ve Gösterme
linktitle: Satır ve Sütunları Gizleme ve Gösterme
type: docs
weight: 60
url: /tr/cpp/hiding-and-showing-rows-and-columns/
description: Aspose.Cells kullanarak Excel dosyalarında satır ve sütunları programlı olarak gizleme ve gösterme yöntemlerini öğrenin.
---

{{% alert color="primary" %}}

Bazen, çalışma sayfasında belirli satır veya sütunları gizlemek ve sonra tekrar göstermek mantıklıdır. Microsoft Excel bu özelliği sağlar ve Aspose.Cells de sağlar.

{{% /alert %}}

## **Satır ve Sütunların Görünürlüğünü Kontrol Etme**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlamak için bir [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu, bir çalışma sayfasındaki satırları veya sütunları yönetmek için birkaç metod sağlar. Bunlardan bazıları aşağıda tartışılmıştır.

### **Satır ve Sütunları Gizleme**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun sırasıyla [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) ve [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) metodlarını çağırarak bir satır veya sütunu gizleyebilirler. Her iki metod da belirli satır veya sütunu gizlemek için satır veya sütun dizinini parametre olarak alır.

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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully. File saved to: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Bir satır veya sütunu sıfır genişliğine ayarlayarak bir satır veya sütunu gizlemek de mümkündür.

{{% /alert %}}

### **Satır ve Sütunları Gösterme**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun sırasıyla [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) ve [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) metodlarını çağırarak gizlenen herhangi bir satır veya sütunu gösterebilirler. Her iki metod da iki parametre alır:

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhide the 3rd row and set its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhide the 2nd column and set its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File modified and saved successfully!" << std::endl;

    return 0;
}
```

{{% alert color="primary" %}}

Gizli bir sütunu görünür hale getirirken, önceden atanan genişliğe veya orijinal genişliğe geri yüklemeniz gerekirse, negatif genişlik ile sütunu gizleme inverse edebilirsiniz. Örneğin: `worksheet.Cells.UnhideColumn(5, -1)`

{{% /alert %}}

### **Birden Fazla Satır ve Sütunu Gizleme**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun sırasıyla [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) ve [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) metodlarını çağırarak bir defada birden fazla satır veya sütunu gizleyebilirler. Her iki metod da gizlenmesi gereken başlangıç satırı veya sütunu dizini ve gizlenmesi gereken satır veya sütun sayısını parametre olarak alır.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet (zero-based index)
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet (zero-based index)
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Aynı şekilde birden fazla satır ve sütunu görünür hale getirmek için [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) sınıfının [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) ve [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) metodları da kullanılabilir.

{{% /alert %}}
