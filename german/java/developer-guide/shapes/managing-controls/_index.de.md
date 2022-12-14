---
title: Steuerelemente verwalten
type: docs
weight: 120
url: /de/java/managing-controls/
---
## **Einführung**

Entwickler können verschiedene Zeichnungsobjekte wie Textfelder, Kontrollkästchen, Optionsfelder, Kombinationsfelder, Beschriftungen, Schaltflächen, Linien, Rechtecke, Bögen, Ovale, Spinner, Bildlaufleisten, Gruppenfelder usw. hinzufügen alle Zeichenobjekte. Es gibt jedoch einige Zeichnungsobjekte oder -formen, die noch nicht unterstützt werden. Erstellen Sie diese Zeichenobjekte in einem Designer-Arbeitsblatt mit Microsoft Excel und importieren Sie dann das Designer-Arbeitsblatt in Aspose.Cells. Mit Aspose.Cells können Sie diese Zeichenobjekte aus einem Designer-Arbeitsblatt laden und in eine generierte Datei schreiben.

## **TextBox-Steuerelement zum Arbeitsblatt hinzufügen**

Eine Möglichkeit, wichtige Informationen in einem Bericht hervorzuheben, ist die Verwendung eines Textfelds. Fügen Sie beispielsweise Text hinzu, um den Firmennamen hervorzuheben oder die geografische Region mit den höchsten Umsätzen usw. anzugeben. Aspose.Cells stellt die TextBoxes-Klasse bereit, die zum Hinzufügen eines neuen Textfelds zur Sammlung verwendet wird. Es gibt eine andere Klasse,[**Textfeld**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox), das ein Textfeld darstellt, das zum Definieren aller Arten von Einstellungen verwendet wird. Es hat einige wichtige Mitglieder:

-  Das[**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame) Methode gibt a zurück[**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame) Objekt zum Anpassen des Inhalts des Textfelds.
-  Das[**setPlacement**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) Methode gibt den Platzierungstyp an.
-  Das[**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font) Die Methode gibt die Schriftartattribute an.
-  Das[**Hyperlink hinzufügen**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink(java.lang.String))-Methode fügt einen Hyperlink für das Textfeld hinzu.
-  Das[**Füllformat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat) Eigenschaft Renditen[**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat) Objekt, mit dem das Füllformat für das Textfeld festgelegt wird.
-  Das[**Zeilenformat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat) Eigenschaft gibt die zurück[**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat) Objekt, das normalerweise zum Stil und Gewicht der Textfeldlinie verwendet wird.
-  Das[**Text setzen**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text)-Methode gibt den Eingabetext für das Textfeld an.

Im folgenden Beispiel werden zwei Textfelder im ersten Arbeitsblatt der Arbeitsmappe erstellt. Das erste Textfeld ist mit verschiedenen Formateinstellungen gut ausgestattet. Die zweite ist eine einfache.

Die folgende Ausgabe wird durch Ausführen des Codes generiert:

**Im Arbeitsblatt werden zwei Textfelder erstellt** 

![todo: Bild_alt_Text](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **Bearbeiten von Textfeldsteuerelementen in den Designer-Tabellenkalkulationen**

 Mit Aspose.Cells können Sie auch auf Textfelder in den Designer-Arbeitsblättern zugreifen und sie bearbeiten. Verwenden Sie die[**Arbeitsblatt.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) -Eigenschaft, um die Textboxes-Auflistung im Blatt abzurufen.

Das folgende Beispiel verwendet die Excel-Datei Microsoft – tsttextboxes.xls – die wir im obigen Beispiel erstellt haben. Es ruft die Textzeichenfolgen der beiden Textfelder ab und ändert den Text des zweiten Textfelds, um die Datei zu speichern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **CheckBox-Steuerelement zum Arbeitsblatt hinzufügen**

Kontrollkästchen sind praktisch, wenn Sie einem Benutzer die Möglichkeit geben möchten, zwischen zwei Optionen zu wählen, z. B. wahr oder falsch; ja oder Nein. Aspose.Cells ermöglicht Ihnen die Verwendung von Kontrollkästchen in Arbeitsblättern. Beispielsweise haben Sie möglicherweise ein Arbeitsblatt für die Finanzprognose entwickelt, in dem Sie entweder eine bestimmte Akquisition berücksichtigen können oder nicht. In diesem Fall möchten Sie möglicherweise ein Kontrollkästchen oben im Arbeitsblatt platzieren. Sie können dann den Status dieses Kontrollkästchens mit einer anderen Zelle verknüpfen, sodass der Wert der Zelle bei aktiviertem Kontrollkästchen True ist; wenn es nicht ausgewählt ist, ist der Wert der Zelle False.

### **Mit Microsoft Excel**

Gehen Sie folgendermaßen vor, um ein Kontrollkästchen-Steuerelement in Ihr Arbeitsblatt einzufügen:

1. Stellen Sie sicher, dass die Symbolleiste Formulare angezeigt wird.
1.  Drücke den**Kontrollkästchen aktivieren** Werkzeug auf der Symbolleiste Formulare.
1. Klicken und ziehen Sie in Ihrem Arbeitsblattbereich, um das Rechteck zu definieren, das das Kontrollkästchen und die Beschriftung neben dem Kontrollkästchen enthält.
1. Sobald das Kontrollkästchen platziert ist, bewegen Sie den Mauszeiger in den Beschriftungsbereich und ändern Sie die Beschriftung.
1.  In dem**Cell Verbindung**geben Sie die Adresse der Zelle an, mit der dieses Kontrollkästchen verknüpft werden soll.
1.  Klicke auf**OK**.

### **Mit Aspose.Cells**

 Aspose.Cells bietet die[**CheckBoxCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection) Klasse, die verwendet wird, um der Sammlung ein neues Kontrollkästchen hinzuzufügen. Es gibt eine andere Klasse,[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox), das ein Kontrollkästchen darstellt. Es hat einige wichtige Mitglieder:

-  Das[**setLinkedCell**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell) Methode gibt eine Zelle an, die mit dem Kontrollkästchen verknüpft ist.
-  Das[**Text setzen**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text) Methode gibt die dem Kontrollkästchen zugeordnete Textzeichenfolge an. Es ist die Bezeichnung des Kontrollkästchens.
-  Das[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value) Methode gibt an, ob das Kontrollkästchen aktiviert ist oder nicht.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt ein Kontrollkästchen hinzufügen. Die folgende Ausgabe wird nach der Ausführung des Codes generiert.

**Dem Arbeitsblatt wird ein Kontrollkästchen hinzugefügt** 

![todo: Bild_alt_Text](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **RadioButton-Steuerelement zum Arbeitsblatt hinzufügen**

Eine Optionsschaltfläche oder eine Optionsschaltfläche ist ein Steuerelement, das aus einem runden Kästchen besteht. Der Benutzer trifft seine Entscheidung, indem er das runde Kästchen auswählt. Ein Optionsfeld wird normalerweise, wenn nicht immer, von anderen begleitet. Solche Optionsfelder werden als Gruppe angezeigt und verhalten sich wie eine Gruppe. Der Benutzer entscheidet, welche Schaltfläche gültig ist, indem er nur eine davon auswählt. Wenn der Benutzer auf eine Schaltfläche klickt, wird sie gefüllt. Wenn eine Schaltfläche in der Gruppe ausgewählt ist, sind Schaltflächen derselben Gruppe leer.

### **Mit Microsoft Excel**

Führen Sie die folgenden Schritte aus, um ein Optionsfeld-Steuerelement in Ihrem Arbeitsblatt zu platzieren:

1.  Stellen Sie sicher, dass**Formen** Symbolleiste wird angezeigt.
1.  Drücke den**Optionsschaltfläche** Werkzeug.
1. Klicken und ziehen Sie im Arbeitsblatt, um das Rechteck zu definieren, das die Optionsschaltfläche und die Beschriftung neben der Optionsschaltfläche enthält.
1. Sobald das Optionsfeld im Arbeitsblatt platziert ist, bewegen Sie den Mauszeiger in den Beschriftungsbereich und ändern Sie die Beschriftung.
1.  In dem**Cell Verbindung** Geben Sie im Feld die Adresse der Zelle an, mit der dieses Optionsfeld verknüpft werden soll.
1.  Klicken**OK**.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)Die Klasse stellt eine Methode namens addShape bereit, die verwendet werden kann, um einem Arbeitsblatt ein Optionsfeld-Steuerelement hinzuzufügen. Die Methode kann ein RadioButton-Objekt zurückgeben. Die Klasse RadioButton repräsentiert ein Optionsfeld. Es hat einige wichtige Mitglieder:

- Die Methode setLinkedCell gibt eine Zelle an, die mit dem Optionsfeld verknüpft ist.
- Die setText-Methode gibt die dem Optionsfeld zugeordnete Textzeichenfolge an. Es ist die Beschriftung des Optionsfelds.
- Die Checked-Eigenschaft gibt an, ob das Optionsfeld aktiviert ist oder nicht.
- Die Methode setFillFormat gibt das Füllformat des Optionsfelds an.
- Die setLineFormat-Methode gibt die Linienformatstile des Optionsfelds an.

Das folgende Beispiel zeigt, wie Optionsfelder zu einem Arbeitsblatt hinzugefügt werden. Das Beispiel fügt drei Optionsfelder hinzu, die Altersgruppen darstellen. Die folgende Ausgabe würde nach der Ausführung des Codes generiert werden.

**Einige RadioButtons werden im Arbeitsblatt hinzugefügt** 

![todo: Bild_alt_Text](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

## **Hinzufügen eines Kombinationsfeld-Steuerelements zu einem Arbeitsblatt**

Um die Dateneingabe zu vereinfachen oder Einträge auf bestimmte von Ihnen definierte Elemente zu beschränken, können Sie ein Kombinationsfeld oder eine Dropdown-Liste gültiger Einträge erstellen, die aus Zellen an anderer Stelle im Arbeitsblatt zusammengestellt wird. Wenn Sie eine Dropdown-Liste für eine Zelle erstellen, wird neben dieser Zelle ein Pfeil angezeigt. Um Informationen in diese Zelle einzugeben, klicken Sie auf den Pfeil und dann auf den gewünschten Eintrag.

### **Mit Microsoft Excel**

Führen Sie die folgenden Schritte aus, um ein Kombinationsfeld-Steuerelement in Ihrem Arbeitsblatt zu platzieren:

1.  Stellen Sie sicher, dass**Formen** Symbolleiste wird angezeigt.
1.  Klick auf das**Kombinationsfeld** Werkzeug.
1. Klicken und ziehen Sie in Ihrem Arbeitsblattbereich, um das Rechteck zu definieren, das das Kombinationsfeld enthält.
1.  Sobald das Kombinationsfeld im Arbeitsblatt platziert ist, klicken Sie mit der rechten Maustaste auf das Steuerelement, um es anzuklicken**Formatsteuerung** und geben Sie den Eingangsbereich an.
1.  In dem**Cell Verbindung** geben Sie die Adresse der Zelle an, mit der dieses Kombinationsfeld verknüpft werden soll.
1.  Klicke auf**OK**.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)Die Klasse stellt eine Methode namens addShape bereit, die verwendet werden kann, um dem Arbeitsblatt ein Kombinationsfeld-Steuerelement hinzuzufügen. Die Methode kann ein ComboBox-Objekt zurückgeben. Die Klasse ComboBox repräsentiert ein Kombinationsfeld. Es hat einige wichtige Mitglieder:

- Die Methode setLinkedCell gibt eine Zelle an, die mit dem Kombinationsfeld verknüpft ist.
- Die setInputRange-Methode gibt den Arbeitsblattbereich von Zellen an, die zum Füllen des Kombinationsfelds verwendet werden.
- Die Methode setDropDownLines gibt die Anzahl der Listenzeilen an, die im Dropdown-Teil eines Kombinationsfelds angezeigt werden.
- Die setShadow-Methode gibt an, ob das Kombinationsfeld 3D-Schattierung hat.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt ein Kombinationsfeld hinzufügen. Beim Ausführen des Codes wird die folgende Ausgabe generiert.

**Dem Arbeitsblatt wird ein Kombinationsfeld hinzugefügt** 

![todo: Bild_alt_Text](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **Label Control zu einem Arbeitsblatt hinzufügen**

 Labels sind ein Mittel, um Benutzern Informationen über den Inhalt einer Tabelle zu geben. Aspose.Cells ermöglicht das Hinzufügen und Bearbeiten von Beschriftungen in einem Arbeitsblatt. Das[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)Die Klasse stellt eine Methode namens addShape bereit, die zum Hinzufügen eines Beschriftungssteuerelements zum Arbeitsblatt verwendet wird. Die Methode gibt ein Label-Objekt zurück. Die Klasse Label repräsentiert ein Label im Arbeitsblatt. Es hat einige wichtige Mitglieder:

- Die setText-Methode gibt die Beschriftungszeichenfolge eines Etiketts an.
- Die setPlacement-Methode gibt den PlacementType an, die Art und Weise, wie die Beschriftung an die Zellen im Arbeitsblatt angehängt wird.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt eine Beschriftung hinzufügen. Beim Ausführen des Codes wird die folgende Ausgabe generiert.

**Dem Arbeitsblatt wird eine Beschriftung hinzugefügt**

![todo: Bild_alt_Text](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

## **Listenfeld-Steuerelement zu einem Arbeitsblatt hinzufügen**

Ein Listenfeld-Steuerelement erstellt ein Listensteuerelement, das die Auswahl einzelner oder mehrerer Elemente ermöglicht.

### **Mit Microsoft Excel**

So platzieren Sie ein Listenfeld-Steuerelement in einem Arbeitsblatt:

1.  Stellen Sie sicher, dass**Formen** Symbolleiste wird angezeigt.
1.  Klick auf das**Listenfeld** Werkzeug.
1. Klicken und ziehen Sie in Ihrem Arbeitsblattbereich, um das Rechteck zu definieren, das das Listenfeld enthält.
1.  Sobald das Listenfeld im Arbeitsblatt platziert ist, klicken Sie mit der rechten Maustaste auf das Steuerelement, um es anzuklicken**Formatsteuerung** und geben Sie den Eingangsbereich an.
1.  In dem**Cell Verbindung**Geben Sie die Adresse der Zelle an, mit der dieses Listenfeld verknüpft werden soll, und legen Sie das Attribut Auswahltyp (Einzeln, Mehrfach, Erweitern) fest
1.  Klicken**OK**.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) -Klasse stellt eine Methode namens addShape bereit, die zum Hinzufügen eines Listenfeld-Steuerelements zu einem Arbeitsblatt verwendet wird. Die Methode gibt ein ListBox-Objekt zurück. Die Klasse ListBox repräsentiert eine Listbox. Es hat einige wichtige Mitglieder:

- Die Methode setLinkedCell gibt eine Zelle an, die mit der Listbox verknüpft ist.
- Die setInputRange-Methode gibt den Arbeitsblattbereich von Zellen an, die zum Füllen des Listenfelds verwendet werden.
- Die Methode setSelectionType gibt den Auswahlmodus der Listbox an.
- Die setShadow-Methode gibt an, ob das Listenfeld eine 3D-Schattierung hat.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt ein Listenfeld hinzufügen. Beim Ausführen des Codes wird die folgende Ausgabe generiert.

**Dem Arbeitsblatt wird ein Listenfeld hinzugefügt** 

![todo: Bild_alt_Text](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

## **Schaltflächen-Steuerelement zu einem Arbeitsblatt hinzufügen**

Schaltflächen sind nützlich, um einige Aktionen auszuführen. Manchmal ist es hilfreich, der Schaltfläche ein VBA-Makro zuzuweisen oder einen Hyperlink zum Öffnen einer Webseite zuzuweisen.

### **Mit Microsoft Excel**

So platzieren Sie ein Schaltflächen-Steuerelement in Ihrem Arbeitsblatt:

1.  Stellen Sie sicher, dass**Formen** Symbolleiste wird angezeigt.
1.  Klick auf das**Taste** Werkzeug.
1. Klicken und ziehen Sie in Ihrem Arbeitsblattbereich, um das Rechteck zu definieren, das die Schaltfläche halten wird.
1.  Sobald das Listenfeld im Arbeitsblatt platziert ist, klicken Sie mit der rechten Maustaste auf das Steuerelement und wählen Sie es aus**Formatsteuerung**, geben Sie dann ein VBA-Makro und Attribute für Schriftart, Ausrichtung, Größe, Rand usw. an.
1.  Klicke auf**OK**.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) Die Klasse stellt eine Methode namens addShape bereit, die zum Hinzufügen eines Schaltflächen-Steuerelements zum Arbeitsblatt verwendet wird. Die Methode kann ein Button-Objekt zurückgeben. Die Klasse Button repräsentiert eine Schaltfläche. Es hat einige wichtige Mitglieder:

- Die setText-Methode gibt die Beschriftung der Schaltfläche an.
- Die setPlacement-Methode gibt den PlacementType an, also die Art und Weise, wie die Schaltfläche an die Zellen im Arbeitsblatt angehängt wird.
- Die addHyperlink-Methode fügt einen Hyperlink für das Schaltflächen-Steuerelement hinzu. Durch Klicken auf die Schaltfläche wird zur zugehörigen URL navigiert.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt eine Schaltfläche hinzufügen. Beim Ausführen des Codes wird die folgende Ausgabe generiert

**Im Arbeitsblatt wird eine Schaltfläche hinzugefügt**

![todo: Bild_alt_Text](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **Hinzufügen einer Liniensteuerung zu einem Arbeitsblatt**

Aspose.Cells ermöglicht Ihnen das Zeichnen von Autoshapes in Ihren Arbeitsblättern. Sie können ganz einfach eine Linie erstellen. Sie dürfen die Zeile auch formatieren. Sie können beispielsweise die Farbe der Linie ändern, das Gewicht und den Stil der Linie für Ihre Bedürfnisse festlegen.

### **Mit Microsoft Excel**

1.  Auf der**Zeichnung** Symbolleiste, klicken Sie auf**AutoFormen** , zeigen auf**Linien**, und wählen Sie den gewünschten Linienstil aus.
1. Ziehen Sie, um die Linie zu zeichnen.
1. Führen Sie einen oder beide der folgenden Schritte aus:
 1. Um die Linie auf einen 15-Grad-Winkel von ihrem Startpunkt zu beschränken, halten Sie beim Ziehen die UMSCHALTTASTE gedrückt.
 1. Um die Linie vom ersten Endpunkt in entgegengesetzte Richtungen zu verlängern, halten Sie beim Ziehen die STRG-Taste gedrückt.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)Die Klasse stellt eine Methode namens addShape bereit, die verwendet wird, um dem Arbeitsblatt eine Linienform hinzuzufügen. Die Methode kann ein LineShape-Objekt zurückgeben. Die Klasse LineShape repräsentiert eine Linie. Es hat einige wichtige Mitglieder:

- Die Methode setDashStyle gibt das Format einer Zeile an.
- Die setPlacement-Methode gibt den PlacementType an, die Art und Weise, wie die Linie an die Zellen im Arbeitsblatt angehängt wird.

Das folgende Beispiel zeigt, wie dem Arbeitsblatt Zeilen hinzugefügt werden. Es erstellt drei Linien mit unterschiedlichen Stilen. Die folgende Ausgabe wird nach der Ausführung des Codes generiert

**Im Arbeitsblatt werden einige Zeilen hinzugefügt** 

![todo: Bild_alt_Text](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **Hinzufügen einer Pfeilspitze zu einer Linie**

Mit Aspose.Cells können Sie auch Pfeillinien zeichnen. Es ist möglich, einer Linie eine Pfeilspitze hinzuzufügen und die Linie zu formatieren. Sie können beispielsweise die Farbe der Linie ändern oder die Stärke und den Stil der Linie festlegen.

Das folgende Beispiel zeigt, wie Sie einer Linie eine Pfeilspitze hinzufügen. Beim Ausführen des Codes wird die folgende Ausgabe generiert.

**Im Arbeitsblatt wird eine Zeile mit Pfeilspitze hinzugefügt** 

![todo: Bild_alt_Text](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **Rectangle Control zu einem Arbeitsblatt hinzufügen**

Aspose.Cells ermöglicht es Ihnen, rechteckige Formen in Ihren Arbeitsblättern zu zeichnen. Sie können ein Rechteck, ein Quadrat usw. erstellen. Sie können auch die Füllfarbe und die Farbe der Rahmenlinie des Steuerelements formatieren. Sie können beispielsweise die Farbe des Rechtecks ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil des Rechtecks nach Bedarf festlegen.

### **Mit Microsoft Excel**

1.  Auf der**Zeichnung** Symbolleiste, klicken Sie auf**Rechteck**.
1. Ziehen Sie, um das Rechteck zu zeichnen.
1. Führen Sie einen oder beide der folgenden Schritte aus:
 1. Um das Rechteck so zu beschränken, dass ein Quadrat von seinem Startpunkt gezeichnet wird, halten Sie beim Ziehen die UMSCHALTTASTE gedrückt.
 1. Um ein Rechteck von einem Mittelpunkt aus zu zeichnen, halten Sie beim Ziehen die STRG-Taste gedrückt.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) -Klasse stellt eine Methode namens addShape bereit, die verwendet wird, um einem Arbeitsblatt eine rechteckige Form hinzuzufügen. Die Methode kann ein RectangleShape-Objekt zurückgeben. Die Klasse RectangleShape repräsentiert ein Rechteck. Es hat einige wichtige Mitglieder:

- Die Methode setLineFormat gibt die Linienformatattribute eines Rechtecks an.
- Die setPlacement-Methode gibt den PlacementType an, die Art und Weise, wie das Rechteck an die Zellen im Arbeitsblatt angefügt wird.
- Die FillFormat-Eigenschaft gibt die Füllformatstile eines Rechtecks an.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt ein Rechteck hinzufügen. Beim Ausführen des Codes wird die folgende Ausgabe generiert.

**Dem Arbeitsblatt wird ein Rechteck hinzugefügt** 

![todo: Bild_alt_Text](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **Bogensteuerung zum Arbeitsblatt hinzufügen**

Aspose.Cells ermöglicht Ihnen das Zeichnen von Bogenformen in Ihren Arbeitsblättern. Sie können einfache und gefüllte Bögen erstellen. Sie dürfen die Füllfarbe und die Rahmenfarbe des Steuerelements formatieren. Sie können beispielsweise die Farbe des Bogens angeben / ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil der Form für Ihren Bedarf festlegen.

### **Mit Microsoft Excel**

1.  Auf der**Zeichnung** Symbolleiste, klicken Sie auf**Bogen** in dem**AutoFormen**.
1. Ziehen Sie, um den Bogen zu zeichnen.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) Die Klasse stellt eine Methode namens addShape bereit, die verwendet wird, um dem Arbeitsblatt eine Bogenform hinzuzufügen. Die Methode kann ein ArcShape-Objekt zurückgeben. Die Klasse ArcShape repräsentiert einen Bogen. Es hat einige wichtige Mitglieder:

- Die setLineFormat-Methode gibt die Linienformatattribute einer Bogenform an.
- Die setPlacement-Methode gibt den PlacementType an, die Art und Weise, wie der Bogen an die Zellen im Arbeitsblatt angefügt wird.
- Die FillFormat-Eigenschaft gibt die Füllformatstile der Form an.

Das folgende Beispiel zeigt, wie dem Arbeitsblatt Bogenformen hinzugefügt werden. Das Beispiel erstellt zwei Bogenformen: eine ist gefüllt und die andere einfach. Beim Ausführen des Codes wird die folgende Ausgabe generiert

**Dem Arbeitsblatt werden zwei Bogenformen hinzugefügt** 

![todo: Bild_alt_Text](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **Oval Control zu einem Arbeitsblatt hinzufügen**

Aspose.Cells ermöglicht es Ihnen, ovale Formen in Arbeitsblätter zu zeichnen. Erstellen Sie einfache und gefüllte ovale Formen und formatieren Sie die Füllfarbe und die Rahmenlinienfarbe des Steuerelements. Sie können beispielsweise die Farbe des Ovals festlegen / ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil der Form festlegen.

### **Mit Microsoft Excel**

1.  Auf der**Zeichnung** Symbolleiste, klicken Sie auf**Oval** .
1. Ziehen Sie, um das Oval zu zeichnen.
1. Führen Sie einen oder beide der folgenden Schritte aus:
 1. Um das Oval so zu zwingen, dass es von seinem Startpunkt aus einen Kreis zeichnet, halten Sie beim Ziehen die UMSCHALTTASTE gedrückt.
1. Um ein Oval von einem Mittelpunkt aus zu zeichnen, halten Sie beim Ziehen die STRG-Taste gedrückt.

### **Mit Aspose.Cells**

 Das[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) -Klasse stellt eine Methode namens addShape bereit, die verwendet wird, um einem Arbeitsblatt eine ovale Form hinzuzufügen. Die Methode kann ein Oval-Objekt zurückgeben. Die Klasse Oval repräsentiert eine ovale Form. Es hat einige wichtige Mitglieder:

- Die setLineFormat-Methode gibt die Linienformatattribute einer ovalen Form an.
-  Die setPlacement-Methode gibt die**Platzierungstyp** , die Art und Weise, wie das Oval mit den Zellen im Arbeitsblatt verbunden ist.
- Die FillFormat-Eigenschaft gibt die Füllformatstile der Form an.

Das folgende Beispiel zeigt, wie Sie dem Arbeitsblatt ovale Formen hinzufügen. Das Beispiel erstellt zwei ovale Formen: eine ist ein gefülltes Oval, die andere ein einfacher Kreis. Beim Ausführen des Codes wird die folgende Ausgabe generiert.

**Dem Arbeitsblatt werden zwei ovale Formen hinzugefügt** 

![todo: Bild_alt_Text](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **Themen vorantreiben**
- [Fügen Sie ActiveX-Steuerelemente mit Aspose.Cells hinzu](/cells/de/java/add-activex-controls-using-aspose-cells/)
- [Entfernen Sie das ActiveX-Steuerelement](/cells/de/java/remove-activex-control/)
