---
title: Copier et Déplacer des Feuilles de calcul
type: docs
weight: 20
url: /fr/python-java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

Parfois, vous avez besoin d'un certain nombre de feuilles de calcul avec une mise en forme et des données communes. Par exemple, si vous travaillez avec des budgets trimestriels, vous voudrez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonne, en-têtes de ligne et formules. Il y a un moyen de le faire : en créant une feuille, puis en la copiant.

Aspose.Cells prend en charge la copie et le déplacement de feuilles dans ou entre des classeurs. Les feuilles, avec des données, une mise en forme, des tableaux, des matrices, des graphiques, des images et d'autres objets, sont copiées avec le plus grand degré de précision.

{{% /alert %}} 
## **Déplacement ou Copie de feuilles à l'aide de Microsoft Excel**
Les étapes suivantes sont impliquées dans la copie et le déplacement de feuilles dans ou entre des classeurs.

1. Ouvrez le classeur qui recevra les feuilles.
1. Basculez vers le classeur contenant les feuilles que vous souhaitez déplacer ou copier, puis sélectionnez les feuilles.
1. Dans le menu **Édition**, cliquez sur **Déplacer ou Copier la feuille**.
1. Dans la zone Vers le classeur, cliquez sur le classeur pour recevoir les feuilles.
1. Pour déplacer ou copier les feuilles sélectionnées vers un nouveau classeur, cliquez sur **nouveau classeur**.
1. Dans la case **Avant la feuille**, cliquez sur la feuille avant laquelle vous souhaitez insérer les feuilles déplacées ou copiées.
1. Pour copier les feuilles au lieu de les déplacer, sélectionnez la case à cocher **Créer une copie**.
### **Copier des feuilles de calcul dans un classeur**
Aspose.Cells fournit une méthode [WorksheetCollection.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\)) surchargée qui est utilisée pour copier une feuille de calcul existante. Une version de la méthode prend l'index de la feuille de calcul source en tant que paramètre. L'autre version prend le nom de la feuille de calcul source.

L'exemple suivant montre comment copier une feuille existante dans un classeur.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **Copier des feuilles de calcul entre des classeurs**
Aspose.Cells fournit la méthode [Worksheet.copy()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\)) utilisée pour copier des feuilles de calcul vers d'autres classeurs. La méthode prend l'objet feuille de calcul source en tant que paramètre.

L'exemple suivant montre comment copier une feuille de calcul d'un classeur à un autre.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **Déplacer des feuilles de calcul dans un classeur**
Aspose.Cells fournit la méthode [Worksheet.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\)) utilisée pour déplacer une feuille de calcul vers un autre emplacement dans la même feuille de calcul.

L'exemple suivant montre comment déplacer une feuille de calcul vers un autre emplacement dans le classeur.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
