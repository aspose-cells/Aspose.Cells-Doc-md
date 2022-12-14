---
title: Accéder et modifier la valeur d'un Cell
type: docs
weight: 20
url: /fr/net/accessing-and-modifying-the-value-of-a-cell/
---
{{% alert color="primary" %}} 

Dans notre rubrique précédente, nous avons discuté de l'accès aux cellules d'une feuille de calcul. Dans cette rubrique, nous allons simplement étendre cette rubrique pour montrer aux développeurs comment accéder et modifier les valeurs des cellules à l'aide du API de Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Accéder et modifier la valeur Cell à l'aide de Aspose.Cells.GridDesktop**
 Avant d'accéder et de modifier la valeur d'une cellule, nous devons savoir comment accéder aux cellules. Il existe trois approches pour accéder aux cellules d'une feuille de calcul. Pour plus de détails sur ces trois approches, veuillez[Accéder à Cells dans une feuille de travail.](/cells/fr/net/accessing-cells-in-a-worksheet/)

Chaque cellule a une propriété nommée Value . Ainsi, une fois qu'une cellule est accédée, les développeurs peuvent accéder et modifier le contenu de la propriété Value afin d'accéder et de modifier la valeur d'une cellule.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**IMPORTANT:**L'utilisation de la propriété Value d'une cellule pour modifier sa valeur est une bonne approche pour définir la valeur d'une ou de quelques cellules. Si vous devez définir les valeurs de plusieurs cellules, les performances de cette approche ne seront pas bonnes. Donc, pour définir les valeurs de plusieurs cellules, vous devez utiliser**DéfinirValeurCellule** méthode de la cellule pour améliorer les performances de vos applications. Une version modifiée de l'extrait de code ci-dessus utilisant**DéfinirValeurCellule** méthode est présentée ci-dessous.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
