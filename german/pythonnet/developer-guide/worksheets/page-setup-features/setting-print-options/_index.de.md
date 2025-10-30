---
title: Druckoptionen festlegen
type: docs
weight: 40
url: /de/python-net/setting-print-options/
description: Dieser Artikel zeigt, wie Sie programmgesteuert die Druckoptionen der Seitenlayoutfunktion in Excel mit der Aspose.Cells für Python via .NET API festlegen. Sie können den Druckbereich, Drucktitel und Seitenreihenfolge einstellen.
keywords: Python Excel Bibliothek, Python Druckbereich in Excel festlegen, Python Drucktitel in Excel festlegen, Python Seitenreihenfolge in Excel festlegen, Python Druckoptionen einstellen, Python Druckbereich festlegen, Python Drucktitel festlegen. 
---

{{% alert color="primary" %}}

Die Seiteneinrichtungseinstellungen von Microsoft Excel bieten mehrere Druckoptionen (auch als Bogenoptionen bezeichnet), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden.

{{% /alert %}}

## **Druckoptionen festlegen**

Diese Druckoptionen ermöglichen es Benutzern:

- Einen bestimmten Druckbereich auf einem Arbeitsblatt auswählen.
- Titel drucken.
- Gitternetzlinien drucken.
- Zeilen-/Spaltenüberschriften drucken.
- Entwurfsqualität erreichen.
- Kommentare drucken.
- Zellenfehler drucken.
- Seiteneinteilung definieren.

Aspose.Cells für Python via .NET unterstützt alle Druckoptionen, die von Microsoft Excel angeboten werden, und Entwickler können diese Optionen für Arbeitsblätter einfach konfigurieren, indem sie die Eigenschaften der [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) Klasse verwenden. Wie diese Eigenschaften verwendet werden, wird unten im Detail erläutert.

## **Druckbereich festlegen**

Standardmäßig umfasst der Druckbereich alle Bereiche des Arbeitsblatts, die Daten enthalten. Entwickler können einen bestimmten Druckbereich des Arbeitsblatts festlegen.

Verwenden Sie zum Auswählen eines bestimmten Druckbereichs die [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)-Klasse' [**print_area**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_area/)-Eigenschaft. Weisen Sie dieser Eigenschaft einen Zellenbereich zu, der den Druckbereich definiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintArea-1.py" >}}

## **Drucktitel festlegen**

Aspose.Cells für Python via .NET ermöglicht es Ihnen, Zeilen- und Spaltenüberschriften so festzulegen, dass sie auf allen Seiten eines gedruckten Arbeitsblatts wiederholt werden. Verwenden Sie dazu die Eigenschaften [**print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) und [**print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows) der [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) Klasse.

Die zu wiederholenden Zeilen oder Spalten werden durch Übergabe ihrer Zeilen- oder Spaltennummern definiert. Zum Beispiel werden Zeilen als $1:$2 und Spalten als $A:$B definiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintTitle-1.py" >}}

## **Weitere Druckoptionen festlegen**

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
|PRINT_IN_PLACE| Legt fest, Kommentare so zu drucken, wie sie im Arbeitsblatt angezeigt werden.
|PRINT_NO_COMMENTS| Legt fest, keine Kommentare zu drucken.
|PRINT_SHEET_END| Legt fest, Kommentare am Ende des Arbeitsblatts zu drucken.

Die vordefinierten Werte der [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) Aufzählung sind unten mit ihren Beschreibungen aufgelistet.



|**Druckfehlertypen**|**Beschreibung**|
| :- | :- |
|PRINT_ERRORS_BLANK| Legt fest, Fehler nicht zu drucken.
|PRINT_ERRORS_DASH| Legt fest, Fehler als "--" zu drucken.
|PRINT_ERRORS_DISPLAYED| Legt fest, Fehler so zu drucken, wie sie angezeigt werden.
|PRINT_ERRORS_NA| Legt fest, Fehler als "#N/A" zu drucken.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-OtherPrintOptions-1.py" >}}

## **Seitenreihenfolge festlegen**

Die [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) Klasse bietet die [**Order**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/order) Eigenschaft, die verwendet wird, um die Reihenfolge mehrerer Seiten Ihres Arbeitsblatts zum Drucken festzulegen. Es gibt zwei Möglichkeiten, die Seiten wie folgt anzuordnen.

- **Zuerst nach unten:** druckt alle Seiten nach unten, bevor Seiten rechts gedruckt werden.
- **Zuerst nach rechts:** druckt Seiten von links nach rechts, bevor die Seiten unterhalb gedruckt werden.

Aspose.Cells bietet eine Aufzählung, [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype), die alle vordefinierten Anordnungstypen enthält.

Die vordefinierten Werte der [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) Aufzählung sind unten aufgeführt.

|**Druckreihenfolgetypen**|**Beschreibung**|
| :- | :- |
|DOWN_THEN_OVER| Druckreihenfolge: zuerst nach unten, dann nach rechts.
|OVER_THEN_DOWN| Druckreihenfolge: zuerst nach rechts, dann nach unten.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPageOrder-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
