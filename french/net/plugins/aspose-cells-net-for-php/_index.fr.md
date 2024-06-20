---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /fr/net/aspose-cells-net-for-php/
---

## **Pour commencer**

### **Introduction**

### **Configuration requise et plateformes prises en charge**

#### **Configuration requise**

**Voici les configurations requises pour utiliser Aspose.Cells .NET pour PHP:**

- IIS avec PHP et PHP Manager installés.
- Aspose.Total APIs.
- Le fichier dll et tlb d'interopérabilité Aspose.Cells.

#### **Plateformes prises en charge**

**Voici les plateformes prises en charge:**

- PHP 5.3 ou supérieur
- Système d'exploitation Windows

### **Télécharger et Configurer**

#### **Télécharger les bibliothèques requises**

Téléchargez les bibliothèques requises mentionnées ci-dessous. Ce sont les éléments nécessaires pour exécuter les exemples Aspose.Cells Java pour PHP.

- [Téléchargez les fichiers Aspose.Cells for .NET (DLL ou MSI) depuis la section de téléchargement](https://downloads.aspose.com/cells/net)
- [Téléchargez le DLL d'interop Aspose.Cells for .NET](https://downloads.aspose.com/cells/net)

Si vous téléchargez la version MSI, vous trouverez Aspose.Cells.dll dans l'emplacement installé, qui est C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0 par défaut.
Cependant, si vous avez téléchargé la version DLL, vous pouvez l'extraire et ensuite copier Aspose.Cells.dll depuis le dossier .NET 2.0 vers votre dossier c:\temp pour plus de facilité d'utilisation.
De même, extrayez le fichier zip d'interop et copiez Aspose.Inteop.dll vers c:\temp

#### **Téléchargez les exemples des sites de codage social**

Les versions suivantes des exemples en cours d'exécution sont disponibles en téléchargement sur les sites de codage social mentionnés ci-dessous:

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP Examples**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Comment configurer le code source sur la plateforme Windows**

Veuillez suivre ces étapes simples pour ouvrir et étendre le code source lors de son utilisation:

##### **1. Enregistrer les fichiers dll et interop.dll comme Aspose.Cells.dll et Aspose.Cells.Interop.dll.**

{{< highlight java >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. Activer les extensions COM et DOTNET dans PHP.**

Dans IIS, ouvrez PHP Manager puis cliquez sur 'Activer ou désactiver une extension'. Trouvez php_com_dotnet.dll et assurez-vous qu'il est activé.

##### **3. Configurer les exemples Aspose.Cells .NET pour PHP**

###### **Méthode 1**

Cloner les exemples PHP depuis [github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
et exécutez la commande suivante

{{< highlight java >}}

 composer install

{{< /highlight >}}

###### **Méthode 2**

Ajoutez les lignes suivantes dans le fichier composer.json de votre projet PHP

{{< highlight java >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

et exécutez la commande d'installation

{{< highlight java >}}

 composer install

{{< /highlight >}}

To read about composer visit <https://getcomposer.org/>

### **Prise en charge de l'extension et de la contribution**

#### **Soutien**

Dès les premiers jours d'Aspose, nous savions que le simple fait de fournir de bons produits à nos clients ne suffirait pas. Nous devions également offrir un bon service. Nous sommes nous-mêmes des développeurs et comprenons à quel point il est frustrant de voir un problème technique ou une bizarrerie dans le logiciel vous empêcher de faire ce que vous devez faire. Nous sommes ici pour résoudre les problèmes, pas pour en créer.

C'est pourquoi nous offrons un support gratuit. Toute personne qui utilise notre produit, qu'elle l'ait acheté ou qu'elle l'utilise en évaluation, mérite toute notre attention et notre respect.

Vous pouvez enregistrer tout problème ou suggestion lié à Aspose.Cells .NET for PHP en utilisant l'une des plateformes suivantes :

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Élargir et contribuer**

Aspose.Cells .NET for PHP est open source et son code source est disponible sur les principaux sites de codage social répertoriés ci-dessous. Les développeurs sont encouragés à télécharger le code source et à contribuer en proposant ou en ajoutant de nouvelles fonctionnalités ou en améliorant celles existantes, afin que d'autres puissent en bénéficier également.

#### **Code source**

Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Exemples de code source**

Cette section comprend les sujets suivants

- [Guide des Programmateurs PHP](/cells/fr/net/php-programmers-guide/)
  - [Travailler avec les fichiers en PHP](/cells/fr/net/working-with-files-in-php/)
    - [Fonctionnalités de manipulation de fichiers en PHP](/cells/fr/net/file-handling-features-in-php/)
      - [Ouverture des fichiers en PHP](/cells/fr/net/opening-files-in-php/)
      - [Enregistrement des fichiers en PHP](/cells/fr/net/saving-files-in-php/)
    - [Fonctionnalités utilitaires en PHP](/cells/fr/net/utility-features-in-php/)
      - [Chiffrement des fichiers en PHP](/cells/fr/net/encrypting-files-in-php/)
      - [Conversion Excel en PDF en PHP](/cells/fr/net/excel-to-pdf-conversion-in-php/)
      - [Gestion des propriétés de document en PHP](/cells/fr/net/managing-document-properties-in-php/)
      - [Conversion de feuille de calcul en image en PHP](/cells/fr/net/worksheet-to-image-conversion-in-php/)
  - [Travailler avec des formules en PHP](/cells/fr/net/working-with-formulas-in-php/)
    - [Calcul de formules en PHP](/cells/fr/net/calculating-formulas-in-php/)
  - [Travailler avec des feuilles de calcul en PHP](/cells/fr/net/working-with-worksheets-in-php/)
    - [Fonctionnalités de gestion en PHP](/cells/fr/net/management-features-in-php/)
      - [Gestion des feuilles de calcul en PHP](/cells/fr/net/managing-worksheets-in-php/)
        - [Ajouter des feuilles de calcul à un fichier Excel existant en PHP](/cells/fr/net/add-worksheets-to-existing-excel-file-in-php/)
        - [Ajouter des feuilles de calcul à un nouveau fichier Excel en PHP](/cells/fr/net/add-worksheets-to-new-excel-file-in-php/)
        - [Suppression de feuilles de calcul en utilisant l'index de feuille en PHP](/cells/fr/net/removing-worksheets-using-sheet-index-in-php/)
        - [Suppression de feuilles de calcul en utilisant le nom de la feuille en PHP](/cells/fr/net/removing-worksheets-using-sheet-name-in-php/)
