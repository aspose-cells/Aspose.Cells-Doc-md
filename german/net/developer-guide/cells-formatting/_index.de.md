---
title: Zellen formatieren
linktitle: Zellen formatieren
type: docs
weight: 120
url: /de/net/cells-formatting/
description: Legen Sie Zahlenformat, Rahmen und Hintergrundfarbe für Excel-Dateien auf .NET Framework, .NET Core, Mono oder Xamarin-Plattformen fest.
---
## **Einführung**

{{% alert color="primary" %}}

 Aspose.Cells bietet die[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) und[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) Methoden der[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse, die zum Abrufen/Festlegen des Formatierungsstils einer Zelle verwendet wird. Aspose.Cells bietet auch eine[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Klasse.

{{% /alert %}}

## **Formatieren Sie Cells mit den Methoden GetStyle und SetStyle**

Wenden Sie verschiedene Arten von Formatierungsstilen auf Zellen an, um Hintergrund- oder Vordergrundfarben, Rahmen, Schriftarten, horizontale und vertikale Ausrichtung, Einzugsebene, Textrichtung, Drehwinkel und vieles mehr festzulegen.

### **Verwenden der GetStyle- und SetStyle-Methoden**

 Wenn Entwickler unterschiedliche Formatierungsstile auf verschiedene Zellen anwenden müssen, ist es besser, die[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) der Zelle mit[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) -Methode, geben Sie die Stilattribute an und wenden Sie dann die Formatierung an[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)Methode. Ein Beispiel ist unten angegeben, um diesen Ansatz zu veranschaulichen, um verschiedene Formatierungen auf eine Zelle anzuwenden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Verwenden des Stilobjekts zum Formatieren verschiedener Cells**

 Wenn Entwickler denselben Formatierungsstil auf verschiedene Zellen anwenden müssen, können sie verwenden[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt. Bitte befolgen Sie die nachstehenden Schritte, um die zu verwenden[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Objekt:

1.  Füge hinzu ein[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt durch Aufrufen der[**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) Methode der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse
1.  Greifen Sie auf die neu hinzugefügten zu[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Objekt
1.  Stellen Sie die gewünschten Eigenschaften/Attribute der ein[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Objekt, um die gewünschten Formatierungseinstellungen anzuwenden
1. Weisen Sie die konfigurierte zu[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Objekt zu Ihren gewünschten Zellen

Dieser Ansatz kann die Effizienz Ihrer Anwendungen erheblich verbessern und auch Speicher sparen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Verwenden von Microsoft Excel 2007 vordefinierte Stile**

Wenn Sie verschiedene Formatierungsstile für Microsoft Excel 2007 anwenden müssen, wenden Sie Stile mit dem Aspose.Cells API an. Ein Beispiel wird unten gegeben, um diesen Ansatz zu demonstrieren, um einen vordefinierten Stil auf eine Zelle anzuwenden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Ausgewählte Zeichen in Cell formatieren**

Der Umgang mit Schrifteinstellungen erklärt, wie Text in Zellen formatiert wird, aber es erklärt nur, wie der gesamte Zellinhalt formatiert wird. Was ist, wenn Sie nur ausgewählte Zeichen formatieren möchten?

Aspose.Cells unterstützt diese Funktion ebenfalls. In diesem Thema wird erläutert, wie wir diese Funktion effektiv nutzen.

### **Ausgewählte Zeichen formatieren**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält die[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Jeder Artikel in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung stellt ein Objekt der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Das[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse bietet die[**Figuren**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)Methode, die die folgenden Parameter benötigt, um einen Bereich von Zeichen in einer Zelle auszuwählen:

- **Startindex**, der Index des Zeichens, bei dem die Auswahl beginnt.
- **Anzahl von Charakteren**, die Anzahl der auszuwählenden Zeichen.

 Das[**Figuren**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) -Methode gibt eine Instanz von zurück[**Schrifteinstellung**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)-Klasse, mit der Entwickler die Zeichen genauso formatieren können wie eine Zelle, wie unten im Codebeispiel gezeigt. In der Ausgabedatei wird in der A1-Zelle das Wort „Besuch“ mit der Standardschrift formatiert, aber „Aspose!“. ist fett und blau.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

 Wenn Sie daran interessiert sind, einen Teil von Rich Text in einer Zelle zu formatieren, sollten Sie die Verwendung von in Betracht ziehen[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) Methoden. Das[[**Cell.GetCharacters**]](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) -Methode verwendet werden, um auf die Teile des Textes zuzugreifen, und dann können Änderungen mit vorgenommen werden[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) Methode, während die**Erhalten**-Methode gibt ein Array von zurück[**Schrifteinstellung**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) Objekte, die manipuliert werden können, um verschiedene Eigenschaften wie Schriftartname, Schriftfarbe, Fettschrift usw. festzulegen, und**Satz** -Methode verwendet werden, um die Änderungen anzuwenden.

{{% /alert %}}

## **Zeilen und Spalten formatieren**

Manchmal müssen Entwickler dieselbe Formatierung auf Zeilen oder Spalten anwenden. Das Anwenden der Formatierung auf einzelne Zellen dauert oft länger und ist keine gute Lösung.
Um dieses Problem zu beheben, bietet Aspose.Cells eine einfache und schnelle Möglichkeit, die in diesem Artikel ausführlich beschrieben wird.

### **Zeilen und Spalten formatieren**

 Aspose.Cells bietet eine Klasse, die[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Das[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung bietet a[**Reihen**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)Sammlung.

### **Formatieren einer Zeile**

 Jeder Artikel in der[**Reihen**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) Sammlung repräsentiert a[**Die Zeile**](https://reference.aspose.com/cells/net/aspose.cells/row) Objekt. Das[**Die Zeile**](https://reference.aspose.com/cells/net/aspose.cells/row)Objekt bietet die[**Stil anwenden**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) Methode zum Festlegen der Formatierung der Zeile. Um dieselbe Formatierung auf eine Zeile anzuwenden, verwenden Sie die[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Objekt. Die folgenden Schritte zeigen, wie Sie es verwenden.

1.  Füge hinzu ein[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Widerspruch gegen die[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse durch den Aufruf seiner[**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)Methode.
1.  Stellen Sie die ein[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Objekteigenschaften, um Formatierungseinstellungen anzuwenden.
1.  Setzen Sie die relevanten Attribute für die auf ON[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)Objekt.
1. Weisen Sie die konfigurierte zu[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Widerspruch gegen die[**Die Zeile**](https://reference.aspose.com/cells/net/aspose.cells/row)Objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Formatieren einer Spalte**

 Das[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung bietet auch a[**Säulen**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) Sammlung. Jeder Artikel in der[**Säulen**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) Sammlung repräsentiert a[**Spalte**](https://reference.aspose.com/cells/net/aspose.cells/column) Objekt. Ähnlich wie ein[**Die Zeile**](https://reference.aspose.com/cells/net/aspose.cells/row) Objekt, das[**Spalte**](https://reference.aspose.com/cells/net/aspose.cells/column) Objekt bietet auch die[**Stil anwenden**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)Methode zum Formatieren einer Spalte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **Themen vorantreiben**
- [Ausrichtungseinstellungen](/cells/de/net/cells-alignment-settings/)
- [Rahmeneinstellungen](/cells/de/net/cells-border-settings/)
- [Legen Sie bedingte Formate von Excel- und ODS-Dateien fest.](/cells/de/net/conditional-formatting/)
- [Excel-Designs und -Farben](/cells/de/net/excel-themes-and-colors/)
- [Einstellungen füllen](/cells/de/net/cells-fill-settings/)
- [Schrifteinstellungen](/cells/de/net/cells-font-settings/)
- [Formatieren Sie das Arbeitsblatt Cells in einer Arbeitsmappe](/cells/de/net/format-worksheet-cells-in-a-workbook/)
- [Implementieren Sie das 1904-Datumssystem](/cells/de/net/implement-1904-date-system/)
- [Zusammenführen und Trennen Cells](/cells/de/net/merging-and-unmerging-cells/)
- [Nummerneinstellungen](/cells/de/net/cells-number-settings/)
- [Abrufen und Festlegen des Stils für Zellen](/cells/de/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

