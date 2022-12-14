---
title: Steuerelemente in Diagrammen
linktitle: Formen im Diagramm
type: docs
weight: 60
url: /de/java/controls-in-charts/
---
{{% alert color="primary" %}}

Manchmal müssen Sie Zeichnungsobjekte wie Beschriftungen, Textfelder, Bilder usw. in ein Diagramm einfügen. Aspose.Cells kann die Steuerelemente zur Laufzeit zu einem Diagramm hinzufügen.

{{% /alert %}}

## **Label Control zum Diagramm hinzufügen**

Labels bieten eine Möglichkeit, Benutzern Informationen über den Inhalt einer Tabelle zu geben. Aspose.Cells ermöglicht das Hinzufügen und Bearbeiten von Beschriftungen sogar in Diagrammen.

 Das[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) Die Klasse stellt eine Methode mit dem Namen bereit[**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart(int,%20int,%20int,%20int)), die zum Hinzufügen eines Label-Steuerelements zu einem Diagramm verwendet wird. Nachfolgend finden Sie eine Liste der für das Verfahren verwendeten Parameter:

- **oben** – der vertikale Versatz des Etiketts von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **links** – der vertikale Versatz des Etiketts von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **Höhe** – die Höhe des Etiketts in Einheiten von 1/4000 des Diagrammbereichs.
- **Breite** – die Breite des Etiketts in Einheiten von 1/4000 des Diagrammbereichs.

 Die Methode gibt ein Objekt der zurück[**Etikett**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) Klasse, wo die[**Etikett**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)Klasse stellt eine Bezeichnung im Diagramm dar. Es hat einige wichtige Mitglieder, wie unten beschrieben:

- [**Text**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text)-Eigenschaft gibt die Beschriftungszeichenfolge eines Labels an.
- [**Füllen**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) -Eigenschaft gibt die Füllfarbenattribute an.

Das folgende Beispiel zeigt, wie Sie dem Diagramm eine Beschriftung hinzufügen. Das Beispiel verwendet eine Designerdatei, die ein Diagramm enthält. Wir verwenden diese Datei, um eine Beschriftung in das Diagramm einzufügen.

Unten ist ein Screenshot der Designer-Datei.

**Das Designer-Diagramm**

![todo: Bild_alt_Text](controls-in-charts_1.png)

Unten ist der ursprüngliche Code zum Hinzufügen einer Beschriftung zum Diagramm. Beim Ausführen des Codes wird die folgende Ausgabe generiert.

**Dem Diagramm wird eine Beschriftung hinzugefügt**

![todo: Bild_alt_Text](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **TextBox-Steuerelement zum Diagramm hinzufügen**

 Eine Möglichkeit, wichtige Informationen in einem Bericht hervorzuheben, ist die Verwendung eines Textfelds. Geben Sie beispielsweise Text ein, um den Firmennamen hervorzuheben oder die geografische Region mit den höchsten Umsätzen anzugeben. Das[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) Die Klasse stellt eine Methode mit dem Namen bereit[**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart(int,%20int,%20int,%20int)), die verwendet wird, um einem Diagramm ein Textfeld-Steuerelement hinzuzufügen. Es folgt die für die Methode verwendete Parameterliste:

- **oben** – der vertikale Abstand des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **links** – der vertikale Abstand des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **Höhe**– die Höhe des Textfelds in Einheiten von 1/4000 des Diagrammbereichs.
- **Breite** – die Breite des Textfelds in Einheiten von 1/4000 des Diagrammbereichs.

 Die Methode gibt ein Objekt der zurück[**Textfeld**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) Klasse, wo die[**Textfeld**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)Klasse repräsentiert ein Textfeld im Diagramm.

Das folgende Beispiel zeigt, wie Sie einem Diagramm ein Textfeld hinzufügen. Das Beispiel verwendet die vorherige Designerdatei, die ein Diagramm enthält. Wir verwenden diese Datei, um ein Textfeld in das Diagramm einzufügen, um den Diagrammtitel anzuzeigen.

Unten ist der ursprüngliche Code zum Hinzufügen eines Textfelds zum Diagramm. Beim Ausführen des Codes wird die folgende Ausgabe generiert.

**Im Diagramm wird ein Textfeld hinzugefügt**

![todo: Bild_alt_Text](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **Bild zum Diagramm hinzufügen**

Mit Aspose.Cells können Sie Bilder in ein Diagramm einfügen. Fügen Sie beispielsweise ein Bild hinzu, um ein Diagramm oder seinen Inhalt hervorzuheben oder ihm mehr Bedeutung zu verleihen, oder fügen Sie eine Markenbilddatei ein.

 Das[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) Die Klasse stellt eine Methode mit dem Namen bereit[**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart(int,%20int,%20java.io.InputStream,%20int,%20int)), die zum Hinzufügen eines Bildobjekts zum Diagramm verwendet wird. Es folgt die für die Methode verwendete Parameterliste:

- **oben**– der vertikale Abstand des Bildes von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **links**– der vertikale Abstand des Bildes von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **Strom** – ein Stream-Objekt, das die Bilddaten enthält.
- **widthScale** – die Skala der Bildbreite, ein Prozentwert.
- **Höhenskala** – die Skala der Bildhöhe, ein Prozentwert.

 Die Methode gibt ein Objekt der zurück[**Bild**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) Klasse, wo die[**Bild**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)Die Klasse repräsentiert ein Bildobjekt im Diagramm.

Das folgende Beispiel zeigt, wie Sie dem Diagramm ein Bild hinzufügen. Das Beispiel verwendet die vorherige Designerdatei, die ein Diagramm enthält. Wir verwenden diese Datei, um ein Bild in das Diagramm einzufügen.

Unten ist der ursprüngliche Code zum Hinzufügen eines Bildes zum Diagramm. Beim Ausführen des Codes wird die folgende Ausgabe generiert

**Ein Bild wird in das Diagramm eingefügt**

![todo: Bild_alt_Text](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **Kontrollkästchen im Diagramm hinzufügen**

Aspose.Cells ermöglicht es Ihnen, Kontrollkästchen in ein Diagrammblatt einzufügen, indem Sie verwenden[**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType) Aufzählung. Das folgende Beispiel zeigt das Hinzufügen eines Kontrollkästchens zu einem Diagrammblatt.

Das folgende Bild zeigt das Diagrammblatt mit dem Kontrollkästchen in der Ausgabedatei.

![todo: Bild_alt_Text](controls-in-charts_5.jpg)

Das[Ausgabedatei](InsertCheckboxInChartSheet_out.xlsx)generiert durch das folgende Code-Snippet ist als Referenz beigefügt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
