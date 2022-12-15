---
title: Druckoptionen einstellen
type: docs
weight: 40
url: /de/net/setting-print-options/
---
{{% alert color="primary" %}}

Microsoft Die Seiteneinrichtungseinstellungen von Excel bieten mehrere Druckoptionen (auch als Blattoptionen bezeichnet), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden.

{{% /alert %}}

## **Druckoptionen einstellen**

Mit diesen Druckoptionen können Benutzer:

- Wählen Sie einen bestimmten Druckbereich auf einem Arbeitsblatt aus.
- Titel drucken.
- Rasterlinien drucken.
- Zeilen-/Spaltenüberschriften drucken.
- Erzielen Sie Entwurfsqualität.
- Kommentare drucken.
- Zellfehler drucken.
- Definieren Sie die Seitenreihenfolge.

 Aspose.Cells unterstützt alle Druckoptionen, die von Microsoft Excel angeboten werden, und Entwickler können diese Optionen für Arbeitsblätter einfach konfigurieren, indem sie die von angebotenen Eigenschaften verwenden[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)Klasse. Wie diese Eigenschaften verwendet werden, wird unten ausführlicher erörtert.

### **Druckbereich festlegen**

Standardmäßig umfasst der Druckbereich alle Bereiche des Arbeitsblatts, die Daten enthalten. Entwickler können einen bestimmten Druckbereich des Arbeitsblatts festlegen.

 Um einen bestimmten Druckbereich auszuwählen, verwenden Sie die[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Klasse'[**Druckbereich**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)Eigentum. Weisen Sie dieser Eigenschaft einen Zellbereich zu, der den Druckbereich definiert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **Drucktitel festlegen**

 Aspose.Cells ermöglicht es Ihnen, Zeilen- und Spaltenüberschriften festzulegen, die auf allen Seiten eines gedruckten Arbeitsblatts wiederholt werden sollen. Verwenden Sie dazu die[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Klasse'[**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) und[**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)Eigenschaften.

Die Zeilen oder Spalten, die wiederholt werden, werden durch die Übergabe ihrer Zeilen- oder Spaltennummern definiert. Beispielsweise werden Zeilen als $1:$2 und Spalten als $A:$B definiert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **Legen Sie andere Druckoptionen fest**

 Das[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)Die Klasse bietet auch mehrere andere Eigenschaften, um allgemeine Druckoptionen wie folgt festzulegen:

- [**Gitternetzlinien drucken**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines)eine boolesche Eigenschaft, die definiert, ob Gitternetzlinien gedruckt werden oder nicht.
- [**Überschriften drucken**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): eine boolesche Eigenschaft, die definiert, ob Zeilen- und Spaltenüberschriften gedruckt werden oder nicht.
- [**Schwarz und weiß**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): eine boolesche Eigenschaft, die definiert, ob das Arbeitsblatt im Schwarzweißmodus gedruckt werden soll oder nicht.
- [**Kommentare drucken**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): legt fest, ob die Druckkommentare auf dem Arbeitsblatt oder am Ende des Arbeitsblatts angezeigt werden.
- [**Entwurf drucken**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): eine boolesche Eigenschaft, die definiert, ob das Blatt ohne Grafiken gedruckt werden soll.
- [**Druckfehler**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): Definiert, ob Zellfehler als angezeigt, leer, Bindestrich oder N/A gedruckt werden.

 Zum Einstellen der[**Kommentare drucken**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) und[**Druckfehler**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) Eigenschaften, Aspose.Cells bietet auch zwei Aufzählungen,[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) , und[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) die vordefinierte Werte enthalten, die dem zugewiesen werden[**Kommentare drucken**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) und[**Druckfehler**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)Eigenschaften bzw.

 Die vordefinierten Werte in der[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)Aufzählung sind unten mit ihren Beschreibungen aufgeführt.

|**Kommentartypen drucken**|**Beschreibung**|
|:- |:- |
|PrintInPlace|Gibt an, dass Kommentare so gedruckt werden, wie sie auf dem Arbeitsblatt angezeigt werden.|
|KeineKommentare drucken|Gibt an, dass Kommentare nicht gedruckt werden.|
|PrintSheetEnd|Gibt an, dass Kommentare am Ende des Arbeitsblatts gedruckt werden.|

 Die vordefinierten Werte von[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)Aufzählung sind unten mit ihren Beschreibungen aufgeführt.



|**Druckfehlertypen**|**Beschreibung**|
|:- |:- |
|DruckfehlerLeer|Gibt an, Fehler nicht zu drucken.|
|PrintErrorsDash|Gibt an, dass Fehler als "--" gedruckt werden.|
|Druckfehlerangezeigt|Gibt an, dass Fehler wie angezeigt gedruckt werden.|
|PrintErrorsNA|Gibt an, dass Fehler als „#N/A“ gedruckt werden.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **Seitenreihenfolge festlegen**

 Das[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Klasse bietet die[**Befehl**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order)-Eigenschaft, die verwendet wird, um mehrere Seiten Ihres Arbeitsblatts zum Drucken anzuordnen. Es gibt zwei Möglichkeiten, die Seiten wie folgt anzuordnen.

- **Runter dann rüber:** druckt alle Seiten nach unten, bevor Seiten nach rechts gedruckt werden.
- **Über dann nach unten:** druckt Seiten von links nach rechts, bevor die folgenden Seiten gedruckt werden.

 Aspose.Cells liefert eine Aufzählung,[**Druckauftragstyp**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)die alle vordefinierten Auftragstypen enthält.

 Die vordefinierten Werte der[**Druckauftragstyp**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)Aufzählung sind unten aufgeführt.

|**Auftragsarten drucken**|**Beschreibung**|
|:- |:- |
|DownThenOver|Stellt die Druckreihenfolge als unten dann oben dar.|
|OverThenDown|Stellt die Druckreihenfolge als über dann nach unten dar.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
