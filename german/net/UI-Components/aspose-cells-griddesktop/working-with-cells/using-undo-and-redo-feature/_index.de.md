---
title: Verwenden Sie die Funktion Rückgängig machen und Wiederholen
type: docs
weight: 120
url: /de/net/aspose-cells-griddesktop/use-undo-and-redo-feature/
keywords: GridDesktop, rückgängig machen, wiederholen
description: Dieser Artikel stellt die Funktion Rückgängig machen und Wiederholen in GridDesktop vor.
---

{{% alert color="primary" %}} 

Die Rückgängig-/Wiederherstellen-Funktion des GridDesktops ist sehr nützlich. Der Name erklärt bereits die Funktionalität, sie ermöglicht es Ihnen, die letzten Aktionen in einem Arbeitsblatt rückgängig zu machen/zu wiederholen. Beispielsweise können versehentlich gelöschte Formeln oder bearbeitete Daten in einer Zelle, die Sie nicht wirklich wollen, durch die Rückgängig- und Wiederherstellen-Operationen des Steuerlements korrigiert werden.

{{% /alert %}} 
## **Durchführen der Rückgängig machen und Wiederholen Operation**
Die folgenden APIs stehen für die Aufgabe zur Verfügung. Die Beschreibung ist bei jeder API angegeben, bitte überprüfen Sie sie.

- **GridDesktop.EnableUndo** - Attribut: Es zeigt an, ob die Rückgängig-Funktion aktiviert ist, der Standardwert ist "false".
- **UndoManager** – Klasse: Wird zur Verwaltung der Rückgängig-/Wiederholungsoperation verwendet.
- **GridDesktop.UndoManager** – Attribut: Hiermit wird die Instanz des Objekts **UndoManager** abgerufen.
- **UndoManager.Undo** – Methode: Führt eine Rückgängig-Operation durch.
- **UndoManager.Redo -** Methode: Führt die Wiederherstellen-Operation durch.
- **UndoManager.ClearStack** – Methode: Löscht den Rückgängig-/Wiederholungs-Stack.
- **UndoManager.UndoStepsCount** – Attribut: Es erhält die Anzahl der verfügbaren rückgängig zu machenden Schritte.
- **UndoManager.RedoStepsCount** – Attribut: Es erhält die Anzahl der verfügbaren wiederherzustellenden Schritte.
- **UndoManager.UndoStackSize** – Attribut: Es erhält/setzt die Größe des Rückgängig-Stacks.
### **Rückgängig machen**
Der folgende Beispielcode zeigt, wie die Rückgängig-Funktion mithilfe der GridDesktop-API implementiert wird.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **Wiederholen**
Der folgende Beispielcode zeigt, wie die Wiederholen-Funktion mithilfe der GridDesktop-API implementiert wird.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

Derzeit bezieht sich die Rückgängig-/Wiederholen-Funktion auf die Änderung im Zellenwert.

{{% /alert %}}
