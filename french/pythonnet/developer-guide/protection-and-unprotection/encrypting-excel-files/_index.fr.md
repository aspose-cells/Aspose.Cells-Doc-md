---
title: Chiffrement des fichiers Excel
type: docs
weight: 90
url: /fr/python-net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) vous permet de chiffrer et de protéger par mot de passe vos feuilles de calcul. Il utilise des algorithmes fournis par un fournisseur de services cryptographiques (CSP), un ensemble d'algorithmes cryptographiques avec différentes propriétés. Le CSP par défaut est 'Compatible avec Office 97/2000' ou 'Chiffrement faible (XOR)'. Il est important de choisir la bonne longueur de clé de chiffrement. Certains CSP ne prennent pas en charge plus de 40 ou 56 bits. Cela est considéré comme un chiffrement faible. Pour un chiffrement fort, une longueur de clé minimale de 128 bits est requise. Microsoft Windows contient également des CSP qui offrent des types de chiffrement forts, par exemple le 'Fournisseur cryptographique fort Microsoft'. Pour vous donner une idée, un chiffrement de 128 bits est ce que les banques utilisent pour chiffrer la connexion avec leurs systèmes de banque en ligne.

Aspose.Cells pour Python via .NET permet de chiffrer et de protéger par mot de passe les fichiers Microsoft Excel avec le type de chiffrement souhaité.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Pour définir les paramètres de chiffrement de fichier dans Microsoft Excel (ici Microsoft Excel 2003) :

1. Dans le menu **Outils**, sélectionnez **Options**. Une boîte de dialogue apparaîtra.
1. Sélectionnez l'onglet **Sécurité**.
1. Saisissez un mot de passe et cliquez sur **Avancé**
1. Choisissez le type de chiffrement et confirmez le mot de passe.

## **Chiffrement avec Aspose.Cells**

L'exemple suivant montre comment chiffrer et protéger par mot de passe un fichier Excel en utilisant l'API Aspose.Cells pour Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **Option de spécification du mot de passe pour modifier**

L'exemple suivant montre comment définir l'option **Mot de passe pour modifier** Microsoft Excel pour un fichier existant en utilisant l'API Aspose.Cells pour Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}

## **Vérifiez le mot de passe du fichier chiffré**

Pour vérifier le mot de passe du fichier chiffré, Aspose.Cells pour Python via .NET fournit la méthode [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password). Ces méthodes acceptent deux paramètres, le flux de fichier et le mot de passe à vérifier.
Le code d'exemple suivant démontre l'utilisation de la méthode [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) pour vérifier si le mot de passe fourni est valide ou non.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}

## **Chiffrement / déchiffrement de fichier ODS**

Aspose.Cells pour Python via .NET permet de chiffrer et de déchiffrer les fichiers ODS. Le fichier ODS déchiffré peut être ouvert à la fois dans Excel et OpenOffice, cependant le fichier ODS chiffré ne peut être ouvert que dans OpenOffice après avoir fourni le mot de passe. Excel ne peut pas ouvrir le fichier ODS chiffré et peut afficher un message d'avertissement. Les options de chiffrement ne s'appliquent pas aux fichiers ODS contrairement à d'autres types de fichiers. Pour chiffrer un fichier ODS, chargez le fichier et définissez la valeur [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) avec le mot de passe réel avant de l'enregistrer. Le fichier ODS chiffré résultant peut être ouvert uniquement dans OpenOffice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

Pour déchiffrer un fichier ODS, chargez le fichier en fournissant un mot de passe dans le [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). Une fois le fichier chargé, définissez la chaîne [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) comme nulle.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
