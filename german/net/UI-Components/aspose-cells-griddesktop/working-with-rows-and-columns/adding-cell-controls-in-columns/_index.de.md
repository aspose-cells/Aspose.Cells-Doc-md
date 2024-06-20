---
title: Hinzufügen von Zellensteuerelementen in Spalten
type: docs
weight: 90
url: /de/net/aspose-cells-griddesktop/add-cell-controls-in-columns/
keywords: GridDesktop,add,control,controls
description: Dieser Artikel stellt vor, wie man ein Steuerelement in einer Spalte in GridDesktop hinzufügt.
---

{{% alert color="primary" %}} 

In unseren späteren Diskussionen haben wir darüber gesprochen, wie man Zellensteuerelemente in Arbeitsblättern hinzufügt und verwaltet. Aber unter Verwendung dieser Ansätze können wir nur Zellensteuerelemente einzeln zu einzelnen Zellen hinzufügen. Was ist, wenn jemand Zellensteuerelemente zu allen Zellen einer oder mehrerer Spalten hinzufügen möchte? In solchen Fällen bietet Aspose.Cells.GridDesktop die Möglichkeit, Zellensteuerelemente pro Spalte hinzuzufügen. Das bedeutet, dass Entwickler lediglich eine gewünschte Spalte auswählen und ein beliebiges Zellensteuerelement angeben können. Das angegebene Zellensteuerelement wird allen Zellen der angegebenen Spalte hinzugefügt. Schauen wir uns an, wie wir diese Funktion nutzen können.

{{% /alert %}} 
## **Einführung**
Derzeit unterstützt Aspose.Cells.GridDesktop das Hinzufügen von drei Arten von Zellsteuerelementen, die folgende beinhalten:

- **Schaltfläche**
- **Kontrollkästchen**
- **Kombinationsfeld**

Alle diese Steuerelemente sind von einer abstrakten Klasse, **Zellensteuerung**, abgeleitet.

**WICHTIG:** Wenn Sie Zellensteuerelemente zu einer einzelnen Zelle anstelle der ganzen Spalte hinzufügen möchten, können Sie sich auf [Hinzufügen von Zellensteuerelementen in Arbeitsblättern](/cells/de/net/adding-cell-controls-in-worksheets/) beziehen.
### **Schaltfläche hinzufügen**
Um Schaltflächen in einer Spalte mit Aspose.Cells.GridDesktop hinzuzufügen, befolgen Sie bitte die folgenden Schritte:

- Fügen Sie das Steuerelement Aspose.Cells.GridDesktop zu Ihrem **Formular** hinzu
- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Fügen Sie eine **Schaltfläche** in eine beliebige **Spalte** des **Arbeitsblatts** hinzu

**HINWEIS:** Beim Hinzufügen einer **Schaltfläche** können wir die Breite, Höhe und Beschriftung der Schaltfläche angeben.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


Der obige Codeabschnitt fügt Schaltflächen zu allen Zellen der angegebenen Spalte hinzu. Wenn eine Zelle dieser bestimmten Spalte ausgewählt wird, wird eine Schaltfläche sichtbar. Weitere Informationen zur Ereignisbehandlung von Schaltflächen finden Sie unter [Ereignisbehandlung eines Schaltflächen-Steuerelements.](/cells/de/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **Checkbox hinzufügen**
Um Kontrollkästchen in eine Spalte mit Aspose.Cells.GridDesktop hinzuzufügen, befolgen Sie bitte die folgenden Schritte:

- Fügen Sie das Steuerelement Aspose.Cells.GridDesktop zu Ihrem **Formular** hinzu
- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Fügen Sie ein **CheckBox** in eine bestimmte **Spalte** des **Arbeitsblatts** hinzu

**HINWEIS:** Beim Hinzufügen eines **CheckBox** können wir auch den Zustand des Kontrollkästchens angeben.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


Der obige Code-Schnipsel fügt Kontrollkästchen zu allen Zellen der angegebenen Spalte hinzu. Für weitere Informationen zur Ereignisbehandlung von Kontrollkästchen siehe [Ereignisbehandlung eines CheckBox-Steuerung.](/cells/de/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **ComboBox hinzufügen**
Um Kombinationsfelder in eine Spalte mit Aspose.Cells.GridDesktop hinzuzufügen, folgen Sie bitte den folgenden Schritten:

- Fügen Sie das Steuerelement Aspose.Cells.GridDesktop zu Ihrem **Formular** hinzu
- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Erstellen Sie ein Array von Elementen (oder Werten), die dem **ComboBox** hinzugefügt werden sollen
- Fügen Sie dem **ComboBox** (mit Elementen oder Werten) in eine bestimmte **Spalte** des **Arbeitsblatts** hinzu



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


Der obige Code-Schnipsel fügt Kombinationsfelder zu allen Zellen der angegebenen Spalte hinzu. Wann immer eine Zelle dieser spezifischen Spalte ausgewählt wird, wird ein Kombinationsfeld angezeigt. Für weitere Informationen zur Ereignisbehandlung von Kombinationsfeldern siehe [Ereignisbehandlung einer ComboBox-Steuerung.](/cells/de/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
