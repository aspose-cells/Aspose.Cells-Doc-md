---
title: Crypter et décrypter des fichiers Excel
type: docs
weight: 10
url: /fr/python-java/encrypt-and-decrypt-excel-files/
description: Comment chiffrer et déchiffrer des fichiers Excel à l'aide de Python. Verrouiller et déverrouiller des fichiers Excel.
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365) vous permet de crypter et de protéger par mot de passe vos feuilles de calcul. Il utilise des algorithmes fournis par un fournisseur de services cryptographiques, ou CSP, un ensemble d'algorithmes cryptographiques aux propriétés différentes. Le CSP par défaut est 'Office 97/2000 Compatible' ou 'Weak Encryption (XOR)'. Il est important de choisir la bonne longueur de clé de chiffrement. Certains CSP ne prennent pas en charge plus de 40 ou 56 bits. C'est considéré comme un cryptage faible. Pour un cryptage fort, une longueur de clé minimale de 128 bits est requise. Microsoft Windows contient des CSP qui offrent également des types de chiffrement fort, par exemple le « Microsoft Strong Cryptographic Provider ». Pour vous donner une idée, le cryptage 128 bits est ce que les banques utilisent pour crypter la connexion avec leurs systèmes bancaires par Internet.

Aspose.Cells for Python vous permet de crypter et de protéger par mot de passe les fichiers Excel Microsoft avec le type de cryptage souhaité.

{{% /alert %}}

## **Utilisation d'Excel Microsoft**

Pour définir les paramètres de cryptage des fichiers dans Microsoft Excel (ici Microsoft Excel 2003) :

1.  Du**Outils** menu, sélectionnez**Choix**Une boîte de dialogue apparaîtra.
1.  Sélectionnez le**Sécurité** languette.
1.  Entrez un mot de passe et cliquez**Avancé**
1. Choisissez le type de cryptage et confirmez le mot de passe.

## **Chiffrement du fichier Excel avec Aspose.Cells**

L'exemple suivant montre comment chiffrer et protéger par mot de passe un fichier Excel en utilisant le Aspose.Cells API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-CSharp-Files-Utility-EncryptingFiles-1.py" >}}

## **Décryptage du fichier Excel avec Aspose.Cells**
Il est très facile d'ouvrir le fichier Excel protégé par mot de passe et de le décrypter en utilisant le Aspose.Cells API comme codes suivants :

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Decrypt-Excel-File.py" >}}


