---
title: Editor di Fogli di Calcolo  Lavorare con le Funzioni
type: docs
weight: 60
url: /it/java/spreadsheet-editor-working-with-functions/
---

**Tabella dei contenuti**

- [Barra delle Formule](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
  - saveFormulaBarContents
- [Inserisci una Funzione](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Barra delle Formule**
La barra delle formule è una casella di testo in cima all'area del foglio. Mostra la formula della cella corrente e consente all'utente di modificarla.

**Come funziona?**

Quando una cella è selezionata, la barra delle formule si sincronizza con la cella e visualizza la formula. All'utente è consentito modificare. Quando l'utente modifica e preme il tasto Invio, la funzione JavaScript **salvaContenutiBarraFormule** viene eseguita
#### **saveFormulaBarContents**
{{< highlight java >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Inserisci una Funzione**
Per inserire una funzione o formula:

1. Fare clic su una cella per selezionarla.
1. Fare clic sul pulsante **Inserisci Funzione** in alto.
1. Seguire le istruzioni sulla finestra di dialogo **Inserisci Funzione**.
