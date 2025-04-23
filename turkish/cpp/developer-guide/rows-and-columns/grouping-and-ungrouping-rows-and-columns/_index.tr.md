---
title: C++ ile Satır ve Sütunları Gruplama ve Gruplardan Çıkarma
linktitle: Satır ve Sütunları Gruplandırma ve Grubu Çözme
type: docs
weight: 50
url: /tr/cpp/grouping-and-ungrouping-rows-and-columns/
description: Aspose.Cells kullanarak Excel dosyalarında satır ve sütunları gruplayıp gruplardan çıkarma yöntemlerini öğrenin.
---

## **Giriş**

Bir Microsoft Excel dosyasında, veriler için bir biçim oluşturarak tek bir fare tıklamasıyla ayrıntı seviyelerini gösterip gizleyebilirsiniz.

Yalnızca özetler veya başlıkların bulunduğu satırları veya sütunları hızlı bir şekilde görüntülemek için **Özet Sembolleri**, 1,2,3, + ve - simgelerine tıklayabilirsiniz veya simgeleri kullanarak bir çalışma sayfasındaki bir bölümün altındaki ayrıntıları görebilirsiniz, aşağıdaki şekilde gösterildiği gibi:

|**Satır ve Sütun Gruplama.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Satır ve Sütun Grubu Yönetimi**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu sağlar.

[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu, çalışma sayfasındaki satırları veya sütunları yönetmek için birkaç yöntem sağlar, bunlardan bazıları aşağıda daha detaylı olarak tartışılmıştır.

### **Satır ve Sütun Gruplama**

[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun [**GroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) ve [**GroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) yöntemlerini çağırarak satırları veya sütunları gruplamak mümkündür. Her iki yöntem de aşağıdaki parametreleri alır:

- İlk satır/sütun indeksi, grup içindeki ilk satır veya sütun.
- Son satır/sütun indeksi, grup içindeki son satır veya sütun.
- Gizli mi, satırları/sütunları gruplandırmadan sonra gizlemek için bir Boolean parametre.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Group first six rows (from 0 to 5) and make them hidden
    worksheet.GetCells().GroupRows(0, 5, true);

    // Group first three columns (from 0 to 2) and make them hidden
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns grouped successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Grup Ayarları**

Microsoft Excel, görüntüleme için grup ayarlarını yapılandırmanıza izin verir:

- Detayın altında özet satırlar.
- Ayrıntının sağında özet sütunlar.

Geliştiriciler, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının [**GetOutline()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoutline/) özelliğini kullanarak bu grup ayarlarını yapılandırabilir.

### **Detaydan Aşağı Özet Satırlar**

Özet satırların detayın altında gösterilip gösterilmeyeceğini kontrol etmek de **true** veya **false** olarak [**GetSummaryRowBelow()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummaryrowbelow/) sınıfının [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/) özelliğini ayarlayarak mümkündür.

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Grouping first six rows and first three columns
    worksheet.GetCells().GroupRows(0, 5, true);
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Setting SummaryRowBelow property to false
    worksheet.GetOutline().SetSummaryRowBelow(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Detayın Sağına Özet Sütunlar**

Geliştiriciler, ayrıntının sağında özet sütunları göstermek veya gizlemek için [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/) sınıfının [**GetSummaryColumnRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummarycolumnright/) özelliğini **true** veya **false** olarak ayarlayabilirler.

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Grouping first six rows and first three columns
    worksheet.GetCells().GroupRows(0, 5, true);
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Set summary column to the right
    worksheet.GetOutline().SetSummaryColumnRight(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Satır ve Sütunların Gruplandırılmasını Kaldırma**

Gruplanmış herhangi bir satır veya sütunu ayırmak için, [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun [**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) ve [**UngroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) metodlarını çağırın. Her iki metod da iki parametre alır:

- İlk satır veya sütun dizini, ayrılmak istenen ilk satır/sütun.
- Son satır veya sütun dizini, ayrılmak istenen son satır/sütun.

[**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/), üçüncü bir Boolean parametresi alan bir aşırı yüklemesi vardır. **true** olarak ayarlayarak tüm gruplanmış bilgileri kaldırabilirsiniz. Aksi takdirde, yalnızca dış grup bilgileri kaldırılır.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Ungrouping first six rows (from 0 to 5)
    worksheet.GetCells().UngroupRows(0, 5);

    // Ungrouping first three columns (from 0 to 2)
    worksheet.GetCells().UngroupColumns(0, 2);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    return 0;
}
```
