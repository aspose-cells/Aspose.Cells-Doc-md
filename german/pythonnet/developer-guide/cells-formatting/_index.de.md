---
title: Zellen formatieren
description: Erfahren Sie, wie Sie Zellen in Aspose.Cells für Python via .NET formatieren und stylen, einschließlich Zahlenformatierung, Datumsformatierung, Schriftarten und anderer Zellstiloptionen. Unser Leitfaden hilft Ihnen, ansprechende und professionell aussehende Tabellen zu erstellen.
keywords: Aspose.Cells für Python via .NET, Zellenformatierung, Styling, Zahlenformatierung, Datumsformatierung, Schriftstil, Zellstiloptionen, Tabellen, erstellen, professionelles Aussehen, Zeilen und Spalten formatieren.
linktitle: Zellen formatieren
type: docs
weight: 120
url: /de/python-net/cells-formatting/
---

## **Einführung**

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET bietet die [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style)- und [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style)-Methoden der [Cell](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-Klasse, die verwendet werden, um den Formatstil einer Zelle zu erhalten/zu setzen. Aspose.Cells für Python via .NET stellt auch eine [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-Klasse bereit.

{{% /alert %}}

## **Wie man Zellen mit den Methoden GetStyle und SetStyle formatiert**

Auf Zellen verschiedene Arten von Formatierungsstilen anwenden, um Hintergrund- oder Vordergrundfarben, Rahmen, Schriftarten, horizontale und vertikale Ausrichtungen, Einrückungsebene, Textausrichtung, Drehwinkel und vieles mehr festzulegen.

### **Wie man die GetStyle und SetStyle Methoden verwendet**

Wenn Entwickler unterschiedliche Formatierungsstile auf verschiedene Zellen anwenden müssen, ist es besser, den [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) der Zelle mit der [**Cell.get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) Methode abzurufen, die Style-Attribute anzugeben und dann die Formatierung mit der [**Cell.set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) Methode anzuwenden. Ein Beispiel ist unten gegeben, um diesen Ansatz zur Anwendung verschiedener Formatierungen auf einer Zelle zu demonstrieren.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.py" >}}

### **Wie man das Style-Objekt verwendet, um verschiedene Zellen zu formatieren**

Wenn Entwickler denselben Formatierungsstil auf verschiedenen Zellen anwenden müssen, können sie das [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) Objekt verwenden. Bitte folgen Sie den unten stehenden Schritten, um das [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) Objekt zu verwenden:

1. Fügen Sie ein [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) Objekt hinzu, indem Sie die [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style) Methode der [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) Klasse aufrufen
1. Greifen Sie auf das neu hinzugefügte [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) Objekt zu
1. Setzen Sie die gewünschten Eigenschaften/Attribute des [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) Objekts, um die gewünschten Formatierungseinstellungen anzuwenden
1. Weisen Sie den konfigurierten [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) Objekt Ihren gewünschten Zellen zu

Dieser Ansatz kann die Effizienz Ihrer Anwendungen erheblich verbessern und auch Speicherplatz sparen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingStyleObject-1.py" >}}

### **Wie man die Microsoft Excel 2007 vordefinierten Stile verwendet**

Wenn Sie unterschiedliche Formatierungsstile für Microsoft Excel 2007 anwenden müssen, nutzen Sie die Styles mit der Aspose.Cells für Python via .NET API. Unten ist ein Beispiel, um diesen Ansatz zu demonstrieren, wie man einen vordefinierten Stil auf eine Zelle anwendet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.py" >}}



## **Wie man ausgewählte Zeichen in einer Zelle formatiert**

Der Umgang mit Schriftart-Einstellungen erklärt, wie Text in Zellen formatiert wird, aber es erklärt nur, wie der gesamte Zellinhalt formatiert wird. Was ist, wenn Sie nur bestimmte Zeichen formatieren möchten?

Aspose.Cells für Python via .NET unterstützt diese Funktion ebenfalls. Dieser Abschnitt erklärt, wie man diese Funktion effektiv nutzt.

### **Wie man ausgewählte Zeichen formatiert**

Aspose.Cells für Python via .NET bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse enthält die [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse bietet eine [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Sammlung. Jedes Element in der [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Sammlung stellt ein Objekt der [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-Klasse dar.

Die [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) Klasse bietet die [**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters) Methode, die folgende Parameter annimmt, um eine Reihe von Zeichen innerhalb einer Zelle auszuwählen:

- **Startindex**: Der Index des Zeichens, von dem die Auswahl beginnt.
- **Anzahl der Zeichen**: Die Anzahl der ausgewählten Zeichen.

Die [**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters) Methode gibt eine Instanz der [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) Klasse zurück, die Entwicklern ermöglicht, die Zeichen genauso zu formatieren, wie sie eine Zelle formatieren würden, wie unten im Beispielcode gezeigt. In der Ausgabedatei wird im A1-Zelle das Wort 'Besuchen' mit der Standardschriftart formatiert, aber 'Aspose!' ist fett und blau.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormattingSelectedCharacters-1.py" >}}

{{% alert color="primary" %}}

Wenn Sie daran interessiert sind, einen Teil des Rich Text in einer Zelle zu formatieren, sollten Sie die Methoden [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) & [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters) verwenden. Die [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters)-Methode wird verwendet, um auf die Textteile zuzugreifen, und Änderungen können mit der [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters)-Methode vorgenommen werden, während die **Get**-Methode ein Array von [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting)-Objekten zurückgibt, die manipuliert werden können, um verschiedene Eigenschaften wie Schriftart, Schriftfarbe, Fettdruck usw. einzustellen. Die **Set**-Methode kann zum Anwenden der Änderungen verwendet werden.

{{% /alert %}}

## **Wie man Zeilen und Spalten formatiert**

Manchmal müssen Entwickler dieselbe Formatierung auf Zeilen oder Spalten anwenden. Die Formatierung einzelner Zellen nacheinander dauert oft länger und ist keine gute Lösung.
Um dieses Problem zu lösen, bietet Aspose.Cells für Python via .NET eine einfache, schnelle Methode, die in diesem Artikel ausführlich erläutert wird.

### **Formatierung von Zeilen & Spalten**

Aspose.Cells für Python via .NET bietet eine Klasse, die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) heißt, welche eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse bietet eine [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Sammlung. Die [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Sammlung stellt eine [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows)-Sammlung bereit.

### **Wie man eine Zeile formatiert**

Jedes Element in der [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows)-Sammlung repräsentiert ein [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)-Objekt. Das [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)-Objekt bietet die [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style)-Methode zum Festlegen der Formatierung der Zeile. Um dieselbe Formatierung auf eine Zeile anzuwenden, verwenden Sie das [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-Objekt. Die folgenden Schritte zeigen, wie es verwendet wird.

1. Fügen Sie ein [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-Objekt zur [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse hinzu, indem Sie ihre [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style)-Methode aufrufen.
1. Legen Sie die Eigenschaften des [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-Objekts fest, um Formatierungseinstellungen anzuwenden.
1. Schalten Sie die relevanten Attribute für das [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag)-Objekt EIN.
1. Weisen Sie das konfigurierte [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-Objekt der [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)-Klasse zu.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingARow-1.py" >}}

### **Wie man eine Spalte formatiert**

Die [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Sammlung bietet auch eine [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns)-Sammlung. Jedes Element in der [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns)-Sammlung repräsentiert ein [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column)-Objekt. Ähnlich wie ein [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)-Objekt, bietet das [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column)-Objekt auch die [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style)-Methode zur Formatierung einer Spalte.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingAColumn-1.py" >}}

## **Erweiterte Themen**
- [Ausrichtungseinstellungen](/cells/de/python-net/cells-alignment-settings/)
- [Rahmeneinstellungen](/cells/de/python-net/cells-border-settings/)
- [Bedingte Formate von Excel- und ODS-Dateien festlegen.](/cells/de/python-net/conditional-formatting/)
- [Excel-Themen und Farben](/cells/de/python-net/excel-themes-and-colors/)
- [Fülleinstellungen](/cells/de/python-net/cells-fill-settings/)
- [Schriftarteinstellungen](/cells/de/python-net/cells-font-settings/)
- [Zellenformat in einer Arbeitsmappe](/cells/de/python-net/format-worksheet-cells-in-a-workbook/)
- [Implementieren des 1904-Datumsformats](/cells/de/python-net/implement-1904-date-system/)
- [Zusammenführen und Aufheben der Zellenzusammenführung](/cells/de/python-net/merging-and-unmerging-cells/)
- [Nummern-Einstellungen](/cells/de/python-net/cells-number-settings/)
- [Stil für Zellen abrufen und festlegen](/cells/de/python-net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="python-net" >}}
