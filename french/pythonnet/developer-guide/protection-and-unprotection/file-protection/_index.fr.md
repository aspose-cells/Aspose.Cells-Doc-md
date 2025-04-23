---
title: Chiffrer et déchiffrer les fichiers Excel
type: docs
weight: 10
url: /fr/python-net/encrypt-and-decrypt-excel-files/
description: Comment chiffrer et déchiffrer des fichiers Excel en utilisant Python. Verrouiller et déverrouiller des fichiers Excel.
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

## **Chiffrer un fichier Excel avec Aspose.Cells**

L'exemple suivant montre comment chiffrer et protéger par mot de passe un fichier Excel en utilisant l'API Aspose.Cells pour Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **Option de spécification du mot de passe pour modifier**

L'exemple suivant montre comment définir l'option **Mot de passe pour modifier** Microsoft Excel pour un fichier existant en utilisant l'API Aspose.Cells pour Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}


## **Déchiffrer le fichier Excel avec Aspose.Cells**
Il est très facile d'ouvrir un fichier Excel protégé par mot de passe et de le déchiffrer en utilisant l'API Aspose.Cells pour Python via .NET avec les codes suivants :

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-Decrypt-Excel-File.py" >}}


## **Sujets avancés**
- [Chiffrer et déchiffrer des fichiers ODS](/cells/fr/python-net/encrypt-and-decrypt-ods-files/)
- [Définition du type de chiffrement fort](/cells/fr/python-net/setting-strong-encryption-type/)
- [Spécifier l'auteur lors de la protection en écriture du classeur](/cells/fr/python-net/specify-author-while-write-protecting-workbook/)
- [Vérifier le mot de passe des fichiers chiffrés](/cells/fr/python-net/verify-password-of-encrypted-excel-and-ods-files/)

