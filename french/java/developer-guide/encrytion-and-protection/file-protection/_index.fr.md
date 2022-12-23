---
title: Crypter et décrypter des fichiers Excel
type: docs
weight: 40
url: /fr/java/encrypt-and-decrypt-excel-files/
description: Comment chiffrer et déchiffrer des fichiers Excel en utilisant Java. Verrouillez et déverrouillez les fichiers Excel.
---
{{% alert color="primary" %}}
Microsoft Excel (97 - 365 ) vous permet de chiffrer/protéger par mot de passe vos feuilles de calcul. Il utilise des algorithmes fournis par Crypto Service Provider. Un fournisseur de services cryptographiques ou CSP est un ensemble d'algorithmes cryptographiques avec différentes propriétés. Le CSP par défaut est "Office 97/2000 Compatible" ou "Week Encryption (XOR)". Il est également important de choisir une longueur de clé de cryptage appropriée. Certains des fournisseurs de services de cryptage ne prennent pas en charge plus de 40 ou 56 bits. C'est considéré comme un type de cryptage faible. Mais, pour le type de cryptage fort, une longueur de clé minimale de 128 bits est requise. Microsoft Windows contient des fournisseurs de services de cryptage qui proposent également des types de cryptage renforcés, par exemple, le « Microsoft Strong Cryptographic Provider ». Pour donner une idée, le cryptage 128 bits est ce que les banques utilisent pour crypter la connexion avec leurs systèmes bancaires par Internet. Aspose.Cells vous permet de crypter / protéger par mot de passe vos fichiers Excel avec le type de cryptage souhaité.

{{% /alert %}}

## **Utilisation de MS Excel**

Dans MS Excel (par exemple MS Excel 2003), pour implémenter les paramètres de cryptage des fichiers, vous pouvez essayer :

-  Du**Outils** menu, sélectionnez**Choix** , puis sélectionnez le**Sécurité** languette.
-  Contribution**Mot de passe pour ouvrir** et cliquez sur le**Avancé** bouton.
- Choisissez le type de cryptage et confirmez le mot de passe.

![tâche : image_autre_texte](encrypting-excel-files_1.png)

**Figure : Boîte de dialogue Options**

![tâche : image_autre_texte](encrypting-excel-files_2.png)

**Figure : Boîte de dialogue Type de chiffrement**

## **Chiffrement du fichier Excel**
L'exemple suivant montre comment vous pouvez chiffrer/protéger par mot de passe un fichier Excel en utilisant le Aspose.Cells API.

### **Exemple de code :**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **Décryptage du fichier Excel avec Aspose.Cells**
Il est très facile d'ouvrir le fichier Excel protégé par mot de passe et de le décrypter en utilisant le Aspose.Cells API comme codes suivants :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



