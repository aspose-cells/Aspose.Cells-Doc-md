---
title: Importer le fichier Excel Microsoft
type: docs
weight: 40
url: /fr/net/import-microsoft-excel-file/
---
{{% alert color="primary" %}} 

Comme Aspose.Cells.GridDesktop, le contrôle Aspose.Cells.GridWeb peut ouvrir et charger des fichiers Excel Microsoft - complets avec données, formatage, graphiques, images, etc. - mais dans des applications Web. Cette rubrique explique comment.

{{% /alert %}} 
## **Importer des fichiers Excel**
### **Importer depuis un fichier**
Pour ouvrir un fichier Excel à l'aide du contrôle Aspose.Cells.GridWeb :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Importez le fichier Excel en spécifiant le chemin du fichier.
1. Exécutez l'application.

{{% alert color="primary" %}} 

 Si vous ne savez pas comment ajouter le contrôle à un formulaire Web, reportez-vous à[Ajouter GridWeb au formulaire Web](/cells/fr/net/add-gridweb-to-web-form/).

{{% /alert %}} 

Lorsque le contrôle Aspose.Cells.GridWeb est ajouté à un formulaire Web, le contrôle est automatiquement instancié et ajouté au formulaire avec une taille par défaut. Vous n'avez pas besoin de créer un objet de contrôle Aspose.Cells.GridWeb, tout ce que vous avez à faire est de faire glisser et déposer le contrôle et de commencer à l'utiliser.

Cependant, pour charger le contenu d'un fichier Excel dans le contrôle Aspose.Cells.GridWeb, vous devez appeler la méthode ImportExcelFile pour spécifier le chemin du fichier Excel. Après cela, le contrôle Aspose.Cells.GridWeb trouvera automatiquement le fichier à partir du chemin spécifié et affichera son contenu. Un extrait de code qui charge le contenu d'un fichier Excel est fourni ci-dessous.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


L'extrait de code ci-dessus peut être utilisé comme vous le souhaitez. Par exemple, pour charger automatiquement un fichier Excel lors du chargement d'un formulaire Web, ajoutez ce code à l'événement Page_Load du formulaire. Si vous souhaitez ouvrir un fichier lorsqu'un bouton est cliqué, ajoutez un bouton au formulaire Web et écrivez le code ci-dessus sous l'événement Click du bouton.

**Un fichier Excel est chargé lorsqu'un bouton est cliqué** 

![tâche : image_autre_texte](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

Si votre système de fichiers est NTFS, vous devez accorder une autorisation d'accès en lecture aux comptes d'utilisateurs ASPNET ou Tout le monde, sinon vous obtiendrez une exception d'accès refusé lors de l'exécution.

{{% /alert %}} 
### **Importer depuis le flux**
En plus d'ouvrir des fichiers Excel à partir d'un fichier, le contrôle Aspose.Cells.GridWeb peut charger des fichiers Excel à partir d'un flux. L'utilisation de fichier en tant que flux est une meilleure approche pour interdire tout type d'accès aux fichiers ou de partage de problèmes de violation, car cette approche garantit la fermeture de toutes les connexions aux fichiers en fermant le flux.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
