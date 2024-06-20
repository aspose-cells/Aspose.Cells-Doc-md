---
title: Steuerelemente verwalten
type: docs
weight: 120
url: /de/java/managing-controls/
---

## **Einführung**

Entwickler können verschiedene Zeichenobjekte wie Textfelder, Kontrollkästchen, Optionsfelder, Kombinationsfelder, Beschriftungen, Schaltflächen, Linien, Rechtecke, Bögen, Ovale, Spinner, Bildlaufleisten, Gruppenfelder usw. hinzufügen. Aspose.Cells bietet den Aspose.Cells.Drawing-Namespace, der alle Zeichenobjekte enthält. Es gibt jedoch einige Zeichenobjekte oder Formen, die noch nicht unterstützt werden. Erstellen Sie diese Zeichenobjekte in einem Designer-Arbeitsblatt mit Microsoft Excel und importieren Sie das Designer-Arbeitsblatt dann in Aspose.Cells. Aspose.Cells ermöglicht es Ihnen, diese Zeichenobjekte aus einem Designer-Arbeitsblatt zu laden und in eine erstellte Datei zu schreiben.

## **TextBox-Steuerung zur Arbeitsmappe hinzufügen**

Eine Möglichkeit, wichtige Informationen in einem Bericht zu betonen, besteht darin, ein Textfeld zu verwenden. Zum Beispiel fügen Sie Text hinzu, um den Firmennamen hervorzuheben oder um die geografische Region mit den höchsten Verkäufen anzugeben usw. Aspose.Cells bietet die TextBoxes-Klasse, die verwendet wird, um ein neues Textfeld zur Sammlung hinzuzufügen. Es gibt eine weitere Klasse, [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox), die ein Textfeld darstellt, das verwendet wird, um alle Arten von Einstellungen zu definieren. Es hat einige wichtige Elemente:

- Die Methode [**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame) gibt ein [**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame)-Objekt zurück, das zur Anpassung des Inhalts des Textfelds verwendet wird.
- Die Methode [**setPlacement**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) gibt den Platzierungstyp an.
- Die Methode [**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font) gibt die Schriftattribute an.
- Die Methode [**addHyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink(java.lang.String)) fügt dem Textfeld einen Hyperlink hinzu.
- Die Eigenschaft [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat) gibt ein [**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat)-Objekt zurück, das zur Festlegung des Füllformats für das Textfeld verwendet wird.
- Die Eigenschaft [**LineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat) gibt normalerweise das [**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat)-Objekt zurück, das zur Formatierung und Gewichtung der Textfeldlinie verwendet wird.
- Die Methode [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text) gibt den Eingabetext für das Textfeld an.

Im folgenden Beispiel werden zwei Textfelder im ersten Arbeitsblatt der Arbeitsmappe erstellt. Das erste Textfeld ist gut ausgestattet mit verschiedenen Formatierungseinstellungen. Das zweite ist einfach gehalten.

Die folgende Ausgabe wird durch Ausführen des Codes generiert:

**Zwei Textfelder werden im Arbeitsblatt erstellt** 

![todo:image_alt_text](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **Manipulation von Textfeldsteuerelementen in den Designer-Arbeitsmappen**

Aspose.Cells ermöglicht es Ihnen auch, auf Textfelder in den Designer-Arbeitsblättern zuzugreifen und diese zu manipulieren. Verwenden Sie die Eigenschaft [**Worksheet.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes), um die Textfelder-Sammlung im Blatt zu erhalten.

Im folgenden Beispiel wird die Microsoft Excel-Datei – tsttextboxes.xls – verwendet, die im obigen Beispiel erstellt wurde. Es werden die Textzeichenfolgen der beiden Textfelder abgerufen und der Text des zweiten Textfelds geändert, um die Datei zu speichern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **Hinzufügen eines Kontrollkästchen-Steuerelements zum Arbeitsblatt**

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

Aspose.Cells bietet die Klasse [**CheckBoxCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection), die verwendet wird, um ein neues Kontrollkästchen der Sammlung hinzuzufügen. Es gibt eine weitere Klasse, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox), die ein Kontrollkästchen darstellt. Es hat einige wichtige Elemente:

- Die Methode [**setLinkedCell**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell) gibt eine Zelle an, die mit dem Kontrollkästchen verknüpft ist.
- Die Methode [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text) gibt die mit dem Kontrollkästchen verknüpfte Textzeichenfolge an. Es ist das Etikett des Kontrollkästchens.
- Die Methode [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value) gibt an, ob das Kontrollkästchen ausgewählt ist oder nicht.

Das folgende Beispiel zeigt, wie man ein Kontrollkästchen zum Arbeitsblatt hinzufügt. Die Ausgabe unten wird nach Ausführen des Codes generiert.

**Ein Kontrollkästchen wird zum Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **Hinzufügen einer Optionsfeldsteuerelement zum Arbeitsblatt**

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

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) bietet eine Methode namens addShape, die verwendet werden kann, um ein Optionsfeldsteuerelement zu einem Arbeitsblatt hinzuzufügen. Die Methode kann ein RadioButton-Objekt zurückgeben. Die Klasse RadioButton repräsentiert ein Optionsfeld. Sie verfügt über einige wichtige Elemente:

- Die Methode setLinkedCell gibt eine Zelle an, mit der das Optionsfeld verbunden ist.
- Die Methode setText gibt den mit dem Optionsfeld verbundenen Textstring an. Es handelt sich um das Etikett des Optionsfelds.
- Die Eigenschaft Checked gibt an, ob das Optionsfeld ausgewählt ist oder nicht.
- Die Methode setFillFormat gibt das Füllformat des Optionsfelds an.
- Die Methode setLineFormat gibt die Linienformatstile des Optionsfelds an.

Das folgende Beispiel zeigt, wie man Optionsfelder zum Arbeitsblatt hinzufügt. Das Beispiel fügt drei Optionsfelder hinzu, die Altersgruppen repräsentieren. Die folgende Ausgabe würde nach Ausführen des Codes generiert.

**Einige Optionsfelder sind dem Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

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

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) bietet eine Methode namens addShape, die zum Hinzufügen eines Kombinationsfeld-Steuerelements zum Arbeitsblatt verwendet werden kann. Die Methode gibt das ComboBox-Objekt zurück. Die Klasse ComboBox repräsentiert ein Kombinationsfeld. Sie hat einige wichtige Elemente:

- Die Methode setLinkedCell gibt eine mit dem Kombinationsfeld verknüpfte Zelle an.
- Die Methode setInputRange gibt den Arbeitsblattbereich der Zellen an, die zum Füllen des Kombinationsfelds verwendet werden.
- Die Methode setDropDownLines gibt die Anzahl der in dem Kombinationsfeld angezeigten Listeneinträge im Dropdown-Bereich an.
- Die Methode setShadow gibt an, ob das Kombinationsfeld 3D-Schattierung hat.

Das folgende Beispiel zeigt, wie ein Kombinationsfeld zum Arbeitsblatt hinzugefügt wird. Der folgende Ausgang wird beim Ausführen des Codes generiert.

**Ein Kombinationsfeld wird im Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **Hinzufügen eines Beschriftungssteuerelements zu einem Arbeitsblatt**

Beschriftungen dienen dazu, Benutzern Informationen über den Inhalt einer Kalkulationstabelle bereitzustellen. Aspose.Cells ermöglicht das Hinzufügen und Manipulieren von Beschriftungen in einem Arbeitsblatt. Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) bietet eine Methode namens addShape, mit der ein Beschriftungssteuerelement zum Arbeitsblatt hinzugefügt werden kann. Die Methode gibt ein Label-Objekt zurück. Die Klasse Label repräsentiert eine Beschriftung im Arbeitsblatt. Sie hat einige wichtige Elemente:

- Die Methode setText gibt einen Beschriftungstext an.
- Die Methode setPlacement gibt den PlacementType an, die Art und Weise, wie die Beschriftung an die Zellen im Arbeitsblatt angehängt ist.

Das folgende Beispiel zeigt, wie einem Arbeitsblatt eine Beschriftung hinzugefügt wird. Der folgende Ausgang wird beim Ausführen des Codes generiert.

**Ein Label wird im Arbeitsblatt hinzugefügt**

![todo:image_alt_text](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

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

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) enthält eine Methode namens addShape, die verwendet wird, um einem Arbeitsblatt eine Listfeld-Steuerung hinzuzufügen. Die Methode gibt ein ListBox-Objekt zurück. Die Klasse ListBox repräsentiert ein Listenfeld. Sie hat einige wichtige Elemente:

- Die Methode setLinkedCell legt eine Zelle fest, die mit dem Listenfeld verknüpft ist.
- Die Methode setInputRange gibt den Arbeitsblattbereich von Zellen an, der verwendet wird, um das Listenfeld aufzufüllen.
- Die Methode setSelectionType legt den Auswahlmodus des Listenfelds fest.
- Die Methode setShadow gibt an, ob das Listenfeld eine 3D-Schattierung hat.

Das folgende Beispiel zeigt, wie ein Listenfeld dem Arbeitsblatt hinzugefügt wird. Der folgende Output wird generiert, wenn der Code ausgeführt wird.

**Ein Listenfeld wird dem Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

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

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) stellt eine Methode namens addShape bereit, die verwendet wird, um eine Schaltflächensteuerung dem Arbeitsblatt hinzuzufügen. Die Methode kann ein Button-Objekt zurückgeben. Die Button-Klasse stellt eine Schaltfläche dar. Sie verfügt über einige wichtige Elemente:

- Die setText-Methode gibt die Beschriftung der Schaltfläche an.
- Die setPlacement-Methode gibt den PlacementType an, die Art und Weise, wie die Schaltfläche mit den Zellen im Arbeitsblatt verbunden ist.
- Die addHyperlink-Methode fügt der Schaltflächensteuerung einen Hyperlink hinzu. Durch Klicken auf die Schaltfläche wird zu der entsprechenden URL navigiert.

Das folgende Beispiel zeigt, wie Sie eine Schaltfläche dem Arbeitsblatt hinzufügen. Der folgende Output wird generiert, wenn der Code ausgeführt wird

**Eine Schaltfläche wird dem Arbeitsblatt hinzugefügt**

![todo:image_alt_text](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **Hinzufügen einer Liniensteuerung zu einem Arbeitsblatt**

Aspose.Cells ermöglicht es Ihnen, Autoshapes in Ihren Arbeitsblättern zu zeichnen. Sie können eine Linie einfach erstellen. Sie dürfen die Linie auch formatieren. Sie können beispielsweise die Farbe der Linie ändern, das Gewicht und den Stil der Linie nach Bedarf festlegen.

### **Verwendung von Microsoft Excel**

1. Auf der **Zeichnen**-Symbolleiste klicken Sie auf **AutoFormen**, zeigen auf **Linien** und wählen den Linienstil aus, den Sie möchten.
1. Ziehen Sie, um die Linie zu zeichnen.
1. Führen Sie einen oder beide der folgenden Schritte aus:
   1. Um die Linie auf 15-Grad-Winkel von ihrem Ausgangspunkt zu beschränken, halten Sie die UMSCHALTTASTE gedrückt, während Sie ziehen.
   1. Um die Linie in entgegengesetzte Richtungen vom ersten Endpunkt zu verlängern, halten Sie STRG gedrückt, während Sie ziehen.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) bietet eine Methode namens addShape, die verwendet wird, um eine Linienform dem Arbeitsblatt hinzuzufügen. Die Methode kann ein LineShape-Objekt zurückgeben. Die LineShape-Klasse stellt eine Linie dar. Sie verfügt über einige wichtige Elemente:

- Die setDashStyle-Methode gibt das Format einer Linie an.
- Die setPlacement-Methode gibt den PlacementType an, die Art und Weise, wie die Linie mit den Zellen im Arbeitsblatt verbunden ist.

Das folgende Beispiel zeigt, wie Linien zum Arbeitsblatt hinzugefügt werden. Es erstellt drei Linien mit unterschiedlichen Stilen. Die folgende Ausgabe wird nach Ausführung des Codes generiert

**Ein paar Linien werden im Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **Hinzufügen einer Pfeilspitze zu einer Linie**

Aspose.Cells ermöglicht es auch, Pfeillinien zu zeichnen. Es ist möglich, einer Linie eine Pfeilspitze hinzuzufügen und die Linie zu formatieren. Sie können z.B. die Farbe der Linie ändern oder das Gewicht und den Stil der Linie festlegen.

Das folgende Beispiel zeigt, wie eine Pfeilspitze zu einer Linie hinzugefügt wird. Die folgende Ausgabe wird generiert, wenn der Code ausgeführt wird.

**Eine Linie mit Pfeilspitze wird im Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **Hinzufügen einer Rechtecksteuerung zu einem Arbeitsblatt**

Aspose.Cells ermöglicht es Ihnen, Rechteckformen in Ihren Arbeitsblättern zu zeichnen. Sie können ein Rechteck, ein Quadrat usw. erstellen. Es ist auch möglich, die Füllfarbe und die Rahmenlinienfarbe der Steuerung zu formatieren. Sie können z.B. die Farbe des Rechtecks ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil des Rechtecks spezifizieren, wie Sie es benötigen.

### **Verwendung von Microsoft Excel**

1. Klicken Sie auf der **Zeichnen**-Symbolleiste auf **Rechteck**.
1. Ziehen Sie, um das Rechteck zu zeichnen.
1. Führen Sie einen oder beide der folgenden Schritte aus:
   1. Halten Sie die UMSCHALTTASTE gedrückt, um das Rechteck zu zeichnen und so ein Quadrat von seinem Ausgangspunkt aus zu beschränken.
   1. Halten Sie STRG gedrückt, um ein Rechteck von einem Mittelpunkt aus zu zeichnen.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) bietet eine Methode namens addShape, die verwendet wird, um eine Rechteckform zum Arbeitsblatt hinzuzufügen. Die Methode kann ein RectangleShape-Objekt zurückgeben. Die Klasse RectangleShape repräsentiert ein Rechteck. Sie hat einige wichtige Elemente:

- Die Methode setLineFormat spezifiziert die Linienformatattribute eines Rechtecks.
- Die Methode setPlacement spezifiziert den PlacementType, die Art und Weise, wie das Rechteck an die Zellen im Arbeitsblatt angehängt ist.
- Die Eigenschaft FillFormat spezifiziert die Füllformatstile eines Rechtecks.

Das folgende Beispiel zeigt, wie ein Rechteck zum Arbeitsblatt hinzugefügt wird. Die folgende Ausgabe wird generiert, wenn der Code ausgeführt wird.

**Ein Rechteck wird im Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **Hinzufügen einer Bogensteuerung zum Arbeitsblatt**

Aspose.Cells ermöglicht es Ihnen, Bogenformen in Ihren Arbeitsblättern zu zeichnen. Sie können einfache und gefüllte Bogen erstellen. Sie können die Füllfarbe und die Randlinienfarbe des Steuerelements formatieren. Sie können zum Beispiel die Farbe des Bogens festlegen/ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil der Form nach Bedarf festlegen.

### **Verwendung von Microsoft Excel**

1. Klicken Sie in der Symbolleiste **Zeichnen** auf **Bogen** in den **AutoFormen**.
1. Ziehen Sie, um den Bogen zu zeichnen.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) bietet eine Methode namens addShape, die verwendet wird, um eine Bogenform dem Arbeitsblatt hinzuzufügen. Die Methode kann ein ArcShape-Objekt zurückgeben. Die Klasse ArcShape stellt einen Bogen dar. Sie hat einige wichtige Elemente:

- Die Methode setLineFormat legt die Linienformatattribute einer Bogenform fest.
- Die Methode setPlacement gibt den PlacementType an, die Art und Weise, wie der Bogen an die Zellen im Arbeitsblatt angefügt ist.
- Die FillFormat-Eigenschaft gibt die Füllformatstile der Form an.

Im folgenden Beispiel wird gezeigt, wie Bogenformen dem Arbeitsblatt hinzugefügt werden. Das Beispiel erstellt zwei Bogenformen: eine gefüllte und eine einfache. Die folgende Ausgabe wird erzeugt, wenn der Code ausgeführt wird

**Zwei Bogenformen werden dem Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **Ovale Steuerung zu einem Arbeitsblatt hinzufügen**

Mit Aspose.Cells können Sie ovale Formen in Arbeitsblättern zeichnen. Erstellen Sie einfache und gefüllte ovale Formen und formatieren Sie die Füllfarbe und die Randlinienfarbe des Steuerelements. Sie können zum Beispiel die Farbe des Ovals spezifizieren/ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil der Form festlegen.

### **Verwendung von Microsoft Excel**

1. Klicken Sie in der Symbolleiste **Zeichnen** auf **Oval** .
1. Ziehen Sie, um das Oval zu zeichnen.
1. Führen Sie einen oder beide der folgenden Schritte aus:
   1. Halten Sie beim Ziehen, um das Oval zu einem Kreis von seinem Startpunkt zu beschränken, die UMSCHALTTASTE gedrückt.
   1. Halten Sie beim Ziehen eines Ovals von einem Mittelpunkt aus die STRG-TASTE gedrückt.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) bietet eine Methode namens addShape, die verwendet wird, um eine ovale Form einem Arbeitsblatt hinzuzufügen. Die Methode kann ein Oval-Objekt zurückgeben. Die Klasse Oval stellt eine ovale Form dar. Sie hat einige wichtige Elemente:

- Die Methode setLineFormat legt die Linienformatattribute einer ovalen Form fest.
- Die Methode setPlacement gibt den **PlacementType** an, die Art und Weise, wie das Oval an die Zellen im Arbeitsblatt angefügt ist.
- Die FillFormat-Eigenschaft gibt die Füllformatstile der Form an.

Das folgende Beispiel zeigt, wie ovale Formen dem Arbeitsblatt hinzugefügt werden. Das Beispiel erstellt zwei ovale Formen: ein gefülltes Oval und einen einfachen Kreis. Der folgende Output wird generiert, wenn der Code ausgeführt wird.

**Zwei ovale Formen werden dem Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **Erweiterte Themen**
- [AktiveX-Steuerelemente mit Aspose.Cells hinzufügen](/cells/de/java/add-activex-controls-using-aspose-cells/)
- [AktiveX-Steuerung entfernen](/cells/de/java/remove-activex-control/)
