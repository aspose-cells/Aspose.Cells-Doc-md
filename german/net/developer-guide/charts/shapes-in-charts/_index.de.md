---
title: Formen in Diagrammen
description: Erfahren Sie, wie Sie Aspose.Cells for .NET verwenden können, um Steuerelemente hinzuzufügen und Diagramme in Microsoft Excel anzupassen. Unsere Anleitung wird zeigen, wie Sie Diagrammelemente manipulieren, das Format anpassen und das gesamte Erscheinungsbild und die Benutzerfreundlichkeit Ihrer Diagramme verbessern können.
keywords: Aspose.Cells for .NET, Diagrammsteuerungen, Diagrammanpassung, Microsoft Excel, Diagrammelemente, Formatierung.
type: docs
weight: 70
url: /de/net/controls-in-charts/
---

{{% alert color="primary" %}}

Manchmal müssen Sie Zeichenobjekte wie Beschriftungen, Textfelder, Bilder usw. in ein Diagramm einfügen. Aspose.Cells kann die Steuerelemente zur Laufzeit zu einem Diagramm hinzufügen.

{{% /alert %}}

## **Hinzufügen von Beschriftungssteuerung zum Diagramm**

Beschriftungen bieten eine Möglichkeit, Benutzern Informationen über den Inhalt eines Arbeitsblatts bereitzustellen.
Aspose.Cells ermöglicht es Ihnen, Beschriftungen sogar in Diagramme zu hinzuzufügen und zu manipulieren.

Die Klasse [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) stellt eine Methode namens [**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart) zur Verfügung, die verwendet wird, um dem Diagramm eine Beschriftungssteuerung hinzuzufügen. Im Folgenden finden Sie eine Liste der Parameter, die für die Methode verwendet werden:

- **top** – der vertikale Versatz der Beschriftung von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Versatz der Beschriftung von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **height** – die Höhe der Beschriftung, in Einheiten von 1/4000 des Diagrammbereichs.
- **width** – die Breite der Beschriftung, in Einheiten von 1/4000 des Diagrammbereichs.

Die Methode gibt ein [**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)-Objekt zurück. Die Klasse [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) stellt eine Beschriftung im Diagramm dar. Sie verfügt über einige wichtige Elemente:

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) (Eigenschaft) – gibt einen Beschriftungszeichenfolgenwert an.
- [**Fill**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (Eigenschaft) – gibt die Farbfüllungseigenschaften an.

Im folgenden Beispiel wird gezeigt, wie eine Beschriftung dem Diagramm hinzugefügt wird. Das Beispiel verwendet eine Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um eine Beschriftung in das Diagramm einzufügen. Unten finden Sie den ursprünglichen Code zum Hinzufügen einer Beschriftung zum Diagramm. Die folgende Ausgabe wird beim Ausführen des Codes generiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

## **Hinzufügen einer Textfeldsteuerung zum Diagramm**

Eine Möglichkeit, wichtige Informationen in einem Bericht hervorzuheben, besteht darin, einen Textbereich zu verwenden. Geben Sie beispielsweise Text ein, um den Firmennamen hervorzuheben oder das geografische Gebiet mit den höchsten Verkäufen anzuzeigen. Die Klasse [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) stellt eine Methode namens [**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart) zur Verfügung, die verwendet wird, um dem Diagramm eine Textfeldsteuerung hinzuzufügen. Im Folgenden finden Sie die verwendete Parameterliste für die Methode:

- **top** – der vertikale Versatz des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Versatz des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **height** – die Höhe des Textfelds, in Einheiten von 1/4000 des Diagrammbereichs.
- **width** – die Breite des Textfelds, in Einheiten von 1/4000 des Diagrammbereichs.

Die Methode gibt ein [**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)-Objekt zurück. Die Klasse [**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) stellt ein Textfeld im Diagramm dar.

Im folgenden Beispiel wird gezeigt, wie ein Textfeld zu einem Diagramm hinzugefügt wird. Das Beispiel verwendet die vorherige Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um ein Textfeld in das Diagramm einzufügen, um den Diagrammtitel anzuzeigen. Unten finden Sie den ursprünglichen Code zum Hinzufügen eines Textfelds zum Diagramm.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **Hinzufügen eines Bilds zum Diagramm**

Mit Aspose.Cells können Sie Bilder in ein Diagramm einfügen. Fügen Sie beispielsweise ein Bild hinzu, um ein Diagramm oder seine Inhalte zu betonen oder mehr Bedeutung zu verleihen oder fügen Sie eine Markenbild-Datei ein.

Die Klasse [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) stellt eine Methode namens [**AddPictureInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart) zur Verfügung, die verwendet wird, um ein Bildobjekt dem Diagramm hinzuzufügen. Im Folgenden finden Sie die verwendete Parameterliste für die Methode:

- **top** – der vertikale Abstand des Bildes von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Abstand des Bildes von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **stream** – ein Stream-Objekt, das die Bilddaten enthält.
- **widthScale** – die Skalierung der Bildbreite, ein Prozentsatz.
- **heightScale** – die Skalierung der Bildhöhe, ein Prozentsatz.

Die Methode gibt ein [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)-Objekt zurück. Die Klasse [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) stellt ein Bildobjekt im Diagramm dar.

Das folgende Beispiel zeigt, wie Sie ein Bild zum Diagramm hinzufügen. Das Beispiel verwendet die vorige Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um ein Bild in das Diagramm einzufügen. Unten finden Sie den ursprünglichen Code zum Hinzufügen eines Bildes zum Diagramm.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **Checkbox in das Diagramm einfügen**

Aspose.Cells ermöglicht es Ihnen, Checkboxen in ein Diagrammblatt einzufügen, indem Sie die [**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype)-Aufzählung verwenden. Das folgende Beispiel zeigt das Hinzufügen einer Checkbox zu einem Diagrammblatt.

Das folgende Bild zeigt das Diagrammblatt mit der Checkbox in der Ausgabedatei.

![todo:image_alt_text](controls-in-charts_1.jpg)

Die [Ausgabedatei](101089316.xlsx), die durch den folgenden Code-Schnipsel generiert wurde, ist als Referenz angehängt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **Erweiterte Themen**
- [Fügen Sie dem Diagramm ein WordArt-Wasserzeichen hinzu](/cells/de/net/add-wordart-watermark-to-chart/)
{{< app/cells/assistant language="csharp" >}}
