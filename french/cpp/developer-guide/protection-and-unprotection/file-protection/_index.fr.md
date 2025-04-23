---
title: Crypter et décrypter des fichiers Excel avec C++
linktitle: Chiffrer et déchiffrer les fichiers Excel
type: docs
weight: 10
url: /fr/cpp/encrypt-and-decrypt-excel-files/
description: Comment crypter et décrypter des fichiers Excel à l aide de C++. Verrouiller et déverrouiller des fichiers Excel.
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) vous permet de chiffrer et de protéger par mot de passe vos feuilles de calcul. Il utilise des algorithmes fournis par un fournisseur de services cryptographiques (CSP), un ensemble d'algorithmes cryptographiques avec différentes propriétés. Le CSP par défaut est 'Compatible avec Office 97/2000' ou 'Chiffrement faible (XOR)'. Il est important de choisir la bonne longueur de clé de chiffrement. Certains CSP ne prennent pas en charge plus de 40 ou 56 bits. Cela est considéré comme un chiffrement faible. Pour un chiffrement fort, une longueur de clé minimale de 128 bits est requise. Microsoft Windows contient également des CSP qui offrent des types de chiffrement forts, par exemple le 'Fournisseur cryptographique fort Microsoft'. Pour vous donner une idée, un chiffrement de 128 bits est ce que les banques utilisent pour chiffrer la connexion avec leurs systèmes de banque en ligne.

Aspose.Cells vous permet de chiffrer et de protéger par mot de passe des fichiers Microsoft Excel avec le type de chiffrement de votre choix.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Pour définir les paramètres de chiffrement de fichier dans Microsoft Excel (ici Microsoft Excel 2003) :

1. Dans le menu **Outils**, sélectionnez **Options**. Une boîte de dialogue apparaîtra.
1. Sélectionnez l'onglet **Sécurité**.
1. Saisissez un mot de passe et cliquez sur **Avancé**
1. Choisissez le type de chiffrement et confirmez le mot de passe.

## **Chiffrer un fichier Excel avec Aspose.Cells**

L'exemple suivant montre comment crypter et protéger par mot de passe un fichier Excel à l'aide de l'API Aspose.Cells.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"encryptedBook1.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify XOR encryption type
    workbook.SetEncryptionOptions(EncryptionType::XOR, 40);

    // Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider)
    workbook.SetEncryptionOptions(EncryptionType::StrongCryptographicProvider, 128);

    // Password protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Workbook encrypted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Option de spécification du mot de passe pour modifier**

L'exemple suivant montre comment définir l'option **Mot de passe pour modifier** de Microsoft Excel pour un fichier existant à l'aide de l'API Aspose.Cells.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"SpecifyPasswordToModifyOption.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Set the password for modification
    workbook.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Password for modification set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Déchiffrer le fichier Excel avec Aspose.Cells**

Il est très facile d'ouvrir un fichier Excel protégé par mot de passe et de le décrypter en utilisant l'API Aspose.Cells comme indiqué dans le code suivant :

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create load options and set password
    LoadOptions loadOptions;
    loadOptions.SetPassword(u"password");

    // Open encrypted Excel file
    Workbook workbook(u"Book1.xlsx", loadOptions);

    // Remove password protection
    workbook.GetSettings().SetPassword(nullptr);

    // Save the modified workbook
    workbook.Save(u"Book1.xlsx");

    std::cout << "Password removed and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**

- [Chiffrer et déchiffrer des fichiers ODS](/cells/fr/cpp/encrypt-and-decrypt-ods-files/)
- [Définition du type de chiffrement fort](/cells/fr/cpp/setting-strong-encryption-type/)
- [Spécifier l'auteur lors de la protection en écriture du classeur](/cells/fr/cpp/specify-author-while-write-protecting-workbook/)
- [Vérifier le mot de passe des fichiers chiffrés](/cells/fr/cpp/verify-password-of-encrypted-excel-and-ods-files/)
