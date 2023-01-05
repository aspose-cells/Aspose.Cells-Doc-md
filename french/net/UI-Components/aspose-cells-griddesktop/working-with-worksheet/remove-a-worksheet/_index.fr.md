---
title: Supprimer une feuille de calcul
type: docs
weight: 30
url: /fr/net/remove-a-worksheet/
---
{{% alert color="primary" %}} 

Cette rubrique décrit la suppression de feuilles de calcul à l'aide du contrôle Aspose.Cells.GridDesktop. Il existe quelques approches simples pour accomplir cette tâche de base.

{{% /alert %}} 
## **Suppression d'une feuille de calcul**
Pour supprimer une feuille de calcul à l'aide du contrôle Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

1. Ajoutez le contrôle Aspose.Cells.GridDesktop à un formulaire.
1. Appelez la méthode Remove de la collection Worksheets dans le contrôle GridDesktop.
### **Utilisation de l'index de feuille de calcul**
Dans cette approche, il suffit de passer l'index de la feuille de calcul (dans la collection de feuilles de calcul de la grille) de la feuille de calcul à supprimer.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **Utilisation du nom de la feuille de calcul**
Si le nom de la feuille de calcul est connu, il est possible de supprimer une feuille de calcul spécifique en spécifiant son nom.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Remove est une méthode. Utilisez-le pour supprimer une feuille de calcul à l'aide de son index (dans la collection de feuilles de calcul) ou utilisez la méthode RemoveAt pour supprimer la feuille de calcul à l'aide de son index/nom.

{{% /alert %}}
