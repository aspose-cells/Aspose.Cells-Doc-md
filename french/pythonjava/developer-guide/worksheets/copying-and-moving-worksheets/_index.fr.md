---
title: Copier et déplacer des feuilles de calcul
type: docs
weight: 20
url: /fr/python-java/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

Parfois, vous avez besoin d'un certain nombre de feuilles de calcul avec un formatage et des données communs. Par exemple, si vous travaillez avec des budgets trimestriels, vous souhaiterez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonne, en-têtes de ligne et formules. Il existe un moyen de le faire : en créant une feuille, puis en la copiant.

Aspose.Cells prend en charge la copie et le déplacement de feuilles de calcul dans ou entre des classeurs. Les feuilles de calcul, complètes avec les données, le formatage, les tableaux, les matrices, les graphiques, les images et d'autres objets, sont copiées avec le plus haut degré de précision.

{{% /alert %}} 
## **Déplacer ou copier des feuilles à l'aide d'Excel Microsoft**
Voici les étapes impliquées dans la copie et le déplacement de feuilles de calcul dans ou entre des classeurs.

1. Ouvrez le classeur qui recevra les feuilles.
1. Basculez vers le classeur contenant les feuilles que vous souhaitez déplacer ou copier, puis sélectionnez les feuilles.
1. Sur le**Éditer**menu, cliquez sur**Déplacer ou copier une feuille**.
1. Dans la zone À réserver, cliquez sur le classeur pour recevoir les feuilles.
1. Pour déplacer ou copier les feuilles sélectionnées dans un nouveau classeur, cliquez sur**nouveau livre**.
1. Dans le**Avant feuille**, cliquez sur la feuille devant laquelle vous souhaitez insérer les feuilles déplacées ou copiées.
1. Pour copier les feuilles au lieu de les déplacer, sélectionnez le**Créer une copie**case à cocher.
### **Copier des feuilles de calcul dans un classeur**
Aspose.Cells fournit une surcharge[WorksheetCollection.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\)) méthode utilisée pour copier une feuille de calcul existante. Une version de la méthode prend l'index de la feuille de calcul source comme paramètre. L'autre version prend le nom de la feuille de calcul source.

L'exemple suivant montre comment copier une feuille de calcul existante dans un classeur.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **Copier des feuilles de calcul entre des classeurs**
Aspose.Cells fournit le[Feuille de calcul.copie()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\)) méthode utilisée pour copier des feuilles de calcul dans d'autres classeurs. La méthode prend l'objet feuille de calcul source comme paramètre.

L'exemple suivant montre comment copier une feuille de calcul d'un classeur vers un autre classeur.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **Déplacer des feuilles de calcul dans le classeur**
Aspose.Cells fournit le[Feuille de calcul.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\)) méthode utilisée pour déplacer une feuille de calcul vers un autre emplacement dans la même feuille de calcul.

L'exemple suivant montre comment déplacer une feuille de calcul vers un autre emplacement dans le classeur.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
