---
title: Aspose.Cells for Java 19.3 Versionshinweise
type: docs
weight: 100
url: /de/java/aspose-cells-for-java-19-3-release-notes/
---
{{% alert color="primary" %}} 

Diese Seite enthält Versionshinweise für Aspose.Cells for Java 19.3.

{{% /alert %}} 

|**Taste**|**Zusammenfassung**|**Kategorie**|
|:- |:- |:- |
|CELLSJAVA-42845|Behalten Sie Trennzeichen für leere Zeilen bei, wenn Sie eine XLS-Datei in CSV exportieren|Neue Funktion|
|CELLSJAVA-42846|Die Ergebnisse der Textextraktion weichen vom Original ab|Erweiterung|
|CELLSJAVA-42844|Der Text wird in der PDF-Ausgabe nicht richtig ausgerichtet|Insekt|
|CELLSJAVA-42834|Die Textfarbe (schwarz) wird beim HTML-Rendering in rot geändert|Insekt|
|CELLSJAVA-42839|Streudiagramm wird bei der Konvertierung von Excel in PDF nicht gerendert|Insekt|
|CELLSJAVA-42840|Beschriftungen der horizontalen Achse werden für Diagramme beim Rendern von Excel in PDF nicht korrekt gerendert|Insekt|
|CELLSJAVA-42842|2D-Blasendiagramme werden bei der Konvertierung von Excel in PDF nicht gerendert|Insekt|
|CELLSJAVA-42833|Problem beim Einbetten derselben PDF-Datei in mehrere Blätter einer Arbeitsmappe|Insekt|
|CELLSJAVA-42836|Workbook.hasExernalLinks() gibt für DDE-Links nicht „true“ zurück|Insekt|
|CELLSJAVA-42848|Schriftarteinstellung und andere Objekte, die nicht mit der Funktion Range.copy() kopiert wurden|Insekt|
|CELLSJAVA-42849|IndexOutOfBoundsException-Ausnahme beim Konvertieren von XLSX in HTML|Ausnahme|
|CELLSJAVA-42831|Von MS Excel ausgelöste Ausnahme nach dem Anwenden des Stils auf den Bereich der Kopfzellen|Ausnahme|

## **Öffentliche API und rückwärts inkompatible Änderungen**
Im Folgenden finden Sie eine Liste aller Änderungen, die an der öffentlichen API vorgenommen wurden, z. B. hinzugefügte, umbenannte, entfernte oder veraltete Mitglieder, sowie alle nicht abwärtskompatiblen Änderungen, die an Aspose.Cells for Java vorgenommen wurden das Aspose.Cells Support-Forum.
### **Änderungen für die Standardschriftart der geladenen XLS-Vorlagendatei**
In älteren Versionen haben wir es nicht unterstützt, die im Design definierte Schriftart (erweiterte Funktion in MS Excel 2007 und späteren Versionen) entsprechend der Region beim Laden der XLS-Vorlagendateien anzuwenden. Auf Anforderung einiger Benutzer haben wir es ab v19.3 unterstützt. Wenn die Region in der XLS-Vorlagendatei angegeben wurde, wenden wir die im Design definierte Schriftart gemäß dem gespeicherten angegebenen Regionswert an. Andernfalls wenden wir die im Design definierte Schriftart gemäß den regionalen Einstellungen der Anwendungsumgebung an. Dadurch wird die Standardschriftart der Arbeitsmappe (geladen aus einer XLS-Vorlagendatei mit festgelegten Designdaten) geändert und beeinflusst dann andere Funktionen wie Spaltenbreite, Formgröße, Rendering-Effekt usw.
### **Fügt die Name.GetReferredAreas(bool recalculate)-Methode hinzu**
Stellt die Referenzen bereit, auf die durch den definierten Namen wie die Methode GetRanges(bool recalculate) verwiesen wird. Die zurückgegebenen Verweise werden jedoch durch das Objekt ReferredArea dargestellt, das umfangreichere Funktionen einschließlich externer Links bietet.
### **Fügt die TxtSaveOptions.KeepSeparatorsForBlankRow-Eigenschaft hinzu**
Gibt an, ob Trennzeichen für Leerzeilen ausgegeben werden sollen. Der Standardwert ist „false“, was bedeutet, dass der Inhalt für eine leere Zeile leer ist.
### **Fügt Aufzählung AutoFitMergedCellsType hinzu**
Stellt den Typ der automatisch angepassten verbundenen Zellen dar.
### **Veraltet die AutoFitterOptions.AutoFitMergedCells-Eigenschaft und fügt die AutoFitterOptions.AutoFitMergedCellsType-Eigenschaft hinzu**
Ruft den Typ der automatisch angepassten Zeilenhöhe ab und legt diesen fest.
### **Fügt die Klassen JSONUtility und JsonLayoutOptions hinzu**
Es wird zum Importieren von JSON-Dateien verwendet.
### **Fügt die Klasse TableToRangeOptions und die Methode ListObject.ConvertToRange(TableToRangeOptions options) hinzu**
Wandelt die Tabelle in einen Bereich mit Optionen um.
