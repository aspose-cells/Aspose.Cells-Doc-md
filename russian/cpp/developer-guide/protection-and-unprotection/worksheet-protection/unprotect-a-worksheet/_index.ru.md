---
title: Разоблачить защиту листа с помощью C++
linktitle: Снять защиту листа
type: docs
weight: 20
url: /ru/cpp/unprotect-a-worksheet/
description: Узнайте, как снять защиту с листа с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Если разработчику нужно снять защиту с защищенного листа во время выполнения, чтобы внести изменения в файл, это можно легко сделать с помощью Aspose.Cells.

{{% /alert %}}

## **Снятие защиты с листа**

### **Использование Microsoft Excel**

Для снятия защиты с листа:

Из меню **Инструменты** выберите **Защита**, затем **Снять защиту листа**. Защита будет снята, если лист не защищен паролем. В противном случае появится диалоговое окно для ввода пароля. Введите пароль, и лист будет снят с защиты.

### **Снятие защиты с просто защищенного листа с помощью Aspose.Cells**

Лист можно снять с защиты, вызвав метод [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Лист, защищенный без пароля, можно снять, вызвав метод [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) без передачи параметров.

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

### **Снятие защиты с защищенного паролем листа с помощью Aspose.Cells**

Лист, защищенный паролем, — это лист, защищенный паролем. Такие листы можно снять, вызвав переподписанный метод [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) с паролем в качестве параметра.

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
