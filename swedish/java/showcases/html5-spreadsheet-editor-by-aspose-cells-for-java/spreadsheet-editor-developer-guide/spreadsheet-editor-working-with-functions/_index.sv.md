---
title: Kalkylbladsredigerare  Arbeta med funktioner
type: docs
weight: 60
url: /sv/java/spreadsheet-editor-working-with-functions/
---

Innehållsförteckning

- [Formellista](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
  - saveFormulaBarContents
- [Infoga en funktion](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Formellista**
Formellistan är en textruta högst upp på arkivområdet. Den visar formeln för aktuell cell samt låter användaren redigera den.

**Hur fungerar det?**

När en cell är vald synkroniseras formellistan med cellen och formeln visas. Användaren får redigera. När användaren redigerar och trycker på Retur-tangenten körs JavaScript-funktionen **saveFormulaBarContents**
#### **saveFormulaBarContents**
{{< highlight java >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Infoga en funktion**
För att infoga en funktion eller formel:

1. Klicka på en cell för att markera den.
1. Klicka på knappen **Infoga funktion** högst upp.
1. Följ instruktionerna i dialogrutan för **Infoga funktion**.
