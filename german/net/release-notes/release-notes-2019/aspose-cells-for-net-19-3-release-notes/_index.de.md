---
title: Aspose.Cells for .NET 19.3 Versionshinweise
type: docs
weight: 100
url: /de/net/aspose-cells-for-net-19-3-release-notes/
---
{{% alert color="primary" %}} 

 Diese Seite enthält Versionshinweise für[Aspose.Cells for .NET 19.3](https://www.nuget.org/packages/Aspose.Cells/19.3.0).

{{% /alert %}} 

|**Taste**|**Zusammenfassung**|**Kategorie**|
|:- |:- |:- |
|CELLSNET-46598|Methode Name.GetReferredAreas (boolesche Neuberechnung) hinzufügen, um umfassendere Daten zu erhalten (einschließlich externer Referenzen und verknüpfter Daten)|Neue Funktion|
|CELLSNET-46580|Falsches Rendern von gedrehten Formen bei der Form-zu-Bild-Konvertierung|Insekt|
|CELLSNET-46587|Pivot-Tabelle bricht beim Löschen von Zeilen und Spalten ab|Insekt|
|CELLSNET-46608|Pivot-Tabellenfilter werden nach dem Laden und Speichern gelöscht|Insekt|
|CELLSNET-46623|Probleme in eingebetteten freigegebenen Datei-URLs beim Konvertieren von Excel-Dateien in HTML|Insekt|
|CELLSNET-46590|Fehler in einer Zelle, die ein Makro aufruft, nachdem die Datei von Aspose.Cells verarbeitet wurde|Insekt|
|CELLSNET-46597|Falscher Wert in PDF in Excel zu PDF-Rendering|Insekt|
|CELLSNET-46613|Probleme beim Abrufen und Erstellen benannter Bereiche|Insekt|
|CELLSNET-46625|Falscher Tabellenhintergrund in Ausgabe-PDF und HTML|Insekt|
|CELLSNET-46628|Unterschied in der Ausgabe PDF|Insekt|
|CELLSNET-46589|Unerwartete Gitterlinien erschienen in SVG, die aus einem MS Excel-Arbeitsblatt konvertiert wurden|Insekt|
|CELLSNET-46600|Doppelte Unterstreichung verschwindet beim Konvertieren von Excel-Dateien in PDF|Insekt|
|CELLSNET-46626|Probleme mit der Leerzeichenformatierung beim Konvertieren von XLSX-Dateien in PDF|Insekt|
|CELLSNET-46585|Problem mit DataLabel-Schriftart|Insekt|
|CELLSNET-46602|OutOfMemoryException beim Rendern eines vertikalen oder horizontalen Balkendiagramms|Insekt|
|CELLSNET-46605|Die Höhe der Zeile wird nach dem Vorgang zum automatischen Anpassen von Zeilen (Optionen) erhöht|Insekt|
|CELLSNET-46609|Einfügeoption CopyFormatType.Clear funktioniert nicht richtig|Insekt|
|CELLSNET-46611|Probleme mit externen Links und deren Anzeige|Insekt|
|CELLSNET-46616|Handhabung von ListObject.ConvertToRange auf gigantischen Tabellen|Insekt|
|CELLSNET-46620|Line.SolidFill.Color funktioniert bei Shapes nicht ordnungsgemäß, wenn Farbe von Argb oder von bekanntem Namen übergeben wird|Insekt|
|CELLSNET-46622|Cells.ImportData importiert die falsche Anzahl von Spalten aus der Datentabelle|Insekt|
|CELLSNET-46624|Problem beim Laden der XLSX-Datei|Insekt|
|CELLSNET-46635|Zu viele Seitenumbrüche in ODS-Datei (Rendering von XLSX zu ODS)|Insekt|
|CELLSNET-46618|Ausnahme „Instanz ist schreibgeschützt“|Ausnahme|
|CELLSNET-46617|Ausnahme beim Laden einer Arbeitsmappe|Ausnahme|
|CELLSNET-46636|Ausnahme beim Laden einer XLSX-Datei|Ausnahme|
### **Öffentliche API und rückwärts inkompatible Änderungen**
Im Folgenden finden Sie eine Liste aller Änderungen, die an der öffentlichen API vorgenommen wurden, z. B. hinzugefügte, umbenannte, entfernte oder veraltete Mitglieder, sowie alle nicht abwärtskompatiblen Änderungen, die an Aspose.Cells for .NET vorgenommen wurden das Aspose.Cells Support-Forum.
#### **Änderungen für die Standardschriftart der geladenen XLS-Vorlagendatei**
In älteren Versionen haben wir es nicht unterstützt, die im Design definierte Schriftart (erweiterte Funktion in MS Excel 2007 und späteren Versionen) entsprechend der Region beim Laden der XLS-Vorlagendateien anzuwenden. Auf Anforderung einiger Benutzer haben wir es ab v19.3 unterstützt. Wenn die Region in der XLS-Vorlagendatei angegeben wurde, wenden wir die im Design definierte Schriftart gemäß dem gespeicherten angegebenen Regionswert an. Andernfalls wenden wir die im Design definierte Schriftart gemäß den regionalen Einstellungen der Anwendungsumgebung an. Dadurch wird die Standardschriftart der Arbeitsmappe (geladen aus einer XLS-Vorlagendatei mit festgelegten Designdaten) geändert und beeinflusst dann andere Funktionen wie Spaltenbreite, Formgröße, Rendering-Effekt usw.
#### **Fügt die Name.GetReferredAreas(bool recalculate)-Methode hinzu**
Stellt die Referenzen bereit, auf die durch den definierten Namen wie die Methode GetRanges(bool recalculate) verwiesen wird. Die zurückgegebenen Verweise werden jedoch durch das Objekt ReferredArea dargestellt, das umfangreichere Funktionen einschließlich externer Links bietet.
#### **Fügt die TxtSaveOptions.KeepSeparatorsForBlankRow-Eigenschaft hinzu**
Gibt an, ob Trennzeichen für Leerzeilen ausgegeben werden sollen. Der Standardwert ist „false“, was bedeutet, dass der Inhalt für eine leere Zeile leer ist.
#### **Fügt Aufzählung AutoFitMergedCellsType hinzu**
Stellt den Typ der automatisch angepassten verbundenen Zellen dar.
#### **Veraltet die AutoFitterOptions.AutoFitMergedCells-Eigenschaft und fügt die AutoFitterOptions.AutoFitMergedCellsType-Eigenschaft hinzu**
Ruft den Typ der automatisch angepassten Zeilenhöhe ab und legt diesen fest.
#### **Fügt die Klassen JSONUtility und JsonLayoutOptions hinzu**
Es wird zum Importieren von JSON-Dateien verwendet.
#### **Fügt die Klasse TableToRangeOptions und die Methode ListObject.ConvertToRange(TableToRangeOptions options) hinzu**
Wandelt die Tabelle in einen Bereich mit Optionen um.
