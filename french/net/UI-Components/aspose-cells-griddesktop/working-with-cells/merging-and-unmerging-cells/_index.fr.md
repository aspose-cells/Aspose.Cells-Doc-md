---
title: Fusion et défusion Cells dans GridDesktop
linktitle: Fusion et défusion Cells
type: docs
weight: 90
url: /fr/net/merging-and-unmerging-cells-griddesktop/
---
{{% alert color="primary" %}} 

Dans cette rubrique, nous aborderons une fonctionnalité utilitaire de fusion et d'annulation de la fusion des cellules d'une feuille de calcul. Cette fonctionnalité est utile dans les cas où nous devons étendre certaines lignes ou colonnes pour améliorer la lisibilité des données.

{{% /alert %}} 
## **Fusion Cells**
Pour fusionner des cellules en une seule grande cellule, veuillez suivre les étapes ci-dessous :

-  Accédez à tout**Feuille de travail**
-  Créer un**Gamme de Cells** être fusionné
- **Fusionner** la plage de cellules dans une grande cellule

 Vous pouvez utiliser**Fusionner** méthode de**Feuille de travail** pour fusionner des cellules. Cependant, une plage de cellules peut être définie en utilisant**CellRange** objet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **Défusion Cells**
Pour dissocier une grande cellule en plusieurs cellules, veuillez suivre les étapes ci-dessous :

-  Accédez à tout**Feuille de travail**
- Accéder à la cellule fusionnée qui doit être dissociée
- **Annuler la fusion** la grande cellule en plusieurs cellules en utilisant l'emplacement de la cellule fusionnée

 Vous pouvez utiliser**Annuler la fusion** méthode de**Feuille de travail** pour dissocier une cellule à l'aide de son emplacement.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

Lorsque vous fusionnez des cellules en une seule cellule, les paramètres de mise en forme de la cellule supérieure gauche (dans la plage de cellules) sont appliqués à la cellule fusionnée, mais lorsque la cellule n'est pas fusionnée, toutes les cellules non fusionnées conservent leurs paramètres de mise en forme.

{{% /alert %}}
