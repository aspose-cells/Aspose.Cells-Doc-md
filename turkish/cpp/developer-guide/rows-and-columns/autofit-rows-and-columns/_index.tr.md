---
title: C++ ile Satır ve Sütunları Otomatik Boyutlandırma
linktitle: Satırların ve Sütunların Otomatik Sığdırması
type: docs
weight: 20
url: /tr/cpp/autofit-rows-and-columns/
description: Bu makale, Aspose.Cells for C++ API sini kullanarak satırları, sütunları, birleştirilmiş hücrelerin satırlarını ve hücre aralıklarındaki satırları otomatik boyutlandırma yöntemlerini gösterir.
keywords: Satırları otomatik sığdır, sütunları otomatik sığdır, hücre aralığında satırı otomatik sığdır, birleştirilmiş hücrelerin satırlarını otomatik sığdır
---

{{% alert color="primary" %}}

Microsoft Excel, kullanıcıların hücrelerin genişliği ve yüksekliğini içeriğe göre otomatik ayarlamasına izin verir. Bu özellik ayrıca Aspose.Cells aracılığıyla da sunulmaktadır, böylece geliştiriciler çalışma zamanında hücrenin boyutlarını otomatik ayarlayabilir.

{{% /alert %}}

## **Otomatik Uydurma**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişimi sağlayan [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, bir çalışma sayfasını yönetmek için geniş bir metod yelpazesi sunar. Bu makale, satır veya sütunları otomatik sığdırmak için [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfını kullanmayı inceler.

### **Satırı Otomatik Uydurma - Basit**

Bir satırın genişliği ve yüksekliğini otomatik boyutlandırmanın en basit yolu, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) metodunu çağırmaktır. [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) yöntemi, yeniden boyutlandırılacak satırın satır indeksini parametre olarak alır.

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

    // Auto-fit the 2nd row (index 1) of the worksheet
    worksheet.AutoFitRow(1);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Hücre Aralığında Satır Otomatik Sığdırma**

Bir satır, birçok sütundan oluşur. Aspose.Cells, satırdaki hücre aralığındaki içeriğe göre satırı otomatik sığdırmak için [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) metodunun aşırı yüklenmiş bir versiyonunu çağırmaya izin verir. Aşağıdaki parametreleri alır:

- **Satır dizini**, otomatik olarak uyarlama yapılacak satırın dizini.
- **İlk sütun dizini**, satırın ilk sütununun dizini.
- **Son sütun dizini**, satırın son sütununun dizini.

[**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) metodu, satırdaki tüm sütunların içeriğini kontrol eder ve ardından satırı otomatik sığdırır.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fitting the 3rd row of the worksheet
    worksheet.AutoFitRow(1, 0, 5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Hücre Aralığında Sütun Otomatik Sığdırma**

Bir sütun birçok satırdan oluşur. Bir sütunun içeriğine göre genişliğini otomatik ayarlamak için aşırı yüklü [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) metodunu kullanabilirsiniz ve aşağıdaki parametreleri alır:

- **Sütun dizini**, otomatik olarak sığdırılacak sütunun dizini.
- **İlk satır indeksi**, sütunun ilk satırının indeksi.
- **Son satır indeksi**, sütunun son satırının indeksi.

[**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) metodu, sütundaki tüm satırların içeriğini kontrol eder ve sonra sütunu otomatik sığdırır.

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

    // Auto-fit the 5th column (index 4) from row 4 to 6
    worksheet.AutoFitColumn(4, 4, 6);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Birleştirilmiş Hücreler İçin Satırları Otomatik Uydurma**

Aspose.Cells ile, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) API'sini kullanarak birleştirilmiş hücrelerde bile satırların otomatik olarak sığdırılması mümkündür. [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) sınıfı, birleştirilmiş hücreler için satırları otomatik sığdırmak üzere kullanılabilecek [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) özelliğini sağlar. [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) kabul eder ve aşağıdaki üyeleri içerir:

- Hiçbiri: Birleştirilmiş hücreleri yoksay.
- FirstLine: Sadece ilk satırın yüksekliğini artırır.
- LastLine: Sadece son satırın yüksekliğini artırır.
- EachLine: Her satırın yüksekliğini artırır.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook wb;

    // Get the first (default) worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Create a range A1:B1
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 2);

    // Merge the cells
    range.Merge();

    // Insert value to the merged cell A1
    worksheet.GetCells().Get(0, 0).SetValue(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

    // Create a style object
    Style style = worksheet.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style.SetIsTextWrapped(true);

    // Apply the style to the cell
    worksheet.GetCells().Get(0, 0).SetStyle(style);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options;

    // Set auto-fit for merged cells
    options.SetAutoFitMergedCellsType(AutoFitMergedCellsType::EachLine);

    // Autofit rows in the sheet (including the merged cells)
    worksheet.AutoFitRows(options);

    // Save the Excel file
    wb.Save(outDir + u"AutofitRowsforMergedCells.xlsx");

    std::cout << "Autofit rows for merged cells completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Ayrıca, [**AutoFitRows**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrows/) ve [**AutoFitColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumns/) metodlarının aşırı yüklenmiş sürümlerini kullanmayı deneyebilir ve belirli satır/sütun aralığını ve [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) örneğini alarak, istediğiniz [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) ile seçilen satırları/sütunları otomatik sığdırabilirsiniz.

Yukarıdaki metodların imzaları aşağıdaki gibidir:

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) seçenekleri)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) seçenekleri)

{{% /alert %}}

## **Bilinmesi Gerekenler**

{{% alert color="primary" %}}

Bir hücre birleştirilmişse, ardından AutoFit yöntemleri uygulanmayacaktır ki bu da Microsoft Excel ile aynı davranıştır. Bunu aşmak için otomatik filtre API'sini kullanabilirsiniz. Ayrıca, hücredeki metin sarılmışsa, [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) yöntemi de uygulanmayacaktır. Ayrıca, AutoFit yöntemlerinin zaman alıcı olduğunu bilmeniz gerekir. Bu yüzden, uygulamanızın verimliliğini sağlamak için bu yöntemleri olabildiğince az çağırmalısınız.

{{% /alert %}}

## **Gelişmiş Konular**
- [Birleştirilmiş Hücreler için Satırları Otomatik Uydurma](/cells/tr/cpp/autofit-rows-for-merged-cells/)
