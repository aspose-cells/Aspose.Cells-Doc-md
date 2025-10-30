---
title: C++ ile ODS Dosyalarında Hücre Doğrulamasını Alın
linktitle: ODS Dosyalarında Hücre Doğrulamasını Al
type: docs
weight: 180
url: /tr/cpp/get-cell-validation-in-ods-files/
description: Aspose.Cells for C++ API’sini kullanarak ODS dosyalarında hücre doğrulamasını nasıl alınacağını öğrenin.
keywords: Hücre Doğrulaması Al, Hücre Doğrulaması Alın 
---

## **ODS Dosyalarında Hücre Doğrulamasını Al**

Aspose.Cells for C++ ile, ODS dosyalarında bir hücreye uygulanan doğrulamayı alabilirsiniz. Bu API, [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) metodunu [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfında sağlar.

Aşağıdaki kod örneği, [source ODS dosyasını](101089354.ods) yükleyerek ve A9 hücresinin doğrulamasını okuyarak [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) metodunu nasıl kullanacağınızı gösterir.

### **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    U16String inputFilePath = srcDir + u"SampleBook1.ods";
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access cell A9
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(U16String(u"A9"));

    // Check validation existence
    Validation validation = cell.GetValidation();
    if (validation.IsNull() == false)
    {
        std::cout << "Validation type: " << static_cast<int>(validation.GetType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
