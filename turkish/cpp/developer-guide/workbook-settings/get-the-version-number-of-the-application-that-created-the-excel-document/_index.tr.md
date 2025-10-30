---
title: C++ kullanarak Excel Belgesini Oluşturan Uygulamanın Sürüm Numarasını Alın
linktitle: Uygulama Sürüm Numarasını Alın
type: docs
weight: 210
url: /tr/cpp/get-the-version-number-of-the-application-that-created-the-excel-document/
description: Aspose.Cells kullanarak, bir Excel belgesini oluşturan uygulamanın sürüm numarasını nasıl alacağınızı öğrenin.
---

{{% alert color="primary" %}}

Sıklıkla, bir Microsoft Excel belgesini oluşturan uygulamanın sürüm numarasını bilmeniz gerekir. Aspose.Cells bu amaca yönelik [**Workbook.GetVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getversion/) özelliğini sağlar.

{{% /alert %}}

Aşağıdaki örnek kod, [**Workbook.GetVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getversion/) özelliğinin kullanımını gösterir. Microsoft Excel 2003, 2007, 2010 ve 2013 ile oluşturulan Excel dosyalarını yükler ve bu belgeyi oluşturan uygulamanın sürüm numarasını yazdırır.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook reference
    Workbook workbook;

    // Print the version number of Excel 2003 XLS file
    workbook = Workbook(srcDir + u"Excel2003.xls");
    std::cout << "Excel 2003 XLS Version: " << workbook.GetBuiltInDocumentProperties().GetVersion().ToUtf8() << std::endl;

    // Print the version number of Excel 2007 XLS file
    workbook = Workbook(srcDir + u"Excel2007.xls");
    std::cout << "Excel 2007 XLS Version: " << workbook.GetBuiltInDocumentProperties().GetVersion().ToUtf8() << std::endl;

    // Print the version number of Excel 2010 XLS file
    workbook = Workbook(srcDir + u"Excel2010.xls");
    std::cout << "Excel 2010 XLS Version: " << workbook.GetBuiltInDocumentProperties().GetVersion().ToUtf8() << std::endl;

    // Print the version number of Excel 2013 XLS file
    workbook = Workbook(srcDir + u"Excel2013.xls");
    std::cout << "Excel 2013 XLS Version: " << workbook.GetBuiltInDocumentProperties().GetVersion().ToUtf8() << std::endl;

    // Print the version number of Excel 2007 XLSX file
    workbook = Workbook(srcDir + u"Excel2007.xlsx");
    std::cout << "Excel 2007 XLSX Version: " << workbook.GetBuiltInDocumentProperties().GetVersion().ToUtf8() << std::endl;

    // Print the version number of Excel 2010 XLSX file
    workbook = Workbook(srcDir + u"Excel2010.xlsx");
    std::cout << "Excel 2010 XLSX Version: " << workbook.GetBuiltInDocumentProperties().GetVersion().ToUtf8() << std::endl;

    // Print the version number of Excel 2013 XLSX file
    workbook = Workbook(srcDir + u"Excel2013.xlsx");
    std::cout << "Excel 2013 XLSX Version: " << workbook.GetBuiltInDocumentProperties().GetVersion().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
