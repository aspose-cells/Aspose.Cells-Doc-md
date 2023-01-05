---
title: Éditeur de feuille de calcul - Utilisation des fonctions
type: docs
weight: 60
url: /fr/java/spreadsheet-editor-working-with-functions/
---
**Table des matières**

- [Barre de formule](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
 - enregistrer le contenu de la barre de formule
- [Insérer une fonction](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Barre de formule**
La barre de formule est une zone de texte située en haut de la zone de la feuille. Il affiche la formule de la cellule actuelle et permet à l'utilisateur de la modifier.

**Comment ça fonctionne?**

 Lorsqu'une cellule est sélectionnée, la barre de formule est synchronisée avec la cellule et la formule s'affiche. L'utilisateur est autorisé à modifier. Lorsque l'utilisateur modifie et appuie sur la touche Entrée, la fonction JavaScript**saveFormulaBarContents** est exécuté
#### **saveFormulaBarContents**
{{< highlight "java" >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Insérer une fonction**
Pour insérer une fonction ou une formule :

1. Cliquez sur une cellule pour la sélectionner.
1.  Cliquez sur**Insérer une fonction** bouton sur le dessus.
1.  Suivez les instructions sur le**Insérer une fonction** dialogue.
