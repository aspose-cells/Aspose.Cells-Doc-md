---
title: Supprimer une feuille de calcul
type: docs
weight: 30
url: /fr/net/aspose-cells-griddesktop/remove-a-worksheet/
keywords: GridDesktop, supprimer, feuille de calcul
description: Cet article présente comment supprimer une feuille de calcul dans GridDesktop.
---

{{% alert color="primary" %}} 

Ce sujet traite de la suppression de feuilles de calcul à l'aide du contrôle Aspose.Cells.GridDesktop. Il existe quelques approches simples pour accomplir cette tâche de base.

{{% /alert %}} 
## **Suppression d'une feuille de calcul**
Pour supprimer une feuille de calcul à l'aide du contrôle Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

1. Ajoutez le contrôle Aspose.Cells.GridDesktop à un formulaire.
1. Appelez la méthode Remove de la collection Worksheets dans le contrôle GridDesktop.
### **Utilisation de l'index de la feuille de calcul**
Dans cette approche, il suffit de passer l'index de la feuille de calcul (dans la collection de feuilles de calcul du tableau) de la feuille de calcul à supprimer.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **Utilisation du nom de la feuille de calcul**
Si le nom de la feuille de calcul est connu, il est possible de supprimer une feuille de calcul spécifique en spécifiant son nom.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Supprimer est une méthode. Utilisez-la pour supprimer une feuille de calcul en utilisant son index (dans la collection de feuilles de calcul) ou utilisez la méthode RemoveAt pour supprimer la feuille de calcul en utilisant son index/nom.

{{% /alert %}}
