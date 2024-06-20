---
title: Konfigurationsparameter
type: docs
weight: 10
url: /de/jasperreports/configuration-parameters/
---

{{% alert color="primary" %}} 

Die folgende Tabelle listet die Konfigurationsparameter auf. 

{{% /alert %}} 

|**Parametername** |**Beschreibung** |
| :- | :- |
|FORMAT_TYPE |Kann auf "EXCEL97TO2003" oder "EXCEL2007" gesetzt werden, um Microsoft Excel 79 0 2003- oder Excel 2007-Formatdateien zu generieren. |
|IS_ONE_PAGE_PER_SHEET |Ein boolescher Wert, der angibt, ob jede Berichtsseite in ein anderes XLS-Arbeitsblatt geschrieben werden soll. |
|IS_REMOVE_EMPTY_SPACE_BETWEEN_ROWS |Ein boolescher Wert, der angibt, ob die leeren Zwischenräume, die zwischen den Zeilen erscheinen können, entfernt werden sollen oder nicht. |
|IS_REMOVE_EMPTY_SPACE_BETWEEN_COLUMNS |Ein boolescher Wert, der angibt, ob die leeren Zwischenräume, die zwischen den Spalten erscheinen können, entfernt werden sollen oder nicht. |
|IS_WHITE_PAGE_BACKGROUND |Ein boolescher Wert, der angibt, ob der Seitenhintergrund weiß oder die Standard-XLS-Hintergrundfarbe sein soll. Welche Farbe der XLS-Hintergrund hat, kann je nach Eigenschaften des XLS-Viewers oder dem Farbschema des Betriebssystems variieren. |
|IS_DETECT_CELL_TYPE |Flag zum Anzeigen, ob der Exporteur die Art der ursprünglichen Textfeldausdrücke berücksichtigen und die Zelltypen und Werte entsprechend setzen soll. |
|SHEET_NAMES |Ein Array von Zeichenfolgen, die benutzerdefinierte Blattnamen repräsentieren. Dies ist nützlich, wenn es mit dem Parameter IS_ONE_PAGE_PER_SHEET verwendet wird. |
|IS_FONT_SIZE_FIX_ENABLED |Flag zum Verkleinern der Schriftgröße, damit der Text in die festgelegte Zellhöhe passt. |
|MAXIMUM_ROWS_PER_SHEET |Ein Integer-Wert, der die maximal erlaubte Anzahl von Zeilen in einem Blatt angibt. Wenn festgelegt, wird für die verbleibenden anzuzeigenden Zeilen ein neues Blatt erstellt. Negative Werte oder Null bedeuten, dass kein Limit festgelegt wurde. |
|IS_IGNORE_GRAPHICS |Flag zum Ignorieren grafischer Elemente und zum Exportieren nur von Textelementen. |
|IS_COLLAPSE_ROW_SPAN |Flag zum Zusammenfassen von Zeilenspannen und zum Vermeiden des Zusammenführens von Zellen über Zeilen hinweg. |
|IS_IGNORE_CELL_BORDER |Flag zum Ignorieren des Zellenrahmens.
|IS_USE_EXCEL_CHART |Flag für die Verwendung eines bearbeitbaren Diagramms im Microsoft Excel-Format anstatt von statischen Bildern. Der Standardwert ist wahr.

