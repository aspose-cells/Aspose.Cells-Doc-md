---
title: Fusionner et fractionner les cellules dans GridDesktop
linktitle: Fusionner et séparer des cellules
type: docs
weight: 90
url: /fr/net/aspose-cells-griddesktop/merge-and-unmerge-cells-griddesktop/
keywords: GridDesktop, fusion, fractionnement
description: Cet article présente la fusion et le fractionnement dans GridDesktop.
---

{{% alert color="primary" %}} 

Dans ce sujet, nous discuterons d'une fonctionnalité d'utilité de fusionner et fractionner les cellules d'une feuille de calcul. Cette fonctionnalité est utile dans les cas où nous devons étendre certaines lignes ou colonnes pour améliorer la lisibilité des données.

{{% /alert %}} 
## **Fusionner les cellules**
Pour fusionner des cellules en une seule grande cellule, veuillez suivre les étapes ci-dessous:

- Accédez à n'importe quelle **Worksheet** souhaitée
- Créer une **Plage de cellules** à fusionner
- **Fusionner** la plage de cellules en une grande cellule

Vous pouvez utiliser la méthode **Fusionner** de **Feuille de calcul** pour fusionner des cellules. Cependant, une plage de cellules peut être définie à l'aide de l'objet **CellRange**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **Défusionner les cellules**
Pour défusionner une grande cellule en plusieurs cellules, veuillez suivre les étapes ci-dessous:

- Accédez à n'importe quelle **Worksheet** souhaitée
- Accédez à la cellule fusionnée à défusionner
- **Défusionnez** la grande cellule en plusieurs cellules en utilisant l'emplacement de la cellule fusionnée

Vous pouvez utiliser la méthode **unmerge** de **Worksheet** pour défusionner une cellule en utilisant son emplacement.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

Lorsque vous fusionnez des cellules en une seule cellule, les paramètres de mise en forme de la cellule en haut à gauche (dans la plage de cellules) sont appliqués sur la cellule fusionnée, mais lorsque la cellule est défusionnée, toutes les cellules défusionnées conservent leurs paramètres de mise en forme.

{{% /alert %}}
