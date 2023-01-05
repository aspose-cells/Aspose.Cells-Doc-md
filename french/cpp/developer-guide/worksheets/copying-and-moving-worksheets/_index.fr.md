---
title: Copier et déplacer des feuilles de calcul
type: docs
weight: 10
url: /fr/cpp/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

Parfois, vous avez besoin d'un certain nombre de feuilles de calcul avec un formatage et des données communs. Par exemple, si vous travaillez avec des budgets trimestriels, vous souhaiterez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonne, en-têtes de ligne et formules. Il existe un moyen de le faire : en créant une feuille, puis en la copiant.

Aspose.Cells prend en charge la copie et le déplacement de feuilles de calcul dans ou entre des classeurs. Une feuille de calcul, complète avec des données, une mise en forme, des tableaux, des matrices, des graphiques, des images et d'autres objets, est copiée avec le plus haut degré de précision.

{{% /alert %}} 
## **Déplacer ou copier des feuilles à l'aide d'Excel Microsoft**
Voici les étapes à suivre pour copier et déplacer des feuilles de calcul dans ou entre des classeurs dans Microsoft Excel.

1. Pour déplacer ou copier des feuilles vers un autre classeur, ouvrez le classeur qui recevra les feuilles.
1. Basculez vers le classeur contenant les feuilles que vous souhaitez déplacer ou copier, puis sélectionnez les feuilles.
1.  Sur le**Éditer** menu, cliquez sur**Déplacer ou copier une feuille**.
1.  Dans le**Réserver** boîte de dialogue, cliquez sur le classeur pour recevoir les feuilles.
1.  Pour déplacer ou copier les feuilles sélectionnées dans un nouveau classeur, cliquez sur**Nouveau livre**.
1.  Dans le**Avant feuille** , cliquez sur la feuille devant laquelle vous souhaitez insérer les feuilles déplacées ou copiées.
1.  Pour copier les feuilles au lieu de les déplacer, sélectionnez le**Créer une copie** case à cocher.
### **Copier des feuilles de calcul dans un classeur avec Aspose.Cells**
 Aspose.Cells fournit une méthode surchargée[AjouterCopie()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa1e73c54ea19bb7aa0f9f197c2baa5ba)qui est utilisé pour ajouter une feuille de calcul à la collection et copier des données à partir d'une feuille de calcul existante. Une version de la méthode prend l'index de la feuille de calcul source comme paramètre. L'autre version prend le nom de la feuille de calcul source. L'exemple suivant montre comment copier une feuille de calcul existante dans un classeur.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook.cpp" >}}
### **Déplacer des feuilles de calcul dans le classeur**
 Aspose.Cells fournit une méthode[Déménager à()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a240bf1d3d52ea8c8bfd54ffa320921b7)qui est utilisé pour déplacer une feuille de calcul vers un autre emplacement dans la même feuille de calcul. La méthode prend l'index de la feuille de calcul cible comme paramètre. L'exemple suivant montre comment déplacer une feuille de calcul vers un autre emplacement dans le classeur.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook.cpp" >}}
