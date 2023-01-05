---
title: Verwenden der Rückgängig- und Wiederherstellen-Funktion
type: docs
weight: 120
url: /de/net/using-undo-and-redo-feature/
---
{{% alert color="primary" %}} 

Die Undo/Redo-Funktion von GridDesktop ist sehr nützlich. Der Name erklärt seine Funktionalität selbst, es ermöglicht Ihnen, die letzte(n) Aktion(en) in einem Arbeitsblatt rückgängig zu machen/zu wiederholen. Wenn beispielsweise eine Formel versehentlich gelöscht wird oder Sie Daten in einer Zelle bearbeiten, die Sie eigentlich nicht möchten, können diese Aktionen mit den vom Steuerelement bereitgestellten Operationen Rückgängig und Wiederherstellen korrigiert werden.

{{% /alert %}} 
## **Ausführen von Undo- und Redo-Operationen**
Die folgenden APIs sind für die Aufgabe verfügbar. Die Beschreibung liegt jeder API bei, bitte überprüfen Sie diese.

- **GridDesktop.EnableUndo** - Attribut: Gibt an, ob die Undo-Funktion aktiviert ist, der Standardwert ist "false".
- **Rückgängig-Manager** – Klasse: Wird verwendet, um die Undo/Redo-Operation zu verwalten.
- **GridDesktop.UndoManager** – Attribut: Es erhält die Instanz von**Rückgängig-Manager** Objekt.
- **UndoManager.Undo** – Methode: Führt eine Undo-Operation durch.
- **UndoManager.Redo -** Methode: Führt die Redo-Operation durch.
- **UndoManager.ClearStack** – Methode: Löscht den Undo/Redo-Stack.
- **UndoManager.UndoStepsCount** – Attribut: Es erhält die Anzahl der aktuell verfügbaren Undo-Schritte.
- **UndoManager.RedoStepsCount** – Attribut: Es erhält die Anzahl der aktuell verfügbaren Redo-Schritte.
- **UndoManager.UndoStackSize** – Attribut: Es erhält/setzt die Undo-Stack-Größe.
### **Rückgängig machen**
Der folgende Beispielcode zeigt, wie der Undo-Vorgang mithilfe von GridDesktop API implementiert wird.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **Wiederholen**
Der folgende Beispielcode zeigt, wie der Redo-Vorgang mithilfe von GridDesktop API implementiert wird.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

Derzeit bezieht sich die Operation Rückgängig/Wiederherstellen auf die Änderung eines Zellenwerts.

{{% /alert %}}
