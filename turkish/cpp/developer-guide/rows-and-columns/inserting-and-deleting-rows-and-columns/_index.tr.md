---
title: C++ ile Excel dosyasına Satır ve Sütun Ekleme ve Silme
linktitle: Satırları ve Sütunları Eklemek ve Silmek
type: docs
weight: 70
url: /tr/cpp/inserting-and-deleting-rows-and-columns/
description: Bu makale, Aspose.Cells for C++ API kullanarak satır ve sütun ekleme ve silme işlemlerini gösterir.
keywords: Aspose.Cells C++ satır ve sütunları yönetme, satır ve sütun ekleme, satır ve sütun silme
---

## **Giriş**

Sıfırdan yeni bir çalışma sayfası oluştururken veya mevcut bir çalışma sayfası üzerinde çalışırken, daha fazla veri eklemek için ekstra satırlar veya sütunlar eklememiz gerekebilir. Tersine, çalışma sayfasının belirli pozisyonlarından satırları veya sütunları silebiliriz.
Bu gereksinimleri karşılamak için, Aspose.Cells çok basit bir sınıf ve yöntemler seti sağlar, aşağıda açıklanmıştır.

### **Satırları ve Sütunları Yönetmek**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişimi sağlayan [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonunu sağlar.

[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonu, çalışma sayfasındaki satır ve sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda anlatılmaktadır.

{{% alert color="primary" %}}

Satır veya sütunlar eklendiğinde, çalışma sayfasındaki içerik aşağı veya sağa kayar; satır veya sütunlar kaldırıldığında ise içerik yukarı veya sola kayar.

{{% /alert %}}

## **Satırları ve Sütunları Eklemek**

### **Bir Satır Nasıl Eklenir**

Çalışma sayfasına herhangi bir konumda satır eklemek için, [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonunun [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) metodunu çağırın. [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) yöntemi, eklenecek satırın indeksini alır.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Instantiating a Workbook object
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRow(2);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Birkaç Satır Nasıl Eklenir**

Birden fazla satır eklemek için, [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonunun [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) metodunu çağırın. [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) yöntemi iki parametre alır:

- Satır indeksi, yeni satırların ekleneceği satırın indeksi.
- Satır sayısı, eklenmesi gereken toplam satır sayısı.

```c++
#include <iostream>
#include <fstream>
#include <memory>
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

    // Insert 10 rows into the worksheet starting from 3rd row
    worksheet.GetCells().InsertRows(2, 10);

    // Path of output excel file
    U16String outputFilePath = srcDir + u"output.out.xls";

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Biçimlendirme Seçenekleriyle Bir Satır Nasıl Eklenir**

Biçimlendirme seçenekleriyle satır eklemek için, [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/) parametresi alan [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) aşırı yüklemesini kullanın. [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) özelliğini [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/) sınıfında, [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) Enumeration kullanarak ayarlayın. [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) Enumeration'un üç üyesi aşağıda listelenmiştir.

- SameAsAbove: Yukarıdaki satır gibi biçimlendirir.
- SameAsBelow: Aşağıdaki satır gibi biçimlendirir.
- Temizle: Biçimlendirmeyi temizler.

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
    U16String outputFilePath = outDir + u"InsertingARowWithFormatting_out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting Formatting options
    InsertOptions insertOptions;
    insertOptions.SetCopyFormatType(CopyFormatType::SameAsAbove);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRows(2, 1, insertOptions);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully with formatting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Bir Sütun Nasıl Eklenir**

Geliştiriciler, herhangi bir konumda sütun eklemek için [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonunun [**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) metodunu çağırabilir. [**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) yöntemi, eklenecek sütunun indeksini alır.

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

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a column into the worksheet at 2nd position
    worksheet.GetCells().InsertColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Column inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Satırları ve Sütunları Silmek**

### **Birden Fazla Satır Nasıl Silinir**

Bir çalışma sayfasındanden çoklu satır silmek için, [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonunun [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) metodunu çağırın. [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) yöntemi iki parametre alır:

- Satır endeksi, satırların silineceği başlangıç satırının endeksi.
- satır sayısı, silinmesi gereken toplam satır sayısı

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete 10 rows from the worksheet starting from 3rd row
    worksheet.GetCells().DeleteRows(2, 10);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Rows deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Bir Sütunu Nasıl Silebilirsiniz**

Herhangi bir konumdaki sütunu silmek için, [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonunun [**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) metodunu çağırın. [**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) yöntemi, silinecek sütunun indeksini alır.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete a column from the worksheet at 5th position (index 4)
    worksheet.GetCells().DeleteColumn(4);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
