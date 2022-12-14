---
title: Aspose.Cells für Android über Java 9.0.0 Versionshinweise
type: docs
weight: 20
url: /de/java/aspose-cells-for-android-via-java-9-0-0-release-notes/
---
|**Taste**|**Zusammenfassung**|**Kategorie**|
|:- |:- |:- |
|CELLSJAVA-41925|Die Berechnungszeit hat sich mit den letzten API-Revisionen erhöht|Neue Funktion|
|CELLSJAVA-40958|Ein vom Benutzer konfigurierbarer Ersatzmechanismus für Schriftarten ist erforderlich|Neue Funktion|
|CELLSJAVA-41925|Die Berechnungszeit hat sich mit den letzten API-Revisionen erhöht|Neue Funktion|
|CELLSJAVA-41947|Fähigkeit zu erkennen, ob sich ein DataPoint in Pie oder Bar befindet|Neue Funktion|
|CELLSJAVA-41936|Die Workbook.calculateFormula()-Methode wird für die Excel-Quelldatei nie beendet|Erweiterung|
|CELLSJAVA-41827|Spreadsheet benötigt mehr als 3 Minuten, um Formeln mit der Methode Workbook.calculateFormula() zu berechnen|Erweiterung|
|CELLSJAVA-41928|Bildressource kann beim Rendern der Tabelle in HTML mit IStreamProvider nicht erfasst werden|Insekt|
|CELLSJAVA-41841|Problem beim Rendern von Kontrollkästchen in HTML|Insekt|
|CELLSJAVA-41932|Problem mit getDisplayStringValue() für Werte im Datumsformat|Insekt|
|CELLSJAVA-41930|Bei Verwendung von Light Cells-APIs zum Verarbeiten einer XLS-Datei wird immer die erste Zelle des ersten Blatts verarbeitet|Insekt|
|CELLSJAVA-41931|Zeichenabstand und -umbruch für vertikalen Text beim Rendern der Tabelle in PDF nicht korrekt|Insekt|
|CELLSJAVA-41709|Spaltenbreiten sind auf CentOS anders als auf Windows|Insekt|
|CELLSJAVA-41933|Der Diagrammmaßstab hat sich beim Rendern der Tabelle in PDF verschoben|Insekt|
|CELLSJAVA-41934|Ausrichtungsproblem beim Rendern einer Excel-Datei in PDF|Insekt|
|CELLSJAVA-41935|Die Formatierung von Legendeneinträgen wird beim Rendern der Tabelle in PDF gestört|Insekt|
|CELLSJAVA-41943|Die horizontalen Achsenbeschriftungen wurden nicht vollständig gerendert, das heißt; Bei allen Beschriftungen fehlen einige Inhalte im gerenderten Bild.|Insekt|
|CELLSJAVA-41940|Datei ist nach Formelberechnung und Speichern beschädigt|Insekt|
|CELLSJAVA-41952|Berechnungsergebnis ist nicht korrekt|Insekt|
|CELLSJAVA-41941|Matrixformel wird nicht richtig berechnet|Insekt|
|CELLSJAVA-41937|Einige Werte aus der Excel-Datei fehlen in der HTML-Ausgabe – XLS-zu-HTML-Konvertierung|Insekt|
|CELLSJAVA-41969|Cell Schattierung fehlt beim Konvertieren von HTML in XLSX|Insekt|
|CELLSJAVA-41955|Workbook to HTML zeigt '#' in Zellen|Insekt|
|CELLSJAVA-41942|Fehlende Ränder, Zellenschattierungen und Bilder – Rendern von HTML in Excel|Insekt|
|CELLSJAVA-41967|Cells fehlt in PDF, wenn mehrere Druckbereiche auf einem Blatt definiert sind|Insekt|
|CELLSJAVA-41958|Die Legende auf der rechten Seite wird im Diagrammbild abgeschnitten|Insekt|
|CELLSJAVA-41953|Text im Diagramm falsch platziert, nachdem er in das HTML-Format konvertiert wurde|Insekt|
|CELLSJAVA-41948|Das Diagramm wird beim Konvertieren der Tabelle in HTML geändert|Insekt|
|CELLSJAVA-41981|Falsche Position der vertikalen Linie im PDF des Diagramms|Insekt|
|CELLSJAVA-41964|Autofit berücksichtigt die Einzugsebene nicht|Insekt|
|CELLSJAVA-40260|Ändern des Textes einer vorhandenen WordArt in einer Excel-Datei|Insekt|
|CELLSJAVA-41927|Ausnahme: „java.lang.OutOfMemoryError“ beim Speichern im HTML-Dateiformat|Ausnahme|
|CELLSJAVA-41945|CellsException: Fehler bei der Berechnung von Cell[0Sheet1!E5]in Workbook.calculateFormula während der Berechnung der TREND-Funktion|Ausnahme|
|CELLSJAVA-41946|Das Öffnen einer Excel-Datei verursacht eine java.lang.NumberFormatException: Für die Eingabezeichenfolge: "80000020"|Ausnahme|
|CELLSJAVA-41922|IndexOutOfBoundsException beim Kopieren von Zellen|Ausnahme|
|CELLSJAVA-41971|Cell.getValidationValue() löst NullPointerException für den benutzerdefinierten Validierungstyp aus|Ausnahme|
|CELLSJAVA-41963|Beim Öffnen der Quelle a5.xlsx tritt eine Ausnahme wegen unzulässiger Schlüsselgröße auf|Ausnahme|
|CELLSJAVA-41962|Beim Öffnen der Quelle a4.xls tritt eine ArrayIndexOutOfBoundsException-Ausnahme auf|Ausnahme|
|CELLSJAVA-41961|Beim Öffnen der Quelle a3.xls tritt eine ungültige Zeichenfolge in der Dateiausnahme auf|Ausnahme|
|CELLSJAVA-41960|Die Ausnahme „NegativeArraySizeException“ tritt beim Öffnen der Quelle „a2.xls“ auf|Ausnahme|
|CELLSJAVA-41959|Beim Öffnen der Quelle a1.xlsx tritt eine NullPointerException-Ausnahme auf|Ausnahme|
## **Öffentliche API und rückwärts inkompatible Änderungen**
Im Folgenden finden Sie eine Liste aller Änderungen, die an der öffentlichen API vorgenommen wurden, z. B. hinzugefügte, umbenannte, entfernte oder veraltete Mitglieder, sowie alle nicht abwärtskompatiblen Änderungen, die an Aspose.Cells für Android vorgenommen wurden. Wenn Sie Bedenken zu einer der aufgeführten Änderungen haben, äußern Sie diese bitte im Aspose.Cells-Supportforum.
### **Fügt die Eigenschaft CopyOptions.ReferToDestinationSheet und die Methode Cells.CopyRows(Cells sourceCells, int sourceRowIndex, int destinationRowIndex, int rowNumber, CopyOptions copyOptions) hinzu**
Wenn der Bereich kopiert wird und das Diagramm auf das Quellblatt verweist, bedeutet False, dass die Datenquelle des kopierten Diagramms nicht geändert wird. True bedeutet, dass die Datenquelle des kopierten Diagramms auf das Zielblatt verweist.
### **Fügt die HtmlSaveOptions.FilePathProvider-Eigenschaft hinzu**
Ruft den IFilePathProvider zum separaten Exportieren von Worksheet in HTML ab oder legt diesen fest.
### **Fügt die IFilePathProvider-Schnittstelle hinzu**
Stellt den exportierten Dateipfadanbieter dar.
### **Fügt die FontConfigs-Klasse hinzu**
Gibt Schriftarteinstellungen an.
### **Fügt die FontSourceBase-Klasse hinzu**
Dies ist eine abstrakte Basisklasse für die Klassen, die es dem Benutzer ermöglichen, verschiedene Schriftartquellen anzugeben.
### **Fügt die FileFontSource-Klasse hinzu**
Stellt die einzelne TrueType-Schriftartdatei dar, die im Dateisystem gespeichert ist.
### **Fügt die FolderFontSource-Klasse hinzu**
Stellt den Ordner dar, der TrueType-Schriftartdateien enthält.
### **Fügt die MemoryFontSource-Klasse hinzu**
Stellt die einzelne TrueType-Schriftartdatei dar, die im Arbeitsspeicher gespeichert ist.
### **Fügt FontSourceType-Aufzählung hinzu**
Gibt den Typ einer Schriftartquelle an.
### **Fügt die CalculationOptions.Recursive-Eigenschaft hinzu**
Gibt an, ob die abhängigen Zellen bei der Berechnung einer Zelle rekursiv berechnet werden und von anderen Zellen abhängen.
### **Veraltet die CellsHelper.FontDir-Eigenschaft**
Verwenden Sie stattdessen die Methode „FontConfigs.SetFontFolder(string, bool)“, wobei der Ordner rekursiv zu „false“ wird.
### **Veraltet die CellsHelper.FontDirs-Eigenschaft**
Verwenden Sie stattdessen die Methode „FontConfigs.SetFontFolders(string[], bool)“, wobei der Ordner rekursiv zu „false“ wird.
### **Veraltet die CellsHelper.FontFiles-Eigenschaft**
Verwenden Sie stattdessen FontConfigs.SetFontSources(FontSourceBase[]).
### **Veraltet die Shape.LineFormat-Eigenschaft und fügt die Shape.Line-Eigenschaft hinzu**
Bitte verwenden Sie stattdessen die Shape.Line-Eigenschaft.
### **Veraltet die Shape.FillFormat-Eigenschaft und fügt die Shape.Fill-Eigenschaft hinzu**
Bitte verwenden Sie stattdessen die Shape.Fill-Eigenschaft.
### **Veraltet die ShapeFormat-Klasse und die Shape.Format-Eigenschaft**
Bitte verwenden Sie direkt die Shape.Fill- und Shape.Line-Eigenschaften.
### **Veraltet die ShapeFont-Klasse und fügt die TextOptions-Klasse hinzu**
Bitte verwenden Sie stattdessen die TextOptions-Klasse.
### **Fügt die Eigenschaften TextOptions.Fill, TextOptions.Outline und TextOptions.Shadow hinzu**
Repräsentiert die Füllung, den Umriss und den Schatten des Textes.
### **Veraltet die FontSetting.ShapeFont-Eigenschaft und fügt die FontSetting.TextOptions-Eigenschaft hinzu**
Bitte verwenden Sie stattdessen die Eigenschaft FontSetting.TextOptions.
### **Fügt die Shape.TextOptions-Eigenschaft hinzu.**
Stellt die Textoptionen der Form dar.
### **Veraltet Worksheet.SetBackground-Methode.**
Bitte verwenden Sie stattdessen die Worksheet.BackgroundImage-Eigenschaft.
### **Veraltet LineShape.BeginArrowheadStyle und ArcShape.BeginArrowheadStyle**
Bitte verwenden Sie stattdessen die Eigenschaft Shape.Line.BeginArrowheadStyle.
### **Veraltet LineShape.BeginArrowheadWidth und ArcShape.BeginArrowheadWidth**
Bitte verwenden Sie stattdessen die Eigenschaft Shape.Line.BeginArrowheadWidth.
### **Veraltet LineShape.BeginArrowheadLength und ArcShape.BeginArrowheadLength**
Bitte verwenden Sie stattdessen die Eigenschaft Shape.Line.BeginArrowheadLength.
### **Veraltet LineShape.EndArrowheadStyle und ArcShape.EndArrowheadStyle**
Bitte verwenden Sie stattdessen die Eigenschaft Shape.Line.EndArrowheadStyle.
### **Veraltet LineShape.EndArrowheadWidth und ArcShape.EndArrowheadWidth**
Bitte verwenden Sie stattdessen die Eigenschaft Shape.Line.EndArrowheadWidth.
### **Veraltet LineShape.EndArrowheadLength und ArcShape.EndArrowheadLength**
Bitte verwenden Sie stattdessen die Eigenschaft Shape.Line.EndArrowheadLength.
### **Löscht die veraltete Methode Worksheet.CopyConditionalFormatting().**
### **Löscht die veraltete Methode Workbook.CheckWriteProtectedPassword().**
Verwenden Sie stattdessen die Methode WorkbookSettings.WriteProtection.ValidatePassword.
### **Benennt Workbook.RemoveDigitallySign in Workbook.RemoveDigitalSignature-Methode um.**
### **Die obsolete WorksheetCollection.ClearPivots-Methode fügt die WorksheetCollection.ClearPivottables-Methode hinzu.**
Bitte verwenden Sie die WorksheetCollection.ClearPivottables-Methode.
### **Fügt die ChartSplitType.Auto-Eigenschaft hinzu.**
Stellt dar, dass die Datenpunkte unter Verwendung des Standardmechanismus für diesen Diagrammtyp geteilt werden sollen.
### **Fügt die ChartPoint.IsInSecondaryPlot-Eigenschaft hinzu.**
Ruft einen Wert ab oder legt einen Wert fest, der angibt, ob sich dieser Datenpunkt im zweiten Kreis oder Balken eines Kreisdiagramms oder eines Balkendiagramms befindet.
### **Fügt die OleObject.ClassIdentifier-Eigenschaft hinzu.**
Ruft den Klassenbezeichner des eingebetteten Objekts ab oder legt diesen fest.

{{% alert color="primary" %}} 

Da die Codebasis von Aspose.Cells für Android mit dem Code von Relevanten .NET und Java übereinstimmt, sind die meisten Änderungen, Verbesserungen und Fixes, die in der Aspose.Cells 076181381381381381381, 0761381, 0761381616161616161616161616161616161616161616161616161615,. .9.1, Aspose.Cells for Java v8.9.2 und Aspose.Cells for Java v9.0.0 sind ebenfalls in diesem Aspose.Cells für Android v9.0.0 enthalten.

{{% /alert %}}
