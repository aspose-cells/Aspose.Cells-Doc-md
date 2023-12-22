---
title: Zellen formatieren
description: Erfahren Sie, wie Sie Zellen in Aspose.Cells for .NET formatieren und formatieren, einschließlich Zahlenformatierung, Datumsformatierung, Schriftarten und anderen Zellenstiloptionen. Unser Leitfaden hilft Ihnen bei der Erstellung attraktiver und professionell aussehender Tabellenkalkulationen.
keywords: Aspose.Cells for .NET, cell formatting, styling, number formatting, date formatting, font style, cell style options, spreadsheet, create, professional look, format rows and columns.
linktitle: Zellen formatieren
type: docs
weight: 120
url: /de/net/cells-formatting/
---
##  **Einführung**

{{% alert color="primary" %}}

 Aspose.Cells bietet die[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) Und[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) Methoden der[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse, die zum Abrufen/Festlegen des Formatierungsstils einer Zelle verwendet wird. Aspose.Cells bietet auch eine[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Klasse.

{{% /alert %}}

##  **So formatieren Sie Cells mit den Methoden GetStyle und SetStyle**

Wenden Sie verschiedene Arten von Formatierungsstilen auf Zellen an, um Hintergrund- oder Vordergrundfarben, Rahmen, Schriftarten, horizontale und vertikale Ausrichtung, Einrückungsebene, Textrichtung, Drehwinkel und vieles mehr festzulegen.

###  **So verwenden Sie die Methoden GetStyle und SetStyle**

 Wenn Entwickler unterschiedliche Formatierungsstile auf verschiedene Zellen anwenden müssen, ist es besser, diese zu erhalten[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) der Zelle verwenden[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) Geben Sie mit der Methode die Stilattribute an und wenden Sie dann die Formatierung an[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)Methode. Nachfolgend finden Sie ein Beispiel, um diesen Ansatz zum Anwenden verschiedener Formatierungen auf eine Zelle zu veranschaulichen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

###  **So verwenden Sie ein Stilobjekt zum Formatieren anderer Cells**

 Wenn Entwickler denselben Formatierungsstil auf verschiedene Zellen anwenden müssen, können sie diesen verwenden[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt. Bitte befolgen Sie die folgenden Schritte, um das zu verwenden[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Objekt:

1.  Füge hinzu ein[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt durch Aufrufen des[**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) Methode der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse
1.  Greifen Sie auf die neu hinzugefügten zu[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) object
1.  Legen Sie die gewünschten Eigenschaften/Attribute fest[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Objekt, um die gewünschten Formatierungseinstellungen anzuwenden
1.  Weisen Sie die konfigurierten zu[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)widersprechen Sie den gewünschten Zellen

Dieser Ansatz kann die Effizienz Ihrer Anwendungen erheblich verbessern und außerdem Speicher sparen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

###  **So verwenden Sie Microsoft vordefinierte Excel 2007-Stile**

Wenn Sie verschiedene Formatierungsstile für Microsoft Excel 2007 anwenden müssen, wenden Sie Stile mit Aspose.Cells API an. Nachfolgend finden Sie ein Beispiel, um diesen Ansatz zum Anwenden eines vordefinierten Stils auf eine Zelle zu veranschaulichen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



##  **So formatieren Sie ausgewählte Zeichen in einem Cell**

Im Umgang mit den Schriftarteinstellungen wird erläutert, wie Text in Zellen formatiert wird, es wird jedoch nur erklärt, wie der gesamte Zellinhalt formatiert wird. Was ist, wenn Sie nur ausgewählte Zeichen formatieren möchten?

Aspose.Cells unterstützt diese Funktion ebenfalls. In diesem Thema wird erläutert, wie wir diese Funktion effektiv nutzen.

###  **So formatieren Sie ausgewählte Zeichen**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält die[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Jedes Element in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Die Sammlung stellt ein Objekt dar[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse bietet die[**Figuren**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)Methode, die die folgenden Parameter verwendet, um einen Bereich von Zeichen innerhalb einer Zelle auszuwählen:

- *Startindex**, der Index des Zeichens, bei dem die Auswahl beginnt.
- *Anzahl der Zeichen**, die Anzahl der auszuwählenden Zeichen.

 Der[**Figuren**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) Die Methode gibt eine Instanz von zurück[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)Klasse, die es Entwicklern ermöglicht, die Zeichen auf die gleiche Weise zu formatieren wie eine Zelle, wie unten im Codebeispiel gezeigt. In der Ausgabedatei wird in der Zelle A1 das Wort „Visit“ mit der Standardschriftart formatiert, jedoch mit „Aspose!“. ist fett und blau.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

Wenn Sie daran interessiert sind, einen Teil des Rich-Texts in einer Zelle zu formatieren, sollten Sie die Verwendung von in Betracht ziehen[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) Methoden. Der[[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) Die Methode soll verwendet werden, um auf die Teile des Textes zuzugreifen, und dann können Änderungen mit der vorgenommen werden[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) Methode, während die**Erhalten** Methode gibt ein Array von zurück[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) Objekte, die manipuliert werden können, um verschiedene Eigenschaften wie Schriftartnamen, Schriftfarbe, Fettigkeit usw. festzulegen**Satz** Mit dieser Methode können die Änderungen übernommen werden.

{{% /alert %}}

##  **So formatieren Sie Zeilen und Spalten**

Manchmal müssen Entwickler dieselbe Formatierung auf Zeilen oder Spalten anwenden. Das Anwenden einer Formatierung auf Zellen einzeln dauert oft länger und ist keine gute Lösung.
Um dieses Problem zu beheben, bietet Aspose.Cells eine einfache und schnelle Möglichkeit, die in diesem Artikel ausführlich erläutert wird.

###  **Zeilen und Spalten formatieren**

 Aspose.Cells bietet eine Klasse, die[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung bietet a[**Reihen**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)Sammlung.

###  **So formatieren Sie eine Zeile**

 Jedes Element in der[**Reihen**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) Sammlung repräsentiert a[**Reihe**](https://reference.aspose.com/cells/net/aspose.cells/row) Objekt. Der[**Reihe**](https://reference.aspose.com/cells/net/aspose.cells/row)Objekt bietet die[**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) Methode, mit der die Formatierung der Zeile festgelegt wird. Um dieselbe Formatierung auf eine Zeile anzuwenden, verwenden Sie die[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Objekt. Die folgenden Schritte zeigen, wie Sie es verwenden.

1.  Füge hinzu ein[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Einspruch gegen die[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse durch Aufrufen von its[**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)Methode.
1.  Stellen Sie die ein[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Objekteigenschaften, um Formatierungseinstellungen anzuwenden.
1.  Aktivieren Sie die relevanten Attribute für[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)Objekt.
1.  Weisen Sie die konfigurierten zu[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Einspruch gegen die[**Reihe**](https://reference.aspose.com/cells/net/aspose.cells/row)Objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

###  **So formatieren Sie eine Spalte**

 Der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung bietet auch eine[**Säulen**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) Sammlung. Jedes Element in der[**Säulen**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) Sammlung repräsentiert a[**Spalte**](https://reference.aspose.com/cells/net/aspose.cells/column) Objekt. Ähnlich wie a[**Reihe**](https://reference.aspose.com/cells/net/aspose.cells/row) Objekt, das[**Spalte**](https://reference.aspose.com/cells/net/aspose.cells/column) Objekt bietet auch die[**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)Methode zum Formatieren einer Spalte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

##  **Vorabthemen**
- [Ausrichtungseinstellungen](/cells/de/net/cells-alignment-settings/)
- [Randeinstellungen](/cells/de/net/cells-border-settings/)
- [Legen Sie bedingte Formate für Excel- und ODS-Dateien fest.](/cells/de/net/conditional-formatting/)
- [Excel-Themen und -Farben](/cells/de/net/excel-themes-and-colors/)
- [Fülleinstellungen](/cells/de/net/cells-fill-settings/)
- [Schriftarteinstellungen](/cells/de/net/cells-font-settings/)
- [Formatieren Sie das Arbeitsblatt Cells in einer Arbeitsmappe](/cells/de/net/format-worksheet-cells-in-a-workbook/)
- [Implementieren Sie das Datumssystem von 1904](/cells/de/net/implement-1904-date-system/)
- [Zusammenführen und Aufheben der Zusammenführung Cells](/cells/de/net/merging-and-unmerging-cells/)
- [Nummerneinstellungen](/cells/de/net/cells-number-settings/)
- [Stil für Zellen abrufen und festlegen](/cells/de/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

