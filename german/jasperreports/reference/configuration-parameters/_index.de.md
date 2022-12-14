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
|:- |:- |
| FORMAT_TYPE| Kann auf „EXCEL97TO2003“ oder „EXCEL2007“ eingestellt werden, um Dateien im Format Microsoft Excel 79 0 2003 oder Excel 2007 zu generieren.|
|IST_EINES_SEITE_PRO_ BLECH| Ein boolescher Wert, der angibt, ob jede Berichtsseite in ein anderes XLS-Arbeitsblatt geschrieben werden soll.|
|IST_LÖSCHEN_LEER_PLATZ_ BETWEEN_ROWS| Ein boolescher Wert, der angibt, ob die Leerzeichen, die zwischen Zeilen auftreten können, entfernt werden sollen oder nicht.|
|IST_LÖSCHEN_LEER_PLATZ_ ZWISCHEN_SPALTEN| Ein boolescher Wert, der angibt, ob die Leerzeichen, die zwischen Spalten auftreten können, entfernt werden sollen oder nicht.|
|IST_WEISS_ SEITENHINTERGRUND| Ein boolescher Wert, der angibt, ob der Seitenhintergrund weiß oder die standardmäßige XLS-Hintergrundfarbe sein soll. Die XLS-Hintergrundfarbe kann je nach den Eigenschaften des XLS-Viewers oder dem Farbschema des Betriebssystems variieren.|
|IST_ERKENNEN_ ZELLTYP| Flag, das verwendet wird, um anzugeben, ob der Exporteur den Typ der ursprünglichen Textfeldausdrücke berücksichtigen und die Zelltypen und Werte entsprechend festlegen soll.|
| BLATT_NAMES|Ein Array von Zeichenfolgen, die benutzerdefinierte Blattnamen darstellen. Dies ist nützlich, wenn es mit dem IS verwendet wird_EINES_SEITE_PRO_ SHEET-Parameter.|
|IST_SCHRIFTART_GRÖSSE_FIX_ AKTIVIERT|Flag zum Verringern der Schriftgröße, damit der Text in die angegebene Zellenhöhe passt.|
|MAXIMAL_REIHEN_ PRO BLATT| Ein ganzzahliger Wert, der die maximale Anzahl von Zeilen angibt, die in einem Blatt angezeigt werden dürfen. Wenn gesetzt, wird ein neues Blatt für die verbleibenden Zeilen erstellt, die angezeigt werden sollen. Negative Werte oder Null bedeuten, dass kein Limit gesetzt wurde.|
|IST_IGNORIEREN_ GRAFIK| Flag, um grafische Elemente zu ignorieren und nur Textelemente zu exportieren.|
|IST_ZUSAMMENBRUCH_ ROW_SPAN| Markieren Sie das Reduzieren der Zeilenspanne und vermeiden Sie das Zusammenführen von Zellen über Zeilen hinweg.|
|IST_IGNORIEREN_ CELL_BORDER| Flag zum Ignorieren der Zellengrenze.|
|IST_VERWENDEN_ EXCEL_CHART| Markierung für die Verwendung eines bearbeitbaren Diagramms im Excel-Format Microsoft anstelle von statischen Bildern. Der Standardwert ist wahr.|

