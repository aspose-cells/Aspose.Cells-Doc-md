---
title: Umbraco Export Members to Excel
type: docs
weight: 10
url: /fr/net/umbraco-export-members-to-excel/
---

## **Introduction**

Export Members to Excel est un module complémentaire pour Umbraco qui vous permet d'exporter des membres de votre CMS Umbraco vers un fichier Excel et une feuille de calcul OpenDocument en utilisant [Aspose.Cells](https://products.aspose.com/cells/net/). Un nouveau nœud intitulé **Export Members To Excel** apparaît sous l'arborescence des membres dans l'interface d'administration d'Umbraco après l'installation, où vous pouvez simplement sélectionner les membres à exporter et le format de sortie pour obtenir les membres dans le format de document de sortie sélectionné.

### **Fonctionnalités du module**

Cette version initiale du module dispose des fonctionnalités suivantes :

- Exporter les membres vers des documents Microsoft Excel (.xls, .xlsx et .xlsb)
- Exporter les membres vers un document texte tabulé (.txt)
- Exporter les membres au format CSV (délimité par une virgule) (*.csv)
- Exporter les membres vers une feuille de calcul OpenDocument (*.ods)
- Option pour sélectionner le format de sortie souhaité avant l'exportation
- Option pour exporter tous les membres ou les membres sélectionnés vers le format de document de sortie sélectionné.
- Fonctionne avec toutes les versions de .NET à partir de .NET 2.0.
- Le document exporté est automatiquement envoyé au navigateur pour le téléchargement
- Si vous sélectionnez une copie du document exporté est enregistrée dans le dossier App_Data/AsposeMemberExport sur le serveur pour une utilisation ultérieure.
- Compatible avec un large éventail de versions Umbraco **4.5**+ **y compris les Versions 6 et 7.**

## **Configuration requise et plateformes prises en charge**

### **Configuration requise**

Pour configurer ce module, vous devez répondre aux exigences suivantes :

- Umbraco 6.0 +

N'hésitez pas à nous contacter si vous souhaitez installer ce module sur d'autres versions d'Umbraco.

### **Plateformes prises en charge**

Le module est pris en charge sur toutes les versions de

- Umbraco fonctionnant sur ASP.NET 4.0

## **Téléchargement**

Vous pouvez télécharger l'extension Export Members to Excel depuis l'un des emplacements suivants

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **Installer**

Une fois le téléchargement terminé, veuillez suivre ces étapes pour installer ce package dans votre site Umbraco :

1. Connectez-vous à la section **Developer** Umbraco, par exemple `http://www.myblog.com/umbraco/`
1. Dans l'arborescence, développez le dossier **Packages**.
1. À partir d'ici, il existe deux façons d'installer un package : sélectionnez **Installer un package local** ou parcourez le **Dépôt de packages Umbraco.**
1. Si vous installez un **package local**, ne décompressez pas le package mais chargez le zip dans Umbraco.
1. Suivez les instructions à l'écran.

**Remarque :** Vous pouvez rencontrer une erreur de « Dépassement de la durée maximum de la requête » lors de l'installation. Vous pouvez facilement corriger ce problème en mettant à jour la valeur « maxRequestLength » dans votre fichier web.config Umbraco.

{{< highlight java >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **En utilisant**

Une fois que vous avez installé le macro, il est vraiment simple de commencer à l'utiliser sur votre site web :

1. Assurez-vous que vous êtes connecté à la section **Developpeur** d'Umbraco, par exemple `http://www.myblog.com/umbraco/`
1. Cliquez sur **Membres** dans la liste des sections en bas à gauche de l'écran.
1. À la fin de l'arborescence, vous verrez un nœud intitulé **Export Members To Excel**. Cliquez dessus pour lancer l'addon Export to Excel.
1. Sélectionnez le format de document de sortie souhaité et sélectionnez les membres à exporter. Si vous souhaitez exporter tous les membres, laissez la sélection des membres ou cliquez sur la case à cocher dans la ligne d'en-tête.
1. Cliquez sur le bouton **Exporter** en bas de page et vous serez invité à télécharger le fichier exporté.

## **Démo vidéo**

Veuillez consulter [la vidéo](https://www.youtube.com/watch?v=6PxZFvjWr2Y) ci-dessous pour voir le module en action.

## **Soutenir, étendre et contribuer**

### **Soutien**

Dès les premiers jours d'Aspose, nous savions que le simple fait de fournir de bons produits à nos clients ne suffirait pas. Nous devions également offrir un bon service. Nous sommes nous-mêmes des développeurs et comprenons à quel point il est frustrant de voir un problème technique ou une bizarrerie dans le logiciel vous empêcher de faire ce que vous devez faire. Nous sommes ici pour résoudre les problèmes, pas pour en créer.

C'est pourquoi nous offrons un support gratuit. Toute personne qui utilise notre produit, qu'elle l'ait acheté ou qu'elle l'utilise en évaluation, mérite toute notre attention et notre respect.

Vous pouvez signaler tout problème ou suggestion lié aux modules Aspose.Words .NET pour Umbraco en utilisant l'une des plateformes suivantes

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Élargir et contribuer**

Export Members to Excel est un module open source et son code source est disponible sur les principaux sites de codage social listés ci-dessous. Les développeurs sont encouragés à télécharger le code source et à étendre la fonctionnalité selon leurs propres besoins.

#### **Code source**

Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **Comment configurer le code source**

Vous devez avoir les éléments suivants installés pour ouvrir et étendre le code source

- Visual Studio 2010 ou version ultérieure

Veuillez suivre ces étapes simples pour commencer

1. Téléchargez/clônez le code source.
1. Ouvrez Visual Studio 2010 et choisissez **Fichier** > **Ouvrir un projet**
1. Accédez au code source le plus récent que vous avez téléchargé et ouvrez **par exemple Aspose.UmbracoMemberExportToExcel.sln**
