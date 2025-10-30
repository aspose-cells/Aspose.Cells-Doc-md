---  
title: Belirtilen Çalışma Sayfalarını PDF ye Kaydet  C++ ile  
linktitle: Belirtilen Çalışma Sayfalarını PDF Olarak Kaydet  
type: docs  
weight: 140  
url: /tr/cpp/save-specified-worksheets-to-pdf/  
description: Aspose.Cells kullanarak belirli çalışma sayfalarını PDF ye aktarın.  
---  

 Varsayılan olarak, Aspose.Cells çalışma kitabındaki tüm **görünen** çalışma sayfalarını PDF dosyasına kaydeder. [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) seçeneği ile, belirli çalışma sayfalarını PDF'ye kaydedebilirsiniz. Örneğin, aktif çalışma sayfasını PDF'ye kaydedebilir, tüm çalışma sayfalarını (görünür ve gizli çalışma sayfaları) PDF'ye kaydedebilir veya özel çoklu çalışma sayfalarını PDF'ye kaydedebilirsiniz.

## **Etkin Çalışma Sayfasını PDF Olarak Kaydet**

 Sadece aktif sayfayı PDF'ye aktarmak istiyorsanız, bunu [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) seçeneğine [**SheetSet.GetActive()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getactive/) geçirerek başarabilirsiniz.

 Kaynak dosyanın aktif sayfası [sheetset-example.xlsx](sheetset-example.xlsx) dosyasındaki `Sheet2` sayfasıdır.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Set active sheet to output
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(SheetSet::GetActive());

    // Save the pdf file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## ** Tüm Çalışma Sayfalarını PDF'ye Kaydet**

[**SheetSet.GetVisible()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getvisible/) bir çalışma kitabındaki görünür sayfaları belirtir, [**SheetSet.GetAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getall/) ise tüm sayfaları (görünür ve gizli sayfalar dahil) belirtir. Tüm sayfaları PDF'ye aktarmak istiyorsanız, yalnızca [**SheetSet.GetAll**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getall/) seçeneğine [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) geçirmeniz yeterlidir.

Kaynak dosya [sheetset-example.xlsx](sheetset-example.xlsx) gizli Sheet3 sayfası dahil olmak üzere dört sayfayı içerir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
#include "Aspose.Cells/SheetSet.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template Excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Set all sheets to output
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(SheetSet::GetAll());

    // Save the PDF file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Belirtilen Çalışsayfalarını PDF olarak kaydet**

 İstenen / özelleştirilmiş çoklu sayfayı PDF'ye aktarmak istiyorsanız, bunu [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) seçeneğine birden çok sayfa dizisi geçirerek başarabilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
#include "Aspose.Cells/SheetSet.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template Excel file
    U16String inputFilePath(u"sheetset-example.xlsx");
    Workbook workbook(inputFilePath);

    // Set custom multiple sheets (Sheet1, Sheet3) to output
    Vector<int32_t> sheetIndexes = {0, 2};
    SheetSet sheetSet(sheetIndexes);

    // Initialize PDF save options
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(sheetSet);

    // Save the PDF file with PdfSaveOptions
    U16String outputFilePath(u"output.pdf");
    workbook.Save(outputFilePath, pdfSaveOptions);

    std::cout << "Excel file saved as PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## ** Çalışma Sayfalarını PDF'ye Yeniden Sırala**

 Dönüşüm sırasında kaynak dosyayı değiştirmeden sayfaları (ör. ters sırayla) PDF'ye yeniden sıralamak istiyorsanız, sıralanmış sayfa dizisini [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) seçeneğine geçirerek bunu başarabilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Reorder sheets (Sheet1, Sheet2, Sheet3, Sheet4) to (Sheet4, Sheet3, Sheet2, Sheet1)
    Vector<int32_t> sheetIndexes = { 3, 2, 1, 0 };
    SheetSet sheetSet(sheetIndexes);

    // Create PdfSaveOptions and assign the sheet set
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(sheetSet);

    // Save the pdf file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
