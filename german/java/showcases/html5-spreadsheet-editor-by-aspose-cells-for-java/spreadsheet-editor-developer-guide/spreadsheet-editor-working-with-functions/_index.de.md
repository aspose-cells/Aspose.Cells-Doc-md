---
title: Tabelleneditor - Arbeiten mit Funktionen
type: docs
weight: 60
url: /de/java/spreadsheet-editor-working-with-functions/
---
**Inhaltsverzeichnis**

- [Formelbar](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
 - SaveFormulaBarContents
- [Fügen Sie eine Funktion ein](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Formelbar**
Die Bearbeitungsleiste ist ein Textfeld über dem Blattbereich. Es zeigt die Formel der aktuellen Zelle an und ermöglicht dem Benutzer, sie zu bearbeiten.

**Wie es funktioniert?**

 Wenn eine Zelle ausgewählt wird, wird die Bearbeitungsleiste mit der Zelle synchronisiert und die Formel angezeigt. Der Benutzer darf editieren. Wenn der Benutzer bearbeitet und die Eingabetaste drückt, wird die JavaScript-Funktion aktiviert**saveFormulaBarContents** wird ausgeführt
#### **saveFormulaBarContents**
{{< highlight "java" >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Fügen Sie eine Funktion ein**
So fügen Sie eine Funktion oder Formel ein:

1. Klicken Sie auf eine Zelle, um sie auszuwählen.
1.  Klicken**Funktion einfügen** Knopf oben.
1.  Befolgen Sie die Anweisungen auf der**Funktion einfügen**Dialog.
