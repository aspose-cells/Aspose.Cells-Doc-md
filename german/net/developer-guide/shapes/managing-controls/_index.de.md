---
title: Steuerelemente verwalten
type: docs
weight: 150
url: /de/net/managing-controls/
---

## **Einführung**

Entwickler können verschiedene Zeichenobjekte wie Textfelder, Kontrollkästchen, Optionsfelder, Kombinationsfelder, Beschriftungen, Schaltflächen, Linien, Rechtecke, Bögen, Ovale, Spinner, Bildlaufleisten, Gruppenfelder usw. hinzufügen. Aspose.Cells bietet den Aspose.Cells.Drawing-Namespace, der alle Zeichenobjekte enthält. Es gibt jedoch einige Zeichenobjekte oder Formen, die noch nicht unterstützt werden. Erstellen Sie diese Zeichenobjekte in einem Designer-Arbeitsblatt mit Microsoft Excel und importieren Sie das Designer-Arbeitsblatt dann in Aspose.Cells. Aspose.Cells ermöglicht es Ihnen, diese Zeichenobjekte aus einem Designer-Arbeitsblatt zu laden und in eine erstellte Datei zu schreiben.

## **Hinzufügen einer Textfeldsteuerung zu einem Arbeitsblatt**

Eine Möglichkeit, wichtige Informationen in einem Bericht zu betonen, besteht darin, ein Textfeld zu verwenden. Fügen Sie beispielsweise Text hinzu, um den Firmennamen hervorzuheben oder die geografische Region mit den höchsten Umsätzen anzuzeigen usw. Aspose.Cells bietet die [**TextBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection)-Klasse, die verwendet wird, um ein neues Textfeld zur Sammlung hinzuzufügen. Es gibt eine weitere Klasse, [**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox), die ein Textfeld zum Definieren aller Arten von Einstellungen repräsentiert. Sie hat einige wichtige Elemente:

- Die [**TextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe)-Eigenschaft gibt ein [**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe)-Objekt zurück, das verwendet wird, um den Inhalt des Textfelds anzupassen.
- Die [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)-Eigenschaft gibt den Platzierungstyp an.
- Die [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font)-Eigenschaft gibt die Schriftattributen an.
- Die Methode [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) fügt dem Textfeld einen Hyperlink hinzu.
- Die [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)-Eigenschaft gibt ein [**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat)-Objekt zurück, das verwendet wird, um das Füllformat für das Textfeld festzulegen.
- Die Eigenschaft [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) gibt normalerweise das [**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat)-Objekt zurück, das zur Formatierung und Gewichtung der Textfeldlinie verwendet wird.
- Die [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)-Eigenschaft gibt den Eingabetext für das Textfeld an.

Im folgenden Beispiel werden zwei Textfelder im ersten Arbeitsblatt der Arbeitsmappe erstellt. Das erste Textfeld ist gut ausgestattet mit verschiedenen Formatierungseinstellungen. Das zweite ist einfach gehalten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **Bearbeiten von Textfeldsteuerungen in Designer-Arbeitsmappen**

Aspose.Cells ermöglicht es Ihnen auch, auf Textfelder in den Designer-Arbeitsblättern zuzugreifen und diese zu manipulieren. Verwenden Sie die Eigenschaft [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes), um die Textfelder-Sammlung im Blatt zu erhalten.

Im folgenden Beispiel wird die Microsoft Excel-Datei verwendet, die wir im obigen Beispiel erstellt haben. Es ruft die Textzeichenfolgen der beiden Textfelder ab und ändert den Text des zweiten Textfelds, um die Datei zu speichern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **Hinzufügen einer Kontrollkästchensteuerung zu einem Arbeitsblatt**

Kontrollkästen sind praktisch, wenn Sie dem Benutzer eine Auswahl zwischen zwei Optionen ermöglichen möchten, beispielsweise true oder false; Ja oder Nein. Aspose.Cells ermöglicht es Ihnen, Kontrollkästchen in Arbeitsblättern zu verwenden. Beispielsweise könnten Sie ein Finanzprognose-Arbeitsblatt entwickelt haben, in dem Sie entweder eine bestimmte Akquisition berücksichtigen können oder nicht. In diesem Fall möchten Sie möglicherweise ein Kontrollkästchen oben auf dem Arbeitsblatt platzieren. Sie können dann den Status dieses Kontrollkästchens mit einer anderen Zelle verknüpfen, sodass, wenn das Kontrollkästchen ausgewählt ist, der Wert der Zelle wahr ist; wenn es nicht ausgewählt ist, ist der Wert der Zelle falsch.

### **Verwendung von Microsoft Excel**

Um ein Kontrollkästchen-Steuerelement in Ihr Arbeitsblatt zu platzieren, befolgen Sie diese Schritte:

1. Stellen Sie sicher, dass die Formen-Symbolleiste angezeigt wird.
1. Klicken Sie auf das **Kontrollkästchen**-Symbol in der Symbolleiste Formulare.
1. Klicken und ziehen Sie im Arbeitsblattbereich, um das Rechteck zu definieren, das das Kontrollkästchen und das Label neben dem Kontrollkästchen enthält.
1. Sobald das Kontrollkästchen platziert ist, bewegen Sie den Mauszeiger in den Etikettenbereich und ändern Sie das Etikett.
1. Geben Sie im Feld **Zellenbezug** die Adresse der Zelle an, mit der dieses Kontrollkästchen verknüpft sein soll.
1. Klicken Sie auf **OK**.

### **Verwendung von Aspose.Cells**

Aspose.Cells bietet die Klasse [**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection), die verwendet wird, um ein neues Kontrollkästchen der Sammlung hinzuzufügen. Es gibt eine weitere Klasse, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox), die ein Kontrollkästchen darstellt. Es hat einige wichtige Elemente:

- Die Eigenschaft [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) gibt eine Zelle an, die mit dem Kontrollkästchen verknüpft ist.
- Die Eigenschaft [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) gibt den Textstring an, der mit dem Kontrollkästchen verbunden ist. Es ist die Beschriftung des Kontrollkästchens.
- Die Eigenschaft [**Value**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) gibt an, ob das Kontrollkästchen aktiviert ist oder nicht.

Das folgende Beispiel zeigt, wie ein Kontrollkästchen dem Arbeitsblatt hinzugefügt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **Radio Button Steuerelement dem Arbeitsblatt hinzufügen**

Ein Optionsfeld oder Kontrollkästchen ist ein Steuerelement in Form eines runden Kastens. Der Benutzer trifft seine Entscheidung, indem er den runden Kasten auswählt. Ein Optionsfeld ist normalerweise, wenn nicht immer, von anderen begleitet. Solche Optionsfelder erscheinen und verhalten sich als Gruppe. Der Benutzer entscheidet, welcher Schaltfläche gültig ist, indem er nur eine davon auswählt. Wenn der Benutzer eine Schaltfläche anklickt, wird sie gefüllt. Wenn eine Schaltfläche in der Gruppe ausgewählt ist, sind die Schaltflächen derselben Gruppe leer.

### **Verwendung von Microsoft Excel**

So platzieren Sie ein Optionsfeldsteuerelement in Ihrem Arbeitsblatt:

1. Stellen Sie sicher, dass die **Formulare**-Symbolleiste angezeigt wird.
1. Klicken Sie auf die Schaltfläche **Optionsfeld**.
1. Klicken und ziehen Sie im Arbeitsblatt, um das Rechteck zu definieren, in dem das Optionsfeld und das daneben stehende Etikett platziert werden sollen.
1. Sobald das Optionsfeld im Arbeitsblatt platziert ist, bewegen Sie den Mauszeiger in den Etikettenbereich und ändern das Etikett.
1. Geben Sie im Feld **Zellverknüpfung** die Adresse der Zelle an, mit der dieses Optionsfeld verbunden werden soll.
1. Klicken Sie auf **OK**.

### **Verwendung von Aspose.Cells**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Klasse bietet eine Methode mit dem Namen [**AddRadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton), die verwendet wird, um ein Optionsfeldsteuerelement zu einem Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton)-Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) stellt ein Optionsfeld dar. Sie hat einige wichtige Elemente:

- Die Eigenschaft [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) gibt eine Zelle an, die mit dem Optionsfeld verknüpft ist.
- Die Eigenschaft [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) gibt den Textstring an, der mit dem Optionsfeld verbunden ist. Es ist die Beschriftung des Optionsfelds.
- Die Eigenschaft [**IsChecked**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) gibt an, ob das Optionsfeld aktiviert ist oder nicht.
- Die Eigenschaft [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) gibt das Füllformat des Optionsfeldes an.
- Die Eigenschaft [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) gibt die Linienformatstile des Optionsfeldes an.

Das folgende Beispiel zeigt, wie Radio-Buttons einem Arbeitsblatt hinzugefügt werden. Das Beispiel fügt drei Radio-Buttons hinzu, die Altersgruppen repräsentieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

## **Hinzufügen eines Kombinationsfeldsteuerelements zu einem Arbeitsblatt**

Um die Dateneingabe zu vereinfachen oder die Eingabe auf bestimmte von Ihnen definierte Elemente zu beschränken, können Sie eine Kombinationsfeld oder Dropdown-Liste der gültigen Eingaben erstellen, die aus Zellen an anderer Stelle im Arbeitsblatt zusammengestellt werden. Wenn Sie für eine Zelle eine Dropdown-Liste erstellen, wird ein Pfeil neben dieser Zelle angezeigt. Um Informationen in diese Zelle einzugeben, klicken Sie auf den Pfeil und dann auf den Eintrag, den Sie möchten.

### **Verwendung von Microsoft Excel**

Um ein Kombinationsfeld-Steuerelement in Ihrem Arbeitsblatt zu platzieren, befolgen Sie diese Schritte:

1. Stellen Sie sicher, dass die **Formulare**-Symbolleiste angezeigt wird.
1. Klicken Sie auf das **Kombinationsfeld**-Werkzeug.
1. Klicken und ziehen Sie im Arbeitsblattbereich, um das Rechteck zu definieren, das das Kombinationsfeld halten wird.
1. Sobald das Kombinationsfeld im Arbeitsblatt platziert ist, klicken Sie mit der rechten Maustaste auf das Steuerelement, um **Steuerelement formatieren** zu klicken und den Eingabebereich festzulegen.
1. Geben Sie im Feld **Zellverknüpfung** die Adresse der Zelle an, mit der dieses Kombinationsfeld verknüpft werden soll.
1. Klicken Sie auf **OK**.

### **Verwendung von Aspose.Cells**

Die Klasse [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) bietet eine Methode namens [**AddComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox), mit der ein Combo-Box-Steuerlement einem Arbeitsblatt hinzugefügt werden kann. Die Methode gibt ein [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)-Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) repräsentiert eine Combo-Box. Sie hat einige wichtige Elemente:

- Die Eigenschaft [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) gibt eine Zelle an, die mit der Combo-Box verknüpft ist.
- Die Eigenschaft [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) gibt den Arbeitsblattbereich der Zellen an, die die Combo-Box füllen.
- Die Eigenschaft [**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) gibt die Anzahl der Listenzeilen an, die im Dropdown-Teil einer Combo-Box angezeigt werden.
- Die Eigenschaft [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) gibt an, ob die Combo-Box 3D-Schattierung aufweist.

Das folgende Beispiel zeigt, wie eine Combo-Box dem Arbeitsblatt hinzugefügt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **Hinzufügen eines Beschriftungssteuerelements zu einem Arbeitsblatt**

Labels sind eine Möglichkeit, Benutzern Informationen über den Inhalt eines Tabellenblatts zur Verfügung zu stellen. Aspose.Cells ermöglicht es, Labels einem Arbeitsblatt hinzuzufügen und zu manipulieren. Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) bietet eine Methode namens [**AddLabel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel), mit der ein Label-Steuerlement dem Arbeitsblatt hinzugefügt wird. Die Methode gibt ein [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)-Objekt zurück. Die Klasse [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) repräsentiert ein Label im Arbeitsblatt. Sie hat einige wichtige Elemente:

- Die Methode [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) gibt einen Beschriftungszeichenfolge an.
- Die [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)-Methode gibt die [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype) an, die Art und Weise, wie das Label an die Zellen im Arbeitsblatt angehängt ist.

Das folgende Beispiel zeigt, wie man einem Arbeitsblatt eine Beschriftung hinzufügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

## **Hinzufügen eine Listfeld-Steuerung zu einem Arbeitsblatt**

Ein Listenfeld erstellt eine Liste-Steuerung, die die Auswahl eines einzelnen oder mehrerer Elemente ermöglicht.

### **Verwendung von Microsoft Excel**

Um eine Listfeld-Steuerung in einem Arbeitsblatt zu platzieren:

1. Stellen Sie sicher, dass die **Formulare**-Symbolleiste angezeigt wird.
1. Klicken Sie auf das **Listfeld**-Werkzeug.
1. Klicken und ziehen Sie im Arbeitsblattbereich, um das Rechteck zu definieren, das das Listenfeld halten wird.
1. Sobald das Listenfeld im Arbeitsblatt platziert ist, klicken Sie mit der rechten Maustaste auf die Steuerung, um auf **Steuerelement formatieren** zu klicken und den Eingabebereich anzugeben.
1. Geben Sie im Feld **Zellenverknüpfung** die Adresse der Zelle an, mit der dieses Listenfeld verknüpft werden soll, und setzen Sie das Attribut für den Auswahltyp (Einzelauswahl, Mehrfachauswahl, Erweiterte Auswahl).
1. Klicken Sie auf **OK**.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) bietet eine Methode namens [**AddListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox), die dazu verwendet wird, ein Listenfeld-Steuerlement zu einem Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox)-Objekt zurück. Die Klasse [**ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) repräsentiert ein Listenfeld. Sie hat einige wichtige Elemente:

- Die [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)-Methode gibt eine Zelle an, die mit dem Listenfeld verknüpft ist.
- Die [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange)-Methode gibt den Arbeitsblattbereich von Zellen an, die zur Befüllung des Listenfelds verwendet werden.
- Die [**SelectionType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype)-Methode gibt den Auswahmodus des Listenfelds an.
- Die [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow)-Methode zeigt an, ob das Listenfeld 3D-Schattierung hat.

Das folgende Beispiel zeigt, wie man einem Arbeitsblatt ein Listenfeld hinzufügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

## **Hinzufügen einer Schaltflächensteuerung zu einem Arbeitsblatt**

Schaltflächen sind nützlich, um Aktionen auszuführen. Manchmal ist es nützlich, einer Schaltfläche ein VBA-Makro zuzuweisen oder einen Hyperlink zuzuweisen, um eine Webseite zu öffnen.

### **Verwendung von Microsoft Excel**

Um eine Schaltflächensteuerung in Ihrem Arbeitsblatt zu platzieren:

1. Stellen Sie sicher, dass die **Formulare**-Symbolleiste angezeigt wird.
1. Klicken Sie auf das **Schaltflächen**-Werkzeug.
1. Klicken und ziehen Sie im Arbeitsblattbereich, um das Rechteck zu definieren, das die Schaltfläche enthält.
1. Nachdem die Listenfeld im Arbeitsblatt platziert wurde, klicken Sie mit der rechten Maustaste auf die Steuerung und wählen Sie **Steuerung formatieren** aus, dann geben Sie ein VBA-Makro an und Attribute wie Schriftart, Ausrichtung, Größe, Rand usw. an.
1. Klicken Sie auf **OK**.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) enthält eine Methode namens [**AddButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton), die verwendet wird, um eine Schaltflächensteuerung zum Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button)-Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) repräsentiert eine Schaltfläche. Sie verfügt über einige wichtige Elemente:

- Die Eigenschaft [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) gibt die Beschriftung der Schaltfläche an.
- Die Eigenschaft [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) gibt die Schriftattribute für das Label der Schaltflächensteuerung an.
- Die Eigenschaft [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) gibt die [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype) an, wie die Schaltfläche an die Zellen im Arbeitsblatt angebracht ist.
- Die Eigenschaft [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) fügt eine Verknüpfung für die Schaltflächensteuerung hinzu. Durch Klicken auf die Schaltfläche wird zu der entsprechenden URL navigiert.

Das folgende Beispiel zeigt, wie Sie eine Schaltfläche zum Arbeitsblatt hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **Hinzufügen einer Liniensteuerung zum Arbeitsblatt.**

### **Verwendung von Microsoft Excel**

1. Auf der **Zeichnen**-Symbolleiste klicken Sie auf **AutoFormen**, zeigen auf **Linien** und wählen den Linienstil aus, den Sie möchten.
1. Ziehen Sie, um die Linie zu zeichnen.
1. Führen Sie einen oder beide der folgenden Schritte aus:
   1. Um die Linie auf 15-Grad-Winkel von ihrem Ausgangspunkt zu beschränken, halten Sie die UMSCHALTTASTE gedrückt, während Sie ziehen.
   1. Um die Linie in entgegengesetzte Richtungen vom ersten Endpunkt zu verlängern, halten Sie STRG gedrückt, während Sie ziehen.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) enthält eine Methode mit dem Namen [**AddLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline), die verwendet wird, um eine Linienschape zum Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)-Objekt zurück. Die Klasse [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) repräsentiert eine Linie. Sie verfügt über einige wichtige Elemente:

- Die Methode [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) gibt das Format einer Linie an.
- Die Methode [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) gibt die [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype) an, wie die Linie an die Zellen im Arbeitsblatt angebracht ist.

Das folgende Beispiel zeigt, wie Sie Linien zum Arbeitsblatt hinzufügen. Es erstellt drei Linien mit unterschiedlichen Stilen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **Hinzufügen eines Pfeilkopfs zu einer Linie**

Aspose.Cells ermöglicht es auch, Pfeillinien zu zeichnen. Es ist möglich, einer Linie eine Pfeilspitze hinzuzufügen und die Linie zu formatieren. Sie können z.B. die Farbe der Linie ändern oder das Gewicht und den Stil der Linie festlegen.

Das folgende Beispiel zeigt, wie Sie einen Pfeilkopf zu einer Linie hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **Hinzufügen einer Rechtecksteuerung zu einem Arbeitsblatt**

Aspose.Cells ermöglicht es Ihnen, Rechteckformen in Ihren Arbeitsblättern zu zeichnen. Sie können ein Rechteck, ein Quadrat usw. erstellen. Es ist auch möglich, die Füllfarbe und die Rahmenlinienfarbe der Steuerung zu formatieren. Sie können z.B. die Farbe des Rechtecks ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil des Rechtecks spezifizieren, wie Sie es benötigen.

### **Verwendung von Microsoft Excel**

1. Klicken Sie auf der **Zeichnen**-Symbolleiste auf **Rechteck**.
1. Ziehen Sie, um das Rechteck zu zeichnen.
1. Führen Sie einen oder beide der folgenden Schritte aus:
   1. Halten Sie die UMSCHALTTASTE gedrückt, um das Rechteck zu zeichnen und so ein Quadrat von seinem Ausgangspunkt aus zu beschränken.
   1. Halten Sie STRG gedrückt, um ein Rechteck von einem Mittelpunkt aus zu zeichnen.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) stellt eine Methode namens [**AddRectangle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle) zur Verfügung, die dazu dient, eine Rechtecksform zu einem Arbeitsblatt hinzuzufügen. Diese Methode gibt ein [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape)-Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) stellt ein Rechteck dar. Sie hat einige wichtige Elemente:

- Die Eigenschaft [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) legt die Linienformatattribute eines Rechtecks fest.
- Die Eigenschaft [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) legt das [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype) fest, wie das Rechteck an die Zellen im Arbeitsblatt angefügt ist.
- Die Eigenschaft [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) legt die Füllformatstile eines Rechtecks fest.

Das folgende Beispiel zeigt, wie Sie ein Rechteck zum Arbeitsblatt hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **Hinzufügen einer Bogensteuerung zum Arbeitsblatt**

Aspose.Cells ermöglicht es Ihnen, Bogenformen in Ihren Arbeitsblättern zu zeichnen. Sie können einfache und gefüllte Bogen erstellen. Sie können die Füllfarbe und die Randlinienfarbe des Steuerelements formatieren. Sie können zum Beispiel die Farbe des Bogens festlegen/ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil der Form nach Bedarf festlegen.

### **Verwendung von Microsoft Excel**

1. Klicken Sie in der Symbolleiste **Zeichnen** auf **Bogen** in den **AutoFormen**.
1. Ziehen Sie, um den Bogen zu zeichnen.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) bietet eine Methode namens [**AddArc**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc), die verwendet wird, um eine Bogenform zu einem Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape)-Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) repräsentiert einen Bogen. Sie enthält einige wichtige Elemente:

- Die [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)-Eigenschaft gibt die Linienformatattribute einer Bogenform an.
- Die [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)-Eigenschaft gibt an, wie der Bogen an die Zellen im Arbeitsblatt angefügt ist.
- Die [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)-Eigenschaft gibt die Füllformatstile der Form an.
- Die [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow)-Eigenschaft gibt den Zeilenindex der rechten unteren Ecke an.
- Die [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn)-Eigenschaft gibt den Spaltenindex der rechten unteren Ecke an.

Das folgende Beispiel zeigt, wie Bogenformen zum Arbeitsblatt hinzugefügt werden. Das Beispiel erstellt zwei Bogenformen: eine ist gefüllt und die andere ist einfach.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **Ovale Steuerung zu einem Arbeitsblatt hinzufügen**

Mit Aspose.Cells können Sie ovale Formen in Arbeitsblättern zeichnen. Erstellen Sie einfache und gefüllte ovale Formen und formatieren Sie die Füllfarbe und die Randlinienfarbe des Steuerelements. Sie können zum Beispiel die Farbe des Ovals spezifizieren/ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil der Form festlegen.

### **Verwendung von Microsoft Excel**

- Klicken Sie auf der *Zeichnen*-Symbolleiste auf *Oval*.
- Ziehen Sie, um das Oval zu zeichnen.
- Führen Sie eine oder beide der folgenden Aktionen aus:
- Halten Sie beim Ziehen die UMSCHALTTASTE gedrückt, um das Oval zu einem Kreis von seinem Startpunkt zu beschränken.
- Halten Sie beim Ziehen die STRG-TASTE gedrückt, um ein Oval von einem Mittelpunkt aus zu zeichnen.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) bietet eine Methode namens [**AddOval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval), die verwendet wird, um eine ovale Form zu einem Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval)-Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) repräsentiert eine ovale Form. Sie enthält einige wichtige Elemente:

- Die [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)-Eigenschaft gibt die Linienformatattribute einer ovalen Form an.
- Die [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)-Eigenschaft gibt an, wie das Oval an die Zellen im Arbeitsblatt angefügt ist.
- Die [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)-Eigenschaft gibt die Füllformatstile der Form an.
- Die [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow)-Eigenschaft gibt den Zeilenindex der rechten unteren Ecke an.
- Die [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn)-Eigenschaft gibt den Spaltenindex der rechten unteren Ecke an.

Das folgende Beispiel zeigt, wie ovale Formen zum Arbeitsblatt hinzugefügt werden. Das Beispiel erstellt zwei ovale Formen: eine gefüllte ovale Form und eine einfache Kreisform.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **Hinzufügen von Spinner Control zum Arbeitsblatt**

Ein Drehfeld ist ein Textfeld, das mit einer Schaltfläche (einem Drehfeld) verbunden ist, bestehend aus einem Aufwärts- und einem Abwärtspfeil, den Sie anklicken, um den Wert im Textfeld inkrementell zu ändern. Durch Verwendung von Drehfeldern können Sie sehen, wie sich Eingaben auf Ihr Finanzmodell auf die Modellausgaben auswirken. Sie können ein Drehfeld an eine bestimmte Eingabezelle anhängen. Wenn Sie den Aufwärts- oder Abwärtspfeil am Drehfeld anklicken, wird der ganze Zahlenwert in der Ziel-Eingabezelle erhöht oder verringert. *Aspose.Cells* ermöglicht es Ihnen, Drehfelder in Ihren Arbeitsblättern zu erstellen.

### **Verwendung von Microsoft Excel**

Um ein Drehfeldsteuerelement in Ihrem Arbeitsblatt zu platzieren:

- Stellen Sie sicher, dass die *Formulare* Symbolleiste angezeigt wird.
- Klicken Sie auf das *Spinner* Werkzeug.
- Klicken und ziehen Sie im Arbeitsblattbereich, um das Rechteck festzulegen, das das Drehfeld halten wird.
- Sobald das Drehfeld im Arbeitsblatt platziert ist, klicken Sie mit der rechten Maustaste auf das Steuerelement und klicken Sie auf *Steuerelement formatieren* und geben Sie die maximalen, minimalen und inkrementellen Werte an.
- Geben Sie im Feld *Zellenverknüpfung* die Adresse der Zelle an, mit der dieses Drehfeld verknüpft sein soll.
- Klicken Sie auf *OK*.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) bietet eine Methode namens [**AddSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner), die verwendet wird, um ein Drehfeldsteuerelement zu einem Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) stellt ein Drehfeld dar. Sie hat einige wichtige Elemente:

- Die Eigenschaft [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) gibt eine Zelle an, die mit dem Drehfeld verknüpft ist.
- Die Eigenschaft [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) gibt den maximalen Wert für den Drehfeldbereich an.
- Die Eigenschaft [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) gibt den minimalen Wert für den Drehfeldbereich an.
- Die Eigenschaft [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) gibt den Wertbetrag an, um den ein Spinner eine Zeilenverschiebung inkrementiert.
- Die Eigenschaft [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) gibt an, ob das Drehfeld eine 3D-Schattierung aufweist.
- Die Eigenschaft [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) gibt den aktuellen Wert des Drehfelds an.

Das folgende Beispiel zeigt, wie ein Drehfeld zum Arbeitsblatt hinzugefügt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **Hinzufügen von Bildlaufleistensteuerelement zum Arbeitsblatt**

Ein Bildlaufleistensteuerelement wird verwendet, um Daten auf einem Arbeitsblatt in ähnlicher Weise wie ein Drehfeldsteuerelement auszuwählen. Durch Hinzufügen des Steuerelements zu einem Arbeitsblatt und Verknüpfen mit einer Zelle ist es möglich, einen numerischen Wert für die aktuelle Position des Steuerelements zurückzugeben.

### **Verwendung von Microsoft Excel**

- Um eine Bildlaufleiste in Excel 2003 und in früheren Versionen hinzuzufügen, klicken Sie auf die *Bildlaufleiste* Schaltfläche in der *Formular*-Symbolleiste und erstellen Sie dann eine Bildlaufleiste, die die Zellen B2:B6 in der Höhe abdeckt und etwa ein Viertel der Breite der Spalte ist.
- Um eine Bildlaufleiste in Excel 2007 hinzuzufügen, klicken Sie auf die *Entwickler* Registerkarte, klicken Sie auf *Einfügen* und dann auf *Bildlaufleiste* im Bereich Formularsteuerelemente.
- Klicken Sie mit der rechten Maustaste auf die Bildlaufleiste und wählen Sie dann *Steuerung formatieren*.
- Geben Sie die folgenden Informationen ein und klicken Sie auf *OK*:
  - Geben Sie im Feld *Aktueller Wert* 1 ein.
  - Geben Sie im Feld *Minimalwert* 1 ein. Dieser Wert beschränkt die obere Position der Bildlaufleiste auf den ersten Eintrag in der Liste.
  - Geben Sie im Feld *Maximalwert* 20 ein. Diese Zahl gibt die maximale Anzahl von Einträgen in der Liste an.
  - Geben Sie im Feld *Inkrementeller Wechsel* 1 ein. Dieser Wert steuert, wie viele Zahlen das Bildlaufleiste Steuerelement den aktuellen Wert inkrementiert.
  - Geben Sie im Feld *Seitenwechsel* 5 ein. Dieser Eintrag steuert, wie viel der aktuelle Wert inkrementiert wird, wenn Sie innerhalb der Bildlaufleiste auf einer Seite des Schiebereglers klicken.
  - Geben Sie zur Eingabe eines Zahlenwerts in Zelle G1 (abhängig davon, welches Element in der Liste ausgewählt ist), G1 in das *Zellen verknüpfen* Feld ein.
- Klicken Sie auf eine Zelle, sodass die Bildlaufleiste nicht ausgewählt ist.

Wenn Sie auf die Auf- oder Ab-Steuerung auf der Bildlaufleiste klicken, wird die Zelle G1 auf einen Wert aktualisiert, der den aktuellen Wert der Bildlaufleiste plus oder minus dem inkrementellen Wechsel der Bildlaufleiste angibt.

### **Verwendung von Aspose.Cells**

Die [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Klasse bietet eine Methode mit dem Namen [**AddScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar), die verwendet wird, um ein Bildlaufleiste-Steuerelement zum Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) stellt eine Bildlaufleiste dar. Sie hat einige wichtige Elemente:

- Die [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) Eigenschaft gibt eine Zelle an, die mit der Bildlaufleiste verknüpft ist.
- Die [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) Eigenschaft gibt den maximalen Wert für den Bereich der Bildlaufleiste an.
- Die [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) Eigenschaft gibt den minimalen Wert für den Bereich der Bildlaufleiste an.
- Die [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) Eigenschaft gibt den Wert an, um den eine Bildlaufleiste pro Zeilenwechsel inkrementiert wird.
- Die [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) Eigenschaft gibt an, ob die Bildlaufleiste eine 3D-Schattierung hat.
- Die [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) Eigenschaft gibt den aktuellen Wert der Bildlaufleiste an.
- Die [**PageChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange) Eigenschaft gibt an, um wie viel der aktuelle Wert inkrementiert wird, wenn Sie innerhalb der Bildlaufleiste auf einer Seite des Schiebereglers klicken.

Das folgende Beispiel zeigt, wie Sie eine Bildlaufleiste zum Arbeitsblatt hinzufügen können.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **Hinzufügen von GroupBox-Steuerelementen zu Gruppensteuerungen in einem Arbeitsblatt**

Manchmal müssen Sie Kontrollkästchen oder andere Steuerelemente implementieren, die zu einer bestimmten Gruppe gehören. Dies können Sie erreichen, indem Sie entweder ein Gruppenfeld oder ein Rechteck-Steuerelement einbeziehen. Eines dieser beiden Objekte dient dann als Begrenzung der Gruppe. Nach dem Hinzufügen einer dieser Formen können Sie dann zwei oder mehr Optionsfelder oder andere Gruppenobjekte hinzufügen.

### **Verwendung von Microsoft Excel**

Um ein Gruppenfeldsteuerelement in Ihr Arbeitsblatt einzufügen und Steuerelemente darin zu platzieren:

- Um ein Formular zu starten, klicken Sie im Hauptmenü auf *Ansicht*, gefolgt von *Symbolleisten* und *Formularen*.
- Auf der *Formulare*-Symbolleiste klicken Sie auf die *Gruppenfeld*-Schaltfläche und zeichnen ein Rechteck auf dem Arbeitsblatt.
- Geben Sie einen Beschriftungsstring für das Feld ein.
- Klicken Sie auf der *Formulare*-Symbolleiste auf *Optionsfeld* und klicken Sie innerhalb des *Gruppenfelds* direkt unter dem Beschriftungsstring.
- Klicken Sie erneut auf der *Formulare*-Symbolleiste auf *Optionsfeld* und klicken Sie innerhalb des *Gruppenfelds* unter dem ersten Optionsfeld.
- Noch einmal auf der *Formulare*-Symbolleiste klicken Sie auf *Optionsfeld* und klicken Sie innerhalb des *Gruppenfelds* unter dem vorherigen Optionsfeld.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) bietet eine Methode namens [**AddGroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox), die verwendet wird, um ein Gruppenfeld-Steuerelement zum Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox)-Objekt zurück. Außerdem gruppiert die Methode [**Group**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) der Klasse [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) die Formen. Sie nimmt ein [**Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)-Array als Parameter und gibt ein [**GroupShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape)-Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) repräsentiert ein Gruppenfeld. Sie verfügt über einige wichtige Mitglieder:

- Die Eigenschaft [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) gibt den Beschriftungsstring des Gruppenfelds an.
- Die Eigenschaft [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) gibt an, ob das Gruppenfeld eine 3D-Schattierung hat.

Das folgende Beispiel zeigt, wie Sie ein Gruppenfeld hinzufügen und die Steuerelemente im Arbeitsblatt gruppieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **Erweiterte Themen**
- [AktiveX-Steuerelemente mit Aspose.Cells hinzufügen](/cells/de/net/add-activex-controls-using-aspose-cells/)
- [AktiveX-Steuerung entfernen](/cells/de/net/remove-activex-control/)
- [Aktualisieren Sie das ActiveX-ComboBox-Steuerelement](/cells/de/net/update-activex-combobox-control/)
{{< app/cells/assistant language="csharp" >}}
