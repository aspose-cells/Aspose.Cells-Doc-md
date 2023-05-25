---
title: Druckoptionen festlegen
type: docs
weight: 40
url: /de/net/setting-print-options/
description: In diesem Artikel wird gezeigt, wie Sie die Druckoptionen der Excel-Arbeitsblatt-Seiteneinrichtungsfunktion mithilfe der Bibliotheken C#, API und .NET programmgesteuert festlegen. Sie können den Druckbereich, die Drucktitel und die Seitenreihenfolge festlegen.
keywords: set excel print area c#, set exce print titles c#, set excel page order c#
---
{{% alert color="primary" %}}

Microsoft Die Seiteneinrichtungseinstellungen von Excel bieten mehrere Druckoptionen (auch als Blattoptionen bezeichnet), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden.

{{% /alert %}}

##  **Druckoptionen festlegen**

Mit diesen Druckoptionen können Benutzer:

- Wählen Sie einen bestimmten Druckbereich auf einem Arbeitsblatt aus.
- Titel drucken.
- Gitterlinien drucken.
- Zeilen-/Spaltenüberschriften drucken.
- Erreichen Sie Entwurfsqualität.
- Kommentare drucken.
- Zellfehler drucken.
- Definieren Sie die Seitenreihenfolge.

 Aspose.Cells unterstützt alle von Microsoft Excel angebotenen Druckoptionen und Entwickler können diese Optionen für Arbeitsblätter mithilfe der von angebotenen Eigenschaften einfach konfigurieren[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)Klasse. Wie diese Eigenschaften genutzt werden, wird im Folgenden ausführlicher erläutert.

###  **Druckbereich festlegen**

Standardmäßig umfasst der Druckbereich alle Bereiche des Arbeitsblatts, die Daten enthalten. Entwickler können einen bestimmten Druckbereich des Arbeitsblatts festlegen.

 Um einen bestimmten Druckbereich auszuwählen, verwenden Sie die[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Klasse'[**Druckbereich**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)Eigentum. Weisen Sie dieser Eigenschaft einen Zellbereich zu, der den Druckbereich definiert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

###  **Drucktitel festlegen**

 Mit Aspose.Cells können Sie festlegen, dass Zeilen- und Spaltenüberschriften auf allen Seiten eines gedruckten Arbeitsblatts wiederholt werden. Verwenden Sie dazu die[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Klasse'[**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) Und[**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)Eigenschaften.

Die Zeilen oder Spalten, die wiederholt werden, werden durch die Übergabe ihrer Zeilen- oder Spaltennummern definiert. Beispielsweise sind Zeilen als $1:$2 und Spalten als $A:$B definiert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

###  **Legen Sie andere Druckoptionen fest**

 Der[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)Die Klasse bietet außerdem mehrere andere Eigenschaften zum Festlegen allgemeiner Druckoptionen wie folgt:

- [**Rasterlinien drucken**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines): eine boolesche Eigenschaft, die definiert, ob Gitterlinien gedruckt werden sollen oder nicht.
- [**Überschriften drucken**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): eine boolesche Eigenschaft, die definiert, ob Zeilen- und Spaltenüberschriften gedruckt werden sollen oder nicht.
- [**Schwarz und weiß**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): eine boolesche Eigenschaft, die definiert, ob das Arbeitsblatt im Schwarzweißmodus gedruckt werden soll oder nicht.
- [**Kommentare drucken**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): legt fest, ob die Druckkommentare auf dem Arbeitsblatt oder am Ende des Arbeitsblatts angezeigt werden sollen.
- [**Druckentwurf**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): eine boolesche Eigenschaft, die definiert, ob das Blatt ohne Grafiken gedruckt werden soll.
- [**Druckfehler**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): Definiert, ob Zellenfehler als angezeigt, leer, gestrichelt oder nicht verfügbar gedruckt werden sollen.

 Um das einzustellen[**Kommentare drucken**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) Und[**Druckfehler**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)Eigenschaften bietet Aspose.Cells auch zwei Aufzählungen:[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) , Und[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) die vordefinierte Werte enthalten, die dem zugewiesen werden sollen[**Kommentare drucken**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) Und[**Druckfehler**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)Eigenschaften bzw.

 Die vordefinierten Werte in der[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)Aufzählung sind unten mit ihren Beschreibungen aufgeführt.

|**Kommentartypen drucken**|**Beschreibung**|
| :- | :- |
|PrintInPlace|Gibt an, dass Kommentare so gedruckt werden, wie sie auf dem Arbeitsblatt angezeigt werden.|
|PrintNoComments|Gibt an, dass Kommentare nicht gedruckt werden sollen.|
|PrintSheetEnd|Gibt an, dass Kommentare am Ende des Arbeitsblatts gedruckt werden.|

 Die vordefinierten Werte von[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)Aufzählung sind unten mit ihren Beschreibungen aufgeführt.



|**Druckfehlertypen**|**Beschreibung**|
| :- | :- |
|PrintErrorsBlank|Gibt an, dass keine Fehler gedruckt werden.|
|PrintErrorsDash|Gibt an, dass Fehler als „--“ gedruckt werden.|
|PrintErrorsDisplayed|Gibt an, dass Fehler wie angezeigt gedruckt werden.|
|PrintErrorsNA|Gibt an, dass Fehler als „#N/A“ gedruckt werden.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

###  **Legen Sie die Seitenreihenfolge fest**

 Der[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Klasse bietet die[**Befehl**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order)Eigenschaft, die verwendet wird, um den Druck mehrerer Seiten Ihres Arbeitsblatts anzuordnen. Es gibt zwei Möglichkeiten, die Seiten wie folgt zu bestellen.

- **Runter, dann rüber:** Druckt alle Seiten nach unten, bevor die Seiten nach rechts gedruckt werden.
- **Über und ab:** Druckt die Seiten von links nach rechts, bevor die Seiten darunter gedruckt werden.

 Aspose.Cells bietet eine Aufzählung,[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)das alle vordefinierten Auftragsarten enthält.

 Die vordefinierten Werte der[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)Aufzählung sind unten aufgeführt.

|**Druckauftragsarten**|**Beschreibung**|
| :- | :- |
|Runter, dann vorbei|Stellt die Druckreihenfolge nach unten und dann nach oben dar.|
|OverThenDown|Stellt die Druckreihenfolge von oben nach unten dar.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
