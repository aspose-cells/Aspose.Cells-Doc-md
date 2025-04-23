---
title: C++ ile Çalışma Sayfasını Korumadan Çıkarın
linktitle: Bir Çalışma Sayfasının Korumasını Kaldır
type: docs
weight: 20
url: /tr/cpp/unprotect-a-worksheet/
description: Aspose.Cells for C++ kullanarak çalışma sayfasının nasıl korunmasını kaldıracağınızı öğrenin.
---

{{% alert color="primary" %}}

Koruma kaldırmak için, korunmuş bir çalışma sayfasını çalışma zamanında korumasını kaldırmak için geliştiren bir geliştirici, bunu Aspose.Cells ile kolayca yapabilir.

{{% /alert %}}

## **Bir Çalışma Sayfasını Korumayı Kaldırma**

### **Microsoft Excel Kullanımı**

Çalışma sayfasından korumayı kaldırmak için:

 **Tools** menüsünden **Protection** seçeneğini ardından **Unprotect Sheet** seçeneğini seçin. Çalışma sayfası parola ile korunmamışsa koruma kaldırılır. Bu durumda, bir iletişim kutusu parola isteyen bir ileti gösterir. Parolayı girin ve çalışma sayfası korunmasız hale gelir.

### **Aspose.Cells Kullanarak Basit Korumalı Bir Çalışma Sayfasının Korumasız Bırakılması**

 bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) yöntemi çağrılarak korunma kaldırılabilir. Basitçe korunan bir çalışma sayfası, parola ile korunmamış olanıdır. Bu tür çalışma sayfaları, herhangi bir parametre göndermeden [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) yöntemi çağrılarak korunmasız hale getirilebilir.

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

    // Create a Workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet without a password
    worksheet.Unprotect();

    // Save the Workbook in Excel97-2003 format
    workbook.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet unprotected and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Aspose.Cells Kullanarak Şifre Korumalı Bir Çalışma Sayfasının Korumasız Bırakılması**

Parola ile korunan bir çalışma sayfası, parola ile korunmuş olan çalışma sayfasıdır. Bu tür çalışma sayfaları, parola alan aşırı yüklü [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) yöntemini çağırarak korunması kaldırılabilir.

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
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unprotecting the worksheet with a password
    worksheet.Unprotect(u"");

    // Save Workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
