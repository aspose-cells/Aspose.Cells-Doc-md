---
title: Documents PDF sécurisés avec C++
linktitle: Documents PDF sécurisés
type: docs
weight: 120
url: /fr/cpp/secure-pdf-documents/
description: Apprenez comment sécuriser des documents PDF avec des mots de passe propriétaire et utilisateur en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Parfois, les développeurs ont besoin de travailler avec des fichiers PDF cryptés. Par exemple :

- Sécuriser les documents avec des mots de passe propriétaire et utilisateur afin que n'importe qui ne puisse pas l'ouvrir.
- Définir des restrictions ou des autorisations sur le document après l'ouverture du document. par exemple, restreindre si le contenu du document peut être imprimé ou extrait.

Cet article explique comment passer des options de sécurité PDF lors de l'enregistrement des feuilles de calcul au format PDF.

{{% /alert %}}

Aspose.Cells fournit [**PdfSecurityOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) pour travailler avec la sécurité. Vous pouvez définir des mots de passe propriétaire et utilisateur lors de l'enregistrement en PDF. Le mot de passe propriétaire ou utilisateur sera nécessaire pour ouvrir le PDF crypté pour la visualisation.

- Le mot de passe utilisateur peut être nul ou une chaîne vide, dans ce cas aucun mot de passe ne sera requis de la part de l'utilisateur lors de l'ouverture du document PDF.
- Ouvrir le document PDF avec le bon mot de passe propriétaire donne un accès complet (sans restrictions d'accès spécifiées) au document.
- Ouvrir le document PDF avec le bon mot de passe utilisateur (ou ouvrir un document qui n'a pas de mot de passe utilisateur) permet un accès limité comme les autorisations spécifiées.

Le code d'exemple ci-dessous décrit comment sécuriser des PDF avec Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;
using namespace Aspose::Cells::Rendering::PdfSecurity;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"securepdf_test.out.pdf";

    // Open an Excel file
    Workbook workbook(inputFilePath);

    // Instantiate PDFSaveOptions to manage security attributes
    PdfSaveOptions saveOption;

    // Create and configure PDF security options
    PdfSecurityOptions securityOptions;
    securityOptions.SetUserPassword(u"user");
    securityOptions.SetOwnerPassword(u"owner");
    securityOptions.SetExtractContentPermission(false);
    securityOptions.SetPrintPermission(false);

    // Assign security options to save options
    saveOption.SetSecurityOptions(securityOptions);

    // Save the PDF document with encrypted settings
    workbook.Save(outputFilePath, saveOption);

    std::cout << "PDF saved with security settings successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Si la feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) juste avant de la rendre en PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
