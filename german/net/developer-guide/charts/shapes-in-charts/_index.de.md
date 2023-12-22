---
title: Formen in Diagrammen
description: Erfahren Sie, wie Sie mit Aspose.Cells for .NET Steuerelemente hinzufügen und Diagramme in Microsoft Excel anpassen. Unser Leitfaden zeigt, wie Sie Diagrammelemente manipulieren, die Formatierung anpassen und das Gesamterscheinungsbild und die Benutzerfreundlichkeit Ihrer Diagramme verbessern.
keywords: Aspose.Cells for .NET, Chart Controls, Chart Customization, Microsoft Excel, Chart Elements, Formatting.
type: docs
weight: 70
url: /de/net/controls-in-charts/
---
{{% alert color="primary" %}}

Manchmal müssen Sie Zeichnungsobjekte wie Beschriftungen, Textfelder, Bilder usw. in ein Diagramm einfügen. Aspose.Cells kann die Steuerelemente zur Laufzeit zu einem Diagramm hinzufügen.

{{% /alert %}}

##  **Beschriftungssteuerung zum Diagramm hinzufügen**

Mithilfe von Beschriftungen können Benutzer Informationen über den Inhalt einer Tabelle erhalten.
Mit Aspose.Cells können Sie Beschriftungen sogar in Diagrammen hinzufügen und bearbeiten.

Der[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart), wird zum Hinzufügen eines Beschriftungssteuerelements zu einem Diagramm verwendet. Nachfolgend finden Sie eine Liste der für die Methode verwendeten Parameter:

- **Spitze**– der vertikale Versatz der Beschriftung von der oberen linken Ecke in Einheiten von 1/4000 der Diagrammfläche.
- **links**– der vertikale Versatz der Beschriftung von der oberen linken Ecke in Einheiten von 1/4000 der Diagrammfläche.
- **Höhe** – die Höhe der Beschriftung, in Einheiten von 1/4000 der Diagrammfläche.
- **Breite** – die Breite der Beschriftung, in Einheiten von 1/4000 der Diagrammfläche.

 Die Methode gibt zurück[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)Objekt. Der[**Etikett**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) Die Klasse stellt eine Beschriftung im Diagramm dar. Es hat einige wichtige Mitglieder:

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)(Eigenschaft) – gibt die Beschriftungszeichenfolge eines Etiketts an.
- [**Füllen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (Eigenschaft) – gibt die Füllfarbenattribute an.

Das folgende Beispiel zeigt, wie Sie dem Diagramm eine Beschriftung hinzufügen. Das Beispiel verwendet eine Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um eine Beschriftung in das Diagramm einzufügen. Unten finden Sie den Originalcode zum Hinzufügen einer Beschriftung zum Diagramm. Die folgende Ausgabe wird beim Ausführen des Codes generiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

##  **Hinzufügen eines TextBox-Steuerelements zum Diagramm**

Eine Möglichkeit, wichtige Informationen in einem Bericht hervorzuheben, ist die Verwendung eines Textfelds. Geben Sie beispielsweise Text ein, um den Firmennamen hervorzuheben oder die geografische Region mit den höchsten Umsätzen anzugeben. Der[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart), das zum Hinzufügen eines Textfeld-Steuerelements zu einem Diagramm verwendet wird. Im Folgenden finden Sie die für die Methode verwendete Parameterliste:

- **Spitze** – der vertikale Versatz des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 der Diagrammfläche.
- **links** – der vertikale Versatz des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 der Diagrammfläche.
- **Höhe** – die Höhe des Textfelds, in Einheiten von 1/4000 der Diagrammfläche.
- **Breite** – die Breite des Textfelds, in Einheiten von 1/4000 der Diagrammfläche.

 Die Methode gibt zurück[**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) Objekt. Der[**Textfeld**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)Die Klasse stellt ein Textfeld im Diagramm dar.

Das folgende Beispiel zeigt, wie man einem Diagramm ein Textfeld hinzufügt. Das Beispiel verwendet die vorherige Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um ein Textfeld in das Diagramm einzufügen, um den Diagrammtitel anzuzeigen. Unten finden Sie den Originalcode zum Hinzufügen eines Textfelds zum Diagramm.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

##  **Bild zum Diagramm hinzufügen**

Aspose.Cells ermöglicht das Einfügen von Bildern in ein Diagramm. Fügen Sie beispielsweise ein Bild hinzu, um ein Diagramm oder seinen Inhalt hervorzuheben oder ihm mehr Bedeutung zu verleihen, oder fügen Sie eine Markenbilddatei ein.

 Der[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Die Klasse stellt eine Methode mit dem Namen bereit[**AddPictureInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart), mit dem dem Diagramm ein Bildobjekt hinzugefügt wird. Im Folgenden finden Sie die für die Methode verwendete Parameterliste:

- **Spitze** – der vertikale Versatz des Bildes von der oberen linken Ecke in Einheiten von 1/4000 der Diagrammfläche.
- **links** – der vertikale Versatz des Bildes von der oberen linken Ecke in Einheiten von 1/4000 der Diagrammfläche.
- **Strom** – ein Stream-Objekt, das die Bilddaten enthält.
- **widthScale** – der Maßstab der Bildbreite, ein Prozentwert.
- **heightScale** – die Skalierung der Bildhöhe, ein Prozentwert.

 Die Methode gibt eine zurück[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) Objekt. Der[**Bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)Die Klasse stellt ein Bildobjekt im Diagramm dar.

Das folgende Beispiel zeigt, wie Sie dem Diagramm ein Bild hinzufügen. Das Beispiel verwendet die vorherige Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um ein Bild in das Diagramm einzufügen. Unten finden Sie den Originalcode zum Hinzufügen von Bildern zum Diagramm.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

##  **Kontrollkästchen im Diagramm hinzufügen**

 Aspose.Cells ermöglicht das Einfügen von Kontrollkästchen in ein Diagrammblatt mithilfe von[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) Aufzählung. Das folgende Beispiel zeigt das Hinzufügen eines Kontrollkästchens zu einem Diagrammblatt.

Das folgende Bild zeigt das Diagrammblatt mit dem Kontrollkästchen in der Ausgabedatei.

![todo:image_alt_text](controls-in-charts_1.jpg)

 Der[Ausgabedatei](101089316.xlsx) Der durch den folgenden Codeausschnitt generierte Code ist als Referenz beigefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

##  **Vorabthemen**
- [Fügen Sie WordArt-Wasserzeichen zum Diagramm hinzu](/cells/de/net/add-wordart-watermark-to-chart/)
