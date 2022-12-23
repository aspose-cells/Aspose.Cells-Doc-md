---
title: Hinzufügen von Cell-Steuerelementen in Arbeitsblättern
type: docs
weight: 120
url: /de/net/adding-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

 Cell-Steuerelemente sind tatsächlich diejenigen Steuerelemente, die zu Arbeitsblättern hinzugefügt werden können. Wir nennen sie**Cell Kontrollen** da diese Steuerelemente in Zellen angezeigt werden. In diesem Thema besprechen wir das Hinzufügen und Verarbeiten der Ereignisse dieser Zellsteuerelemente.

{{% /alert %}} 
## **Einführung**
Derzeit unterstützt Aspose.Cells.GridDesktop das Hinzufügen von drei Arten von Zellsteuerelementen, darunter die folgenden:

- **Knopf**
- **Kontrollkästchen**
- **Kombinationsfeld**

Alle diese Steuerelemente werden von einer abstrakten Klasse abgeleitet,**CellControl**Jedes Arbeitsblatt enthält eine Sammlung von**Kontrollen**. Über diese können neue Zellensteuerungen hinzugefügt und auf vorhandene zugegriffen werden**Kontrollen**Abholung problemlos.

**WICHTIG:**Wenn Sie allen Zellen einer Spalte Zellsteuerelemente hinzufügen möchten, anstatt sie einzeln hinzuzufügen, können Sie auf verweisen[Verwalten von Cell-Steuerelementen in Spalten.](/cells/de/net/adding-cell-controls-in-worksheets/)
### **Schaltfläche hinzufügen**
Um dem Arbeitsblatt mit Aspose.Cells.GridDesktop eine Schaltfläche hinzuzufügen, führen Sie bitte die folgenden Schritte aus:

- Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
- Greifen Sie beliebig zu**Arbeitsblatt**
- Addieren**Knopf**zum**Kontrollen**Sammlung der**Arbeitsblatt**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


Beim Hinzufügen**Knopf**, können wir die Position der Zelle (wo sie angezeigt werden soll), Breite und Höhe sowie die Beschriftung der Schaltfläche angeben.
#### **Ereignisbehandlung der Schaltfläche**
Wir haben über das Hinzufügen gesprochen**Knopf**Kontrolle an die**Arbeitsblatt**Aber was ist der Vorteil, nur eine Schaltfläche im Arbeitsblatt zu haben, wenn wir sie nicht verwenden können? Hier kommt also die Notwendigkeit der Ereignisbehandlung der Schaltfläche.

Um die zu handhaben**Klicken**Veranstaltung der**Knopf**Steuerung, Aspose.Cells.GridDesktop bietet**CellButtonClick**Ereignis, das von den Entwicklern nach ihren Bedürfnissen implementiert werden sollte. Zum Beispiel haben wir gerade eine Nachricht angezeigt, wenn auf die Schaltfläche geklickt wird, wie unten gezeigt:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **Festlegen eines Hintergrundbilds für das Schaltflächen-Steuerelement**
Wir können Hintergrundbild/Bild für das Schaltflächensteuerelement mit seiner Beschriftung/Text festlegen, wie im folgenden Code gezeigt:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**WICHTIG:**Alle Ereignisse von Zellsteuerungen enthalten a**CellControlEventArgs**Argument, das die Zeilen- und Spaltennummern der Zelle bereitstellt, die das Zellsteuerelement enthält (dessen Ereignis ausgelöst wird).
### **Kontrollkästchen hinzufügen**
Um ein Kontrollkästchen mit Aspose.Cells.GridDesktop in das Arbeitsblatt einzufügen, führen Sie bitte die folgenden Schritte aus:

- Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
- Greifen Sie beliebig zu**Arbeitsblatt**
- Addieren**Kontrollkästchen**zum**Kontrollen**Sammlung der**Arbeitsblatt**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


Beim Hinzufügen**Kontrollkästchen**, können wir die Position der Zelle (wo sie angezeigt werden soll) und den Status des Kontrollkästchens angeben.
#### **Ereignisbehandlung von CheckBox**
Aspose.Cells.GridDesktop bietet**CellCheckedChanged**Ereignis, das ausgelöst wird, wenn die**Geprüft**Status des Kontrollkästchens wird geändert. Entwickler können dieses Ereignis gemäß ihren Anforderungen handhaben. Zum Beispiel haben wir gerade eine Nachricht angezeigt, um die anzuzeigen**Geprüft**Status des Kontrollkästchens im folgenden Code:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **ComboBox hinzufügen**
Um eine Combobox mit Aspose.Cells.GridDesktop zum Arbeitsblatt hinzuzufügen, führen Sie bitte die folgenden Schritte aus:

- Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
- Greifen Sie beliebig zu**Arbeitsblatt**
- Erstellen Sie ein Array von Elementen (oder Werten), denen hinzugefügt wird**Kombinationsfeld**
- Addieren**Kombinationsfeld**zum**Kontrollen**Sammlung der**Arbeitsblatt**durch Angabe der Position der Zelle (wo das Kombinationsfeld angezeigt wird) und der Elemente/Werte, die angezeigt werden, wenn auf das Kombinationsfeld geklickt wird



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **Ereignisbehandlung von ComboBox**
Aspose.Cells.GridDesktop bietet**CellSelectedIndexChanged**Ereignis, das ausgelöst wird, wenn die**Ausgewählter Index**der Combobox geändert. Entwickler können dieses Ereignis nach ihren Wünschen handhaben. Zum Beispiel haben wir gerade eine Nachricht angezeigt, um die anzuzeigen**Ausgewähltes Objekt**der Combobox:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
