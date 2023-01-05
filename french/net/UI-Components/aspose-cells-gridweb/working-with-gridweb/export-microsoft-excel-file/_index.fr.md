---
title: Exporter le fichier Excel Microsoft
type: docs
weight: 50
url: /fr/net/export-microsoft-excel-file/
---
{{% alert color="primary" %}} 

Il est possible de créer de nouveaux fichiers Excel Microsoft ou de manipuler des fichiers Excel existants sur des sites Web en mode graphique à l'aide du contrôle Aspose.Cells.GridWeb. Les fichiers peuvent ensuite être enregistrés dans des fichiers Excel. Aspose.Cells.GridWeb sert efficacement d'éditeur de feuille de calcul en ligne. Cette rubrique décrit comment enregistrer le contenu de la grille dans des fichiers Excel.

{{% /alert %}} 
## **Exporter des fichiers Excel**
### **Exporter en tant que fichier**
Pour enregistrer le contenu du champ Aspose.Cells.GridWeb sous forme de fichier Excel :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Enregistrez votre travail sous forme de fichier Excel dans un chemin spécifié.
1. Exécutez l'application.

{{% alert color="primary" %}} 

 Si vous ne savez pas comment ajouter le contrôle Aspose.Cells.GridWeb à votre formulaire Web, vous devez vous référer à[Ajouter GridWeb au formulaire Web](/cells/fr/net/add-gridweb-to-web-form/)

{{% /alert %}} 

Lorsque le contrôle Aspose.Cells.GridWeb est ajouté à un formulaire Windows, le contrôle est automatiquement instancié et ajouté au formulaire avec une taille par défaut. Vous n'avez pas besoin de créer un objet de contrôle Aspose.Cells.GridWeb, tout ce que vous avez à faire est de faire glisser et déposer le contrôle et de commencer à l'utiliser.

L'exemple de code ci-dessous illustre comment enregistrer le contenu de la grille dans un fichier Excel.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

Si votre système de fichiers est NTFS, accordez un accès en lecture/écriture aux comptes d'utilisateurs ASPNET ou Tout le monde ou vous obtiendrez une exception d'accès refusé lors de l'exécution.

{{% /alert %}} 

L'extrait de code ci-dessus peut être utilisé de plusieurs façons. Une méthode courante consiste à ajouter un bouton qui enregistre le contenu de la grille dans un fichier Excel lorsque vous cliquez dessus. Aspose.Cells.GridWeb offre une approche plus simple pour la tâche. Aspose.Cells.GridWeb a un événement appelé SaveCommand. L'extrait de code ci-dessus peut être ajouté au gestionnaire d'événements de l'événement SaveCommand qui permet aux utilisateurs d'enregistrer leur travail en cliquant sur le Aspose.Cells.GridWeb intégré**Sauver** bouton.

**L'événement SaveCommand de GridWeb** 

![tâche : image_autre_texte](export-microsoft-excel-file_1.jpg)

**Enregistrement du contenu de la grille dans Excel en cliquant sur le bouton Enregistrer intégré de GridWeb** 

![tâche : image_autre_texte](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

 Si vous travaillez dans Visual Studio, vous pouvez facilement créer le gestionnaire d'événements de l'événement SaveCommand en double-cliquant sur l'événement dans le**Propriétés** vitre. Pour en savoir plus à ce sujet, veuillez consulter[Utilisation des événements GridWeb](/cells/fr/net/working-with-gridweb-events/)

{{% /alert %}} 
### **Exporter en tant que flux**
Il est également possible d'enregistrer le contenu de la grille dans un flux (par exemple MemoryStream).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
