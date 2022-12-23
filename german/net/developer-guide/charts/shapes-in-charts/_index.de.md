---
title: Formen in Diagrammen
type: docs
weight: 70
url: /de/net/controls-in-charts/
---
{{% alert color="primary" %}}

Manchmal müssen Sie Zeichnungsobjekte wie Beschriftungen, Textfelder, Bilder usw. in ein Diagramm einfügen. Aspose.Cells kann die Steuerelemente zur Laufzeit zu einem Diagramm hinzufügen.

{{% /alert %}}

## **Label Control zum Diagramm hinzufügen**

Labels bieten eine Möglichkeit, Benutzern Informationen über den Inhalt einer Tabelle zu geben.
Aspose.Cells ermöglicht das Hinzufügen und Bearbeiten von Beschriftungen sogar in Diagrammen.

Das[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**LabelInChart hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart), wird verwendet, um einem Diagramm ein Beschriftungssteuerelement hinzuzufügen. Nachfolgend finden Sie eine Liste der für das Verfahren verwendeten Parameter:

- **oben** – der vertikale Versatz des Etiketts von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **links** – der vertikale Versatz des Etiketts von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **Höhe** – die Höhe des Etiketts in Einheiten von 1/4000 des Diagrammbereichs.
- **Breite** – die Breite des Etiketts in Einheiten von 1/4000 des Diagrammbereichs.

 Die Methode kehrt zurück[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)Objekt. Das[**Etikette**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) Klasse stellt eine Bezeichnung im Diagramm dar. Es hat einige wichtige Mitglieder:

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)(Eigenschaft) – gibt die Beschriftungszeichenfolge eines Etiketts an.
- [**Füllen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (Eigenschaft) – gibt die Füllfarbenattribute an.

Das folgende Beispiel zeigt, wie Sie dem Diagramm eine Beschriftung hinzufügen. Das Beispiel verwendet eine Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um eine Beschriftung in das Diagramm einzufügen. Unten ist der ursprüngliche Code zum Hinzufügen einer Beschriftung zum Diagramm. Beim Ausführen des Codes wird die folgende Ausgabe generiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

## **TextBox-Steuerelement zum Diagramm hinzufügen**

 Eine Möglichkeit, wichtige Informationen in einem Bericht hervorzuheben, ist die Verwendung eines Textfelds. Geben Sie beispielsweise Text ein, um den Firmennamen hervorzuheben oder die geografische Region mit den höchsten Umsätzen anzugeben. Das[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart)die verwendet wird, um einem Diagramm ein Textfeld-Steuerelement hinzuzufügen. Es folgt die für die Methode verwendete Parameterliste:

- **oben** – der vertikale Abstand des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **links** – der vertikale Abstand des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **Höhe**– die Höhe des Textfelds in Einheiten von 1/4000 des Diagrammbereichs.
- **Breite** – die Breite des Textfelds in Einheiten von 1/4000 des Diagrammbereichs.

 Die Methode kehrt zurück[**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) Objekt. Das[**Textfeld**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)Klasse repräsentiert ein Textfeld im Diagramm.

Das folgende Beispiel zeigt, wie Sie einem Diagramm ein Textfeld hinzufügen. Das Beispiel verwendet die vorherige Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um ein Textfeld in das Diagramm einzufügen, um den Diagrammtitel anzuzeigen. Unten ist der ursprüngliche Code zum Hinzufügen eines Textfelds zum Diagramm.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **Bild zum Diagramm hinzufügen**

Mit Aspose.Cells können Sie Bilder in ein Diagramm einfügen. Fügen Sie beispielsweise ein Bild hinzu, um ein Diagramm oder seinen Inhalt hervorzuheben oder ihm mehr Bedeutung zu verleihen, oder fügen Sie eine Markenbilddatei ein.

 Das[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**BildInDiagramm hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart), die zum Hinzufügen eines Bildobjekts zum Diagramm verwendet wird. Es folgt die für die Methode verwendete Parameterliste:

- **oben**– der vertikale Abstand des Bildes von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **links**– der vertikale Abstand des Bildes von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **Strom** – ein Stream-Objekt, das die Bilddaten enthält.
- **widthScale** – die Skala der Bildbreite, ein Prozentwert.
- **Höhenskala** – die Skala der Bildhöhe, ein Prozentwert.

 Die Methode gibt eine zurück[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) Objekt. Das[**Bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)Die Klasse repräsentiert ein Bildobjekt im Diagramm.

Das folgende Beispiel zeigt, wie Sie dem Diagramm ein Bild hinzufügen. Das Beispiel verwendet die vorherige Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um ein Bild in das Diagramm einzufügen. Unten ist der ursprüngliche Code zum Hinzufügen von Bildern zum Diagramm.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **Kontrollkästchen im Diagramm hinzufügen**

 Aspose.Cells ermöglicht es Ihnen, Kontrollkästchen in ein Diagrammblatt einzufügen, indem Sie verwenden[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) Aufzählung. Das folgende Beispiel zeigt das Hinzufügen eines Kontrollkästchens zu einem Diagrammblatt.

Das folgende Bild zeigt das Diagrammblatt mit dem Kontrollkästchen in der Ausgabedatei.

![todo: Bild_alt_Text](controls-in-charts_1.jpg)

 Das[Ausgabedatei](101089316.xlsx)generiert durch das folgende Code-Snippet ist als Referenz beigefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **Themen vorantreiben**
- [WordArt-Wasserzeichen zum Diagramm hinzufügen](/cells/de/net/add-wordart-watermark-to-chart/)
