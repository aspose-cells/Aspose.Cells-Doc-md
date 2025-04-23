---  
title: Chiffrement et déchiffrement des fichiers ODS avec C++  
linktitle: Crypter et décrypter les fichiers ODS  
type: docs  
weight: 10  
url: /fr/cpp/encrypt-and-decrypt-ods-files/  
description: Protégez par mot de passe et chiffrez les fichiers ODS en utilisant Aspose.Cells for C++, une bibliothèque pure C++.  
---  

{{% alert color="primary" %}}  
OpenOffice.org est une suite bureautique complète qui supporte le mot de passe et le chiffrement des fichiers. Cependant, un fichier ODS chiffré ne peut être ouvert par OpenOffice qu'après avoir fourni le mot de passe. Excel ne peut pas ouvrir le fichier ODS chiffré et peut afficher un message d'avertissement. Les options de chiffrement ne sont pas applicables aux fichiers ODS contrairement à d'autres types de fichiers.  
Aspose.Cells vous permet de chiffrer et déchiffrer les fichiers ODS. Les fichiers ODS déchiffrés peuvent être ouverts dans Excel et OpenOffice.  
{{% /alert %}}  

## **Chiffrer avec OpenOffice Calc**  
1. Sélectionnez **Enregistrer sous** et cliquez sur la case **Enregistrer avec mot de passe**.  
1. Cliquez sur le bouton **Enregistrer**.  
1. Saisissez votre mot de passe souhaité dans les champs **Entrer le mot de passe pour ouvrir** et **Confirmer le mot de passe** dans la fenêtre Définir le mot de passe qui s'ouvre.  
1. Cliquez sur le bouton **OK** pour enregistrer le fichier.  

## **Chiffrer un fichier ODS avec Aspose.Cells for C++**  
Pour chiffrer un fichier ODS, chargez le fichier et définissez la valeur [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) comme mot de passe réel avant de l'enregistrer. Le fichier ODS chiffré en sortie ne pourra être ouvert que dans OpenOffice.  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C++

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an ODS file
    Workbook workbook(sourceDir + u"sampleODSFile.ods");

    // Password protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the ODS file
    workbook.Save(outputDir + u"outputEncryptedODSFile.ods");

    std::cout << "ODS file password protected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  

## **Déchiffrer un fichier ODS avec Aspose.Cells for C++**  

Pour déchiffrer un fichier ODS, chargez le fichier en fournissant un mot de passe dans la propriété [**LoadOptions.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getpassword/). Une fois le fichier chargé, définissez la chaîne [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) à null.  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the source directory
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an encrypted ODS file
    LoadOptions loadOptions(LoadFormat::Ods);

    // Set original password
    loadOptions.SetPassword(u"1234");

    // Load the encrypted ODS file with the appropriate load options
    Workbook workbook(sourceDir + u"sampleEncryptedODSFile.ods", loadOptions);

    // Set the password to null
    workbook.GetSettings().SetPassword(nullptr);

    // Save the decrypted ODS file
    workbook.Save(outputDir + u"outputDecryptedODSFile.ods");

    std::cout << "Decrypted ODS file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
