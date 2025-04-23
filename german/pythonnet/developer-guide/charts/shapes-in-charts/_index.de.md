---
title: Formen in Diagrammen
description: Erfahren Sie, wie Sie Aspose.Cells für Python via .NET verwenden, um Steuerelemente hinzuzufügen und Diagramme in Microsoft Excel anzupassen. Unser Leitfaden zeigt, wie man Diagrammelemente manipuliert, Formatierungen anpasst und das gesamte Erscheinungsbild sowie die Benutzerfreundlichkeit Ihrer Diagramme verbessert.
keywords: Aspose.Cells für Python via .NET, Diagrammsteuerungen, Diagrammanpassung, Microsoft Excel, Diagrammelemente, Formatierung.
type: docs
weight: 70
url: /de/python-net/controls-in-charts/
---

{{% alert color="primary" %}}

Manchmal müssen Sie Zeichnungsobjekte wie Beschriftungen, Textfelder, Bilder usw. in ein Diagramm einfügen. Aspose.Cells für Python via .NET kann Steuerelemente zur Laufzeit zu einem Diagramm hinzufügen.

{{% /alert %}}

## **Hinzufügen von Beschriftungssteuerung zum Diagramm**

Beschriftungen bieten eine Möglichkeit, Benutzern Informationen über den Inhalt eines Arbeitsblatts bereitzustellen.
Aspose.Cells für Python via .NET ermöglicht das Hinzufügen und Bearbeiten von Beschriftungen even in Diagrammen.

Die Klasse [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) stellt eine Methode namens [**add_label_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label_in_chart) zur Verfügung, die verwendet wird, um dem Diagramm eine Beschriftungssteuerung hinzuzufügen. Im Folgenden finden Sie eine Liste der Parameter, die für die Methode verwendet werden:

- **top** – der vertikale Versatz der Beschriftung von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Versatz der Beschriftung von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **height** – die Höhe der Beschriftung, in Einheiten von 1/4000 des Diagrammbereichs.
- **width** – die Breite der Beschriftung, in Einheiten von 1/4000 des Diagrammbereichs.

Die Methode gibt ein [**aspose.cells.drawing.Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label)-Objekt zurück. Die Klasse [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) stellt eine Beschriftung im Diagramm dar. Sie verfügt über einige wichtige Elemente:

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) (Eigenschaft) – gibt einen Beschriftungszeichenfolgenwert an.
- [**fill**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill) (Eigenschaft) – gibt die Farbfüllungseigenschaften an.

Im folgenden Beispiel wird gezeigt, wie eine Beschriftung dem Diagramm hinzugefügt wird. Das Beispiel verwendet eine Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um eine Beschriftung in das Diagramm einzufügen. Unten finden Sie den ursprünglichen Code zum Hinzufügen einer Beschriftung zum Diagramm. Die folgende Ausgabe wird beim Ausführen des Codes generiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingLabelControl-1.py" >}}

## **Hinzufügen einer Textfeldsteuerung zum Diagramm**

Eine Möglichkeit, wichtige Informationen in einem Bericht hervorzuheben, besteht darin, einen Textbereich zu verwenden. Geben Sie beispielsweise Text ein, um den Firmennamen hervorzuheben oder das geografische Gebiet mit den höchsten Verkäufen anzuzeigen. Die Klasse [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) stellt eine Methode namens [**add_text_box_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_text_box_in_chart) zur Verfügung, die verwendet wird, um dem Diagramm eine Textfeldsteuerung hinzuzufügen. Im Folgenden finden Sie die verwendete Parameterliste für die Methode:

- **top** – der vertikale Versatz des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Versatz des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **height** – die Höhe des Textfelds, in Einheiten von 1/4000 des Diagrammbereichs.
- **width** – die Breite des Textfelds, in Einheiten von 1/4000 des Diagrammbereichs.

Die Methode gibt ein [**aspose.cells.drawing.TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox)-Objekt zurück. Die Klasse [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) stellt ein Textfeld im Diagramm dar.

Im folgenden Beispiel wird gezeigt, wie ein Textfeld zu einem Diagramm hinzugefügt wird. Das Beispiel verwendet die vorherige Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um ein Textfeld in das Diagramm einzufügen, um den Diagrammtitel anzuzeigen. Unten finden Sie den ursprünglichen Code zum Hinzufügen eines Textfelds zum Diagramm.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.py" >}}

## **Hinzufügen eines Bilds zum Diagramm**

Aspose.Cells für Python via .NET ermöglicht das Einfügen von Bildern in ein Diagramm. Zum Beispiel ein Bild hinzufügen, um ein Diagramm oder dessen Inhalte zu betonen oder mehr Bedeutung zu verleihen oder eine Markenbilddatei einzufügen.

Die Klasse [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) stellt eine Methode namens [**add_picture_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture_in_chart) zur Verfügung, die verwendet wird, um ein Bildobjekt dem Diagramm hinzuzufügen. Im Folgenden finden Sie die verwendete Parameterliste für die Methode:

- **top** – der vertikale Abstand des Bildes von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Abstand des Bildes von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **stream** – ein Stream-Objekt, das die Bilddaten enthält.
- **widthScale** – die Skalierung der Bildbreite, ein Prozentsatz.
- **heightScale** – die Skalierung der Bildhöhe, ein Prozentsatz.

Die Methode gibt ein [**aspose.cells.drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)-Objekt zurück. Die Klasse [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) stellt ein Bildobjekt im Diagramm dar.

Das folgende Beispiel zeigt, wie Sie ein Bild zum Diagramm hinzufügen. Das Beispiel verwendet die vorige Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um ein Bild in das Diagramm einzufügen. Unten finden Sie den ursprünglichen Code zum Hinzufügen eines Bildes zum Diagramm.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingPictureToChart-1.py" >}}

## **Checkbox in das Diagramm einfügen**

Aspose.Cells für Python via .NET ermöglicht das Einfügen von Kontrollkästchen in ein Diagrammblatt mittels [**MsoDrawingType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msodrawingtype)-Aufzählung. Das folgende Beispiel zeigt, wie man ein Kontrollkästchen zu einem Diagrammblatt hinzufügt.

Das folgende Bild zeigt das Diagrammblatt mit der Checkbox in der Ausgabedatei.

![todo:image_alt_text](controls-in-charts_1.jpg)

Die [Ausgabedatei](101089316.xlsx), die durch den folgenden Code-Schnipsel generiert wurde, ist als Referenz angehängt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.py" >}}

## **Erweiterte Themen**
- [Fügen Sie dem Diagramm ein WordArt-Wasserzeichen hinzu](/cells/de/python-net/add-wordart-watermark-to-chart/)
