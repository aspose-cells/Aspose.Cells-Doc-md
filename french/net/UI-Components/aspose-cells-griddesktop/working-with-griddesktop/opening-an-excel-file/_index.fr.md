---
title: Ouverture d un fichier Excel
type: docs
weight: 10
url: /fr/net/aspose-cells-griddesktop/openg-an-excel-file/
keywords: GridDesktop,ouvrir,fichier
description: Cet article présente comment ouvrir un fichier dans GridDesktop.
---

{{% alert color="primary" %}} 

Une fonctionnalité unique de la suite de grille Aspose.Cells est sa compatibilité avec les fichiers Excel. Dans ce sujet, nous démontrerons comment les utilisateurs peuvent ouvrir des fichiers Excel dans leurs applications Windows en utilisant le contrôle Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Introduction**
Pour ouvrir un fichier Excel en utilisant Aspose.Cells.GridDesktop, vous devez créer une application de bureau avec le contrôle GridDesktop. Si vous ne savez pas comment ajouter le contrôle Aspose.Cells.GridDesktop à votre formulaire Windows, vous devriez vous référer à [Comment utiliser Aspose.Cells.GridDesktop](/cells/fr/net/how-to-use-aspose-cells-griddesktop/)

Aspose.Cells.GridDesktop propose trois façons différentes d'ouvrir un fichier Excel.

1. **Ouvrir à partir d'un fichier**
1. **Ouverture d'un fichier CSV**
1. **Ouvrir à partir d'un flux**
## **Ouverture de fichier Excel**
Dans cet exemple, créez une application de bureau et faites ce qui suit.

- Ajoutez un contrôle GridControl au formulaire.
- Ajoutez trois boutons avec leurs propriétés de texte définies comme suit :
  - **Ouvrir un fichier Excel**
  - **Ouvrir un fichier CSV**
  - **Ouvrir à partir d'un flux**
### **Ouverture à partir d'un fichier**
Pour charger le contenu d'un fichier Excel dans un contrôle Aspose.Cells.GridDesktop, vous devrez appeler une méthode du contrôle pour spécifier le chemin du fichier Excel. Ensuite, le contrôle Aspose.Cells.GridDesktop trouvera automatiquement le fichier à partir du chemin spécifié et affichera son contenu. L'exemple de code pour charger le contenu d'un fichier Excel est fourni dans l'exemple ci-dessous. Créez l'événement Click du bouton **Ouvrir le fichier Excel** et collez le code suivant à l'intérieur.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


Le snippet de code ci-dessus peut être utilisé par les développeurs de n'importe quelle manière qu'ils souhaitent. Par exemple, si vous souhaitez charger automatiquement un fichier Excel lorsque qu'un formulaire Windows se charge, vous pouvez ajouter ce code sous l'événement Load de votre formulaire.
### **Ouvrir un fichier CSV**
Le contrôle Aspose.Cells.GridDesktop prend également en charge le chargement de fichiers CSV. Créez l'événement Click du bouton **Ouvrir un fichier CSV** et collez le code suivant à l'intérieur.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **Ouverture à partir d'un flux**
Dans notre discussion ci-dessus, nous avons discuté du chargement d'un fichier Excel en utilisant son chemin d'accès, mais le contrôle Aspose.Cells.GridDesktop prend également en charge le chargement de fichiers Excel à partir d'un flux. Créez l'événement Click du bouton **Ouvrir à partir d'un flux** et collez le code suivant à l'intérieur.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



L'utilisation d'un fichier en tant que flux est une meilleure approche pour éviter tout problème de violation d'accès ou de partage de fichier car cette approche garantit la fermeture de toutes les connexions aux fichiers en fermant le flux.

{{% alert color="primary" %}} 

IMPORTANT : Un point important à discuter est que le contrôle Aspose.Cells.GridDesktop contient également une méthode nommée LoadFromExcel, qui est également utilisée pour charger le contenu d'un fichier Excel dans le Grid. Cependant, cette méthode est désormais obsolète. Il est donc recommandé à tous les développeurs d'utiliser la méthode ImportExcelFile qui est plus robuste et plus efficace que la précédente.

{{% /alert %}}
