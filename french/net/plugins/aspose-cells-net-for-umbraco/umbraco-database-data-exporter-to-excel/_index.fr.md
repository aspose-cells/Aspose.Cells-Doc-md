---
title: Exportateur des données de la base de données d Umbraco vers Excel
type: docs
weight: 20
url: /fr/net/umbraco-database-data-exporter-to-excel/
---

## **Introduction**
Le module d'exportation des données de la base de données .NET d’Aspose vers Excel pour Umbraco permet aux utilisateurs d'exporter directement des données à partir des tables, des vues de la base de données locale ou distante et par une requête personnalisée dans Microsoft Excel ou OpenOffice Spreadsheet. Ce module démontre la puissante fonction de création de feuille de calcul fournie par Aspose.Cells. Cette version initiale du module est enrichie des fonctionnalités suivantes pour rendre le processus d'exportation simple et facile à utiliser.
### **Fonctionnalités du module**
Cette version initiale du module dispose des fonctionnalités suivantes :

- Permettre de se connecter à la base de données locale de MS SQL Server
- Permettre de se connecter à la base de données distante de MS SQL Server
- Remplir toutes les tables de la base de données connectée
- Remplir toutes les vues de la base de données connectée
- Permettre d'écrire une requête personnalisée
- Ajustement automatique des colonnes à la longueur du contenu.
- Autoriser le saut de chaîne de plus de 32 ko dans les cellules Excel (LoadOptions)
- Appliquer la mise en forme de l'en-tête des colonnes en texte gras
- Autoriser l'utilisation en tant que source de données (tableaux, vues, requête personnalisée)
- Exporter des données vers des documents Microsoft Excel (.xls, .xlsx et .xlsb)
- Exporter des données vers un document texte délimité par des tabulations (*.txt)
- Exporter des données au format CSV (délimité par des virgules) (*.csv)
- Exporter des données vers des feuilles de calcul OpenDocument (*.ods)
- Option pour sélectionner le format de sortie souhaité avant l'exportation.
- Le document exporté est automatiquement envoyé au navigateur pour téléchargement. 

.

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_1)
## **Configuration requise et plateformes prises en charge**
### **Configuration requise**
Pour configurer l'exportateur de données de base de données Aspose .NET vers Excel pour le module Umbraco, vous devez remplir les conditions suivantes :

- Umbraco 6.2.5 et les versions d'Umbraco 6
- Umbraco avec MS SQL Server
- Microsoft .Net Framework 4.0

**Remarque :** Umbraco 7 et les versions ultérieures ne sont pas prises en charge dans cette version. Nous attendons avec impatience vos commentaires et ajouterons la prise en charge d'Umbraco 7 dans la prochaine version.
### **Plateformes prises en charge**
Le module est pris en charge sur toutes les versions de

- Umbraco 6.0 fonctionnant sur ASP.NET 4.0
## **Téléchargement**
Vous pouvez télécharger le module d'exportation de données de base de données Aspose .NET Cells vers Excel pour Umbraco depuis l'un des emplacements suivants

- [Projets Umbraco](https://goo.gl/BPrWm2)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsUmbracoDatatoExcel)
## **Installer**
Une fois le téléchargement terminé, veuillez suivre ces étapes pour installer ce package dans votre site Umbraco :

1. Connectez-vous à la section **Developer** Umbraco, par exemple `http://www.myblog.com/umbraco`
1. Dans l'arborescence, développez le dossier **Packages**.
1. À partir d'ici, il y a deux façons d'installer un package: sélectionner **Installer un package local** ou parcourir le **Répertoire de packages Umbraco.**
1. Si vous installez un **package local**, ne décompressez pas le package mais chargez le zip dans Umbraco.
1. Suivez les instructions à l'écran.

**Remarque :** Vous pouvez rencontrer une erreur de « Dépassement de la durée maximum de la requête » lors de l'installation. Vous pouvez facilement corriger ce problème en mettant à jour la valeur « maxRequestLength » dans votre fichier web.config Umbraco.
<httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
## **En utilisant**
Après avoir installé le module d'exportation de données de base de données Aspose .NET vers Excel pour Umbraco, il est vraiment simple de commencer à l'utiliser sur votre site Web. Veuillez suivre ces étapes simples pour commencer

1. Assurez-vous d'être connecté à la section **Developer** Umbraco, par exemple `http://www.myblog.com/umbraco/`
1. Cliquez sur **Paramètres** dans la liste des sections en bas à gauche de l'écran.
1. Développez le nœud **Modèles** et sélectionnez le modèle auquel vous souhaitez ajouter, par exemple Textpage.
1. Sélectionnez l'emplacement dans le modèle sélectionné où vous souhaitez ajouter le bouton d'exportation. Vous voudrez peut-être le ajouter en haut à droite de la page ou en bas de la page.
1. Cliquez sur **Insérer une macro** dans le ruban supérieur.
1. Depuis **Choisir une macro** (Aspose .NET Database Data Exporter vers Excel pour Umbraco), sélectionnez la macro Aspose .NET Database Data Exporter vers Excel pour Umbraco récemment installée et cliquez sur **OK**.

Veuillez vérifier la capture d'écran ci-dessous pour plus de détails. 

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_2)

Vous avez ajouté avec succès le module d'exportation de données de base de données Aspose .NET vers Excel à votre page.

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_1)

1. Entrez ou utilisez une chaîne de connexion MS SQL Server pré-renseignée
1. Sélectionnez le type de source de données (tableau, vue, requête personnalisée)
1. Sélectionnez ou saisissez la source de données (tableau, vue, requête personnalisée)
1. Sélectionnez le type d'exportation
1. Cliquez sur Exporter les données
1. Le fichier souhaité sera téléchargé automatiquement.
## **Démo vidéo**
Veuillez consulter [la vidéo](https://www.youtube.com/watch?v=MkfKyeLTauE) ci-dessous pour voir le module en action.
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

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.DatabaseDataExportertoExcel)
#### **Comment configurer le code source**
Vous devez avoir les éléments suivants installés pour ouvrir et étendre le code source

- Visual Studio 2010 ou version ultérieure

Veuillez suivre ces étapes simples pour commencer

1. Téléchargez/clônez le code source.
1. Ouvrez Visual Studio 2010 et choisissez **Fichier** > **Ouvrir un projet**
1. Accédez au dernier code source que vous avez téléchargé et ouvrez **par exemple Aspose.DatabaseDataExportertoExcel.sln**
