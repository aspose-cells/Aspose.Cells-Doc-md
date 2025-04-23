---
title: Einfügen von Bildern und Formen von Excel Dateien
linktitle: Formen
type: docs
weight: 140
url: /de/net/insert-shapes/
description: Verwalten von Bildern, OLE Objekten und Formen in Excel Dateien
---

{{% alert color="primary" %}}

Manchmal müssen Sie einige notwendige Formen in das Arbeitsblatt einfügen. Möglicherweise müssen Sie dieselbe Form an verschiedenen Positionen im Arbeitsblatt einfügen. Oder Sie müssen Formen im Arbeitsblatt stapelweise einfügen.

Keine Sorge! [Aspose.Cells](https://products.aspose.com/cells/) unterstützt all diese Operationen.

{{% /alert %}}

Die Formen in Excel sind hauptsächlich in die folgenden Typen unterteilt:
- **Bilder**
- **OLE-Objekte**
- **Linien**
- **Rechtecke**
- **Grundformen**
- **Blockpfeile**
- **Gleichungsformen**
- **Flussdiagramme**
- **Sterne und Banner**
- **Legenden**

Dieses Leitdokument wählt eine oder zwei Formen aus jedem Typ aus, um Beispiele zu erstellen. Anhand dieser Beispiele erfahren Sie, wie Sie [Aspose.Cells](https://products.aspose.com/cells/) verwenden, um die angegebene Form in das Arbeitsblatt einzufügen.

## **Hinzufügen von Bildern in ein Excel-Arbeitsblatt in C#**

Das Hinzufügen von Bildern zu einer Tabelle ist sehr einfach. Es dauert nur wenige Zeilen Code:
Rufen Sie einfach die [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)-Methode der [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)-Sammlung (die im [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Objekt verkapselt ist) auf. Die [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)-Methode akzeptiert die folgenden Parameter:

- **Index der oberen linken Zeile**, der Index der oberen linken Zeile.
- **Index der oberen linken Spalte**, der Index der oberen linken Spalte.
- **Bilddateiname**, der Name der Bilddatei inklusive des Pfads.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **Einfügen von OLE-Objekten in Excel-Arbeitsblatt in C#**

Aspose.Cells unterstützt das Hinzufügen, Extrahieren und Manipulieren von OLE-Objekten in Arbeitsblättern. Aus diesem Grund hat Aspose.Cells die [**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection)-Klasse, die verwendet wird, um ein neues OLE-Objekt zur Sammlungsliste hinzuzufügen. Eine weitere Klasse, [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), stellt ein OLE-Objekt dar. Sie hat einige wichtige Elemente:

- Die [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)-Eigenschaft spezifiziert die Bilddaten im Byte-Array-Format. Das Bild wird angezeigt, um das OLE-Objekt im Arbeitsblatt anzuzeigen.
- Die [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)-Eigenschaft spezifiziert die Objektdaten in Form eines Byte-Arrays. Diese Daten werden in ihrem zugehörigen Programm angezeigt, wenn Sie auf das OLE-Objektsymbol doppelklicken.

Das folgende Beispiel zeigt, wie man OLE-Objekte in ein Arbeitsblatt einfügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **Einfügen einer Linie in Excel-Arbeitsblatt in C#**

Die Form der Linie gehört zur Kategorie **Linien**.

***In Microsoft Excel (zum Beispiel 2007):***

- Wählen Sie die Zelle aus, in die Sie die Linie einfügen möchten.
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.
- Wählen Sie dann die Linie aus 'Zuletzt verwendeten Formen' oder 'Linien' aus.

![](line.png)

***Mit Aspose.Cells verwenden***

Sie können die folgende Methode verwenden, um eine Linie im Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

Die Methode gibt ein [LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)-Objekt zurück.

{{% /alert %}}

Das folgende Beispiel zeigt, wie eine Linie in ein Arbeitsblatt eingefügt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:

![](line2.png)



## **Ein Linienpfeil in Excel-Arbeitsblatt in C# einfügen**

Die Form des Linienpfeils gehört zur Kategorie **Linien**. Es handelt sich um einen speziellen Fall von Linie.

***In Microsoft Excel (zum Beispiel 2007):***

- Wählen Sie die Zelle aus, in der Sie den Linienpfeil einfügen möchten
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.
- Wählen Sie dann den Linienpfeil aus 'Zuletzt verwendete Formen' oder 'Linien'

![](line_arrow1.png)

***Mit Aspose.Cells verwenden***

Sie können die folgende Methode verwenden, um einen Linienpfeil in das Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn,	int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

Die Methode gibt ein [LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)-Objekt zurück.

{{% /alert %}}

Das folgende Beispiel zeigt, wie ein Linienpfeil in ein Arbeitsblatt eingefügt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:

![](line_arrow2.png)



## **Ein Rechteck in Excel-Arbeitsblatt in C# einfügen**

Die Form des Rechtecks gehört zur Kategorie **Rechtecke**.

***In Microsoft Excel (zum Beispiel 2007):***

- Wählen Sie die Zelle, in die Sie das Rechteck einfügen möchten
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.
- Wählen Sie dann das Rechteck aus 'Zuletzt verwendete Formen' oder 'Rechtecke' aus

![](rectangle.png)

***Mit Aspose.Cells verwenden***

Sie können die folgende Methode verwenden, um ein Rechteck im Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[**public RectangleShape AddRectangle(int upperLeftRow,	int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

Die Methode gibt ein [RectangleShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) Objekt zurück.

{{% /alert %}}

Das folgende Beispiel zeigt, wie man ein Rechteck in ein Arbeitsblatt einfügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:

![](rectangle2.png)



## **Einfügen eines Würfels in ein Excel-Arbeitsblatt in C#**

Die Form des Würfels gehört zur Kategorie **Grundformen**.

***In Microsoft Excel (zum Beispiel 2007):***

- Wählen Sie die Zelle, in die Sie den Würfel einfügen möchten
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.
- Wählen Sie dann den Würfel aus der Kategorie **Grundformen** aus

![](cube.png)

***Mit Aspose.Cells verwenden***

Sie können die folgende Methode verwenden, um einen Würfel im Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Die Methode gibt ein [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)-Objekt zurück.

{{% /alert %}}

Das folgende Beispiel zeigt, wie man einen W�rfel in ein Arbeitsblatt einf�gt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:

![](cube2.png)



## **Ein Callout-Quad-Pfeil in Excel-Arbeitsblatt in C# einf�gen**

Die Form des Callout-Quad-Pfeils geh�rt zur Kategorie **Blockpfeile**.

***In Microsoft Excel (zum Beispiel 2007):***

- W�hlen Sie die Zelle aus, in die Sie den Callout-Quad-Pfeil einf�gen m�chten.
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.
- W�hlen Sie dann den Callout-Quad-Pfeil aus **Blockpfeile** aus

![](callout_quad_arrow.png)

***Mit Aspose.Cells verwenden***

Sie k�nnen die folgende Methode verwenden, um einen Callout-Quad-Pfeil in das Arbeitsblatt einzuf�gen.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Die Methode gibt ein [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)-Objekt zurück.

{{% /alert %}}

Das folgende Beispiel zeigt, wie man einen Callout-Quad-Pfeil in ein Arbeitsblatt einf�gt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:

![](callout_quad_arrow2.png)



## **Ein Multiplikationszeichen in Excel-Arbeitsblatt in C# einf�gen**

Die Form des Multiplikationszeichens gehört zur Kategorie **Gleichungsformen**.

***In Microsoft Excel (zum Beispiel 2007):***

- Wählen Sie die Zelle aus, in der Sie das Multiplikationszeichen einfügen möchten
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.
- Wählen Sie dann das Multiplikationszeichen aus **Gleichungsformen**

![](multiplication_sign.png)

***Mit Aspose.Cells verwenden***

Sie können die folgende Methode verwenden, um ein Multiplikationszeichen im Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Die Methode gibt ein [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)-Objekt zurück.

{{% /alert %}}

Im folgenden Beispiel wird gezeigt, wie ein Multiplikationszeichen in ein Arbeitsblatt eingefügt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:

![](multiplication_sign2.png)



## **Einfügen eines Multi-Dokuments in ein Excel-Arbeitsblatt in C#**

Die Form des Multi-Dokuments gehört zur Kategorie **Flussdiagramme**.

***In Microsoft Excel (zum Beispiel 2007):***

- Wählen Sie die Zelle aus, in der Sie das Multi-Dokument einfügen möchten
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.
- Wählen Sie dann das Multi-Dokument aus **Flussdiagramme**

![](multidocument.png)

***Mit Aspose.Cells verwenden***

Sie können die folgende Methode verwenden, um ein Multidokument in das Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Die Methode gibt ein [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)-Objekt zurück.

{{% /alert %}}

Das folgende Beispiel zeigt, wie man ein Multidokument in ein Arbeitsblatt einfügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:

![](multidocument2.png)



## **Einfügen eines Fünfzackigen Sterns in das Excel-Arbeitsblatt in C#**

Die Form des Fünfzackigen Sterns gehört zur Kategorie **Sterne und Banner**.

***In Microsoft Excel (zum Beispiel 2007):***

- Wählen Sie die Zelle aus, in die Sie den Fünfzackigen Stern einfügen möchten
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.
- Wählen Sie dann den Fünfzackigen Stern unter **Sterne und Banner** aus

![](star_5_points.png)

***Mit Aspose.Cells verwenden***

Sie können die folgende Methode verwenden, um einen Fünfzackigen Stern in das Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Die Methode gibt ein [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)-Objekt zurück.

{{% /alert %}}

Das folgende Beispiel zeigt, wie man einen Fünfzackigen Stern in ein Arbeitsblatt einfügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:

![](star_5_points2.png)



## **Einsetzen einer Gedankenblasenwolke in ein Excel-Arbeitsblatt in C#**

Die Form der Gedankenblasenwolke gehört zur **Callouts**-Kategorie.

***In Microsoft Excel (zum Beispiel 2007):***

- Wählen Sie die Zelle aus, in die Sie die Gedankenblasenwolke einfügen möchten
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.
- Wählen Sie dann die Gedankenblasenwolke aus der Kategorie **Callouts** aus

![](thought_bubble_cloud.png)

***Mit Aspose.Cells verwenden***

Sie können die folgende Methode verwenden, um eine Gedankenblasenwolke in das Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Die Methode gibt ein [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)-Objekt zurück.

{{% /alert %}}

Im folgenden Beispiel wird gezeigt, wie man eine Gedankenblasenwolke in ein Arbeitsblatt einfügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:

![](thought_bubble_cloud2.png)

## **Erweiterte Themen**
- [Ändern der Anpassungswerte der Form](/cells/de/net/change-adjustment-values-of-the-shape/)
- [Formen zwischen Arbeitsblättern kopieren](/cells/de/net/copy-shapes-between-worksheets/)
- [Daten in nicht primitiver Form](/cells/de/net/data-in-non-primitive-shape/)
- [Absolute Position der Form im Arbeitsblatt finden](/cells/de/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Verbindungspunkte von Form erhalten](/cells/de/net/get-connection-points-from-shape/)
- [Steuerungen verwalten](/cells/de/net/managing-controls/)
- [Symbole zum Arbeitsblatt hinzufügen](/cells/de/net/insert-svg-to-excel/)
- [OLE-Objekte verwalten](/cells/de/net/managing-ole-objects/)
- [Bilder verwalten](/cells/de/net/managing-pictures/)
- [SmartArt verwalten](/cells/de/net/managing-smartart/)
- [TextBox verwalten](/cells/de/net/managing-textbox-of-excel/)
- [Fügen Sie dem Arbeitsblatt eine WordArt-Wasserzeichen hinzu](/cells/de/net/add-wordart-watermark-to-worksheet/)
- [Werte verlinkter Formen aktualisieren](/cells/de/net/refresh-values-of-linked-shapes/)
- [Form nach vorn oder hinten im Arbeitsblatt senden](/cells/de/net/send-shape-front-or-back-inside-the-worksheet/)
- [Formoptionen verwalten](/cells/de/net/managing-shape-options/)
- [Textoptionen der Form verwalten](/cells/de/net/managing-shape-text-options/)
- [Weberweiterungen - Office-Add-Ins](/cells/de/net/web-extensions-office-add-ins/)

{{< app/cells/assistant language="csharp" >}}
