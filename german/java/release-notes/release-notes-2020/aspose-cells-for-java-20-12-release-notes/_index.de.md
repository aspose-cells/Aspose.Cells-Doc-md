---
title: Aspose.Cells for Java 20.12 Versionshinweise
type: docs
weight: 1
url: /de/java/aspose-cells-for-java-20-12-release-notes/
---
{{% alert color="primary" %}}

 Diese Seite enthält Versionshinweise für[Aspose.Cells for Java 20.12](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.12/).

{{% /alert %}}

|**Taste**|**Zusammenfassung**|**Kategorie**|
|:- |:- |:- |
|CELLSJAVA-43367|Unterstützt die Berechnung der ISFORMULA-Funktion|
|CELLSJAVA-43338|Unterschied in der Ausgabe beim Konvertieren von Excel-Dateien in PDF|
|CELLSJAVA-43346|Die Ausgabedatei ist beschädigt, wenn mehr als 12 Felder in den Seitenfiltern der Pivot-Tabelle hinzugefügt werden|
|CELLSJAVA-43351|Die Hintergrundfarbe der Kopftabelle stimmt beim Konvertieren in PDF nicht|
|CELLSJAVA-43358|Text fehlt während der HTML-zu-Excel-Konvertierung|
|CELLSJAVA-43341|Zusätzliche leere Spalten beim Exportieren von CSV mit LightCellsDataProvider|
|CELLSJAVA-43352|Eine in PDF konvertierte Excel-Datei erzeugt ein Problem mit großen Zahlen|
|CELLSJAVA-43339|Das Bild ist beim Konvertieren der Quelldatei in PDF falsch platziert|
|CELLSJAVA-43340|Fehlende Inhalte bei der XLS-zu-PDF-Konvertierung|
|CELLSJAVA-43336| Diagrammlegendeneinträge werden zu weit links gerendert|
|CELLSJAVA-43356|Leere Werte/Lücken in einem Diagramm werden nicht berücksichtigt, wenn sie zwischen 2 Werten liegen|
|CELLSJAVA-43344|Aktueller Benutzername wird als Autor des letzten Kommentars angezeigt|
|CELLSJAVA-43349|Ausgeblendete Zeilen werden bei der Konvertierung von XML in XLS/XLSX nicht beibehalten|
|CELLSJAVA-43361|Falsche Zellenfarbe bei der Umwandlung von xls in xlsx|
|CELLSJAVA-43366|SetAsTotal-Eigenschaft wird nicht aktualisiert|
|CELLSJAVA-43348|Umwandlung von XLSB in PDF: CellsException: -2147483648|
|CELLSJAVA-43343|Ausnahme beim Exportieren einer Datei in PDF, die kein ausgewähltes Element für eine Form hat|

## **Öffentliche API und rückwärts inkompatible Änderungen**

Im Folgenden finden Sie eine Liste aller Änderungen, die an der öffentlichen API vorgenommen wurden, z. B. hinzugefügte, umbenannte, entfernte oder veraltete Mitglieder, sowie alle nicht abwärtskompatiblen Änderungen, die an Aspose.Cells for Java vorgenommen wurden das Aspose.Cells Support-Forum.

### **Fügt die Methode Cell.SetDynamicArrayFormula(string arrayFormula, FormulaParseOptions options, bool compute) hinzu.**

Unterstützt das Festlegen einer dynamischen Array-Formel und das Überlaufen in benachbarte Zellen, wenn möglich.

### **Fügt die Methode Workbook.RefreshDynamicArrayFormulas(bool compute) hinzu.**

Unterstützt das Aktualisieren dynamischer Array-Formeln und das Überlaufen in benachbarte Zellen gemäß den aktuellen Daten.

### **Fügt die Eigenschaft Cell.Comment hinzu.**

Ruft den Kommentar der Zelle ab.

### **Fügt die HtmlSaveOptions.ExportExtraHeadings-Eigenschaft hinzu**

Gibt an, ob zusätzliche Überschriften exportiert werden, wenn die Textlänge länger als die maximale Anzeigespalte ist.
Der Standardwert ist falsch. Wenn Sie die HTML-Datei in Excel importieren möchten, behalten Sie bitte den Standardwert bei.

### **Fügt die HtmlSaveOptions.ExportFormula-Eigenschaft hinzu**

Gibt an, ob die Formel beim Speichern der Datei in HTML exportiert wird. Der Standardwert ist wahr.
Wenn Sie die HTML-Ausgabe in Excel importieren möchten, behalten Sie bitte den Standardwert bei.

### **Fügt die HtmlSaveOptions.MergeEmptyTdForcely-Eigenschaft hinzu**

Gibt an, ob leere TD-Elemente beim Exportieren der Datei in HTML zwangsweise zusammengeführt werden.
Die Größe der HTML-Datei wird erheblich reduziert, nachdem der Wert auf true gesetzt wurde. Der Standardwert ist falsch.
Wenn Sie die HTML-Datei in Excel importieren oder perfekte Gitterlinien exportieren möchten, wenn Sie die Datei in HTML speichern,
Bitte behalten Sie den Standardwert bei.

### **Fügt die LoadOptions.AutoFilter-Eigenschaft hinzu**

Gibt an, ob die Daten beim Laden der Dateien automatisch gefiltert werden.
Obwohl der Autofilter eingestellt ist, werden die entsprechenden Zeilen manchmal nicht in der Datei ausgeblendet. Funktioniert jetzt nur für SpreadSheetML-Dateien.

### **Fügt die WorkbookSettings.Author-Eigenschaft hinzu**

Ruft den Autor der Arbeitsmappe ab und legt ihn fest.

### **Fügt die Methode MultipleFilterCollection.Add() hinzu.**

Fügt die Filterzeichenfolge des Autofilters hinzu.
