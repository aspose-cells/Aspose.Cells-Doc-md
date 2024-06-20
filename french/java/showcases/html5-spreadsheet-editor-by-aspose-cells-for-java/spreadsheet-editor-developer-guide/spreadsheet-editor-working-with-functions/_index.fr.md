---
title: Editeur de feuille de calcul  Travail avec les fonctions
type: docs
weight: 60
url: /fr/java/spreadsheet-editor-working-with-functions/
---

**Table des matières**

- [Barre de formule](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
  - saveFormulaBarContents
- [Insérer une fonction](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Barre de formule**
La barre de formule est une zone de texte en haut de la feuille. Elle affiche la formule de la cellule actuelle et permet à l'utilisateur de la modifier.

**Comment cela fonctionne?**

Lorsqu'une cellule est sélectionnée, la barre de formule est synchronisée avec la cellule et la formule est affichée. L'utilisateur est autorisé à modifier. Lorsque l'utilisateur modifie et appuie sur la touche entrée, la fonction JavaScript **saveFormulaBarContents** est exécutée
#### **saveFormulaBarContents**
{{< highlight java >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Insérer une fonction**
Pour insérer une fonction ou une formule :

1. Cliquez sur une cellule pour la sélectionner.
1. Cliquez sur le bouton **Insérer une fonction** en haut.
1. Suivez les instructions dans la boîte de dialogue **Insérer une fonction**.
