---
title: Exporter un fichier Microsoft Excel
type: docs
weight: 50
url: /fr/net/aspose-cells-gridweb/export-microsoft-excel-file/
keywords: GridWeb, export
description: Cet article présente comment exporter un fichier dans GridWeb.
---

{{% alert color="primary" %}} 

Il est possible de créer de nouveaux fichiers Microsoft Excel ou de manipuler des fichiers existants sur des sites web en mode GUI à l'aide du contrôle Aspose.Cells.GridWeb. Les fichiers peuvent ensuite être enregistrés en tant que fichiers Excel. Aspose.Cells.GridWeb sert efficacement d'éditeur de feuilles de calcul en ligne. Ce sujet décrit comment enregistrer le contenu de la grille dans des fichiers Excel.

{{% /alert %}} 
## **Exporter des fichiers Excel**
### **Exporter en tant que fichier**
Pour enregistrer le contenu du contrôle Aspose.Cells.GridWeb en tant que fichier Excel :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire web.
1. Enregistrez votre travail sous forme de fichier Excel à un chemin spécifié.
1. Exécutez l'application.

{{% alert color="primary" %}} 

Si vous ne savez pas comment ajouter le contrôle Aspose.Cells.GridWeb à votre formulaire web, vous devriez consulter [Ajouter GridWeb au formulaire Web](/cells/fr/net/aspose-cells-gridweb/ajouter-gridweb-au-formulaire-web/)

{{% /alert %}} 

Lorsque le contrôle Aspose.Cells.GridWeb est ajouté à un formulaire Windows, le contrôle est automatiquement instancié et ajouté au formulaire avec une taille par défaut. Vous n'avez pas besoin de créer un objet contrôle Aspose.Cells.GridWeb, tout ce que vous avez à faire est de glisser-déposer le contrôle et commencer à l'utiliser.

L'exemple de code ci-dessous illustre comment enregistrer le contenu de la grille dans un fichier Excel.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

Si votre système de fichiers est NTFS, accordez l'accès en lecture/écriture aux comptes utilisateur ASPNET ou Tout le monde, sinon vous obtiendrez une exception d'accès refusé à l'exécution.

{{% /alert %}} 

Le snippet de code ci-dessus peut être utilisé de plusieurs manières. Une façon courante est d'ajouter un bouton qui enregistre le contenu de la grille dans un fichier Excel lorsque vous cliquez dessus. Aspose.Cells.GridWeb offre une approche plus facile pour cette tâche. Aspose.Cells.GridWeb dispose d'un événement appelé SaveCommand. Le snippet de code ci-dessus peut être ajouté au gestionnaire d'événements de l'événement SaveCommand qui permet aux utilisateurs d'enregistrer leur travail en cliquant sur le bouton **Enregistrer** intégré à Aspose.Cells.GridWeb.

**L'événement SaveCommand de GridWeb** 

![todo:image_alt_text](export-microsoft-excel-file_1.jpg)

**Enregistrer le contenu de la grille dans Excel en cliquant sur le bouton Enregistrer intégré de GridWeb** 

![todo:image_alt_text](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

Si vous travaillez dans Visual Studio, vous pouvez facilement créer le gestionnaire d'événements de l'événement SaveCommand en double-cliquant sur l'événement dans le volet **Propriétés**. Pour en savoir plus à ce sujet, veuillez vous référer à [Travailler avec les événements de GridWeb](/cells/fr/net/aspose-cells-gridweb/travailler-avec-les-événements-de-gridweb/)

{{% /alert %}} 
### **Exporter en tant que flux**
Il est également possible d'enregistrer le contenu de la grille dans un flux (par exemple MemoryStream).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
