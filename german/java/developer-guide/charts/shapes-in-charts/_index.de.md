---
title: Steuerelemente in Diagrammen
linktitle: Formen im Diagramm
type: docs
weight: 60
url: /de/java/controls-in-charts/
---

{{% alert color="primary" %}}

Manchmal müssen Sie Zeichenobjekte wie Beschriftungen, Textfelder, Bilder usw. in ein Diagramm einfügen. Aspose.Cells kann die Steuerelemente zur Laufzeit zu einem Diagramm hinzufügen.

{{% /alert %}}

## **Hinzufügen von Beschriftungssteuerung zum Diagramm**

Labels bieten eine Möglichkeit, Benutzern Informationen über den Inhalt eines Tabellenblatts zu geben. Aspose.Cells ermöglicht es Ihnen, Labels hinzuzufügen und zu manipulieren, sogar in Diagrammen.

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) bietet eine Methode namens [**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart-int-int-int-int-), die verwendet wird, um eine Label-Steuerung zu einem Diagramm hinzuzufügen. Hier ist eine Liste der für die Methode verwendeten Parameter:

- **top** – der vertikale Versatz der Beschriftung von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Versatz der Beschriftung von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **height** – die Höhe der Beschriftung, in Einheiten von 1/4000 des Diagrammbereichs.
- **width** – die Breite des Labels in Einheiten von 1/4000 des Diagrammbereichs.

Die Methode gibt ein Objekt der Klasse [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) zurück, wobei die Klasse [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) ein Label im Diagramm darstellt. Sie hat einige wichtige Elemente, wie nachstehend detailliert beschrieben:

- Die Eigenschaft [**Text**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text) gibt einen Beschriftungsstring an.
- Die Eigenschaft [**Fill**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) gibt die Füllfarbeattribute an.

Das folgende Beispiel zeigt, wie ein Label zum Diagramm hinzugefügt wird. Das Beispiel verwendet eine Designerdatei, die ein Diagramm enthält. Wir verwenden diese Datei, um ein Label in das Diagramm einzufügen.

Hier ist ein Screenshot der Designerdatei.

**Das Designer-Diagramm**

![todo:image_alt_text](controls-in-charts_1.png)

Hier ist der ursprüngliche Code zum Hinzufügen eines Labels zum Diagramm. Der folgende Ausgang wird beim Ausführen des Codes generiert.

**Ein Label wird im Diagramm hinzugefügt**

![todo:image_alt_text](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **Hinzufügen einer Textfeldsteuerung zum Diagramm**

Eine Möglichkeit, wichtige Informationen in einem Bericht hervorzuheben, besteht darin, einen Textbereich zu verwenden. Geben Sie beispielsweise Text ein, um den Firmennamen hervorzuheben oder das geografische Gebiet mit den höchsten Verkäufen anzuzeigen. Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) stellt eine Methode namens [**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart-int-int-int-int-) zur Verfügung, die verwendet wird, um dem Diagramm eine Textfeldsteuerung hinzuzufügen. Im Folgenden finden Sie die verwendete Parameterliste für die Methode:

- **top** – der vertikale Versatz des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Abstand der Textbox von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **height** – die Höhe des Textfelds, in Einheiten von 1/4000 des Diagrammbereichs.
- **width** – die Breite des Textfelds, in Einheiten von 1/4000 des Diagrammbereichs.

Die Methode gibt ein Objekt der Klasse [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) zurück, wobei die Klasse [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) ein Textfeld im Diagramm darstellt.

Das folgende Beispiel zeigt, wie man ein Textfeld zu einem Diagramm hinzufügt. Das Beispiel verwendet die vorherige Designerdatei, die ein Diagramm enthält. Wir verwenden diese Datei, um ein Textfeld in das Diagramm einzufügen, um den Diagrammtitel anzuzeigen.

Unten finden Sie den Originalcode, um ein Textfeld zum Diagramm hinzuzufügen. Die folgende Ausgabe wird beim Ausführen des Codes generiert.

**Ein Textfeld wird im Diagramm hinzugefügt**

![todo:image_alt_text](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **Hinzufügen eines Bilds zum Diagramm**

Mit Aspose.Cells können Sie Bilder in ein Diagramm einfügen. Fügen Sie beispielsweise ein Bild hinzu, um ein Diagramm oder seine Inhalte zu betonen oder mehr Bedeutung zu verleihen oder fügen Sie eine Markenbild-Datei ein.

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) stellt eine Methode namens [**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart-int-int-java.io.InputStream-int-int-) zur Verfügung, die verwendet wird, um ein Bildobjekt dem Diagramm hinzuzufügen. Im Folgenden finden Sie die verwendete Parameterliste für die Methode:

- **top** – der vertikale Abstand des Bildes von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Abstand des Bildes von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **stream** – ein Stream-Objekt, das die Bilddaten enthält.
- **widthScale** – die Skalierung der Bildbreite, ein Prozentsatz.
- **heightScale** – die Skalierung der Bildhöhe, ein Prozentsatz.

Die Methode gibt ein Objekt der Klasse [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) zurück, wobei die Klasse [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) ein Bildobjekt im Diagramm darstellt.

Das folgende Beispiel zeigt, wie man ein Bild zu einem Diagramm hinzufügt. Das Beispiel verwendet die vorherige Designerdatei, die ein Diagramm enthält. Wir verwenden diese Datei, um ein Bild in das Diagramm einzufügen.

Unten finden Sie den Originalcode, um ein Bild zum Diagramm hinzuzufügen. Die folgende Ausgabe wird beim Ausführen des Codes generiert.

**Ein Bild wird in das Diagramm eingefügt**

![todo:image_alt_text](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **Checkbox in das Diagramm einfügen**

Aspose.Cells ermöglicht es Ihnen, Kontrollkästchen in ein Diagrammblatt einzufügen, indem Sie die [**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType)-Aufzählung verwenden. Das folgende Beispiel zeigt, wie man ein Kontrollkästchen zu einem Diagrammblatt hinzufügt.

Das folgende Bild zeigt das Diagrammblatt mit der Checkbox in der Ausgabedatei.

![todo:image_alt_text](controls-in-charts_5.jpg)

Die [Ausgabedatei](InsertCheckboxInChartSheet_out.xlsx), die durch den folgenden Code-Schnipsel generiert wurde, ist zur Ihrer Referenz angehängt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
{{< app/cells/assistant language="java" >}}
