---
title: Aspose.Cells für Android über Java 19.6 Versionshinweise
type: docs
weight: 30
url: /de/java/aspose-cells-for-android-via-java-19-6-release-notes/
---
{{% alert color="primary" %}} 

Diese Seite enthält Versionshinweise für Aspose.Cells für Android über Java 19.6.

{{% /alert %}} 

|**Taste**|**Zusammenfassung**|**Kategorie**|
|:- |:- |:- |
|CELLSJAVA-42914|Große bedingte Formate verursachen eine OOM-Ausnahme|Erweiterung|
|CELLSJAVA-42916|Datenformatproblem nach Workbook.save()|Erweiterung|
|CELLSJAVA-42930|Fehler beim Laden von Excel95|Erweiterung|
|CELLSJAVA-42927|Gespeicherte Datei wird in Excel nach dem Löschen von Spalten langsam geöffnet|Erweiterung|
|CELLSJAVA-42857|Falscher Wert für Formen im exportierten PDF angezeigt|Insekt|
|CELLSJAVA-42890|Das Bild ist nach der Konvertierung undurchsichtig und nicht transparent - Excel-zu-HTML-Rendering|Insekt|
|CELLSJAVA-42893|Das Diagramm fehlt beim Rendern von Excel in HTML|Insekt|
|CELLSJAVA-42899|Excel-zu-HTML-Problem|Insekt|
|CELLSJAVA-42903|Problem beim Rendern von Excel zu HTML unter CentOS|Insekt|
|CELLSJAVA-42882|Daten konnten nicht aus einer MS Excel 95 XLS-Datei extrahiert werden|Insekt|
|CELLSJAVA-42887|Berechnungsunterschied zwischen MS Excel und Aspose.Cells|Insekt|
|CELLSJAVA-42891|Die XIRR-Funktion gibt einen numerischen Fehler aus, wenn ein Nullwert im Bereich vorhanden ist|Insekt|
|CELLSJAVA-42909|Problem mit DATEVALUE-Funktion|Insekt|
|CELLSJAVA-42910|Problem mit der VLOOKUP-Funktion, wenn ein Zeichen in der Zeichenfolge vorhanden ist|Insekt|
|CELLSJAVA-42911|Problem bei Verwendung der TEXT-Funktion für Datumsangaben|Insekt|
|CELLSJAVA-42896|Die Konvertierung in PDF dreht Telefonnummern um|Insekt|
|CELLSJAVA-42900|Die Konvertierung in PDF ändert die Textreihenfolge|Insekt|
|CELLSJAVA-42932|Bedingter Formatierungsfehler mit der Style.getDisplayStyle-Methode|Insekt|
|CELLSJAVA-42928|Einige Zeilen werden bei der XLSX-zu-PDF-Konvertierung nicht wiedergegeben|Insekt|
|CELLSJAVA-42904|Das Header-Bild beschädigt scheinbar die Datei|Insekt|
|CELLSJAVA-42907|Filter nach dem Speichern der Arbeitsmappe verloren|Insekt|
|CELLSJAVA-42915|Filter werden nach dem Hinzufügen eines Blatts zur Arbeitsmappe geändert|Insekt|
|CELLSJAVA-42918|Diagramm der konvertierten Datei abgeflacht (Konvertierung von XLS in XLSX)|Insekt|
|CELLSJAVA-42938|Das Laden der XLSX-Datei hält die Anwendung an|Insekt|
|CELLSJAVA-42881|Ausnahme "java.lang.IllegalStateException: Invalid encoding: null " beim Laden einer MS Excel 5.0/95 XLS-Datei|Ausnahme|
|CELLSJAVA-42884|Ausnahme "java.lang.ArrayIndexOutOfBoundsException" beim Laden einer MS Excel 5.0/95 XLS-Datei|Ausnahme|
|CELLSJAVA-42859|CellsException für das Laden des Namens aus der ODS-Datei|Ausnahme|
|CELLSJAVA-42908|Ausnahme beim Aufrufen von Name.getRefersTo()|Ausnahme|
|CELLSJAVA-42926|IllegalStateException beim Laden der Arbeitsmappe|Ausnahme|
## **Öffentliche API und rückwärts inkompatible Änderungen**
Im Folgenden finden Sie eine Liste aller Änderungen, die an der öffentlichen API vorgenommen wurden, z. B. hinzugefügte, umbenannte, entfernte oder veraltete Mitglieder, sowie alle nicht abwärtskompatiblen Änderungen, die an Aspose.Cells für Android über Java vorgenommen wurden. Wenn Sie Bedenken hinsichtlich einer der aufgeführten Änderungen haben, wenden Sie sich bitte an uns Erheben Sie es im Aspose.Cells Support-Forum.
### **Fügt den StreamProviderOptions-Konstruktor hinzu**
Neue StreamProviderOptions.
### **Fügt FileFormatType.GraphChart-Aufzählung hinzu**
Stellt die eingebettete Diagrammdatei dar.
### **Fügt ImportTableOptions.CheckMergedCells-Eigenschaften hinzu**
Gibt an, ob verbundene Zellen beim Importieren von Daten überprüft werden.
### **Fügt ODSCellFieldCollection, ODSCellField-Klassen und ODSCellFieldType-Enum hinzu**
Repräsentiert das Zellenfeld von ODS.
### **Fügt Cells.ODSCellFields-Eigenschaften hinzu**
Ruft die Liste der Zellenfelder von ODS ab.
### **Fügt die ODSPageBackground-Klasse und die PageSetup.ODSPageBackground-Eigenschaft hinzu**
Stellt den Hintergrund von ODS dar.
### **Fügt Aufzählung FileFormatType.FODS, FileFormatType.SXC,LoadFormat.FODS,LoadFormat.SXC,SaveFormat.FODS und SaveFormat.SXC hinzu**
Stellt die Dateiformattypen .FODS und .SXC dar.
### **Fügt Aufzählung WarningType.UnsupportedFileFormat hinzu**
Stellt ein nicht unterstütztes Dateiformat für Warnungstypen dar.
### **Fügt Aufzählung ODSGeneratorType hinzu**
Repräsentiert den Generatortyp von Ods.
### **OoxmlSaveOptions.EmbedOoxmlAsOleObject**
Gibt an, ob die OOXML-Datei als OleObject eingebettet wird.
### **Fügt Row.CopySettings(Aspose.Cells.Row,System.Boolean) hinzu**
Kopieren Sie die Einstellungen der Zeile, wie z. B. Stil, Höhe, Sichtbarkeit usw.
