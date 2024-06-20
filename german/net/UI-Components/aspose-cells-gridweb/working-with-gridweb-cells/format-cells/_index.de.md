---
title: Zellen formatieren
type: docs
weight: 40
url: /de/net/aspose-cells-gridweb/format-grid-cell/
keywords: GridWeb, Format, Style
description: Dieser Artikel führt ein, wie man einen Zellenstil für eine Zelle (GridCell) in GridWeb einrichtet oder anwendet.
---

{{% alert color="primary" %}} 

Dieses Thema bietet eine ausführliche Diskussion darüber, wie Zellen formatiert werden können.

Es umfasst die Formatierung von Zellen im GUI-Modus unter Verwendung des Aspose.Cells.GridWeb-SteuerElements "Style". Es zeigt auch, wie Zellen programmgesteuert formatiert werden können. Unterschiedliche Formatierungseinstellungen wie Schriftart, Rahmen und Zahlenformat werden erläutert und anhand von Beispielen illustriert.

{{% /alert %}} 
## **Formatieren von Zellen unter Verwendung des Style-Dialogs**
Zellen können auch [programmgesteuert](/cells/de/net/aspose-cells-gridweb/format-cells/) formatiert werden, aber der einfachste Weg, Zellen im Aspose.Cells.GridWeb-SteuerElement in einer WYSIWYG-Weise zu formatieren, ist die Verwendung des Style-Dialogs.

Um den Style-Dialog zu verwenden:
Markieren Sie einen Zellenbereich, klicken Sie mit der rechten Maustaste und wählen Sie **Format Cell**. 

**Auswahl von Format Cell** 

![todo:image_alt_text](format-cells_1.png)



Der Style-Dialog wird angezeigt. 

**Der Style-Dialog wird zum Formatieren von Zellen verwendet** 

![todo:image_alt_text](format-cells_2.png)

Der Style-Dialog ermöglicht es Benutzern, Zellen durch Anpassung von Schrift- und Rahmen-Einstellungen zu formatieren.
### **Anpassen von Schrift-Einstellungen**
Sie können die folgenden Schrift-Einstellungen mit dem Style-Dialog anpassen:

- Schriftart, wählen Sie eine gewünschte Schriftart aus der Liste.
- Schriftstil, wenden Sie einen Schriftstil wie fett, kursiv usw. an.
- Schriftgröße, wählen Sie eine Schriftgröße in Punkten.
- Unterstreichen, Text unterstreichen.
- Durchgestrichen, einen Durchstreichungseffekt auf den Text anwenden.
- Horizontale Ausrichtung, horizontale Ausrichtung auswählen.
- Vertikale Ausrichtung, vertikale Ausrichtung auswählen.
- Schriftfarbe, eine Schriftfarbe auswählen.
- Hintergrund, eine Farbe für den Hintergrund auswählen.

Sie können die ausgewählten Schrift-Einstellungen in einem kleinen Vorschaubereich überprüfen.

**Angepasste Schrift-Einstellungen** 

![todo:image_alt_text](format-cells_3.png)
### **Anpassen von Rahmen-Einstellungen**
Die Steuerung ermöglicht es Benutzern auch, einen Rahmen um Zellen zu zeichnen, indem sie Rahmen-Einstellungen im Style-Dialog anpassen.

Um die Optionen für rahmenbezogene Einstellungen anzuzeigen:
Klicken Sie auf **Rahmen** im Style-Dialog.
Border-bezogene Optionen werden angezeigt. 

**Randoptionen im Stil-Dialogfeld** 

![todo:image_alt_text](format-cells_4.png)

Die folgenden Randoptionen können im Stil-Dialogfeld ausgewählt werden:

- Randlinienstil: Wählen Sie den Randstil wie durchgezogen, gestrichelt usw. aus.
- Randlinienbreite: Wählen Sie die Randbreite in Pixel aus.
- Randlinienfarbe: Wählen Sie die Linienfarbe aus.
- Randleitungen: Wählen Sie die Nummerierung und Positionierung der Randleitungen aus.

**Benutzerdefinierte Rand-Einstellungen** 

![todo:image_alt_text](format-cells_5.png)
### **Einstellungen anwenden**
Klicken Sie auf **OK** im Stil-Dialog, um die Änderungen anzuwenden.

**Schrift- und Rand-Einstellungen angewandt** 

![todo:image_alt_text](format-cells_6.png)


## **Zellenformatierung mit API**
Zellen können auch programmgesteuert mithilfe des Aspose.Cells.GridWeb API formatiert werden. Jede Zelle hat eine Style-Eigenschaft, die ein GridTableItemStyle-Objekt darstellt. Verwenden Sie die Style-Eigenschaft, um Schrift- und Rand-Einstellungen anzupassen.
### **Schrift festlegen**
Um Schrift-Einstellungen programmgesteuert anzupassen:

1. Fügen Sie der Webformularsteuerung Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Greifen Sie auf die zu formatierende Zelle zu.
1. Greifen Sie auf den Zellenstil zu.
1. Legen Sie die Schriftgröße in Punkten fest.
1. Legen Sie den Schriftstil fest.
1. Setze Vordergrund- und Hintergrundfarben.
1. Setzen Sie die horizontale und vertikale Ausrichtung.
1. Setzen Sie den Stil zurück auf die Zelle.

**Ausgabe: Anpassung der Schriftarteneinstellungen in A1** 

![todo:image_alt_text](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **Rahmen einstellen**
Rahmen können auf einzelne Zellen oder auf einen Bereich angewendet werden.
#### **Einzelne Zelle**
Um die Rahmen einer einzelnen Zelle zu setzen:

1. Fügen Sie der Webformularsteuerung Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Greifen Sie auf die Zelle zu, die Sie formatieren möchten.
1. Greifen Sie auf das Style-Objekt der Zelle zu.
1. Setzen Sie den Rahmenstil.
1. Setzen Sie die Rahmenbreite in Pixeln.
1. Setzen Sie die Rahmenfarbe.
1. Setzen Sie den Stil auf die Zelle.

**Angepasste Rahmeneinstellungen auf einer einzelnen Zelle** 

![todo:image_alt_text](format-cells_8.png)

{{% alert color="primary" %}} 

Es ist möglich, für jede Rahmenlinie unterschiedliche Stile mit den Eigenschaften Style.TopBorderStyle, Style.BottomBorderStyle, Style.LeftBorderStyle, Style.RightBorderStyle der Zelle zu setzen.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **Zellbereich**
Um Rahmen in einem Zellbereich zu setzen:

1. Fügen Sie der Webformularsteuerung Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf ein gewünschtes Arbeitsblatt zu
1. Instanziieren Sie ein Objekt der Klasse WebBorderStyle
1. Setze den Stil des Randes auf Voll oder Gepunktet usw.
1. Setze die Breite des Randes in Pixel
1. Setze die Farbe des Randes
1. Wenden Sie die in WebBorderStyle-Objekt gespeicherten Randeinstellungen auf einen bestimmten Zellenbereich an

**Ein Zellenbereich mit benutzerdefinierten Randeinstellungen** 

![todo:image_alt_text](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **Einstellen von Zahlenformaten**
Aspose.Cells.GridWeb unterstützt das Festlegen von Zahlenformaten. Es gibt 59 eingebaute Zahlenformate. Um sie zu sehen, verweisen Sie bitte auf diese [Liste der unterstützten Zahlenformate](/cells/de/net/aspose-cells-gridweb/list-of-supported-number-formats/).

Alle eingebauten Zahlenformate befinden sich in der NumberType-Enumeration. Um ein eingebautes Zahlenformat zu verwenden, setzen Sie den NumberType mit der SetNumberType-Methode des Zellenobjekts auf ein Zahlenformat aus der NumberType-Enumeration.

Verwenden Sie zum Festlegen eines benutzerdefinierten Zahlenformats die SetCustom-Methode der Zelle.

**Zahlenformat-Einstellungen auf B1 und B2 angewendet** 

![todo:image_alt_text](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}
