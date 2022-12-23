---
title: Fügen Sie Bilder und Formen aus Excel-Dateien ein.
linktitle: Formen
type: docs
weight: 140
url: /de/net/insert-shapes/
description: Verwalten Sie Bilder, Objekte und Formen in Excel-Dateien.
---
{{% alert color="primary" %}}

Manchmal müssen Sie einige notwendige Formen in das Arbeitsblatt einfügen. Möglicherweise müssen Sie dieselbe Form an verschiedenen Positionen des Arbeitsblatts einfügen. Oder Sie müssen Formen im Stapelbetrieb in das Arbeitsblatt einfügen.

 Keine Sorgen![Aspose.Cells](https://products.aspose.com/cells/)unterstützt all diese Operationen.

{{% /alert %}}

Die Formen in Excel werden hauptsächlich in die folgenden Typen unterteilt:
- **Bilder**
- **OleObjects**
- **Linien**
- **Rechtecke**
- **Grundformen**
- **Pfeile blockieren**
- **Gleichungsformen**
- **Flussdiagramme**
- **Sterne und Banner**
- **Beschriftungen**

 In diesem Leitfaden werden ein oder zwei Formen von jedem Typ ausgewählt, um Muster herzustellen. Anhand dieser Beispiele lernen Sie, wie man sie verwendet[Aspose.Cells](https://products.aspose.com/cells/) um die angegebene Form in das Arbeitsblatt einzufügen.

## **Hinzufügen von Bildern im Excel-Arbeitsblatt in C#**

Das Hinzufügen von Bildern zu einer Tabelle ist sehr einfach. Es dauert nur ein paar Zeilen Code:
 Einfach anrufen[**Addieren**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) Methode der[**Bilder**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) Sammlung (eingekapselt in der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Objekt). Das[**Addieren**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)Die Methode nimmt die folgenden Parameter an:

- **Zeilenindex oben links**, der Index der oberen linken Zeile.
- **Spaltenindex oben links**, der Index der oberen linken Spalte.
- **Name der Bilddatei**, der Name der Bilddatei, komplett mit Pfad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **Einfügen von OLE-Objekten in ein Excel-Arbeitsblatt in C#**

Aspose.Cells unterstützt das Hinzufügen, Extrahieren und Bearbeiten von OLE-Objekten in Arbeitsblättern. Aus diesem Grund hat Aspose.Cells die[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) Klasse, die zum Hinzufügen eines neuen OLE-Objekts zur Sammlungsliste verwendet wird. Eine andere Klasse,[**OLE-Objekt**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), stellt ein OLE-Objekt dar. Es hat einige wichtige Mitglieder:

-  Das[**Bilddaten**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)Die Eigenschaft gibt die Bilddaten (Symboldaten) vom Typ Byte-Array an. Das Bild wird angezeigt, um das OLE-Objekt im Arbeitsblatt anzuzeigen.
-  Das[**Objektdaten**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)Die Eigenschaft gibt die Objektdaten in Form eines Byte-Arrays an. Diese Daten werden im zugehörigen Programm angezeigt, wenn Sie auf das OLE-Objekt-Symbol doppelklicken.

Das folgende Beispiel zeigt, wie Sie einem Arbeitsblatt ein oder mehrere OLE-Objekte hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **Einfügen einer Zeile in ein Excel-Arbeitsblatt in C#**

 Die Form der Linie gehört zu den**Linien** Kategorie.

***In Microsoft Excel (z. B. 2007):***

- Wählen Sie die Zelle aus, in die Sie die Zeile einfügen möchten
- Klicken Sie auf das Menü Einfügen und dann auf Formen.
- Wählen Sie dann die Linie aus „Zuletzt verwendete Formen“ oder „Linien“ aus.

![](line.png)

***Mit Aspose.Cells***

Sie können die folgende Methode verwenden, um eine Zeile in das Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[öffentliche LineShape AddLine(
 int obereLinkeReihe,
 int oben,
 int obereLinkeSpalte,
 int links,
 int Höhe,
 int-Breite
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 Die Methode gibt a zurück[Linienform](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) Objekt.

{{% /alert %}}

Das folgende Beispiel zeigt, wie Sie eine Zeile in ein Arbeitsblatt einfügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

Führen Sie den obigen Code aus, Sie erhalten die folgenden Ergebnisse:

![](line2.png)



## **Einfügen eines Linienpfeils in das Excel-Arbeitsblatt in C#**

 Die Form des Linienpfeils gehört zu den**Linien** Kategorie. Es ist ein Sonderfall von line.

***In Microsoft Excel (z. B. 2007):***

- Wählen Sie die Zelle aus, in die Sie den Linienpfeil einfügen möchten
- Klicken Sie auf das Menü Einfügen und dann auf Formen.
- Wählen Sie dann den Linienpfeil aus „Zuletzt verwendete Formen“ oder „Linien“.

![](line_arrow1.png)

***Mit Aspose.Cells***

Sie können die folgende Methode verwenden, um einen Linienpfeil in das Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[öffentliche LineShape AddLine(
 int obereLinkeReihe,
 int oben,
 int obereLinkeSpalte,
 int links,
 int Höhe,
 int-Breite
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 Die Methode gibt a zurück[Linienform](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) Objekt.

{{% /alert %}}

Das folgende Beispiel zeigt, wie Sie einen Linienpfeil in ein Arbeitsblatt einfügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

Führen Sie den obigen Code aus, Sie erhalten die folgenden Ergebnisse:

![](line_arrow2.png)



## **Einfügen eines Rechtecks in ein Excel-Arbeitsblatt in C#**

 Die Form des Rechtecks gehört zu den**Rechtecke** Kategorie.

***In Microsoft Excel (z. B. 2007):***

- Wählen Sie die Zelle aus, in die Sie das Rechteck einfügen möchten
- Klicken Sie auf das Menü Einfügen und dann auf Formen.
- Wählen Sie dann das Rechteck aus „Zuletzt verwendete Formen“ oder „Rechtecke“ aus.

![](rectangle.png)

***Mit Aspose.Cells***

Sie können die folgende Methode verwenden, um ein Rechteck in das Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[public RectangleShape AddRectangle(
 int obereLinkeReihe,
 int oben,
 int obereLinkeSpalte,
 int links,
 int Höhe,
 int-Breite
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

 Die Methode gibt a zurück[Rechteckform](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) Objekt.

{{% /alert %}}

Das folgende Beispiel zeigt, wie Sie ein Rechteck in ein Arbeitsblatt einfügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

Führen Sie den obigen Code aus, Sie erhalten die folgenden Ergebnisse:

![](rectangle2.png)



## **Einfügen eines Cubes in ein Excel-Arbeitsblatt in C#**

Die Form des Würfels gehört zu den**Grundformen** Kategorie.

***In Microsoft Excel (z. B. 2007):***

- Wählen Sie die Zelle aus, in die Sie den Würfel einfügen möchten
- Klicken Sie auf das Menü Einfügen und dann auf Formen.
-  Wählen Sie dann den Würfel aus**Grundformen**

![](cube.png)

***Mit Aspose.Cells***

Sie können die folgende Methode verwenden, um einen Cube in das Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[öffentliche Form AddAutoShape(
 AutoShapeType-Typ,
 int obereLinkeReihe,
 int oben,
 int obereLinkeSpalte,
 int links,
 int Höhe,
 int-Breite
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Die Methode gibt a zurück[Form](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) Objekt.

{{% /alert %}}

Das folgende Beispiel zeigt, wie Sie einen Cube in ein Arbeitsblatt einfügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

Führen Sie den obigen Code aus, Sie erhalten die folgenden Ergebnisse:

![](cube2.png)



## **Einfügen eines Callout-Quad-Pfeils in das Excel-Arbeitsblatt in C#**

 Die Form des Callout-Quad-Pfeils gehört zu den**Pfeile blockieren** Kategorie.

***In Microsoft Excel (z. B. 2007):***

- Wählen Sie die Zelle aus, in die Sie den Callout-Quad-Pfeil einfügen möchten
- Klicken Sie auf das Menü Einfügen und dann auf Formen.
-  Wählen Sie dann den Callout-Quad-Pfeil aus**Pfeile blockieren**

![](callout_quad_arrow.png)

***Mit Aspose.Cells***

Sie können die folgende Methode verwenden, um einen Callout-Quad-Pfeil in das Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[öffentliche Form AddAutoShape(
 AutoShapeType-Typ,
 int obereLinkeReihe,
 int oben,
 int obereLinkeSpalte,
 int links,
 int Höhe,
 int-Breite
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Die Methode gibt a zurück[Form](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) Objekt.

{{% /alert %}}

Das folgende Beispiel zeigt, wie ein Callout-Quad-Pfeil in ein Arbeitsblatt eingefügt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

Führen Sie den obigen Code aus, Sie erhalten die folgenden Ergebnisse:

![](callout_quad_arrow2.png)



## **Einfügen eines Multiplikationszeichens in das Excel-Arbeitsblatt in C#**

 Die Form des Multiplikationszeichens gehört zu den**Gleichungsformen** Kategorie.

***In Microsoft Excel (z. B. 2007):***

- Wählen Sie die Zelle aus, in die Sie das Multiplikationszeichen einfügen möchten
- Klicken Sie auf das Menü Einfügen und dann auf Formen.
-  Wählen Sie dann das Multiplikationszeichen aus**Gleichungsformen**

![](multiplication_sign.png)

***Mit Aspose.Cells***

Sie können die folgende Methode verwenden, um ein Multiplikationszeichen in das Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[öffentliche Form AddAutoShape(
 AutoShapeType-Typ,
 int obereLinkeReihe,
 int oben,
 int obereLinkeSpalte,
 int links,
 int Höhe,
 int-Breite
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Die Methode gibt a zurück[Form](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) Objekt.

{{% /alert %}}

Das folgende Beispiel zeigt, wie Sie ein Multiplikationszeichen in ein Arbeitsblatt einfügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

Führen Sie den obigen Code aus, Sie erhalten die folgenden Ergebnisse:

![](multiplication_sign2.png)



## **Einfügen eines Multidokuments in ein Excel-Arbeitsblatt in C#**

 Die Form des Multidokuments gehört zu den**Flussdiagramme** Kategorie.

***In Microsoft Excel (z. B. 2007):***

- Wählen Sie die Zelle aus, in die Sie das Multidokument einfügen möchten
- Klicken Sie auf das Menü Einfügen und dann auf Formen.
-  Wählen Sie dann das Multidokument aus**Flussdiagramme**

![](multidocument.png)

***Mit Aspose.Cells***

Sie können die folgende Methode verwenden, um ein Multidokument in das Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[öffentliche Form AddAutoShape(
 AutoShapeType-Typ,
 int obereLinkeReihe,
 int oben,
 int obereLinkeSpalte,
 int links,
 int Höhe,
 int-Breite
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Die Methode gibt a zurück[Form](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) Objekt.

{{% /alert %}}

Das folgende Beispiel zeigt, wie Sie mehrere Dokumente in ein Arbeitsblatt einfügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

Führen Sie den obigen Code aus, Sie erhalten die folgenden Ergebnisse:

![](multidocument2.png)



## **Einfügen eines fünfzackigen Sterns in das Excel-Arbeitsblatt in C#**

 Die Form des fünfzackigen Sterns gehört zu den**Sterne und Banner** Kategorie.

***In Microsoft Excel (z. B. 2007):***

- Wählen Sie die Zelle aus, in die Sie den fünfzackigen Stern einfügen möchten
- Klicken Sie auf das Menü Einfügen und dann auf Formen.
-  Wählen Sie dann den fünfzackigen Stern aus**Sterne und Banner**

![](star_5_points.png)

***Mit Aspose.Cells***

Sie können die folgende Methode verwenden, um einen fünfzackigen Stern in das Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[öffentliche Form AddAutoShape(
 AutoShapeType-Typ,
 int obereLinkeReihe,
 int oben,
 int obereLinkeSpalte,
 int links,
 int Höhe,
 int-Breite
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Die Methode gibt a zurück[Form](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) Objekt.

{{% /alert %}}

Das folgende Beispiel zeigt, wie Sie einen fünfzackigen Stern in ein Arbeitsblatt einfügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

Führen Sie den obigen Code aus, Sie erhalten die folgenden Ergebnisse:

![](star_5_points2.png)



## **Einfügen einer Gedankenblasenwolke in ein Excel-Arbeitsblatt in C#**

 Die Form der Gedankenblasenwolke gehört zu den**Beschriftungen** Kategorie.

***In Microsoft Excel (z. B. 2007):***

- Wählen Sie die Zelle aus, in die Sie die Gedankenblasenwolke einfügen möchten
- Klicken Sie auf das Menü Einfügen und dann auf Formen.
-  Wählen Sie dann die Gedankenblasenwolke aus**Beschriftungen**

![](thought_bubble_cloud.png)

***Mit Aspose.Cells***

Sie können die folgende Methode verwenden, um eine Gedankenblasenwolke in das Arbeitsblatt einzufügen.

{{% alert color="primary" %}}

[öffentliche Form AddAutoShape(
 AutoShapeType-Typ,
 int obereLinkeReihe,
 int oben,
 int obereLinkeSpalte,
 int links,
 int Höhe,
 int-Breite
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Die Methode gibt a zurück[Form](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) Objekt.

{{% /alert %}}

Das folgende Beispiel zeigt, wie Sie eine Gedankenblasenwolke in ein Arbeitsblatt einfügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

Führen Sie den obigen Code aus, Sie erhalten die folgenden Ergebnisse:

![](thought_bubble_cloud2.png)

## **Themen vorantreiben**
- [Ändern Sie die Anpassungswerte der Form](/cells/de/net/change-adjustment-values-of-the-shape/)
- [Formen zwischen Arbeitsblättern kopieren](/cells/de/net/copy-shapes-between-worksheets/)
- [Daten in nicht primitiver Form](/cells/de/net/data-in-non-primitive-shape/)
- [Finden der absoluten Position der Form innerhalb des Arbeitsblatts](/cells/de/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Holen Sie sich Verbindungspunkte aus der Form](/cells/de/net/get-connection-points-from-shape/)
- [Steuerelemente verwalten](/cells/de/net/managing-controls/)
- [Symbole zum Arbeitsblatt hinzufügen](/cells/de/net/insert-svg-to-excel/)
- [Verwalten von OLE-Objekten](/cells/de/net/managing-ole-objects/)
- [Bilder verwalten](/cells/de/net/managing-pictures/)
- [Intelligente Kunst verwalten](/cells/de/net/managing-smartart/)
- [Verwalten von TextBox](/cells/de/net/managing-textbox-of-excel/)
- [WordArt-Wasserzeichen zum Arbeitsblatt hinzufügen](/cells/de/net/add-wordart-watermark-to-worksheet/)
- [Aktualisieren Sie die Werte verknüpfter Formen](/cells/de/net/refresh-values-of-linked-shapes/)
- [Senden Sie die Form nach vorne oder hinten in das Arbeitsblatt](/cells/de/net/send-shape-front-or-back-inside-the-worksheet/)
- [Formoptionen verwalten](/cells/de/net/managing-shape-options/)
- [Formentextoptionen verwalten](/cells/de/net/managing-shape-text-options/)
- [Weberweiterungen – Office-Add-Ins](/cells/de/net/web-extensions-office-add-ins/)

