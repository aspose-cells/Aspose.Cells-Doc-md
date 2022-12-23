---
title: Ouvrir un fichier Excel
type: docs
weight: 10
url: /fr/net/opening-an-excel-file/
---
{{% alert color="primary" %}} 

Une caractéristique unique de Aspose.Cells Grid Suite est sa compatibilité avec les fichiers Excel. Dans cette rubrique, nous montrerons comment les utilisateurs peuvent ouvrir des fichiers Excel dans leurs applications Windows à l'aide du contrôle Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Introduction**
 Pour ouvrir un fichier Excel à l'aide de Aspose.Cells.GridDesktop, vous devez créer une application de bureau contenant GridDesktop Control. Si vous ne savez pas comment ajouter le contrôle Aspose.Cells.GridDesktop à votre formulaire Windows, vous devez vous référer à[Comment utiliser Aspose.Cells.GridDesktop](/cells/fr/net/how-to-use-aspose-cells-griddesktop/)

Aspose.Cells.GridDesktop propose trois méthodes différentes pour ouvrir un fichier Excel.

1. **Ouverture à partir d'un fichier**
1. **Ouverture d'un dossier CSV**
1. **Ouverture à partir d'un flux**
## **Ouverture du fichier Excel**
Dans cet exemple, créez une application de bureau et procédez comme suit.

- Ajoutez un contrôle GridControl au formulaire.
- Ajoutez trois boutons avec leurs propriétés de texte définies comme suit :
  - **Ouvrir le fichier Excel**
  - **Ouvrir le fichier CSV**
  - **Ouvrir à partir du flux**
### **Ouverture à partir d'un fichier**
 Pour charger le contenu d'un fichier Excel dans le contrôle Aspose.Cells.GridDesktop, vous devrez appeler une méthode du contrôle pour spécifier le chemin du fichier Excel. Après cela, le contrôle Aspose.Cells.GridDesktop trouvera automatiquement le fichier à partir du chemin spécifié et affichera son contenu. L'extrait de code pour charger le contenu d'un fichier Excel est fourni dans l'exemple ci-dessous. Créez l'événement Click du**Ouvrir le fichier Excel** bouton et collez le code suivant à l'intérieur.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


L'extrait de code ci-dessus peut être utilisé par les développeurs comme ils le souhaitent. Par exemple, si vous souhaitez charger automatiquement un fichier Excel lors du chargement d'un formulaire Windows, vous pouvez ajouter ce code sous l'événement Load de votre formulaire.
### **Ouverture d'un dossier CSV**
Le contrôle Aspose.Cells.GridDesktop prend également en charge le chargement du fichier CSV. Créez l'événement Click du**Ouvrir le fichier CSV** bouton et collez le code suivant à l'intérieur.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **Ouverture à partir d'un flux**
 Dans notre discussion ci-dessus, nous avons discuté du chargement d'un fichier Excel en utilisant son chemin de fichier, mais le contrôle Aspose.Cells.GridDesktop prend également en charge le chargement d'un fichier Excel à partir d'un flux. Créez l'événement Click du**Ouvrir à partir du flux** bouton et collez le code suivant à l'intérieur.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



L'utilisation de fichier en tant que flux est une meilleure approche pour interdire tout type d'accès aux fichiers ou de partage de problèmes de violation, car cette approche garantit la fermeture de toutes les connexions aux fichiers en fermant le flux.

{{% alert color="primary" %}} 

IMPORTANT : Un point important à discuter est que le contrôle Aspose.Cells.GridDesktop contient également une méthode nommée LoadFromExcel, qui est également utilisée pour charger le contenu d'un fichier Excel dans la grille. Mais, cette méthode est maintenant obsolète. Ainsi, il est recommandé à tous les développeurs d'utiliser la méthode ImportExcelFile qui est plus robuste et efficace que celle obsolète.

{{% /alert %}}
