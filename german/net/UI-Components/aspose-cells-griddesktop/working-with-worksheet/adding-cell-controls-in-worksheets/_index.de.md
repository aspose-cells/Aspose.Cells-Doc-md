---
title: Zellsteuerelemente hinzufügen
type: docs
weight: 120
url: /de/net/aspose-cells-griddesktop/add-cell-controls-in-worksheets/
keywords: GridDesktop,add,control,button,checkbox,combobox
description: Dieser Artikel stellt vor, wie man in GridDesktop Steuerelemente in das Arbeitsblatt einfügt.
---

{{% alert color="primary" %}} 

Zellsteuerelemente sind tatsächlich die Steuerelemente, die zu Arbeitsblättern hinzugefügt werden können. Wir nennen sie **Zellsteuerelemente**, weil diese Steuerelemente in Zellen angezeigt werden. In diesem Thema werden wir das Hinzufügen und die Behandlung der Ereignisse dieser Zellsteuerelemente diskutieren.

{{% /alert %}} 
## **Einführung**
Derzeit unterstützt Aspose.Cells.GridDesktop das Hinzufügen von drei Arten von Zellsteuerelementen, die folgende beinhalten:

- **Schaltfläche**
- **Kontrollkästchen**
- **Kombinationsfeld**

All diese Steuerelemente leiten sich von einer abstrakten Klasse, **CellControl**, ab. Jedes Arbeitsblatt enthält eine Sammlung von **Steuerelementen**. Neue Zellensteuerelemente können einfach zu dieser **Steuerelemente**-Sammlung hinzugefügt und vorhandene abgerufen werden.

**WICHTIG:** Wenn Sie Zellensteuerelemente zu allen Zellen einer Spalte hinzufügen möchten, anstatt diese einzeln hinzuzufügen, können Sie sich auf [Verwalten von Zellensteuerelementen in Spalten.](/cells/de/net/aspose-cells-griddesktop/adding-cell-controls-in-worksheets/) beziehen
### **Schaltfläche hinzufügen**
Um mithilfe von Aspose.Cells.GridDesktop eine Schaltfläche in das Arbeitsblatt einzufügen, befolgen Sie bitte die folgenden Schritte:

- Fügen Sie Ihrer **Form** die Aspose.Cells.GridDesktop-Steuerung hinzu
- Greifen Sie auf das gewünschte **Arbeitsblatt** zu
- Fügen Sie die **Schaltfläche** zur **Steuerelemente**-Sammlung des **Arbeitsblatts** hinzu



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


Beim Hinzufügen einer **Schaltfläche** können wir die Zellenposition (wo sie angezeigt werden soll), Breite und Höhe sowie die Beschriftung der Schaltfläche angeben.
#### **Ereignisbehandlung von Schaltflächen**
Wir haben darüber gesprochen, wie man ein **Schaltflächen**-Steuerelement zum **Arbeitsblatt** hinzufügt, aber was ist der Vorteil, nur eine Schaltfläche im Arbeitsblatt zu haben, wenn wir sie nicht verwenden können. Daher ist hier die Notwendigkeit der Ereignisbehandlung der Schaltfläche.

Um das **Klick**-Ereignis des **Schaltflächen**-Steuerelements zu behandeln, stellt Aspose.Cells.GridDesktop das Ereignis **CellButtonClick** bereit, das von den Entwicklern entsprechend ihren Bedürfnissen implementiert werden sollte. Zum Beispiel haben wir einfach eine Nachricht angezeigt, wenn die Schaltfläche angeklickt wird, wie unten gezeigt:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **Festlegen eines Hintergrundbilds für das Schaltflächensteuerelement**
Wir können ein Hintergrundbild/Bild für das Schaltflächensteuerelement mit seiner Beschriftung/Text wie im folgenden Code gezeigt festlegen:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**WICHTIG:** Alle Ereignisse von Zellensteuerelementen enthalten ein **CellControlEventArgs**-Argument, das die Zeilen- und Spaltennummern der Zelle bereitstellt, die das Zellensteuerelement enthält (dessen Ereignis ausgelöst wird).
### **Checkbox hinzufügen**
Um mithilfe von Aspose.Cells.GridDesktop ein Kontrollkästchen in das Arbeitsblatt einzufügen, befolgen Sie bitte die folgenden Schritte:

- Fügen Sie Ihrer **Form** die Aspose.Cells.GridDesktop-Steuerung hinzu
- Greifen Sie auf das gewünschte **Arbeitsblatt** zu
- Fügen Sie das **Kontrollkästchen** zur **Steuerelemente**-Sammlung des **Arbeitsblatts** hinzu



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


Beim Hinzufügen von **CheckBox** können wir den Zellenstandort (wo dieser angezeigt werden soll) und den Zustand des Kontrollkästchens angeben.
#### **Ereignisbehandlung von CheckBox**
Aspose.Cells.GridDesktop bietet das Ereignis **CellCheckedChanged**, das ausgelöst wird, wenn der **Markierungszustand** des Kontrollkästchens geändert wird. Entwickler können dieses Ereignis entsprechend ihren Anforderungen behandeln. Zum Beispiel haben wir gerade eine Meldung angezeigt, um den **Markierungszustand** des Kontrollkästchens im folgenden Code anzuzeigen:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **ComboBox hinzufügen**
Um ein Kombinationsfeld in das Arbeitsblatt mit Aspose.Cells.GridDesktop hinzuzufügen, befolgen Sie bitte die folgenden Schritte:

- Fügen Sie Ihrer **Form** die Aspose.Cells.GridDesktop-Steuerung hinzu
- Greifen Sie auf das gewünschte **Arbeitsblatt** zu
- Erstellen Sie ein Array von Elementen (oder Werten), die dem **ComboBox** hinzugefügt werden sollen
- Fügen Sie den **ComboBox** der **Steuerung**-Sammlung des **Arbeitsblatts** hinzu, indem Sie den Zellenstandort (wo das Kombinationsfeld angezeigt wird) und die Elemente/Werte angeben, die angezeigt werden sollen, wenn das Kombinationsfeld angeklickt wird



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **Ereignisbehandlung von ComboBox**
Aspose.Cells.GridDesktop bietet das Ereignis **CellSelectedIndexChanged**, das ausgelöst wird, wenn der **ausgewählte Index** des Kombinationsfelds geändert wird. Entwickler können dieses Ereignis entsprechend ihren Wünschen behandeln. Zum Beispiel haben wir gerade eine Meldung angezeigt, um das **ausgewählte Element** des Kombinationsfelds anzuzeigen:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
