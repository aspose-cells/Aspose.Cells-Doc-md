---
title: Umbraco Exporter des membres vers Excel
type: docs
weight: 10
url: /fr/net/umbraco-export-members-to-excel/
---
## **Introduction**

 Exporter des membres vers Excel est un module complémentaire pour Umbraco qui vous permet d'exporter des membres de votre CMS Umbraco vers une feuille de calcul Excel et OpenDocument à l'aide[Aspose.Cells](https://products.aspose.com/cells/net/) . Un nouveau nœud intitulé**Exporter les membres vers Excel**apparaît sous l'arborescence des membres dans le backend Umbraco après l'installation où vous pouvez simplement sélectionner les membres à exporter et le format de sortie pour obtenir les membres dans le format de document de sortie sélectionné.

### **Caractéristiques des modules**

Cette version initiale de l'Add-on possède les fonctionnalités suivantes :

- Exporter des membres vers des documents Excel Microsoft (.xls, .xlsx et .xlsb)
- Exporter les membres vers un document texte délimité par des tabulations (.txt)
- Exporter les membres au format CSV (délimité par des virgules) (*.csv)
- Exporter les membres vers la feuille de calcul OpenDocument (*.ods)
- Option pour sélectionner le format de sortie souhaité avant l'exportation
- Option pour exporter tous les membres ou certains membres vers le format de document de sortie sélectionné.
- Fonctionne avec toutes les versions .NET à partir de .NET 2.0.
- Le document exporté est automatiquement envoyé au navigateur pour téléchargement
- Si cette option est sélectionnée, une copie du document exporté est enregistrée dans le dossier App_Data/AsposeMemberExport sur le serveur pour une utilisation ultérieure.
-  Compatible avec une large gamme de versions Umbraco**4.5**+ **y compris les versions 6 et 7.**

## **Configuration système requise et plates-formes prises en charge**

### **Configuration requise**

Pour configurer ce module, vous devez remplir les conditions suivantes :

- Umbraco 6.0 +

N'hésitez pas à nous contacter si vous souhaitez installer ce module sur d'autres versions d'Umbraco.

### **Plates-formes prises en charge**

Le module est pris en charge sur toutes les versions de

- Umbraco fonctionnant sur ASP.NET 4.0

## **Téléchargement**

Vous pouvez télécharger le module complémentaire Exporter les membres vers Excel à partir de l'un des emplacements suivants

- [ GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **Installation**

Une fois téléchargé, veuillez suivre ces étapes pour installer ce package sur votre site Web Umbraco :

1.  Connectez-vous à Umbraco**Développeur** section, par exemple `http://www.myblog.com/umbraco/`
1.  Dans l'arborescence, développez le**Paquets** dossier.
1.  À partir de là, il existe deux façons d'installer un paquet : sélectionnez**Installer le paquet local** ou parcourez le**Référentiel de packages Umbraco.**
1. Si vous installez**forfait local**, ne décompressez pas le package mais chargez le zip dans Umbraco.
1. Suivez les instructions à l'écran.

**Noter:** Vous pouvez obtenir une erreur "Longueur maximale de la demande dépassée" lors de l'installation. Vous pouvez facilement résoudre ce problème en mettant à jour la valeur 'maxRequestLength' dans votre fichier Umbraco web.config.

{{< highlight "java" >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **Utilisant**

Après avoir installé la macro, il est très simple de commencer à l'utiliser sur votre site Web :

1. Assurez-vous que vous êtes connecté à Umbraco**Développeur** section, par exemple `http://www.myblog.com/umbraco/`
1.  Cliquez sur**Membres** dans la liste des rubriques en bas à gauche de l'écran.
1.  À la fin de l'arborescence, vous verrez un nœud intitulé**Exporter les membres vers Excel** cliquez dessus pour lancer le module complémentaire Exporter vers Excel.
1. Sélectionnez le format de document de sortie souhaité et sélectionnez Membres à exporter. Si vous souhaitez exporter tous les membres, laissez la sélection des membres ou cliquez sur la case à cocher dans la ligne d'en-tête.
1.  Cliquez sur**Exporter** en bas et vous serez invité à télécharger le fichier exporté.

## **Démo vidéo**

 Vérifiez s'il vous plaît[la vidéo](https://www.youtube.com/watch?v=6PxZFvjWr2Y) ci-dessous pour voir le module en action.

## **Soutenir, étendre et contribuer**

### **Soutien**

Dès les premiers jours du Aspose, nous savions que donner à nos clients de bons produits ne suffirait pas. Nous devions également fournir un bon service. Nous sommes nous-mêmes des développeurs et comprenons à quel point il est frustrant lorsqu'un problème technique ou une bizarrerie du logiciel vous empêche de faire ce que vous devez faire. Nous sommes ici pour résoudre les problèmes, pas pour les créer.

C'est pourquoi nous proposons une assistance gratuite. Toute personne qui utilise notre produit, qu'elle l'ait acheté ou utilise une évaluation, mérite toute notre attention et notre respect.

Vous pouvez enregistrer tous les problèmes ou suggestions liés à Aspose.Words .NET pour les modules Umbraco en utilisant l'une des plates-formes suivantes

- [ GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Prolonger et contribuer**

Exporter les membres vers Excel est un module complémentaire open source et son code source est disponible sur les principaux sites Web de codage social répertoriés ci-dessous. Les développeurs sont encouragés à télécharger le code source et à étendre les fonctionnalités selon leurs propres besoins.

#### **Code source**

Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants

- [ GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **Comment configurer le code source**

Vous devez avoir installé les éléments suivants pour ouvrir et étendre le code source

- Visual Studio 2010 ou supérieur

Veuillez suivre ces étapes simples pour commencer

1. Téléchargez/clonez le code source.
1.  Ouvrez Visual Studio 2010 et choisissez**Dossier** > **Projet ouvert**
1.  Accédez au dernier code source que vous avez téléchargé et ouvrez**par exemple Aspose.UmbracoMemberExportToExcel.sln**
