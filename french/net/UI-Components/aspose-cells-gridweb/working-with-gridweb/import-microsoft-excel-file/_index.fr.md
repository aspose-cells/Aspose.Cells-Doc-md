---
title: Importer un fichier Microsoft Excel
type: docs
weight: 40
url: /fr/net/aspose-cells-gridweb/import-microsoft-excel-file/
keywords: GridWeb, importation
description: Cet article présente comment importer un fichier dans GridWeb.
---

{{% alert color="primary" %}} 

Comme Aspose.Cells.GridDesktop, le contrôle Aspose.Cells.GridWeb peut ouvrir et charger des fichiers Microsoft Excel - avec les données, la mise en forme, les graphiques, les images, etc. - mais dans des applications web. Ce sujet explique comment faire.

{{% /alert %}} 
## **Importer des fichiers Excel**
### **Importer depuis un fichier**
Pour ouvrir un fichier Excel en utilisant le contrôle Aspose.Cells.GridWeb :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire web.
2. Importez le fichier Excel en spécifiant le chemin du fichier.
1. Exécutez l'application.

{{% alert color="primary" %}} 

Si vous ne savez pas comment ajouter le contrôle à un formulaire web, reportez-vous à [Ajouter GridWeb au formulaire Web](/cells/fr/net/aspose-cells-gridweb/add-gridweb-to-web-form/).

{{% /alert %}} 

Lorsque le contrôle Aspose.Cells.GridWeb est ajouté à un formulaire web, le contrôle est automatiquement instancié et ajouté au formulaire avec une taille par défaut. Vous n'avez pas à créer d'objet contrôle Aspose.Cells.GridWeb, il vous suffit de faire glisser-déposer le contrôle et de commencer à l'utiliser.

Cependant, pour charger le contenu d'un fichier Excel dans le contrôle Aspose.Cells.GridWeb, vous devez appeler la méthode ImportExcelFile pour spécifier le chemin du fichier Excel. Ensuite, le contrôle Aspose.Cells.GridWeb trouvera automatiquement le fichier à partir du chemin spécifié et affichera son contenu. Un extrait de code qui charge le contenu d'un fichier Excel est fourni ci-dessous.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


Vous pouvez utiliser l'extrait de code ci-dessus de n'importe quelle manière. Par exemple, pour charger automatiquement un fichier Excel lors du chargement d'un formulaire web, ajoutez ce code à l'événement Page_Load du formulaire. Si vous souhaitez ouvrir un fichier lorsqu'un bouton est cliqué, ajoutez un bouton au formulaire web et écrivez le code ci-dessus sous l'événement Click du bouton.

**Un fichier Excel est chargé lorsqu'un bouton est cliqué** 

![todo:image_alt_text](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

Si votre système de fichiers est NTFS, vous devez accorder l'autorisation de lecture aux comptes d'utilisateur ASPNET ou Everyone, sinon vous obtiendrez une exception d'accès refusé à l'exécution.

{{% /alert %}} 
### **Importer depuis un flux**
En plus d'ouvrir des fichiers Excel à partir du fichier, le contrôle Aspose.Cells.GridWeb peut charger des fichiers Excel à partir d'un flux. Utiliser un fichier comme flux est une meilleure approche pour interdire tout type de problème d'accès ou de violation de partage de fichier car cette approche garantit la fermeture de toutes les connexions aux fichiers en fermant le flux.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
