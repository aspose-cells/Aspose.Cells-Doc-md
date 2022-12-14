---
title: Aspose.Cells for Java 17.1.0 Versionshinweise
type: docs
weight: 120
url: /de/java/aspose-cells-for-java-17-1-0-release-notes/
---
|**Taste**|**Zusammenfassung**|**Kategorie**|
|:- |:- |:- |
|CELLSJAVA-42132|GetPaperWidth- und GetPaperHeight-Methoden in PageSetup-Klasse hinzugefügt|Neue Funktion|
|CELLSJAVA-41950|Unterstützung von Verlaufsfüllungen für WordArt beim Konvertieren von Tabellenkalkulationen in HTML|Neue Funktion|
|CELLSJAVA-42129|Das Speichern in HTML ist falsch|Insekt|
|CELLSJAVA-42125|Gitternetzlinien hinter Formen werden bei der Konvertierung in HTML nicht exportiert|Insekt|
|CELLSJAVA-42110|Einige CSS-Regeln werden beim Importieren von HTML ignoriert|Insekt|
|CELLSJAVA-42094|Inhalte sind im konvertierten HTML durchgestrichen|Insekt|
|CELLSJAVA-42091|Der Textstil einiger Zellen ist beim Speichern in HTML falsch|Insekt|
|CELLSJAVA-42088|DataBar falsch, wenn Zelle Hintergrundfarbe eingestellt hat|Insekt|
|CELLSJAVA-42018|Das Diagrammbild wird nicht gespeichert, wenn das EMF- oder SVG-Format verwendet wird|Insekt|
|CELLSJAVA-41980|HtrmlSaveOptions.ExportGridLines scheint für eine bestimmte Tabelle nicht zu funktionieren|Insekt|
|CELLSJAVA-42131|Die Neuberechnung einer Reihe von Formeln mit Aspose Cells APIs führt zu "#NUM!" Error|Insekt|
|CELLSJAVA-42124|Problem mit dem Datumsformat beim Importieren von CSV mit ICustomParser|Insekt|
|CELLSJAVA-42118|Name.getRanges() API führt zu unerwarteten Ergebnissen|Insekt|
|CELLSJAVA-42117|Zugriff auf die Instanzvariable m_LoadDataFilterOptions beim Überschreiben der startSheet-Methode der LoadFilter-Klasse nicht möglich|Insekt|
|CELLSJAVA-41882|Cell Stringwert- und Rundungsproblem basierend auf verschiedenen JDK-Versionen|Insekt|
|CELLSJAVA-42142|Rechts-nach-links- und Links-nach-rechts-Steuerzeichen werden in PDF nicht korrekt wiedergegeben, wenn die Konvertierung unter Linux durchgeführt wird|Insekt|
|CELLSJAVA-42136|Hebräisch - In der Tabelle sind die umgebrochenen Zeilen in PDF rechts ausgerichtet, während sie wie in Excel zentriert sein sollten|Insekt|
|CELLSJAVA-42113|Falsche Konvertierung des arabischen Arbeitsblatts in SVG|Insekt|
|CELLSJAVA-42135|Hebräisch - Umbrochener Text wird in PDF nicht wie in Excel rechtsbündig ausgerichtet|Insekt|
|CELLSJAVA-42134|Hebräisch - Serienbeschriftungen mit Zeilenumbruch werden die Zeichen nicht in der richtigen Reihenfolge angezeigt|Insekt|
|CELLSJAVA-42127|Shape to image Fehler beim Rendern von 03.xls in PDF|Insekt|
|CELLSJAVA-42126|Shape to image Fehler beim Rendern von 02.xls in PDF|Insekt|
|CELLSJAVA-42087|Das Diagrammbild im HTML-Code ist falsch|Insekt|
|CELLSJAVA-42079|Ungleichmäßige Linienstärke an Schnittpunkten beim Rendern von Tabellenkalkulationen mit Diagrammen in PDF|Insekt|
|CELLSJAVA-42078|Diagrammbeschriftungen werden in der PDF-Ausgabedatei nicht so angezeigt/gerendert (wie in der ursprünglichen Excel-Datei).|Insekt|
|CELLSJAVA-42076|Der Winkel der X-Achsen-Beschriftungen ist in der PDF-Datei des Diagramms falsch|Insekt|
|CELLSJAVA-42065|Falsches Rendern von Balkendiagrammen beim Rendern von Tabellenkalkulationen in HTML|Insekt|
|CELLSJAVA-42152|Das Festlegen einer Formel, die sich auf eine externe Arbeitsmappe bezieht, erstellt eine 3D-Formel|Insekt|
|CELLSJAVA-42146|Unlesbarer Inhaltsfehler in Excel 2007 nach dem erneuten Speichern einer Tabelle|Insekt|
|CELLSJAVA-42121|Bedingter Formatausdruck ändert sich beim Löschen von Zeilen|Insekt|
|CELLSJAVA-42114|Cell.getFormula() gibt eine fehlerhafte Formel für eine Zelle zurück|Insekt|
|CELLSJAVA-42112|Die Ausgabedatei wird nach dem Ausführen der Methode DataLabels.setPosition() beschädigt|Insekt|
|CELLSJAVA-42108|Die Prioritätsreihenfolge des bedingten Formats ändert sich in der Methode Cells.deleteRows()|Insekt|
|CELLSJAVA-42069|Das VBA-Modul geht beim erneuten Speichern einer XLSM-Datei unter Linux verloren|Insekt|
|CELLSJAVA-42025|API fügt der modifizierten Formel zusätzliche Apostrophe hinzu|Insekt|
|CELLSJAVA-41984|Dynamische Formel in Designer-Tabelle mit {-1} {-2} return Ungültiger Formelfehler|Insekt|
|CELLSJAVA-41739|Die Transparenz der Formen wird beim Konvertieren von XLS in XLSB auf 0 zurückgesetzt|Insekt|
|CELLSJAVA-42122|NullPointerException beim Öffnen einer großen Excel-Datei|Ausnahme|
|CELLSJAVA-42123|Form-zu-Bild-Fehler – beim Rendern einer Excel-Datei|Ausnahme|
|CELLSJAVA-42144|new Workbook() konnte eine Ausnahme in Aspose.Cells for Java 16.12.6 auslösen|Ausnahme|
|CELLSJAVA-42143|Ausnahme: java.lang.ArrayIndexOutOfBoundsException bei der Methode Workbook.save()|Ausnahme|
|CELLSJAVA-42137|Ungültige Spaltenindex-Ausnahme beim Rendern von Excel|Ausnahme|
|CELLSJAVA-42111|Ungültige Formelausnahme für die letzte Zelle|Ausnahme|
## **Öffentliche API und rückwärts inkompatible Änderungen**
Im Folgenden finden Sie eine Liste aller Änderungen, die an der öffentlichen API vorgenommen wurden, z. B. hinzugefügte, umbenannte, entfernte oder veraltete Mitglieder, sowie alle nicht abwärtskompatiblen Änderungen, die an Aspose.Cells for Java vorgenommen wurden das Aspose.Cells Support-Forum.
### **Setter für die Eigenschaft LoadFilter.LoadDataFilterOptions hinzugefügt, um die Variable m_LoadDataFilterOptions zu ersetzen.**
Benutzer können die LoadDataFilterOptions-Eigenschaft in ihrer Implementierung von LoadFilter ändern, um das Verhalten beim Laden von Arbeitsmappen zu ändern.
### **Fügt die CellsHelper.SignificantDigits-Eigenschaft hinzu.**
Ruft die Anzahl signifikanter Stellen ab und legt sie fest.
### **Fügt die GlowEffect.Color-Eigenschaft hinzu.**
Ruft die Farbe des Leuchteffekts ab.
### **Fügt die PageSetup.PaperWidth-Eigenschaft hinzu.**
Repräsentiert die Breite des Papiers in Zoll unter Berücksichtigung der Seitenausrichtung.
### **Fügt die PageSetup.PaperHeight-Eigenschaft hinzu.**
Stellt die Höhe des Papiers in Zoll unter Berücksichtigung der Seitenausrichtung dar.
### **Fügt die WorkbookSettings.CheckCustomNumberFormat-Eigenschaft hinzu.**
Gibt an, ob das benutzerdefinierte Zahlenformat beim Festlegen von Style.Custom überprüft wird.
### **Fügt einige Diagrammtypen hinzu.**
Fügt weitere Diagrammtypen für MS Office 2016 hinzu.
### **Fügt DisplayUnitType.Percentage-Aufzählung hinzu.**
Stellt die Werte im Diagramm dar, die durch 0,01 geteilt werden.
