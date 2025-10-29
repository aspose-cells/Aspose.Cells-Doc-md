---
title: Gérer le code VBA de classeur Excel avec macro activée en C++
linktitle: Projet de macro
type: docs
weight: 200
url: /fr/cpp/manage-vba-project/
description: Ajouter un module VBA et modifier VBA ou Macro avec la bibliothèque Aspose.Cells en C++.
---

## **Ajouter un module VBA en C++**
{{% alert color="primary" %}}

Aspose.Cells vous permet d'ajouter un nouveau module VBA et du code Macro en utilisant Aspose.Cells. Veuillez utiliser la méthode [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/add/) pour ajouter le nouveau module VBA à l’intérieur du classeur.

{{% /alert %}}

Le code d'exemple suivant crée un nouveau classeur, ajoute un nouveau module VBA et du code Macro, et sauvegarde le fichier au format XLSM. Une fois que vous ouvrez le fichier XLSM dans Microsoft Excel et cliquez sur les commandes **Développeur > Visual Basic**, vous verrez un module nommé "TestModule" et à l'intérieur, vous verrez le code macro suivant.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Voici le code d'exemple pour générer le fichier XLSM de sortie avec un module VBA et un code de macro.

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

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add VBA Module
    int32_t idx = workbook.GetVbaProject().GetModules().Add(worksheet);

    // Access the VBA Module, set its name and codes
    VbaModule module = workbook.GetVbaProject().GetModules().Get(idx);
    module.SetName(u"TestModule");

    U16String codes = u"Sub ShowMessage()\r\n"
                      u"    MsgBox \"Welcome to Aspose!\"\r\n"
                      u"End Sub";
    module.SetCodes(codes);

    // Save the workbook
    U16String outputPath = outDir + u"output_out.xlsm";
    workbook.Save(outputPath, SaveFormat::Xlsm);

    std::cout << "VBA module added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Modifier VBA ou Macro en C++**

{{% alert color="primary" %}} 

Vous pouvez modifier le code VBA ou macro en utilisant Aspose.Cells. Aspose.Cells a ajouté l'espace de noms et les classes suivants pour lire et modifier le projet VBA dans le fichier Excel.

- Aspose::Cells::Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Cet article vous montrera comment modifier le code VBA ou Macro à l'intérieur du fichier Excel source en utilisant Aspose.Cells.

{{% /alert %}} 

Le code d'exemple suivant charge le fichier Excel source qui contient le code VBA ou Macro suivant :

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Après l'exécution du code d'exemple Aspose.Cells, le code VBA ou Macro sera modifié comme ceci :

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Vous pouvez télécharger le [fichier Excel source](5112508.xlsm) et le [fichier Excel de sortie](5112511.xlsm) à partir des liens donnés.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"sample.xlsm";
    U16String outputFilePath = outDir + u"output_out.xlsm";

    Workbook workbook(inputFilePath);

    VbaProject vbaProject = workbook.GetVbaProject();
    VbaModuleCollection modules = vbaProject.GetModules();

    for (int i = 0; i < modules.GetCount(); ++i)
    {
        VbaModule module = modules.Get(i);
        U16String code = module.GetCodes();
        U16String searchStr = u"This is test message.";
        U16String replaceStr = u"This is Aspose.Cells message.";

        if (code.IndexOf(searchStr) != -1)
        {
            U16String newCode;
            const char16_t* codeData = code.GetData();
            const char16_t* searchData = searchStr.GetData();
            int codeLen = code.GetLength();
            int searchLen = searchStr.GetLength();

            int pos = 0;
            int searchPos;

            while ((searchPos = code.IndexOf(searchStr)) != -1)
            {
                for (int j = pos; j < searchPos; j++)
                {
                    newCode += codeData[j];
                }

                newCode += replaceStr;

                pos = searchPos + searchLen;
            }

            for (int j = pos; j < codeLen; j++)
            {
                newCode += codeData[j];
            }

            module.SetCodes(newCode);
        }
    }

    workbook.Save(outputFilePath);

    std::cout << "VBA module codes updated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sujets avancés**
- [Ajouter une référence de bibliothèque au projet VBA dans le classeur](/cells/fr/cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Attribuer une macro à un contrôle de formulaire](/cells/fr/cpp/assign-macro-to-form-control/)
- [Vérifier si la signature numérique du code VBA est valide](/cells/fr/cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Vérifier si le code VBA est signé](/cells/fr/cpp/check-if-vba-code-is-signed/)
- [Vérifier si le projet VBA dans un classeur est signé](/cells/fr/cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Vérifier si le projet VBA est protégé et verrouillé pour la visualisation](/cells/fr/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copier le stockage de concepteur de formulaire utilisateur de macro VBA du modèle vers le classeur cible](/cells/fr/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Signer numériquement un projet de code VBA avec un certificat](/cells/fr/cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Exporter le certificat VBA vers un fichier ou un flux](/cells/fr/cpp/export-vba-certificate-to-file-or-stream/)
- [Filtrer le projet VBA lors du chargement d'un classeur](/cells/fr/cpp/filter-vba-project-while-loading-a-workbook/)
- [Découvrir si le projet VBA est protégé](/cells/fr/cpp/find-out-if-vba-project-is-protected/)
- [Protéger par mot de passe le projet VBA du classeur Excel](/cells/fr/cpp/password-protect-the-vba-project-of-excel-workbook/)
{{< app/cells/assistant language="cpp" >}}
