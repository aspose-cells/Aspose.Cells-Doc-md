---
title: Protéger les cellules
type: docs
weight: 50
url: /fr/net/aspose-cells-gridweb/protect-cells/
keywords: GridWeb, protéger, lecture seule, modifiable
description: Cet article présente comment protéger les cellules dans GridWeb.
---

{{% alert color="primary" %}} 

Ce sujet décrit quelques techniques pour protéger les cellules. L'utilisation de ces techniques permet aux développeurs de restreindre les utilisateurs à la modification de toutes ou d'une plage sélectionnée de cellules dans une feuille de calcul.

{{% /alert %}} 
## **Protéger les cellules**
Aspose.Cells.GridWeb propose quelques techniques différentes pour contrôler le niveau de protection des cellules lorsque le contrôle est en [mode d'édition](/cells/fr/net/aspose-cells-gridweb/enable-different-gridweb-modes/#edit-mode) (mode par défaut). Cela protège les cellules contre toute modification par les utilisateurs finaux.
### **Rendre toutes les cellules en lecture seule**
Pour définir toutes les cellules d'une feuille de calcul en lecture seule, appelez la méthode SetAllCellsReadonly de la feuille de calcul.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Rendre toutes les cellules modifiables**
Pour supprimer la protection de toutes les cellules, appelez la méthode SetAllCellsEditable de la feuille de calcul. Cette méthode a l'effet contraire de la méthode SetAllCellsReadonly.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Rendre les cellules sélectionnées en lecture seule**
Pour protéger uniquement une plage de cellules :

1. Tout d'abord, rendez toutes les cellules modifiables en appelant la méthode SetAllCellsEditable.
1. Spécifiez la plage de cellules à protéger en appelant la méthode SetReadonlyRange de la feuille de calcul. Cette méthode prend le nombre de lignes et de colonnes pour spécifier la plage de cellules.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Rendre les cellules sélectionnées modifiables**
Pour désactiver la protection d'une plage de cellules :

1. Rendez toutes les cellules en lecture seule en appelant la méthode SetAllCellsReadonly.
1. Spécifiez la plage de cellules à rendre modifiables en appelant la méthode SetEditableRange de la feuille de calcul. Cette méthode prend le nombre de lignes et de colonnes pour spécifier la plage de cellules.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
