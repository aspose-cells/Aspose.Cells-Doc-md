---
title: Accéder et modifier la valeur d une cellule
type: docs
weight: 20
url: /fr/net/aspose-cells-griddesktop/accessing-and-modifying-the-value-of-a-cell/
keywords: GridDesktop,cell,modify cell,get cell,modify cell value,get cell value
description: Cet article présente comment obtenir et modifier la valeur d une cellule dans GridDesktop.
---

{{% alert color="primary" %}} 

Dans notre sujet précédent, nous avons discuté de l'accès aux cellules d'une feuille de calcul. Dans ce sujet, nous étendrons simplement ce sujet pour montrer aux développeurs comment ils peuvent accéder et modifier les valeurs des cellules en utilisant l'API de Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Accéder et modifier la valeur d'une cellule avec Aspose.Cells.GridDesktop**
Avant d'accéder et de modifier la valeur d'une cellule, nous devrions savoir comment accéder aux cellules. Il existe trois approches pour accéder aux cellules d'une feuille de calcul. Pour plus de détails sur ces trois approches, veuillez consulter [Accès aux cellules dans une feuille de calcul.](/cells/fr/net/accessing-cells-in-a-worksheet/)

Chaque cellule a une propriété nommée Valeur . Ainsi, une fois qu'une cellule est accessible, les développeurs peuvent accéder et modifier le contenu de la propriété Valeur afin d'accéder et de changer la valeur d'une cellule.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**IMPORTANT :** Utiliser la propriété Valeur d'une cellule pour modifier sa valeur est une bonne approche pour définir la valeur d'une ou quelques cellules. Si vous devez définir les valeurs de nombreuses cellules, alors les performances de cette approche ne seraient pas bonnes. Ainsi, pour définir les valeurs de nombreuses cellules, vous devriez utiliser la méthode **SetCellValue** de la cellule pour améliorer les performances de vos applications. Une version modifiée de l'extrait de code ci-dessus utilisant la méthode **SetCellValue** est présentée ci-dessous.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
