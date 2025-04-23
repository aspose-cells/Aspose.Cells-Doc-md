---
title: Vérifier si la signature numérique du code VBA est valide avec C++
linktitle: Vérifiez si la signature numérique du code VBA est valide
type: docs
weight: 120
url: /fr/cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Apprenez comment vérifier la validité d une signature numérique dans le code VBA en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet de vérifier si la signature numérique du code VBA est valide en utilisant la propriété [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isvalidsigned/). Elle renverra **true** si la signature est valide ; sinon, elle renverra **false**. La signature numérique du code VBA devient invalide lorsque vous modifiez le code VBA.

{{% /alert %}}

## **Vérifier si la signature numérique du code VBA est valide en C++**

Le code suivant démontre l'utilisation de cette propriété avec le [fichier Excel d'exemple](5115030.xlsm) que vous pouvez télécharger via le lien fourni. Le même fichier Excel a une signature valide, mais lorsque nous modifions son code VBA et sauvegardons le classeur, puis le revérifions, sa signature est devenue invalide.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the workbook from an existing Excel file with VBA project
    Workbook workbook(srcDir + u"sampleVBAProjectSigned.xlsm");

    // Check if the VBA Code Project is valid signed
    std::cout << "Is VBA Code Project Valid Signed: " << (workbook.GetVbaProject().IsValidSigned() ? "True" : "False") << std::endl;

    // Modify the VBA Code
    U16String code = workbook.GetVbaProject().GetModules().Get(1).GetCodes();
    code = u"Welcome to Aspose.Cells"; // Directly setting new code here
    workbook.GetVbaProject().GetModules().Get(1).SetCodes(code);

    // Save the workbook
    workbook.Save(srcDir + u"output_out.xlsm");

    // Reload the workbook
    workbook = Workbook(srcDir + u"output_out.xlsm");

    // Now the signature is invalid
    std::cout << "Is VBA Code Project Valid Signed: " << (workbook.GetVbaProject().IsValidSigned() ? "True" : "False") << std::endl;

    Aspose::Cells::Cleanup();
}
```
