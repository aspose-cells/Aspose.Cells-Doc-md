---
title: Hinzufügen von Cell-Steuerelementen in Spalten
type: docs
weight: 90
url: /de/net/adding-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

In unseren späteren Diskussionen haben wir über das Hinzufügen und Verwalten von Zellsteuerelementen in Arbeitsblättern gesprochen. Aber mit diesen Ansätzen können wir Zellensteuerungen einzeln zu einzelnen Zellen hinzufügen. Was ist, wenn jemand Zellsteuerelemente zu allen Zellen einer oder mehrerer Spalten hinzufügen möchte? Um in solchen Fällen den Aufwand der Entwickler zu verringern, bietet Aspose.Cells.GridDesktop die Funktion, Zellsteuerelemente pro Spalte hinzuzufügen. Das bedeutet, dass Entwickler nur eine gewünschte Spalte auswählen und ein beliebiges Zellsteuerelement angeben können. Das angegebene Zellensteuerelement wird allen Zellen der angegebenen Spalte hinzugefügt. Mal sehen, wie wir diese Funktion nutzen können.

{{% /alert %}} 
## **Einführung**
Derzeit unterstützt Aspose.Cells.GridDesktop das Hinzufügen von drei Arten von Zellsteuerelementen, darunter die folgenden:

- **Knopf**
- **Kontrollkästchen**
- **Kombinationsfeld**

 Alle diese Steuerelemente werden von einer abstrakten Klasse abgeleitet,**CellControl**.

**WICHTIG:** Wenn Sie Zellsteuerelemente zu einer einzelnen Zelle anstelle der gesamten Spalte hinzufügen möchten, können Sie auf verweisen[Hinzufügen von Cell-Steuerelementen in Arbeitsblättern.](/cells/de/net/adding-cell-controls-in-worksheets/)
### **Schaltfläche hinzufügen**
Um Schaltflächen mit Aspose.Cells.GridDesktop zu einer Spalte hinzuzufügen, führen Sie bitte die folgenden Schritte aus:

-  Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Addieren**Knopf** zu allen angegebenen**Spalte** des**Arbeitsblatt**

**HINWEIS:** Beim Hinzufügen**Knopf**, können wir die Breite, Höhe und Beschriftung der Schaltfläche angeben.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


 Das obige Code-Snippet fügt Schaltflächen zu allen Zellen der angegebenen Spalte hinzu. Immer wenn eine Zelle dieser bestimmten Spalte ausgewählt wird, wird eine Schaltfläche sichtbar. Weitere Informationen zur Ereignisbehandlung von Schaltflächen finden Sie in der[Ereignisbehandlung eines Button Controls.](/cells/de/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **Kontrollkästchen hinzufügen**
Um mit Aspose.Cells.GridDesktop Kontrollkästchen in eine Spalte einzufügen, führen Sie bitte die folgenden Schritte aus:

-  Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Addieren**Kontrollkästchen** zu allen angegebenen**Spalte** des**Arbeitsblatt**

**HINWEIS:** Beim Hinzufügen**Kontrollkästchen**, können wir auch den Status des Kontrollkästchens angeben.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


 Das obige Code-Snippet fügt allen Zellen der angegebenen Spalte Kontrollkästchen hinzu. Weitere Informationen zur Ereignisbehandlung von Checkboxen finden Sie in der[Ereignisbehandlung eines CheckBox-Steuerelements.](/cells/de/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **ComboBox hinzufügen**
Um Comboboxen mit Aspose.Cells.GridDesktop zu einer Spalte hinzuzufügen, führen Sie bitte die folgenden Schritte aus:

-  Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Erstellen Sie ein Array von Elementen (oder Werten), denen hinzugefügt wird**Kombinationsfeld**
-  Addieren**Kombinationsfeld** (mit Elementen oder Werten) zu einem beliebigen angegebenen**Spalte** des**Arbeitsblatt**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


 Das obige Code-Snippet fügt Comboboxen zu allen Zellen der angegebenen Spalte hinzu. Immer wenn eine Zelle dieser bestimmten Spalte ausgewählt wird, wird ein Kombinationsfeld sichtbar. Weitere Informationen zur Ereignisbehandlung von Comboboxen finden Sie in der[Ereignisbehandlung eines ComboBox-Steuerelements.](/cells/de/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
