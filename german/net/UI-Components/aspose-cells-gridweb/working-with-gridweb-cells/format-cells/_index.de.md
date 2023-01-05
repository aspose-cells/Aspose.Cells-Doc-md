---
title: Cells formatieren
type: docs
weight: 40
url: /de/net/format-grid-cells/
---
{{% alert color="primary" %}} 

In diesem Thema wird ausführlich erläutert, wie Zellen formatiert werden.

Es behandelt das Formatieren von Zellen im GUI-Modus mit dem Style-Dialog des Aspose.Cells.GridWeb-Steuerelements. Außerdem wird gezeigt, wie Zellen programmgesteuert formatiert werden. Unterschiedliche Formateinstellungen wie Schriftart, Rahmen und Zahlenformat werden besprochen und mit Beispielen illustriert.

{{% /alert %}} 
## **Formatieren Cells Verwenden des Stildialogs**
 Cells kann formatiert werden[programmatisch](/cells/de/net/format-cells/)Aber der einfachste Weg, Zellen im Aspose.Cells.GridWeb-Steuerelement auf WYSIWYG-Weise zu formatieren, ist die Verwendung des Stil-Dialogfelds.

So verwenden Sie das Dialogfeld „Stil“:
 Wählen Sie einen Bereich von Zellen aus, klicken Sie dann mit der rechten Maustaste und wählen Sie aus**Cell formatieren**. 

**Auswahl des Formats Cell** 

![todo: Bild_alt_Text](format-cells_1.png)



 Das Dialogfeld „Stil“ wird angezeigt.

**Der Stil-Dialog wird verwendet, um Zellen zu formatieren** 

![todo: Bild_alt_Text](format-cells_2.png)

Im Dialogfeld "Stil" können Benutzer Zellen formatieren, indem sie Schriftart- und Rahmeneinstellungen anpassen.
### **Schrifteinstellungen anpassen**
Sie können die folgenden Schriftarteinstellungen mithilfe des Dialogfelds „Stil“ anpassen:

- Schriftartname, wählen Sie eine gewünschte Schriftart aus der Liste aus.
- Schriftstil, wenden Sie einen Schriftstil wie fett, kursiv usw. an.
- Schriftgröße, wählen Sie eine Schriftgröße in Punkt aus.
- Unterstreichen, Text unterstreichen.
- Durchgestrichen, wenden Sie einen durchgestrichenen Effekt auf den Text an.
- Horizontale Ausrichtung, horizontale Ausrichtung auswählen.
- Vertikale Ausrichtung, vertikale Ausrichtung auswählen.
- Schriftfarbe, wählen Sie eine Schriftfarbe aus.
- Hintergrund, wählen Sie eine Farbe für den Hintergrund aus.

In einem kleinen Vorschaubereich können Sie die gewählten Schrifteinstellungen überprüfen.

**Benutzerdefinierte Schriftarteinstellungen** 

![todo: Bild_alt_Text](format-cells_3.png)
### **Randeinstellungen anpassen**
Das Steuerelement ermöglicht es Benutzern auch, einen Rahmen um Zellen zu ziehen, indem sie die Rahmeneinstellungen im Dialogfeld "Stil" anpassen.

So zeigen Sie randbezogene Optionen an:
 Klicken**Grenzen** im Stildialog.
 Rahmenbezogene Optionen werden angezeigt.

**Rahmenoptionen im Stildialog** 

![todo: Bild_alt_Text](format-cells_4.png)

Die folgenden Rahmenoptionen können im Dialogfeld „Stil“ ausgewählt werden:

- Rahmenlinienstil, wählen Sie den Rahmenstil wie durchgehend, gestrichelt usw.
- Rahmenlinienbreite, wählen Sie die Rahmenbreite in Pixel aus.
- Grenzlinienfarbe, wählen Sie die Linienfarbe aus.
- Grenzlinien, wählen Sie die Nummerierung und Positionierung der Grenzlinien aus.

**Benutzerdefinierte Randeinstellungen** 

![todo: Bild_alt_Text](format-cells_5.png)
### **Anwenden von Einstellungen**
 Klicken**OK** im Dialogfeld „Stil“, um die Änderungen zu übernehmen.

**Schrift- und Randeinstellungen angewendet** 

![todo: Bild_alt_Text](format-cells_6.png)


## **Formatieren von Cells Verwenden von API**
Cells kann auch programmgesteuert mit Aspose.Cells.GridWeb API formatiert werden. Jede Zelle hat eine Style-Eigenschaft, die ein GridTableItemStyle-Objekt darstellt. Verwenden Sie die Style-Eigenschaft, um Schriftart- und Rahmeneinstellungen anzupassen.
### **Schriftart einstellen**
So passen Sie die Schriftarteinstellungen programmgesteuert an:

1. Fügen Sie einem Webformular das Aspose.Cells.GridWeb-Steuerelement hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Greifen Sie auf die Zelle zu, die Sie formatieren.
1. Greifen Sie auf den Stil der Zelle zu.
1. Legen Sie die Schriftgröße in Punkt fest.
1. Legen Sie den Schriftstil fest.
1. Vorder- und Hintergrundfarbe festlegen.
1. Legen Sie die horizontale und vertikale Ausrichtung fest.
1. Setzen Sie den Stil zurück auf die Zelle.

**Ausgabe: benutzerdefinierte Schriftarteinstellungen, die in A1 angezeigt werden** 

![todo: Bild_alt_Text](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **Grenzen setzen**
Rahmen können auf einzelne Zellen oder auf einen Bereich angewendet werden.
#### **Einzeln Cell**
So legen Sie die Grenzen einer einzelnen Zelle fest:

1. Fügen Sie einem Webformular das Aspose.Cells.GridWeb-Steuerelement hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Greifen Sie auf die Zelle zu, die Sie formatieren möchten.
1. Greifen Sie auf das Style-Objekt der Zelle zu.
1. Legen Sie den Rahmenstil fest.
1. Stellen Sie die Rahmenbreite in Pixel ein.
1. Legen Sie die Rahmenfarbe fest.
1. Legen Sie den Stil für die Zelle fest.

**Benutzerdefinierte Rahmeneinstellungen für eine einzelne Zelle** 

![todo: Bild_alt_Text](format-cells_8.png)

{{% alert color="primary" %}} 

Mit den Eigenschaften Style.TopBorderStyle, Style.BottomBorderStyle, Style.LeftBorderStyle, Style.RightBorderStyle der Zelle können für jede Rahmenlinie unterschiedliche Stile festgelegt werden.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **Bereich von Cells**
So legen Sie Rahmen für einen Zellbereich fest:

1. Fügen Sie Ihrem Webformular das Aspose.Cells.GridWeb-Steuerelement hinzu
1. Greifen Sie auf ein gewünschtes Arbeitsblatt zu
1. Instanziieren Sie ein Objekt der WebBorderStyle-Klasse
1. Stellen Sie den Stil des Rahmens auf Voll oder Gestrichelt usw. ein.
1. Stellen Sie die Breite des Rahmens in Pixel ein
1. Legen Sie die Farbe des Rahmens fest
1. Wenden Sie die im WebBorderStyle-Objekt gespeicherten Rahmeneinstellungen auf einen angegebenen Zellbereich an

**Eine Reihe von Zellen mit benutzerdefinierten Randeinstellungen** 

![todo: Bild_alt_Text](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **Zahlenformate einstellen**
 Aspose.Cells. GridWeb unterstützt die Einstellung von Zahlenformaten. Es gibt 59 integrierte Zahlenformate. Um sie zu sehen, beziehen Sie sich bitte auf diese[Liste der unterstützten Zahlenformate](/cells/de/net/list-of-supported-number-formats/).

Alle integrierten Zahlenformate befinden sich in der NumberType-Enumeration. Um ein integriertes Zahlenformat zu verwenden, legen Sie den NumberType mithilfe der SetNumberType-Methode eines Zellenobjekts auf ein Zahlenformat aus der NumberType-Enumeration fest.

Um ein benutzerdefiniertes Zahlenformat festzulegen, verwenden Sie die SetCustom-Methode der Zelle.

**Auf B1 und B2 angewendete Zahlenformateinstellungen** 

![todo: Bild_alt_Text](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}
