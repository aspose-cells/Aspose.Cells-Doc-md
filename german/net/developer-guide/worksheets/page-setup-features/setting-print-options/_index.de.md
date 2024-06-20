---
title: Druckoptionen festlegen
type: docs
weight: 40
url: /de/net/setting-print-options/
description: In diesem Artikel wird gezeigt, wie Sie die Druckoptionen des Excel Arbeitsblattseiten Setups programmgesteuert mit der C# API und der .NET Bibliothek festlegen können. Sie können den Druckbereich, die Drucktitel und die Seitenreihenfolge festlegen.
keywords: set excel print area c#, set exce print titles c#, set excel page order c#
---

{{% alert color="primary" %}}

Die Seiteneinrichtungseinstellungen von Microsoft Excel bieten mehrere Druckoptionen (auch als Bogenoptionen bezeichnet), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden.

{{% /alert %}}

## **Druckoptionen einstellen**

Diese Druckoptionen ermöglichen es Benutzern:

- Einen bestimmten Druckbereich auf einem Arbeitsblatt auswählen.
- Titel drucken.
- Gitternetzlinien drucken.
- Zeilen-/Spaltenüberschriften drucken.
- Entwurfsqualität erreichen.
- Kommentare drucken.
- Zellenfehler drucken.
- Seiteneinteilung definieren.

Aspose.Cells unterstützt alle von Microsoft Excel angebotenen Druckoptionen, und Entwickler können diese Optionen für Arbeitsblätter leicht konfigurieren, indem sie die von der [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)-Klasse bereitgestellten Eigenschaften verwenden. Wie diese Eigenschaften im Detail verwendet werden, wird weiter unten ausführlicher erläutert.

### **Druckbereich festlegen**

Standardmäßig umfasst der Druckbereich alle Bereiche des Arbeitsblatts, die Daten enthalten. Entwickler können einen bestimmten Druckbereich des Arbeitsblatts festlegen.

Verwenden Sie zum Auswählen eines bestimmten Druckbereichs die [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)-Klasse' [**PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)-Eigenschaft. Weisen Sie dieser Eigenschaft einen Zellenbereich zu, der den Druckbereich definiert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **Drucktitel festlegen**

Aspose.Cells ermöglicht es Ihnen, Zeilen- und Spaltenüberschriften auf allen Seiten eines gedruckten Arbeitsblatts zu wiederholen. Verwenden Sie dazu die [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)-Klasse' [**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns)- und [**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)-Eigenschaften.

Die zu wiederholenden Zeilen oder Spalten werden durch Übergabe ihrer Zeilen- oder Spaltennummern definiert. Zum Beispiel werden Zeilen als $1:$2 und Spalten als $A:$B definiert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **Andere Druckoptionen festlegen**

Die [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)-Klasse bietet auch mehrere andere Eigenschaften zur Festlegung allgemeiner Druckoptionen wie folgt:

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines): ein Boolescher Wert, der definiert, ob Gitterlinien gedruckt werden oder nicht.
- [**PrintHeadings**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): ein Boolescher Wert, der definiert, ob Zeilen- und Spaltenüberschriften gedruckt werden oder nicht.
- [**BlackAndWhite**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): Eine boolesche Eigenschaft, die definiert, ob das Arbeitsblatt im Schwarz-Weiß-Modus gedruckt werden soll oder nicht.
- [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): definiert, ob die Druckkommentare auf dem Arbeitsblatt oder am Ende des Arbeitsblatts angezeigt werden sollen.
- [**PrintDraft**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): eine boolesche Eigenschaft, die definiert, ob das Blatt ohne Grafiken gedruckt werden soll.
- [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): definiert, ob Zellfehler wie angezeigt, leer, Strich oder N/V gedruckt werden sollen.

Um die [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) und [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) Eigenschaften festzulegen, bietet Aspose.Cells auch zwei Aufzählungen, [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) und [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype), die vordefinierte Werte enthalten, die den [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) und [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) Eigenschaften jeweils zugewiesen werden sollen.

Die vordefinierten Werte in der [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) Aufzählung sind unten mit ihren Beschreibungen aufgelistet.

|**Druckkommentartypen**|**Beschreibung**|
| :- | :- |
|PrintInPlace| Gibt an, Kommentare so zu drucken, wie sie auf dem Arbeitsblatt angezeigt werden.|
|PrintNoComments| Gibt an, Kommentare nicht zu drucken.|
|PrintSheetEnd| Gibt an, Kommentare am Ende des Arbeitsblatts zu drucken.|

Die vordefinierten Werte der [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) Aufzählung sind unten mit ihren Beschreibungen aufgelistet.



|**Druckfehlertypen**|**Beschreibung**|
| :- | :- |
|PrintErrorsBlank| Gibt an, Fehler nicht zu drucken.|
|PrintErrorsDash| Gibt an, Fehler als "--" zu drucken.|
|PrintErrorsDisplayed| Gibt an, Fehler wie angezeigt zu drucken.|
|PrintErrorsNA| Gibt an, Fehler als "#N/A" zu drucken.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **Seitenreihenfolge festlegen**

Die [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Klasse bietet die [**Order**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order) Eigenschaft, die verwendet wird, um die Reihenfolge mehrerer Seiten Ihres Arbeitsblatts zum Drucken festzulegen. Es gibt zwei Möglichkeiten, die Seiten wie folgt anzuordnen.

- **Zuerst nach unten:** druckt alle Seiten nach unten, bevor Seiten rechts gedruckt werden.
- **Zuerst nach rechts:** druckt Seiten von links nach rechts, bevor die Seiten unterhalb gedruckt werden.

Aspose.Cells bietet eine Aufzählung, [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype), die alle vordefinierten Anordnungstypen enthält.

Die vordefinierten Werte der [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) Aufzählung sind unten aufgeführt.

|**Druckreihenfolgetypen**|**Beschreibung**|
| :- | :- |
|DownThenOver|Stellt die Druckreihenfolge als zuerst nach unten und dann nach rechts dar.
|OverThenDown|Stellt die Druckreihenfolge als über dann nach unten dar.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
