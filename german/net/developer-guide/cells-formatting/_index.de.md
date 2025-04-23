---
title: Zellen formatieren
description: Erfahren Sie, wie Sie bei Aspose.Cells for .NET Zellen formatieren und gestalten, einschließlich der Nummernformatierung, Datumsformatierung, Schriftartenstile und anderer Zellformatierungsoptionen. Unser Leitfaden hilft Ihnen, attraktive und professionell aussehende Tabellenkalkulationen zu erstellen.
keywords: Aspose.Cells for .NET, Zellformatierung, Gestaltung, Nummernformatierung, Datumsformatierung, Schriftart Stil, Zellformatierungsoptionen, Tabellenkalkulation, erstellen, professionelles Aussehen, Zeilen und Spalten formatieren.
linktitle: Zellen formatieren
type: docs
weight: 120
url: /de/net/cells-formatting/
---

## **Einführung**

{{% alert color="primary" %}}

Aspose.Cells bietet die Methoden [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) und [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) der Klasse [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) zur Abfrage und Festlegung des Formatierungsstils einer Zelle. Aspose.Cells stellt auch eine Klasse [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) bereit.

{{% /alert %}}

## **Wie man Zellen mit den Methoden GetStyle und SetStyle formatiert**

Auf Zellen verschiedene Arten von Formatierungsstilen anwenden, um Hintergrund- oder Vordergrundfarben, Rahmen, Schriftarten, horizontale und vertikale Ausrichtungen, Einrückungsebene, Textausrichtung, Drehwinkel und vieles mehr festzulegen.

### **Wie man die GetStyle und SetStyle Methoden verwendet**

Wenn Entwickler unterschiedliche Formatierungsstile auf verschiedene Zellen anwenden müssen, ist es besser, den [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) der Zelle mit der [**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) Methode abzurufen, die Style-Attribute anzugeben und dann die Formatierung mit der [**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) Methode anzuwenden. Ein Beispiel ist unten gegeben, um diesen Ansatz zur Anwendung verschiedener Formatierungen auf einer Zelle zu demonstrieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Wie man das Style-Objekt verwendet, um verschiedene Zellen zu formatieren**

Wenn Entwickler denselben Formatierungsstil auf verschiedenen Zellen anwenden müssen, können sie das [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt verwenden. Bitte folgen Sie den unten stehenden Schritten, um das [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt zu verwenden:

1. Fügen Sie ein [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt hinzu, indem Sie die [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) Methode der [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse aufrufen
1. Greifen Sie auf das neu hinzugefügte [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt zu
1. Setzen Sie die gewünschten Eigenschaften/Attribute des [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekts, um die gewünschten Formatierungseinstellungen anzuwenden
1. Weisen Sie den konfigurierten [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt Ihren gewünschten Zellen zu

Dieser Ansatz kann die Effizienz Ihrer Anwendungen erheblich verbessern und auch Speicherplatz sparen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Wie man die Microsoft Excel 2007 vordefinierten Stile verwendet**

Wenn Sie unterschiedliche Formatierungsstile für Microsoft Excel 2007 anwenden müssen, wenden Sie Stile mithilfe der Aspose.Cells API an. Ein Beispiel unten zeigt diesen Ansatz zur Anwendung eines vordefinierten Stils auf einer Zelle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Wie man ausgewählte Zeichen in einer Zelle formatiert**

Der Umgang mit Schriftart-Einstellungen erklärt, wie Text in Zellen formatiert wird, aber es erklärt nur, wie der gesamte Zellinhalt formatiert wird. Was ist, wenn Sie nur bestimmte Zeichen formatieren möchten?

Aspose.Cells unterstützt auch diese Funktion. In diesem Thema wird erläutert, wie wir diese Funktion effektiv verwenden.

### **Wie man ausgewählte Zeichen formatiert**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält die [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jede Arbeitsmappe in einer Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung repräsentiert ein Objekt der [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse.

Die [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse bietet die [**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) Methode, die folgende Parameter annimmt, um eine Reihe von Zeichen innerhalb einer Zelle auszuwählen:

- **Startindex**: Der Index des Zeichens, von dem die Auswahl beginnt.
- **Anzahl der Zeichen**: Die Anzahl der ausgewählten Zeichen.

Die [**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) Methode gibt eine Instanz der [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) Klasse zurück, die Entwicklern ermöglicht, die Zeichen genauso zu formatieren, wie sie eine Zelle formatieren würden, wie unten im Beispielcode gezeigt. In der Ausgabedatei wird im A1-Zelle das Wort 'Besuchen' mit der Standardschriftart formatiert, aber 'Aspose!' ist fett und blau.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

Wenn Sie daran interessiert sind, einen Teil des Rich-Texts in einer Zelle zu formatieren, sollten Sie die Methoden [**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) und [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) in Betracht ziehen. Die [[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters)-Methode wird verwendet, um auf die Textabschnitte zuzugreifen, und dann können Änderungen mit der [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)-Methode vorgenommen werden, während die **Get**-Methode ein Array von [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)-Objekten zurückgibt, die manipuliert werden können, um verschiedene Eigenschaften wie Schriftart, Schriftfarbe, Fettung usw. festzulegen, und die **Set**-Methode kann verwendet werden, um die Änderungen anzuwenden.

{{% /alert %}}

## **Wie man Zeilen und Spalten formatiert**

Manchmal müssen Entwickler dieselbe Formatierung auf Zeilen oder Spalten anwenden. Die Formatierung einzelner Zellen nacheinander dauert oft länger und ist keine gute Lösung.
Um dieses Problem zu lösen, bietet Aspose.Cells einen einfachen, schnellen Weg, der in diesem Artikel ausführlich erörtert wird.

### **Formatierung von Zeilen & Spalten**

Aspose.Cells bietet eine Klasse, die [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung. Die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung bietet eine [**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)-Sammlung.

### **Wie man eine Zeile formatiert**

Jedes Element in der [**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)-Sammlung repräsentiert ein [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)-Objekt. Das [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)-Objekt bietet die [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)-Methode zum Festlegen der Formatierung der Zeile. Um dieselbe Formatierung auf eine Zeile anzuwenden, verwenden Sie das [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-Objekt. Die folgenden Schritte zeigen, wie es verwendet wird.

1. Fügen Sie ein [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-Objekt zur [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse hinzu, indem Sie ihre [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)-Methode aufrufen.
1. Legen Sie die Eigenschaften des [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-Objekts fest, um Formatierungseinstellungen anzuwenden.
1. Schalten Sie die relevanten Attribute für das [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)-Objekt EIN.
1. Weisen Sie das konfigurierte [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-Objekt der [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)-Klasse zu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Wie man eine Spalte formatiert**

Die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung bietet auch eine [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns)-Sammlung. Jedes Element in der [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns)-Sammlung repräsentiert ein [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column)-Objekt. Ähnlich wie ein [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)-Objekt, bietet das [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column)-Objekt auch die [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)-Methode zur Formatierung einer Spalte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **Erweiterte Themen**
- [Ausrichtungseinstellungen](/cells/de/net/cells-alignment-settings/)
- [Rahmeneinstellungen](/cells/de/net/cells-border-settings/)
- [Bedingte Formate von Excel- und ODS-Dateien festlegen.](/cells/de/net/conditional-formatting/)
- [Excel-Themen und Farben](/cells/de/net/excel-themes-and-colors/)
- [Fülleinstellungen](/cells/de/net/cells-fill-settings/)
- [Schriftarteinstellungen](/cells/de/net/cells-font-settings/)
- [Zellenformat in einer Arbeitsmappe](/cells/de/net/format-worksheet-cells-in-a-workbook/)
- [Implementieren des 1904-Datumsformats](/cells/de/net/implement-1904-date-system/)
- [Zusammenführen und Aufheben der Zellenzusammenführung](/cells/de/net/merging-and-unmerging-cells/)
- [Nummern-Einstellungen](/cells/de/net/cells-number-settings/)
- [Stil für Zellen abrufen und festlegen](/cells/de/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="csharp" >}}
