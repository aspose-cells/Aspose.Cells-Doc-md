---
title: Steuerelemente verwalten
type: docs
weight: 150
url: /de/net/managing-controls/
---
## **Einführung**

Entwickler können verschiedene Zeichnungsobjekte wie Textfelder, Kontrollkästchen, Optionsfelder, Kombinationsfelder, Beschriftungen, Schaltflächen, Linien, Rechtecke, Bögen, Ovale, Spinner, Bildlaufleisten, Gruppenfelder usw. hinzufügen alle Zeichenobjekte. Es gibt jedoch einige Zeichnungsobjekte oder -formen, die noch nicht unterstützt werden. Erstellen Sie diese Zeichenobjekte in einem Designer-Arbeitsblatt mit Microsoft Excel und importieren Sie dann das Designer-Arbeitsblatt in Aspose.Cells. Mit Aspose.Cells können Sie diese Zeichenobjekte aus einem Designer-Arbeitsblatt laden und in eine generierte Datei schreiben.

## **Hinzufügen eines Textfeld-Steuerelements zu einem Arbeitsblatt**

 Eine Möglichkeit, wichtige Informationen in einem Bericht hervorzuheben, ist die Verwendung eines Textfelds. Fügen Sie beispielsweise Text hinzu, um den Firmennamen hervorzuheben oder die geografische Region mit den höchsten Umsätzen usw. anzugeben. Aspose.Cells bietet die[**TextBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection) Klasse, die verwendet wird, um der Sammlung ein neues Textfeld hinzuzufügen. Es gibt eine andere Klasse,[**Textfeld**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)das ein Textfeld darstellt, das zum Definieren aller Arten von Einstellungen verwendet wird. Es hat einige wichtige Mitglieder:

-  Das[**Textrahmen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe) Eigenschaft gibt zurück a[**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe) Objekt zum Anpassen des Inhalts des Textfelds.
-  Das[**Platzierung**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) -Eigenschaft gibt den Platzierungstyp an.
-  Das[**Schriftart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) Die Eigenschaft gibt die Schriftartattribute an.
-  Das[**Hyperlink hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) -Methode fügt einen Hyperlink für das Textfeld hinzu.
-  Das[**Füllformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) Eigenschaft gibt eine zurück[**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat) Objekt, mit dem das Füllformat für das Textfeld festgelegt wird.
-  Das[**Zeilenformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) Eigenschaft gibt die zurück[**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat) Objekt, das normalerweise zum Stil und Gewicht der Textfeldlinie verwendet wird.
-  Das[**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) -Eigenschaft gibt den Eingabetext für das Textfeld an.

Im folgenden Beispiel werden zwei Textfelder im ersten Arbeitsblatt der Arbeitsmappe erstellt. Das erste Textfeld ist mit verschiedenen Formateinstellungen gut ausgestattet. Die zweite ist eine einfache.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **Bearbeiten von Textfeldsteuerelementen in Designer-Tabellenkalkulationen**

 Mit Aspose.Cells können Sie auch auf Textfelder in den Designer-Arbeitsblättern zugreifen und sie bearbeiten. Verwenden Sie die[**Arbeitsblatt.TextBoxen**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes) -Eigenschaft, um die Textboxes-Auflistung im Blatt abzurufen.

Das folgende Beispiel verwendet die Excel-Datei Microsoft, die wir im obigen Beispiel erstellt haben. Es ruft die Textzeichenfolgen der beiden Textfelder ab und ändert den Text des zweiten Textfelds, um die Datei zu speichern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **Kontrollkästchen-Steuerelement zu einem Arbeitsblatt hinzufügen**

Kontrollkästchen sind praktisch, wenn Sie einem Benutzer die Möglichkeit geben möchten, zwischen zwei Optionen zu wählen, z. B. wahr oder falsch; ja oder Nein. Aspose.Cells ermöglicht Ihnen die Verwendung von Kontrollkästchen in Arbeitsblättern. Beispielsweise haben Sie möglicherweise ein Arbeitsblatt für die Finanzprognose entwickelt, in dem Sie entweder eine bestimmte Akquisition berücksichtigen können oder nicht. In diesem Fall möchten Sie möglicherweise ein Kontrollkästchen oben im Arbeitsblatt platzieren. Sie können dann den Status dieses Kontrollkästchens mit einer anderen Zelle verknüpfen, sodass der Wert der Zelle bei aktiviertem Kontrollkästchen True ist; wenn es nicht ausgewählt ist, ist der Wert der Zelle False.

### **Mit Microsoft Excel**

Gehen Sie folgendermaßen vor, um ein Kontrollkästchen-Steuerelement in Ihr Arbeitsblatt einzufügen:

1. Stellen Sie sicher, dass die Symbolleiste Formulare angezeigt wird.
1.  Drücke den**Kontrollkästchen aktivieren** Werkzeug auf der Symbolleiste Formulare.
1. Klicken und ziehen Sie in Ihrem Arbeitsblattbereich, um das Rechteck zu definieren, das das Kontrollkästchen und die Beschriftung neben dem Kontrollkästchen enthält.
1. Sobald das Kontrollkästchen platziert ist, bewegen Sie den Mauszeiger in den Beschriftungsbereich und ändern Sie die Beschriftung.
1.  Im**Cell Verbindung**geben Sie die Adresse der Zelle an, mit der dieses Kontrollkästchen verknüpft werden soll.
1.  Klicke auf**OK**.

### **Mit Aspose.Cells**

 Aspose.Cells bietet die[**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection) Klasse, die verwendet wird, um der Auflistung ein neues Kontrollkästchen hinzuzufügen. Es gibt eine andere Klasse,[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox), das ein Kontrollkästchen darstellt. Es hat einige wichtige Mitglieder:

-  Das[**Verknüpfte Zelle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) -Eigenschaft gibt eine Zelle an, die mit dem Kontrollkästchen verknüpft ist.
-  Das[**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) -Eigenschaft gibt die dem Kontrollkästchen zugeordnete Textzeichenfolge an. Es ist die Bezeichnung des Kontrollkästchens.
-  Das[**Wert**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) -Eigenschaft gibt an, ob das Kontrollkästchen aktiviert ist oder nicht.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt ein Kontrollkästchen hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **Optionsfeldsteuerung zum Arbeitsblatt hinzufügen**

Eine Optionsschaltfläche oder eine Optionsschaltfläche ist ein Steuerelement, das aus einem runden Kästchen besteht. Der Benutzer trifft seine Entscheidung, indem er das runde Kästchen auswählt. Ein Optionsfeld wird normalerweise, wenn nicht immer, von anderen begleitet. Solche Optionsfelder werden als Gruppe angezeigt und verhalten sich wie eine Gruppe. Der Benutzer entscheidet, welche Schaltfläche gültig ist, indem er nur eine davon auswählt. Wenn der Benutzer auf eine Schaltfläche klickt, wird sie gefüllt. Wenn eine Schaltfläche in der Gruppe ausgewählt ist, sind Schaltflächen derselben Gruppe leer.

### **Mit Microsoft Excel**

Führen Sie die folgenden Schritte aus, um ein Optionsfeld-Steuerelement in Ihrem Arbeitsblatt zu platzieren:

1.  Stellen Sie sicher, dass**Formen** Symbolleiste wird angezeigt.
1.  Drücke den**Optionsschaltfläche** Werkzeug.
1. Klicken und ziehen Sie im Arbeitsblatt, um das Rechteck zu definieren, das die Optionsschaltfläche und die Beschriftung neben der Optionsschaltfläche enthält.
1. Sobald das Optionsfeld im Arbeitsblatt platziert ist, bewegen Sie den Mauszeiger in den Beschriftungsbereich und ändern Sie die Beschriftung.
1.  Im**Cell Verbindung** Geben Sie im Feld die Adresse der Zelle an, mit der dieses Optionsfeld verknüpft werden soll.
1.  Klicken**OK**.

### **Mit Aspose.Cells**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**RadioButton hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton) , die verwendet wird, um einem Arbeitsblatt ein Optionsfeld-Steuerelement hinzuzufügen. Die Methode gibt eine zurück[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) Objekt. Die Klasse[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) stellt eine Optionsschaltfläche dar. Es hat einige wichtige Mitglieder:

-  Das[**Verknüpfte Zelle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) -Eigenschaft gibt eine Zelle an, die mit dem Optionsfeld verknüpft ist.
-  Das[**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)-Eigenschaft gibt die dem Optionsfeld zugeordnete Textzeichenfolge an. Es ist die Beschriftung des Optionsfelds.
-  Das[**Wird geprüft**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) -Eigenschaft gibt an, ob das Optionsfeld aktiviert ist oder nicht.
-  Das[**Füllformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) -Eigenschaft gibt das Füllformat des Optionsfelds an.
-  Das[**Zeilenformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) -Eigenschaft gibt die Linienformatstile der Optionsschaltfläche an.

Das folgende Beispiel zeigt, wie Optionsfelder zu einem Arbeitsblatt hinzugefügt werden. Das Beispiel fügt drei Optionsfelder hinzu, die Altersgruppen darstellen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

## **Hinzufügen eines Kombinationsfeld-Steuerelements zu einem Arbeitsblatt**

Um die Dateneingabe zu vereinfachen oder Einträge auf bestimmte von Ihnen definierte Elemente zu beschränken, können Sie ein Kombinationsfeld oder eine Dropdown-Liste gültiger Einträge erstellen, die aus Zellen an anderer Stelle im Arbeitsblatt zusammengestellt wird. Wenn Sie eine Dropdown-Liste für eine Zelle erstellen, wird neben dieser Zelle ein Pfeil angezeigt. Um Informationen in diese Zelle einzugeben, klicken Sie auf den Pfeil und dann auf den gewünschten Eintrag.

### **Mit Microsoft Excel**

Führen Sie die folgenden Schritte aus, um ein Kombinationsfeld-Steuerelement in Ihrem Arbeitsblatt zu platzieren:

1.  Stellen Sie sicher, dass**Formen** Symbolleiste wird angezeigt.
1.  Klicke auf das**Kombinationsfeld** Werkzeug.
1. Klicken und ziehen Sie in Ihrem Arbeitsblattbereich, um das Rechteck zu definieren, das das Kombinationsfeld enthält.
1.  Sobald das Kombinationsfeld im Arbeitsblatt platziert ist, klicken Sie mit der rechten Maustaste auf das Steuerelement, um es anzuklicken**Formatsteuerung** und geben Sie den Eingangsbereich an.
1.  Im**Cell Verbindung** geben Sie die Adresse der Zelle an, mit der dieses Kombinationsfeld verknüpft werden soll.
1.  Klicke auf**OK**.

### **Mit Aspose.Cells**

 Das[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**Kombinationsfeld hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox) , die verwendet wird, um einem Arbeitsblatt ein Kombinationsfeld-Steuerelement hinzuzufügen. Die Methode gibt eine zurück[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) Objekt. Die Klasse[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) stellt ein Kombinationsfeld dar. Es hat einige wichtige Mitglieder:

-  Das[**Verknüpfte Zelle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) -Eigenschaft gibt eine Zelle an, die mit dem Kombinationsfeld verknüpft ist.
-  Das[**Eingabebereich**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) -Eigenschaft gibt den Arbeitsblattbereich von Zellen an, die zum Füllen des Kombinationsfelds verwendet werden.
-  Das[**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) -Eigenschaft gibt die Anzahl der Listenzeilen an, die im Dropdown-Bereich eines Kombinationsfelds angezeigt werden.
-  Das[**Schatten**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) -Eigenschaft gibt an, ob das Kombinationsfeld über 3D-Schattierung verfügt.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt ein Kombinationsfeld hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **Label Control zu einem Arbeitsblatt hinzufügen**

 Labels sind ein Mittel, um Benutzern Informationen über den Inhalt einer Tabelle zu geben. Aspose.Cells ermöglicht das Hinzufügen und Bearbeiten von Beschriftungen in einem Arbeitsblatt. Das[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**Label hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel) , wird verwendet, um dem Arbeitsblatt ein Beschriftungssteuerelement hinzuzufügen. Die Methode gibt a zurück[**Etikette**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) Objekt. Die Klasse[**Etikette**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) stellt eine Beschriftung im Arbeitsblatt dar. Es hat einige wichtige Mitglieder:

-  Das[**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) -Methode gibt die Beschriftungszeichenfolge eines Labels an.
-  Das[**Platzierung**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) Methode gibt die an[**Platzierungstyp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), die Art und Weise, wie die Beschriftung an die Zellen im Arbeitsblatt angehängt wird.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt eine Beschriftung hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

## **Listenfeld-Steuerelement zu einem Arbeitsblatt hinzufügen**

Ein Listenfeld-Steuerelement erstellt ein Listensteuerelement, das die Auswahl einzelner oder mehrerer Elemente ermöglicht.

### **Mit Microsoft Excel**

So platzieren Sie ein Listenfeld-Steuerelement in einem Arbeitsblatt:

1.  Stellen Sie sicher, dass**Formen** Symbolleiste wird angezeigt.
1.  Klicke auf das**Listenfeld** Werkzeug.
1. Klicken und ziehen Sie in Ihrem Arbeitsblattbereich, um das Rechteck zu definieren, das das Listenfeld enthält.
1.  Sobald das Listenfeld im Arbeitsblatt platziert ist, klicken Sie mit der rechten Maustaste auf das Steuerelement, um es anzuklicken**Formatsteuerung** und geben Sie den Eingangsbereich an.
1.  Im**Cell Verbindung**Geben Sie die Adresse der Zelle an, mit der dieses Listenfeld verknüpft werden soll, und legen Sie das Attribut Auswahltyp (Einzeln, Mehrfach, Erweitern) fest
1.  Klicken**OK**.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**Listenfeld hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox) , die verwendet wird, um einem Arbeitsblatt ein Listenfeld-Steuerelement hinzuzufügen. Die Methode gibt a zurück[**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) Objekt. Die Klasse[**Listenfeld**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) stellt ein Listenfeld dar. Es hat einige wichtige Mitglieder:

-  Das[**Verknüpfte Zelle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) Methode gibt eine Zelle an, die mit dem Listenfeld verknüpft ist.
-  Das[**Eingabebereich**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) -Methode gibt den Arbeitsblattbereich von Zellen an, die zum Füllen des Listenfelds verwendet werden.
-  Das[**Auswahltyp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype)Methode gibt den Auswahlmodus des Listenfelds an.
-  Das[**Schatten**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) -Methode gibt an, ob das Listenfeld über 3D-Schattierung verfügt.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt ein Listenfeld hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

## **Schaltflächen-Steuerelement zu einem Arbeitsblatt hinzufügen**

Schaltflächen sind nützlich, um einige Aktionen auszuführen. Manchmal ist es hilfreich, der Schaltfläche ein VBA-Makro zuzuweisen oder einen Hyperlink zum Öffnen einer Webseite zuzuweisen.

### **Mit Microsoft Excel**

So platzieren Sie ein Schaltflächen-Steuerelement in Ihrem Arbeitsblatt:

1.  Stellen Sie sicher, dass**Formen** Symbolleiste wird angezeigt.
1.  Klicke auf das**Knopf** Werkzeug.
1. Klicken und ziehen Sie in Ihrem Arbeitsblattbereich, um das Rechteck zu definieren, das die Schaltfläche halten wird.
1.  Sobald das Listenfeld im Arbeitsblatt platziert ist, klicken Sie mit der rechten Maustaste auf das Steuerelement und wählen Sie es aus**Formatsteuerung**, geben Sie dann ein VBA-Makro und Attribute für Schriftart, Ausrichtung, Größe, Rand usw. an.
1.  Klicke auf**OK**.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**Schaltfläche hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton) , wird verwendet, um dem Arbeitsblatt ein Schaltflächen-Steuerelement hinzuzufügen. Die Methode gibt eine zurück[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) Objekt. Die Klasse[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) stellt eine Schaltfläche dar. Es hat einige wichtige Mitglieder:

-  Das[**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) -Eigenschaft gibt die Beschriftung der Schaltfläche an.
-  Das[**Schriftart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) -Eigenschaft gibt die Schriftartattribute für die Bezeichnung des Schaltflächensteuerelements an.
-  Das[**Platzierung**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) Eigenschaft gibt die an[**Platzierungstyp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), die Art und Weise, wie die Schaltfläche mit den Zellen im Arbeitsblatt verbunden ist.
-  Das[**Hyperlink hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) -Eigenschaft fügt einen Hyperlink für das Schaltflächen-Steuerelement hinzu. Durch Klicken auf die Schaltfläche wird zur zugehörigen URL navigiert.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt eine Schaltfläche hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **Liniensteuerung zum Arbeitsblatt hinzufügen**

### **Mit Microsoft Excel**

1.  Auf der**Zeichnung** Symbolleiste, klicken Sie auf**AutoFormen** , zeigen auf**Linien**, und wählen Sie den gewünschten Linienstil aus.
1. Ziehen Sie, um die Linie zu zeichnen.
1. Führen Sie einen oder beide der folgenden Schritte aus:
 1. Um die Linie auf einen 15-Grad-Winkel von ihrem Startpunkt zu beschränken, halten Sie beim Ziehen die UMSCHALTTASTE gedrückt.
 1. Um die Linie vom ersten Endpunkt in entgegengesetzte Richtungen zu verlängern, halten Sie beim Ziehen die STRG-Taste gedrückt.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**AddLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline) , mit dem dem Arbeitsblatt eine Linienform hinzugefügt wird. Die Methode gibt a zurück[**Linienform**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) Objekt. Die Klasse[**Linienform**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) stellt eine Linie dar. Es hat einige wichtige Mitglieder:

-  Das[**Zeilenformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) Methode gibt das Format einer Zeile an.
-  Das[**Platzierung**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) Methode gibt die an[**Platzierungstyp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)die Art und Weise, wie die Linie mit den Zellen im Arbeitsblatt verbunden ist.

Das folgende Beispiel zeigt, wie dem Arbeitsblatt Zeilen hinzugefügt werden. Es erstellt drei Linien mit unterschiedlichen Stilen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **Hinzufügen einer Pfeilspitze zu einer Linie**

Mit Aspose.Cells können Sie auch Pfeillinien zeichnen. Es ist möglich, einer Linie eine Pfeilspitze hinzuzufügen und die Linie zu formatieren. Sie können beispielsweise die Farbe der Linie ändern oder die Stärke und den Stil der Linie festlegen.

Das folgende Beispiel zeigt, wie Sie einer Linie eine Pfeilspitze hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **Rectangle Control zu einem Arbeitsblatt hinzufügen**

Aspose.Cells ermöglicht es Ihnen, rechteckige Formen in Ihren Arbeitsblättern zu zeichnen. Sie können ein Rechteck, ein Quadrat usw. erstellen. Sie können auch die Füllfarbe und die Farbe der Rahmenlinie des Steuerelements formatieren. Sie können beispielsweise die Farbe des Rechtecks ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil des Rechtecks nach Bedarf festlegen.

### **Mit Microsoft Excel**

1.  Auf der**Zeichnung** Symbolleiste, klicken Sie auf**Rechteck**.
1. Ziehen Sie, um das Rechteck zu zeichnen.
1. Führen Sie einen oder beide der folgenden Schritte aus:
 1. Um das Rechteck so zu beschränken, dass ein Quadrat von seinem Startpunkt gezeichnet wird, halten Sie beim Ziehen die UMSCHALTTASTE gedrückt.
 1. Um ein Rechteck von einem Mittelpunkt aus zu zeichnen, halten Sie beim Ziehen die STRG-Taste gedrückt.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**Rechteck hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle) , die verwendet wird, um einem Arbeitsblatt eine rechteckige Form hinzuzufügen. Die Methode kehrt zurück[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) Objekt. Die Klasse[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) stellt ein Rechteck dar. Es hat einige wichtige Mitglieder:

-  Das[**Zeilenformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) -Eigenschaft gibt die Linienformatattribute eines Rechtecks an.
-  Das[**Platzierung**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) Eigenschaft gibt die an[**Platzierungstyp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), die Art und Weise, wie das Rechteck an die Zellen im Arbeitsblatt angefügt wird.
-  Das[**Füllformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) -Eigenschaft gibt die Füllformatstile eines Rechtecks an.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt ein Rechteck hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **Bogensteuerung zum Arbeitsblatt hinzufügen**

Aspose.Cells ermöglicht Ihnen das Zeichnen von Bogenformen in Ihren Arbeitsblättern. Sie können einfache und gefüllte Bögen erstellen. Sie dürfen die Füllfarbe und die Rahmenfarbe des Steuerelements formatieren. Sie können beispielsweise die Farbe des Bogens angeben / ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil der Form für Ihren Bedarf festlegen.

### **Mit Microsoft Excel**

1.  Auf der**Zeichnung** Symbolleiste, klicken Sie auf**Bogen** in dem**AutoFormen**.
1. Ziehen Sie, um den Bogen zu zeichnen.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**Bogen hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc) , die verwendet wird, um einem Arbeitsblatt eine Bogenform hinzuzufügen. Die Methode gibt eine zurück[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) Objekt. Die Klasse[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) stellt einen Bogen dar. Es hat einige wichtige Mitglieder:

-  Das[**Zeilenformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) -Eigenschaft gibt die Linienformatattribute einer Bogenform an.
-  Das[**Platzierung**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) Eigenschaft gibt die an[**Platzierungstyp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), die Art und Weise, wie der Bogen mit den Zellen im Arbeitsblatt verbunden ist.
-  Das[**Füllformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)-Eigenschaft gibt die Füllformatstile der Form an.
-  Das[**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) -Eigenschaft gibt den Zeilenindex der unteren rechten Ecke an.
-  Das[**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) -Eigenschaft gibt den Spaltenindex der unteren rechten Ecke an.

Das folgende Beispiel zeigt, wie dem Arbeitsblatt Bogenformen hinzugefügt werden. Das Beispiel erstellt zwei Bogenformen: eine ist gefüllt und die andere einfach.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **Oval Control zu einem Arbeitsblatt hinzufügen**

Aspose.Cells ermöglicht es Ihnen, ovale Formen in Arbeitsblätter zu zeichnen. Erstellen Sie einfache und gefüllte ovale Formen und formatieren Sie die Füllfarbe und die Rahmenlinienfarbe des Steuerelements. Sie können beispielsweise die Farbe des Ovals festlegen / ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil der Form festlegen.

### **Mit Microsoft Excel**

-  Auf der*Zeichnung* Symbolleiste, klicken Sie auf*Oval*.
- Ziehen Sie, um das Oval zu zeichnen.
- Führen Sie einen oder beide der folgenden Schritte aus:
- Halten Sie beim Ziehen die UMSCHALTTASTE gedrückt, um das Oval so zu zwingen, dass es von seinem Startpunkt aus einen Kreis zeichnet.
- Um ein Oval von einem Mittelpunkt aus zu zeichnen, halten Sie beim Ziehen die STRG-Taste gedrückt.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**AddOval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval) , die verwendet wird, um einem Arbeitsblatt eine ovale Form hinzuzufügen. Die Methode gibt eine zurück[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) Objekt. Die Klasse[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) stellt eine ovale Form dar. Es hat einige wichtige Mitglieder:

-  Das[**Zeilenformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) -Eigenschaft gibt die Linienformatattribute einer ovalen Form an.
-  Das[**Platzierung**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) Eigenschaft gibt die an[**Platzierungstyp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), die Art und Weise, wie das Oval mit den Zellen im Arbeitsblatt verbunden ist.
-  Das[**Füllformat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)-Eigenschaft gibt die Füllformatstile der Form an.
-  Das[**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) -Eigenschaft gibt den Zeilenindex der unteren rechten Ecke an.
-  Das[**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) -Eigenschaft gibt den Spaltenindex der unteren rechten Ecke an.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt ovale Formen hinzufügen. Das Beispiel erstellt zwei ovale Formen: eine ist ein gefülltes Oval, die andere ein einfacher Kreis.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **Spinner Control zum Arbeitsblatt hinzufügen**

 Ein Drehfeld ist ein Textfeld, das mit einer Schaltfläche verbunden ist (Drehfeld genannt), die aus einem Aufwärtspfeil und einem Abwärtspfeil besteht, auf die Sie klicken, um den Wert im Textfeld schrittweise zu ändern. Durch die Verwendung von Drehfeldern können Sie sehen, wie Eingabeänderungen an Ihrem Finanzmodell die Modellausgaben verändern. Sie können eine Drehschaltfläche an eine bestimmte Eingabezelle anhängen. Während Sie auf der Drehschaltfläche auf den Aufwärts- oder Abwärtspfeil klicken, wird der ganzzahlige Wert in der Zieleingabezelle erhöht oder verringert.*Aspose.Cells* ermöglicht es Ihnen, Spinner in Ihren Arbeitsblättern zu erstellen.

### **Mit Microsoft Excel**

So platzieren Sie ein Drehfeld-Steuerelement in Ihrem Arbeitsblatt:

-  Stellen Sie sicher, dass*Formen* Symbolleiste wird angezeigt.
-  Drücke den*Spinner* Werkzeug.
- Klicken und ziehen Sie in Ihrem Arbeitsblattbereich, um das Rechteck zu definieren, das das Spinner halten wird.
-  Sobald das Zahlenauswahlfeld im Arbeitsblatt platziert ist, klicken Sie mit der rechten Maustaste auf das Steuerelement, und klicken Sie darauf*Formatsteuerung* und geben Sie die maximalen, minimalen und inkrementellen Werte an.
-  Im*Cell Verbindung* geben Sie die Adresse der Zelle an, mit der dieses Drehfeld verknüpft werden soll.
-  Klicke auf*OK*.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**AddSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner) die verwendet wird, um einem Arbeitsblatt ein Drehfeld-Steuerelement hinzuzufügen. Die Methode gibt eine zurück[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) Objekt. Die Klasse[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) stellt ein Spinnfeld dar. Es hat einige wichtige Mitglieder:

-  Das[**Verknüpfte Zelle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) -Eigenschaft gibt eine Zelle an, die mit dem Drehfeld verknüpft ist.
-  Das[**max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) -Eigenschaft gibt den Maximalwert für den Bereich des Drehfelds an.
-  Das[**Mindest**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) -Eigenschaft gibt den Mindestwert für den Bereich des Drehfelds an.
-  Das[**Inkrementelle Änderung**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) Die Eigenschaft gibt den Wertbetrag an, für den ein Spinner um einen Zeilenlauf inkrementiert wird.
-  Das[**Schatten**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) -Eigenschaft gibt an, ob das Drehfeld 3D-Schattierung hat.
-  Das[**Aktueller Wert**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) -Eigenschaft gibt den aktuellen Wert des Drehfelds an.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt ein Drehfeld hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **Hinzufügen einer Bildlaufleistensteuerung zu einem Arbeitsblatt**

Ein Bildlaufleisten-Steuerelement wird ähnlich wie ein Drehfeld-Steuerelement verwendet, um die Auswahl von Daten auf einem Arbeitsblatt zu unterstützen. Durch Hinzufügen des Steuerelements zu einem Arbeitsblatt und Verknüpfen mit einer Zelle ist es möglich, einen numerischen Wert für die aktuelle Position des Steuerelements zurückzugeben.

### **Mit Microsoft Excel**

- Um eine Bildlaufleiste in Excel 2003 und früheren Versionen hinzuzufügen, klicken Sie auf die*Scrollleiste* Knopf auf der*Formen* Symbolleiste, und erstellen Sie dann eine Bildlaufleiste, die die Zellen B2:B6 in der Höhe abdeckt und etwa ein Viertel der Breite der Spalte beträgt.
-  Um eine Bildlaufleiste in Excel 2007 hinzuzufügen, klicken Sie auf*Entwickler* Registerkarte, klicken Sie auf*Einfügung* , und klicken Sie dann auf*Scrollleiste* im Abschnitt Formularsteuerelemente.
-  Klicken Sie mit der rechten Maustaste auf die Bildlaufleiste, und klicken Sie dann*Formatsteuerung*.
-  Geben Sie die folgenden Informationen ein und klicken Sie auf*OK*:
 - Im*Aktueller Wert* Feld, Typ 1.
 - Im*Mindestwert* Geben Sie im Feld 1 ein. Dieser Wert beschränkt den oberen Rand der Bildlaufleiste auf das erste Element in der Liste.
 - Im*Maximalwert* Geben Sie im Feld 20 ein. Diese Zahl gibt die maximale Anzahl von Einträgen in der Liste an.
 - Im*Inkrementelle Veränderung* Geben Sie in das Feld 1 ein. Dieser Wert steuert, um wie viele Zahlen das Bildlaufleisten-Steuerelement den aktuellen Wert erhöht.
 - Im*Seitenwechsel* Geben Sie im Feld 5 ein. Dieser Eintrag steuert, um wie viel der aktuelle Wert erhöht wird, wenn Sie in die Bildlaufleiste auf beiden Seiten des Bildlauffelds klicken.
 Um einen Zahlenwert in Zelle G1 einzugeben (je nachdem, welches Element in der Liste ausgewählt ist), geben Sie G1 in das ein*Cell Link* Kasten.
- Klicken Sie auf eine beliebige Zelle, sodass die Bildlaufleiste nicht ausgewählt ist.

Wenn Sie auf die Aufwärts- oder Abwärtssteuerung auf der Bildlaufleiste klicken, wird Zelle G1 auf eine Zahl aktualisiert, die den aktuellen Wert der Bildlaufleiste plus oder minus der inkrementellen Änderung der Bildlaufleiste angibt.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**Bildlaufleiste hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar) , die verwendet wird, um dem Arbeitsblatt ein Bildlaufleisten-Steuerelement hinzuzufügen. Die Methode gibt eine zurück[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) Objekt. Die Klasse[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) stellt eine Bildlaufleiste dar. Es hat einige wichtige Mitglieder:

-  Das[**Verknüpfte Zelle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) -Eigenschaft gibt eine Zelle an, die mit der Bildlaufleiste verknüpft ist.
-  Das[**max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) -Eigenschaft gibt den maximalen Wert für den Bereich der Bildlaufleiste an.
-  Das[**Mindest**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) -Eigenschaft gibt den Mindestwert für den Bereich der Bildlaufleiste an.
-  Das[**Inkrementelle Änderung**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) Die Eigenschaft gibt den Wertbetrag an, um den eine Bildlaufleiste um einen Zeilenlauf inkrementiert wird.
-  Das[**Schatten**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) -Eigenschaft gibt an, ob die Bildlaufleiste 3D-Schattierung hat.
-  Das[**Aktueller Wert**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) -Eigenschaft gibt den aktuellen Wert der Bildlaufleiste an.
-  Das[**Seitenwechsel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange)-Eigenschaft gibt an, um wie viel der aktuelle Wert erhöht wird, wenn Sie in die Bildlaufleiste auf beiden Seiten des Bildlauffelds klicken.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt eine Bildlaufleiste hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **GroupBox-Steuerelement zu Gruppensteuerelementen in einem Arbeitsblatt hinzufügen**

Manchmal müssen Sie Optionsfelder oder andere Steuerelemente implementieren, die zu einer bestimmten Gruppe gehören. Sie können dies implementieren, indem Sie entweder ein Gruppenfeld oder ein Rechtecksteuerelement einfügen. Jedes dieser beiden Objekte würde als Trennzeichen der Gruppe dienen. Nachdem Sie eine dieser Formen hinzugefügt haben, können Sie zwei oder mehr Optionsfelder oder andere Gruppenobjekte hinzufügen.

### **Mit Microsoft Excel**

So platzieren Sie ein Gruppenfeld-Steuerelement in Ihrem Arbeitsblatt und platzieren darin Steuerelemente:

-  Um ein Formular zu starten, klicken Sie im Hauptmenü auf*Sicht* , gefolgt von*Symbolleisten* und*Formen*.
-  Auf der*Formen* Symbolleiste, klicken Sie auf die*Gruppenfeld* und zeichnen Sie ein Rechteck auf dem Arbeitsblatt.
- Geben Sie eine Beschriftungszeichenfolge für das Feld ein.
-  Auf der*Formen* Symbolleiste, klicken Sie auf*Optionsschaltfläche* und klicken Sie hinein*Gruppenfeld* direkt unter der Beschriftungszeichenfolge.
-  Von dem*Formen* Symbolleiste erneut, klicken Sie auf*Optionsschaltfläche* und klicken Sie hinein*Gruppenfeld*unter dem ersten Radiobutton.
-  Noch einmal auf der*Formen* Symbolleiste, klicken Sie auf*Optionsschaltfläche* und klicken Sie hinein*Gruppenfeld* unter dem vorherigen Optionsfeld.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**GroupBox hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox) , die verwendet wird, um dem Arbeitsblatt ein Gruppenfeld-Steuerelement hinzuzufügen. Die Methode gibt eine zurück[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) Objekt. Außerdem die[**Gruppe**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) Methode der[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Klasse gruppiert die Formen, es dauert a[**Form**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) array als Parameter und gibt a zurück[**Gruppenform**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape) Objekt. Die Klasse[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) stellt eine Gruppenbox dar. Es hat einige wichtige Mitglieder:

-  Das[**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) -Eigenschaft gibt die Beschriftungszeichenfolge des Gruppenfelds an.
-  Das[**Schatten**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) -Eigenschaft gibt an, ob das Gruppenfeld 3D-Schattierung hat.

Das folgende Beispiel zeigt, wie Sie ein Gruppenfeld hinzufügen und die Steuerelemente im Arbeitsblatt gruppieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **Themen vorantreiben**
- [Fügen Sie ActiveX-Steuerelemente mit Aspose.Cells hinzu](/cells/de/net/add-activex-controls-using-aspose-cells/)
- [Entfernen Sie das ActiveX-Steuerelement](/cells/de/net/remove-activex-control/)
- [Aktualisieren Sie das ActiveX ComboBox-Steuerelement](/cells/de/net/update-activex-combobox-control/)
