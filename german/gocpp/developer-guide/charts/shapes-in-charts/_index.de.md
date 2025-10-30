---
title: Formen in Diagrammen mit Golang über C++
linktitle: Formen in Diagrammen
description: Lernen Sie, wie Sie Aspose.Cells for C++ verwenden, um Steuerelemente hinzuzufügen und Diagramme in Microsoft Excel anzupassen. Unser Leitfaden zeigt, wie man Diagrammelemente manipuliert, das Format anpasst und das allgemeine Erscheinungsbild sowie die Benutzerfreundlichkeit Ihrer Diagramme verbessert.
keywords: Aspose.Cells for C++, Diagrammsteuerungen, Diagrammanpassung, Microsoft Excel, Diagrammelemente, Formatierung.
type: docs
weight: 70
url: /de/go-cpp/controls-in-charts/
---

{{% alert color="primary" %}}

Manchmal müssen Sie Zeichenobjekte wie Beschriftungen, Textfelder, Bilder usw. in ein Diagramm einfügen. Aspose.Cells kann die Steuerelemente zur Laufzeit zu einem Diagramm hinzufügen.

{{% /alert %}}

## **Hinzufügen von Beschriftungssteuerung zum Diagramm**

Beschriftungen bieten eine Möglichkeit, Benutzern Informationen über den Inhalt eines Arbeitsblatts bereitzustellen.
Aspose.Cells ermöglicht es Ihnen, Beschriftungen sogar in Diagramme zu hinzuzufügen und zu manipulieren.

Die Klasse [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) bietet eine Methode namens [**AddLabelInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlabelinchart/), mit der ein Label-Steuerelement zu einem Diagramm hinzugefügt wird. Nachfolgend eine Liste der für die Methode verwendeten Parameter:

- **top** – der vertikale Versatz der Beschriftung von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Versatz der Beschriftung von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **height** – die Höhe der Beschriftung, in Einheiten von 1/4000 des Diagrammbereichs.
- **width** – die Breite der Beschriftung, in Einheiten von 1/4000 des Diagrammbereichs.

Die Methode gibt ein [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/go-cpp/label/)-Objekt zurück. Die Klasse [**Label**](https://reference.aspose.com/cells/go-cpp/label/) repräsentiert ein Label im Diagramm. Sie verfügt über einige wichtige Mitglieder:

- [**Text**](https://reference.aspose.com/cells/go-cpp/shape/gettext/) (Eigenschaft) – gibt die Beschriftungszeichenkette eines Labels an.
- [**Fill**](https://reference.aspose.com/cells/go-cpp/shape/getfill/) (Eigenschaft) – gibt die Farbfüllungseigenschaften an.

Im folgenden Beispiel wird gezeigt, wie eine Beschriftung dem Diagramm hinzugefügt wird. Das Beispiel verwendet eine Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um eine Beschriftung in das Diagramm einzufügen. Unten finden Sie den ursprünglichen Code zum Hinzufügen einer Beschriftung zum Diagramm. Die folgende Ausgabe wird beim Ausführen des Codes generiert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts.go" >}}
## **Hinzufügen einer Textfeldsteuerung zum Diagramm**

Eine Möglichkeit, wichtige Informationen in einem Bericht hervorzuheben, besteht darin, ein Textfeld zu verwenden. Zum Beispiel können Sie Text eingeben, um den Firmennamen hervorzuheben oder die geografische Region mit den höchsten Verkaufszahlen anzugeben. Die Klasse [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) bietet eine Methode namens [**AddTextBoxInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addtextboxinchart/), mit der ein Textfeld-Steuerelement zu einem Diagramm hinzugefügt wird. Nachfolgend die Parameterliste für die Methode:

- **top** – der vertikale Versatz des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Versatz des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **height** – die Höhe des Textfelds, in Einheiten von 1/4000 des Diagrammbereichs.
- **width** – die Breite des Textfelds, in Einheiten von 1/4000 des Diagrammbereichs.

Die Methode gibt ein [**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/)-Objekt zurück. Die [**TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/)-Klasse stellt ein Textfeld im Diagramm dar.

Im folgenden Beispiel wird gezeigt, wie ein Textfeld zu einem Diagramm hinzugefügt wird. Das Beispiel verwendet die vorherige Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um ein Textfeld in das Diagramm einzufügen, um den Diagrammtitel anzuzeigen. Unten finden Sie den ursprünglichen Code zum Hinzufügen eines Textfelds zum Diagramm.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-1.go" >}}
## **Hinzufügen eines Bilds zum Diagramm**

Mit Aspose.Cells können Sie Bilder in ein Diagramm einfügen. Fügen Sie beispielsweise ein Bild hinzu, um ein Diagramm oder seine Inhalte zu betonen oder mehr Bedeutung zu verleihen oder fügen Sie eine Markenbild-Datei ein.

Die Klasse [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) stellt eine Methode namens [**AddPictureInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpictureinchart/) bereit, mit der ein Bildobjekt zum Diagramm hinzugefügt wird. Nachfolgend die Parameterliste, die für die Methode verwendet wird:

- **top** – der vertikale Abstand des Bildes von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Abstand des Bildes von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **stream** – ein Stream-Objekt, das die Bilddaten enthält.
- **widthScale** – die Skalierung der Bildbreite, ein Prozentsatz.
- **heightScale** – die Skalierung der Bildhöhe, ein Prozentsatz.

Die Methode gibt ein [**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/go-cpp/picture/)-Objekt zurück. Die Klasse [**Picture**](https://reference.aspose.com/cells/go-cpp/picture/) stellt ein Bildobjekt im Diagramm dar.

Das folgende Beispiel zeigt, wie Sie ein Bild zum Diagramm hinzufügen. Das Beispiel verwendet die vorige Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um ein Bild in das Diagramm einzufügen. Unten finden Sie den ursprünglichen Code zum Hinzufügen eines Bildes zum Diagramm.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-2.go" >}}
## **Checkbox in das Diagramm einfügen**

Aspose.Cells ermöglicht es Ihnen, Checkboxen in ein Diagrammblatt einzufügen, indem Sie die [**MsoDrawingType**](https://reference.aspose.com/cells/go-cpp/msodrawingtype/)-Aufzählung verwenden. Das folgende Beispiel zeigt das Hinzufügen einer Checkbox zu einem Diagrammblatt.

Das folgende Bild zeigt das Diagrammblatt mit der Checkbox in der Ausgabedatei.

![todo:image_alt_text](controls-in-charts_1.jpg)

Die [Ausgabedatei](101089316.xlsx), die durch den folgenden Code-Schnipsel generiert wurde, ist als Referenz angehängt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-3.go" >}}
## **Erweiterte Themen**
- [Fügen Sie dem Diagramm ein WordArt-Wasserzeichen hinzu](/cells/de/cpp/add-wordart-watermark-to-chart/)
