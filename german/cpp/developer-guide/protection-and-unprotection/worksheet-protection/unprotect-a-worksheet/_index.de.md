---
title: Arbeitsblatt mit C++ unschutzeln
linktitle: Arbeitsblatt entsperren
type: docs
weight: 20
url: /de/cpp/unprotect-a-worksheet/
description: Erfahren Sie, wie Sie ein Arbeitsblatt mit Aspose.Cells for C++ unprotektieren.
---

{{% alert color="primary" %}}

Wenn ein Entwickler den Schutz eines geschützten Arbeitsblatts zur Laufzeit entfernen muss, damit Änderungen an der Datei vorgenommen werden können, kann dies einfach mit Aspose.Cells erfolgen.

{{% /alert %}}

## **Arbeitsblatt entsperren**

### **Verwendung von Microsoft Excel**

Um den Schutz von einem Arbeitsblatt zu entfernen:

Wählen Sie im Menü **Tools** die Option **Protection**, gefolgt von **Unprotect Sheet**. Der Schutz wird entfernt, sofern das Arbeitsblatt nicht passwortgeschützt ist. Falls doch, erscheint ein Dialog, der nach dem Passwort fragt. Geben Sie das Passwort ein, und das Arbeitsblatt wird ungeschützt.

### **Entsperren eines einfach geschützten Arbeitsblatts mit Aspose.Cells**

Ein Arbeitsblatt kann durch Aufruf der Methode [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) der Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) ungeschützt werden. Ein einfach geschütztes Arbeitsblatt ist eines, das nicht mit einem Passwort geschützt ist. Solche Arbeitsblätter können durch Aufruf der Methode [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) ohne Übergabe eines Parameters ungeschützt werden.

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

### **Entsperren eines passwortgeschützten Arbeitsblatts mit Aspose.Cells**

Ein passwortgeschütztes Arbeitsblatt ist eines, das mit einem Passwort geschützt ist. Solche Arbeitsblätter können durch Aufruf einer überladenen Version der Methode [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/), die das Passwort als Parameter nimmt, ungeschützt werden.

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
