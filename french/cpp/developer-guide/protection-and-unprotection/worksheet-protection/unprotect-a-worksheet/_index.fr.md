---
title: Déprotuer une feuille de calcul avec C++
linktitle: Déprotéger une feuille de calcul
type: docs
weight: 20
url: /fr/cpp/unprotect-a-worksheet/
description: Apprenez comment déprotéger une feuille de calcul en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Si un développeur doit supprimer la protection d'une feuille protégée en temps réel afin de pouvoir effectuer des modifications sur le fichier, cela peut être facilement réalisé avec Aspose.Cells.

{{% /alert %}}

## **Déprotéger une feuille de calcul**

### **Utilisation de Microsoft Excel**

Pour supprimer la protection d'une feuille de calcul:

Dans le menu **Outils**, sélectionnez **Protection** puis **Déprotéger la feuille**. La protection sera levée sauf si la feuille est protégée par un mot de passe. Dans ce cas, une boîte de dialogue demande le mot de passe. Entrez le mot de passe et la feuille sera déprotégée.

### **Déprotéger une feuille de calcul simplement protégée en utilisant Aspose.Cells**

Une feuille de calcul peut être déprotégée en appelant la méthode [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) de la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Une feuille protégée simplement n'a pas de mot de passe. Ces feuilles peuvent être déprotégées en appelant la méthode [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) sans passer de paramètre.

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

### **Déprotéger une feuille de calcul protégée par mot de passe à l'aide d'Aspose.Cells**

Une feuille protégée par mot de passe est celle protégée avec un mot de passe. Ces feuilles peuvent être déprotégées en appelant une version surcharge de la méthode [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) prenant en paramètre le mot de passe.

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
{{< app/cells/assistant language="cpp" >}}
