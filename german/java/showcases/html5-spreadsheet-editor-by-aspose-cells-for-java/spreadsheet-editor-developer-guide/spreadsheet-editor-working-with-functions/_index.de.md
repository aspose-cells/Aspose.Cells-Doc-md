---
title: Tabellenkalkulationsprogramm  Arbeiten mit Funktionen
type: docs
weight: 60
url: /de/java/spreadsheet-editor-working-with-functions/
---

**Inhaltsverzeichnis**

- [Formelzeile](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
  - saveFormulaBarContents
- [Funktion einfügen](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Formelzeile**
Die Formel-Leiste ist ein Textfeld oben im Tabellenbereich. Es zeigt die Formel der aktuellen Zelle an und ermöglicht es dem Benutzer, sie zu bearbeiten.

**Wie funktioniert es?**

Wenn eine Zelle ausgewählt ist, wird die Formel-Leiste mit der Zelle synchronisiert und die Formel wird angezeigt. Der Benutzer darf sie bearbeiten. Wenn der Benutzer sie bearbeitet und die Eingabetaste drückt, wird die JavaScript-Funktion **saveFormulaBarContents** ausgeführt.
#### **saveFormulaBarContents**
{{< highlight java >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Funktion einfügen**
Um eine Funktion oder Formel einzufügen:

1. Klicken Sie auf eine Zelle, um sie auszuwählen.
1. Klicken Sie auf die Schaltfläche **Funktion einfügen** oben.
1. Befolgen Sie die Anweisungen im Dialogfeld **Funktion einfügen**.
{{< app/cells/assistant language="java" >}}
