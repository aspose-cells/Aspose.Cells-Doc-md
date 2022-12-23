---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /fr/net/aspose-cells-net-for-php/
---
## **Commencer**

### **Introduction**

### **Configuration système requise et plates-formes prises en charge**

#### **Configuration requise**

**Voici la configuration système requise pour utiliser Aspose.Cells .NET for PHP :**

- IIS avec PHP et PHP Manager installés.
- Aspose.Total API.
- Aspose.Cells le fichier Interop dll et tlb.

#### **Plates-formes prises en charge**

**Voici les plates-formes prises en charge :**

- PHP 5.3 ou supérieur
- Windows SE

### **Télécharger et configurer**

#### **Télécharger les bibliothèques requises**

Téléchargez les bibliothèques requises mentionnées ci-dessous. Ce sont les éléments requis pour exécuter les exemples Aspose.Cells Java for PHP.

- [Téléchargez les fichiers Aspose.Cells for .NET (DLL ou MSI) à partir de la section de téléchargement](https://downloads.aspose.com/cells/net)
- [Télécharger Aspose.Cells for .NET dll d'interopérabilité](https://downloads.aspose.com/cells/net)

Si vous téléchargez la version MSI, vous trouverez Aspose.Cells.dll dans l'emplacement d'installation qui est le dossier C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0 par défaut.
Cependant, si vous avez téléchargé la version DLL, vous pouvez l'extraire, puis copier Aspose.Cells.dll du dossier .NET 2.0 dans votre dossier c:\temp pour une utilisation plus facile.
De même, extrayez le fichier zip interop et copiez Aspose.Inteop.dll dans c:\temp

#### **Télécharger des exemples à partir de sites de codage social**

Les versions suivantes des exemples en cours d'exécution sont disponibles au téléchargement sur les sites de codage social mentionnés ci-dessous :

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP Exemples**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Comment configurer le code source sur la plate-forme Windows**

Veuillez suivre ces étapes simples afin d'ouvrir et d'étendre le code source lors de l'utilisation :

##### **1. Enregistrez les fichiers dll et interop.dll, par exemple Aspose.Cells.dll et Aspose.Cells.Interop.dll.**

{{< highlight "java" >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. Activez les extensions COM et DOTNET dans PHP.**

Dans IIS, ouvrez PHP Manager, puis cliquez sur "Activer pour désactiver et extension". Trouver php_com_dotnet.dll et assurez-vous qu'il est activé.

##### **3. Configurer Aspose.Cells .NET for PHP Exemples**

###### **Méthode 1**

 Cloner des exemples PHP à partir de[github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
et exécutez la commande suivante

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

###### **Méthode 2**

Dans le fichier composer.json de votre projet PHP, ajoutez les lignes suivantes

{{< highlight "java" >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

et exécutez la commande d'installation

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

 Pour en savoir plus sur la visite du compositeur<https://getcomposer.org/>

### **Soutenir Prolonger et Contribuer**

#### **Soutien**

Dès les premiers jours du Aspose, nous savions que donner à nos clients de bons produits ne suffirait pas. Nous devions également fournir un bon service. Nous sommes nous-mêmes des développeurs et comprenons à quel point il est frustrant lorsqu'un problème technique ou une bizarrerie du logiciel vous empêche de faire ce que vous devez faire. Nous sommes ici pour résoudre les problèmes, pas pour les créer.

C'est pourquoi nous proposons une assistance gratuite. Toute personne qui utilise notre produit, qu'elle l'ait acheté ou utilise une évaluation, mérite toute notre attention et notre respect.

Vous pouvez consigner tous les problèmes ou suggestions liés à Aspose.Cells .NET for PHP en utilisant l'une des plateformes suivantes :

- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Prolonger et contribuer**

Aspose.Cells .NET for PHP est open source et son code source est disponible sur les principaux sites Web de codage social répertoriés ci-dessous. Les développeurs sont encouragés à télécharger le code source et à contribuer en suggérant ou en ajoutant de nouvelles fonctionnalités ou en améliorant celles existantes, afin que d'autres puissent également en bénéficier.

#### **Code source**

Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants

- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Exemples d'exemples de code**

Cette section comprend les rubriques suivantes

- [Guide des programmeurs PHP](/cells/fr/net/php-programmers-guide/)
  - [Travailler avec des fichiers en PHP](/cells/fr/net/working-with-files-in-php/)
    - [Fonctionnalités de gestion de fichiers en PHP](/cells/fr/net/file-handling-features-in-php/)
      - [Ouverture de fichiers en PHP](/cells/fr/net/opening-files-in-php/)
      - [Sauvegarder des fichiers en PHP](/cells/fr/net/saving-files-in-php/)
    - [Fonctionnalités utilitaires en PHP](/cells/fr/net/utility-features-in-php/)
      - [Crypter des fichiers en PHP](/cells/fr/net/encrypting-files-in-php/)
      - [Excel vers PDF Conversion en PHP](/cells/fr/net/excel-to-pdf-conversion-in-php/)
      - [Gestion des propriétés de document en PHP](/cells/fr/net/managing-document-properties-in-php/)
      - [Conversion de feuille de calcul en image en PHP](/cells/fr/net/worksheet-to-image-conversion-in-php/)
  - [Travailler avec des formules en PHP](/cells/fr/net/working-with-formulas-in-php/)
    - [Calculer des formules en PHP](/cells/fr/net/calculating-formulas-in-php/)
  - [Travailler avec des feuilles de calcul en PHP](/cells/fr/net/working-with-worksheets-in-php/)
    - [Fonctionnalités de gestion en PHP](/cells/fr/net/management-features-in-php/)
      - [Gestion des feuilles de calcul en PHP](/cells/fr/net/managing-worksheets-in-php/)
        - [Ajouter des feuilles de calcul au fichier Excel existant en PHP](/cells/fr/net/add-worksheets-to-existing-excel-file-in-php/)
        - [Ajouter des feuilles de calcul au nouveau fichier Excel en PHP](/cells/fr/net/add-worksheets-to-new-excel-file-in-php/)
        - [Suppression de feuilles de calcul à l'aide de l'index de feuilles en PHP](/cells/fr/net/removing-worksheets-using-sheet-index-in-php/)
        - [Suppression de feuilles de calcul à l'aide du nom de la feuille en PHP](/cells/fr/net/removing-worksheets-using-sheet-name-in-php/)
