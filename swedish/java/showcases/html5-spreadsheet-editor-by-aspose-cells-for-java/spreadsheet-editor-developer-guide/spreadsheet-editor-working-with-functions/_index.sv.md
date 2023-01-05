---
title: Kalkylarksredigerare - Arbeta med funktioner
type: docs
weight: 60
url: /sv/java/spreadsheet-editor-working-with-functions/
---
**Innehållsförteckning**

- [Formelbar](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
 - sparaFormulaBarContents
- [Infoga en funktion](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Formelbar**
Formelfältet är en textruta ovanpå arkområdet. Den visar formeln för aktuell cell och låter användaren redigera den.

**Hur det fungerar?**

 När en cell är markerad synkroniseras formelfältet med cellen och formeln visas. Användaren får redigera. När användaren redigerar och trycker på enter-tangenten, JavaScript-funktionen**saveFormulaBarContents** avrättas
#### **saveFormulaBarContents**
{{< highlight "java" >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Infoga en funktion**
Så här infogar du en funktion eller formel:

1. Klicka på en cell för att markera den.
1.  Klick**Infoga funktion** knappen på toppen.
1.  Följ instruktionerna på**Infoga funktion** dialog.
