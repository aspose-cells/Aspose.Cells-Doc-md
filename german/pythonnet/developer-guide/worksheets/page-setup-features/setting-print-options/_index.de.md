---
title: Druckoptionen festlegen
type: docs
weight: 40
url: /de/python-net/setting-print-options/
description: Dieser Artikel zeigt, wie Sie die Druckoptionen des Excel Arbeitsblattseiteneinrichtungsmerkmals programmgesteuert mit der Aspose.Cells für Python via .NET API festlegen können. Sie können den Druckbereich, die Drucktitel und die Seitenausrichtung festlegen.
keywords: Python Excel Bibliothek, Python legt den Excel Druckbereich fest, Python legt die Excel Drucktitel fest, Python, wie man die Excel Seitenreihenfolge festlegt, Wie man Druckoptionen einstellt, Wie man den Druckbereich festlegt, Wie man Drucktitel festlegt. 
---

{{% alert color="primary" %}}

Die Seiteneinrichtungseinstellungen von Microsoft Excel bieten mehrere Druckoptionen (auch als Bogenoptionen bezeichnet), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden.

{{% /alert %}}

## **Wie man Druckoptionen einstellt**

Diese Druckoptionen ermöglichen es Benutzern:

- Einen bestimmten Druckbereich auf einem Arbeitsblatt auswählen.
- Titel drucken.
- Gitternetzlinien drucken.
- Zeilen-/Spaltenüberschriften drucken.
- Entwurfsqualität erreichen.
- Kommentare drucken.
- Zellenfehler drucken.
- Seiteneinteilung definieren.

Aspose.Cells für Python via .NET unterstützt alle von Microsoft Excel angebotenen Druckoptionen und Entwickler können diese Optionen für Arbeitsblätter mithilfe der von der Klasse [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) angebotenen Eigenschaften einfach konfigurieren. Wie diese Eigenschaften verwendet werden, wird im Folgenden detaillierter erläutert.

## **Wie man den Druckbereich festlegt**

Standardmäßig umfasst der Druckbereich alle Bereiche des Arbeitsblatts, die Daten enthalten. Entwickler können einen bestimmten Druckbereich des Arbeitsblatts festlegen.

Verwenden Sie zum Auswählen eines bestimmten Druckbereichs die [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)-Klasse' [**print_area**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_area/)-Eigenschaft. Weisen Sie dieser Eigenschaft einen Zellenbereich zu, der den Druckbereich definiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintArea-1.py" >}}

## **Wie man Drucktitel festlegt**

Aspose.Cells für Python via .NET ermöglicht es Ihnen, Zeilen- und Spaltenüberschriften auf allen Seiten eines gedruckten Arbeitsblatts zu wiederholen. Verwenden Sie dazu die Eigenschaften [**print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) und [**print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows) der Klasse [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup).

Die zu wiederholenden Zeilen oder Spalten werden durch Übergabe ihrer Zeilen- oder Spaltennummern definiert. Zum Beispiel werden Zeilen als $1:$2 und Spalten als $A:$B definiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintTitle-1.py" >}}

## **Wie man andere Druckoptionen einstellt**

Die [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)-Klasse bietet auch mehrere andere Eigenschaften zur Festlegung allgemeiner Druckoptionen wie folgt:

- [**print_grid_lines**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_gridlines/): ein Boolescher Wert, der definiert, ob Gitterlinien gedruckt werden oder nicht.
- [**print_headings**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_headings/): ein Boolescher Wert, der definiert, ob Zeilen- und Spaltenüberschriften gedruckt werden oder nicht.
- [**black_and_white**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/black_and_white/): Eine boolesche Eigenschaft, die definiert, ob das Arbeitsblatt im Schwarz-Weiß-Modus gedruckt werden soll oder nicht.
- [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/): definiert, ob die Druckkommentare auf dem Arbeitsblatt oder am Ende des Arbeitsblatts angezeigt werden sollen.
- [**print_draft**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_draft/): eine boolesche Eigenschaft, die definiert, ob das Blatt ohne Grafiken gedruckt werden soll.
- [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors): definiert, ob Zellfehler wie angezeigt, leer, Strich oder N/V gedruckt werden sollen.

Um die [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) und [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors) Eigenschaften festzulegen, bietet Aspose.Cells auch zwei Aufzählungen, [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) und [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype), die vordefinierte Werte enthalten, die den [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) und [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors) Eigenschaften jeweils zugewiesen werden sollen.

Die vordefinierten Werte in der [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) Aufzählung sind unten mit ihren Beschreibungen aufgelistet.

|**Druckkommentartypen**|**Beschreibung**|
| :- | :- |
|DRUCK_AN_ORT|Gibt an, Kommentare so zu drucken, wie sie auf dem Arbeitsblatt angezeigt werden.|
|DRUCK_KEINE_KOMMENTARE|Gibt an, keine Kommentare zu drucken.|
|DRUCK_BLATT_ENDE|Gibt an, Kommentare am Ende des Arbeitsblatts zu drucken.|

Die vordefinierten Werte der [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) Aufzählung sind unten mit ihren Beschreibungen aufgelistet.



|**Druckfehlertypen**|**Beschreibung**|
| :- | :- |
|DRUCK_FEHLER_LEER|Gibt an, Fehler nicht zu drucken.|
|DRUCK_FEHLER_STRICH|Gibt an, Fehler als "--" zu drucken.|
|DRUCK_FEHLER_ANGEZEIGT|Gibt an, Fehler wie angezeigt zu drucken.|
|DRUCK_FEHLER_NA|Gibt an, Fehler als "#N/A" zu drucken.|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-OtherPrintOptions-1.py" >}}

## **Wie man Seitenreihenfolge einstellt**

Die [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) Klasse bietet die [**Order**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/order) Eigenschaft, die verwendet wird, um die Reihenfolge mehrerer Seiten Ihres Arbeitsblatts zum Drucken festzulegen. Es gibt zwei Möglichkeiten, die Seiten wie folgt anzuordnen.

- **Zuerst nach unten:** druckt alle Seiten nach unten, bevor Seiten rechts gedruckt werden.
- **Zuerst nach rechts:** druckt Seiten von links nach rechts, bevor die Seiten unterhalb gedruckt werden.

Aspose.Cells bietet eine Aufzählung, [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype), die alle vordefinierten Anordnungstypen enthält.

Die vordefinierten Werte der [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) Aufzählung sind unten aufgeführt.

|**Druckreihenfolgetypen**|**Beschreibung**|
| :- | :- |
|VON_OBEN_NACH_UNTEN|Stellt die Druckreihenfolge als von oben nach unten dar.|
|VON_LINKS_NACH_RECHTS|Stellt die Druckreihenfolge als von links nach rechts dar.|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPageOrder-1.py" >}}
