---
title: Protéger Cells
type: docs
weight: 50
url: /fr/net/protect-cells/
---
{{% alert color="primary" %}} 

Cette rubrique décrit quelques techniques de protection des cellules. L'utilisation de ces techniques permet aux développeurs d'empêcher les utilisateurs de modifier toutes les cellules ou une plage sélectionnée de cellules dans une feuille de calcul.

{{% /alert %}} 
## **Protéger Cells**
 Aspose.Cells.GridWeb fournit quelques techniques différentes pour contrôler le niveau de protection sur les cellules lorsque le contrôle est en[Mode édition](/cells/fr/net/enable-different-gridweb-modes/#edit-mode) (le mode par défaut). Cela empêche les cellules d'être modifiées par les utilisateurs finaux.
### **Rendre tous les Cells en lecture seule**
Pour définir toutes les cellules d'une feuille de calcul en lecture seule, appelez la méthode SetAllCellsReadonly de la feuille de calcul.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Rendre tous Cells modifiables**
Pour supprimer la protection de toutes les cellules, appelez la méthode SetAllCellsEditable de la feuille de calcul. Cette méthode a l'effet inverse de la méthode SetAllCellsReadonly.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Rendre la sélection Cells en lecture seule**
Pour protéger uniquement une plage de cellules :

1. Rendez d'abord toutes les cellules modifiables en appelant la méthode SetAllCellsEditable.
1. Spécifiez la plage de cellules à protéger en appelant la méthode SetReadonlyRange de la feuille de calcul. Cette méthode utilise le nombre de lignes et de colonnes pour spécifier la plage de cellules.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Rendre la sélection Cells modifiable**
Pour déprotéger une plage de cellules :

1. Rendez toutes les cellules en lecture seule en appelant la méthode SetAllCellsReadonly.
1. Spécifiez la plage de cellules à modifier en appelant la méthode SetEditableRange de la feuille de calcul. Cette méthode utilise le nombre de lignes et de colonnes pour spécifier la plage de cellules.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
