---
title: Chiffrer et déchiffrer les fichiers Excel
type: docs
weight: 40
url: /fr/java/encrypt-and-decrypt-excel-files/
description: Comment chiffrer et déchiffrer des fichiers Excel en utilisant Java. Verrouiller et déverrouiller les fichiers Excel.
---

{{% alert color="primary" %}}
Microsoft Excel (97 - 365 ) vous permet de chiffrer / protéger par mot de passe vos feuilles de calcul. Il utilise des algorithmes fournis par Crypto Service Provider. Un fournisseur de services cryptographiques ou CSP est un ensemble d'algorithmes cryptographiques avec différentes propriétés. Le CSP par défaut est "Compatible Office 97/2000" ou "Chiffrement hebdomadaire (XOR)". Il est également important de choisir une longueur de clé de chiffrement appropriée. Certains des fournisseurs de services cryptographiques ne prennent pas en charge plus de 40 ou 56 bits. Cela est considéré comme un type de chiffrement faible. Mais, pour un type de chiffrement fort, une longueur de clé minimale de 128 bits est requise. Microsoft Windows contient des fournisseurs de services cryptographiques qui proposent également des types de chiffrement forts, par exemple, le 'Fournisseur de cryptographie forte Microsoft'. Pour donner une idée, le chiffrement de 128 bits est ce que les banques utilisent pour chiffrer la connexion avec leurs systèmes bancaires sur Internet. Aspose.Cells vous permet de chiffrer / protéger par mot de passe vos fichiers Excel avec le type de chiffrement de votre choix.

{{% /alert %}}

## **Utilisation de MS Excel**

Dans MS Excel (par exemple MS Excel 2003), pour implémenter les paramètres de chiffrement de fichier, vous pouvez essayer :

- Dans le menu **Outils**, sélectionnez **Options**, puis sélectionnez l'onglet **Sécurité**.
- Saisissez le **Mot de passe à ouvrir** et cliquez sur le bouton **Avancé**.
- Choisissez le type de chiffrement et confirmez le mot de passe.

![todo:image_alt_text](encrypting-excel-files_1.png)

**Figure : Boîte de dialogue Options**

![todo:image_alt_text](encrypting-excel-files_2.png)

**Figure : Boîte de dialogue Type de chiffrement**

## **Chiffrer le fichier Excel**
L'exemple suivant montre comment vous pouvez chiffrer / protéger par mot de passe un fichier Excel à l'aide de l'API Aspose.Cells.

### **Code exemple :**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **Déchiffrer le fichier Excel avec Aspose.Cells**
Il est très facile d'ouvrir un fichier Excel protégé par mot de passe et de le déchiffrer en utilisant l'API Aspose.Cells avec les codes suivants :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



