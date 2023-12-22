---
title: Copie et déplacement de feuilles de calcul
type: docs
weight: 10
url: /fr/cpp/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

Parfois, vous avez besoin d’un certain nombre de feuilles de calcul avec une mise en forme et des données communes. Par exemple, si vous travaillez avec des budgets trimestriels, vous souhaiterez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonnes, en-têtes de lignes et formules. Il existe un moyen de procéder : en créant une feuille puis en la copiant.

Aspose.Cells prend en charge la copie et le déplacement de feuilles de calcul au sein ou entre des classeurs. Une feuille de calcul, complète avec les données, le formatage, les tableaux, les matrices, les graphiques, les images et autres objets, est copiée avec le plus haut degré de précision.

{{% /alert %}} 
##  **Déplacer ou copier des feuilles à l'aide d'Excel Microsoft**
Voici les étapes impliquées dans la copie et le déplacement de feuilles de calcul dans ou entre des classeurs dans Microsoft Excel.

1. Pour déplacer ou copier des feuilles vers un autre classeur, ouvrez le classeur qui recevra les feuilles.
1. Basculez vers le classeur contenant les feuilles que vous souhaitez déplacer ou copier, puis sélectionnez les feuilles.
1.  Sur le**Modifier** dans le menu, cliquez sur *Déplacer ou copier la feuille**.
1. Dans le**Réserver** boîte de dialogue, cliquez sur le classeur pour recevoir les feuilles.
1. Pour déplacer ou copier les feuilles sélectionnées vers un nouveau classeur, cliquez sur *Nouveau livre**.
1. Dans le**Avant la feuille** , cliquez sur la feuille avant laquelle vous souhaitez insérer les feuilles déplacées ou copiées.
1.  Pour copier les feuilles au lieu de les déplacer, sélectionnez l'icône**Créer une copie** case à cocher.
###  **Copier des feuilles de calcul dans un classeur avec Aspose.Cells**
 Aspose.Cells fournit une méthode surchargée[AddCopy()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/addcopy/)qui est utilisé pour ajouter une feuille de calcul à la collection et copier les données d'une feuille de calcul existante. Une version de la méthode prend l'index de la feuille de calcul source comme paramètre. L'autre version prend le nom de la feuille de calcul source. L'exemple suivant montre comment copier une feuille de calcul existante dans un classeur.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook-new.cpp" >}}
###  **Déplacer des feuilles de calcul dans un classeur**
 Aspose.Cells fournit une méthode[MoveTo()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/moveto/)qui est utilisé pour déplacer une feuille de calcul vers un autre emplacement dans la même feuille de calcul. La méthode prend l’index de la feuille de calcul cible comme paramètre. L'exemple suivant montre comment déplacer une feuille de calcul vers un autre emplacement dans le classeur.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook-new.cpp" >}}
