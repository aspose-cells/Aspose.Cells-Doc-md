---
title: Editor di fogli di calcolo - Lavorare con le funzioni
type: docs
weight: 60
url: /it/java/spreadsheet-editor-working-with-functions/
---
**Sommario**

- [Barra della formula](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
 - saveFormulaBarContents
- [Inserisci una funzione](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Barra della formula**
La barra della formula è una casella di testo sopra l'area del foglio. Visualizza la formula della cella corrente e consente all'utente di modificarla.

**Come funziona?**

 Quando si seleziona una cella, la barra della formula viene sincronizzata con la cella e viene visualizzata la formula. L'utente è autorizzato a modificare. Quando l'utente modifica e preme il tasto Invio, la funzione JavaScript**saveFormulaBarContents** viene eseguito
#### **saveFormulaBarContents**
{{< highlight "java" >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Inserisci una funzione**
Per inserire una funzione o una formula:

1. Fare clic su una cella per selezionarla.
1.  Clic**Inserisci funzione** pulsante in alto.
1.  Seguire le istruzioni sul**Inserisci funzione**dialogo.
