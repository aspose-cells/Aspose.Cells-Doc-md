---
title: Aspose.Cells for .NET 8.0.2 Versionshinweise
type: docs
weight: 70
url: /de/net/aspose-cells-for-net-8-0-2-release-notes/
---
{{% alert color="primary" %}} 

 Diese Seite enthält Versionshinweise für[Aspose.Cells for .NET 8.0.2](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.0.2/)

{{% /alert %}} 

 Aspose.Cells for .NET wurde auf Version 8.0.2 aktualisiert und wir freuen uns, Ihnen mitteilen zu können, dass diese Version über 30 neue nützliche Verbesserungen enthält.
Mit Aspose.Cells for .NET können Sie in Ihren Anwendungen mit XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS und anderen Formaten arbeiten. Sie können Arbeitsmappen auch anzeigen, generieren, ändern, konvertieren, rendern und drucken, ohne Microsoft Excel zu verwenden.
Besuchen Sie die Dokumentation, um zu erfahren, wie Sie mit Aspose.Cells for .NET beginnen.
Beachten Sie, dass dieser Download eine voll funktionsfähige Version des Produkts enthält, jedoch ohne Lizenzsatz im Evaluierungsmodus mit einigen Einschränkungen ausgeführt werden kann. Um Aspose.Cells ohne diese Evaluierungseinschränkungen zu testen, können Sie eine kostenlose temporäre 30-Tage-Lizenz anfordern.
Im Folgenden finden Sie eine Liste der Änderungen in dieser Version von Aspose.Cells.

\1) Aspose.Cells 


## **Andere Verbesserungen und Änderungen**

## **Neue Eigenschaften**


 (CELLSNET-42585) – Richtung des Kommentartexts ändern


## **Leistung**


 (CELLSNET-42278) – System.OutOfMemoryException beim Speichern von XLSX in PDF, wobei XLSX viele leere Zellen mit Formatierung enthält


## **Fehler**


 (CELLSNET-42524) – CalculateTextSize-Funktion der Shape-Objektprobleme

 (CELLSNET-42401) – CalculateTextSize() gibt nicht die korrekte Höhe zurück

(CELLSNET-42235) – Problem mit TextBox AutoSizing

 (CELLSNET-42104) – CalculateTextSize gibt nicht die richtige Höhe zurück

 (CELLSNET-42612) – Die Funktion „Spalten automatisch anpassen“ funktioniert nicht für die gefilterten Dropdown-Spalten des Pivots

 (CELLSNET-42562) – Formeln funktionieren nicht mit Fremdwährung

 (CELLSNET-42269) – PivotTable-Formatierung im Ausgabe-XPS ist nicht korrekt

 (CELLSNET-42597) – AutoFitRows bewirkt, dass der umbrochene Text im resultierenden PDF ausgeblendet wird

 (CELLSNET-42615) – SheetRender gibt hochgestellte Zeichen nicht korrekt wieder

 (CELLSNET-42594) – Die vertikale Textausrichtung funktioniert in SheetRender nicht richtig

 (CELLSNET-42580) – Excel-Datei als PDF speichern ignoriert Farbeinstellungen in der Kopfzeile

 (CELLSNET-42579) – Problem mit Seitenumbruch beim Rendern in PDF

 (CELLSNET-42498) – Rand wird beim Konvertieren von XLSX in PDF auf die nächste Seite kopiert

 (CELLSNET-42495) – PDF-Rendering enthält unerwünschte Zeilen auf Seite 2 und 3

(CELLSNET-42567) – Diagramm verschwindet, wenn es in PDF konvertiert wird

 (CELLSNET-42527) – Liniendiagramm und Balkendiagramm im selben Diagramm befinden sich nicht an der richtigen Position

 (CELLSNET-42595) – Gitternetzlinien werden in der MS-Excel-Druckvorschau angezeigt, wenn die Arbeitsmappe im Xlsb-Format gespeichert wird

 (CELLSNET-42591) – AutoFitColumns funktioniert nicht mit ListObjects, wenn neue Zeilen hinzugefügt werden.

 (CELLSNET-42590) – Das xml:space="preserve"-Attribut geht für den v (value) OpenXML-Knoten von Excel Cell verloren

 (CELLSNET-42588) – Eine Tabelle kann nicht in die XLSB-Datei eingefügt werden

 (CELLSNET-42586) – Die Textausrichtung von Kommentaren funktioniert nicht, wenn sie auf rechts eingestellt ist

 (CELLSNET-42582) – Excel hat beim Öffnen von Aspose.Cells den Fehler „Unlesbarer Inhalt“ gefunden, der XLSM von XLSB konvertiert hat

 (CELLSNET-42581) – ArgumentOutOfRangeException – beim Öffnen der Excel-XLSX-Datei

 (CELLSNET-42570) - Cell-Formeln in den Smart-Markern werden nicht erweitert

 (CELLSNET-42568) – Die Spalte „Siebgröße“ zeigt „#N/A“.


## **Ausnahmen**


(CELLSNET-42576) – Null-Referenz-Ausnahme beim Speichern von xls als PDF

 (CELLSNET-42628) – System.NullReferenceException beim Laden einer MHTML-Tabelle

 (CELLSNET-42609) – Cell.GetDispalyStyle() schlägt bei einigen bedingten Formatierungsregeln fehl

 (CELLSNET-42587) – System.NullReferenceException beim Öffnen der Datei

 (CELLSNET-42577) – NullReferenceException – beim Abrufen des bedingten Stils für eine Zelle





\2) Aspose.Cells Grid-Suite


## **Andere Verbesserungen und Änderungen**

## **Fehler**


 (CELLSNET-42572) – Die Blattregisterkartenfarbe wird im GridWeb nicht beibehalten

 (CELLSNET-42302) – WebGrid-Kontextmenü – FIND schlägt in IE11 mit JS-Fehler fehl: Eigenschaft „acwFindReplaceDialog_Element“ von undefinierter oder Nullreferenz kann nicht abgerufen werden

 (CELLSNET-40531) – Formelproblem beim Laden der Vorlagendatei in GridWeb

 (CELLSNET-42571) – Zahlenformat in Spalte H im GridWeb wird nicht beibehalten

 (CELLSNET-42553) – Formatierung/Stil von Listenobjekten/Tabellen geht beim Importieren von Excel-Dateien in GridWeb verloren

 (CELLSNET-42623) – Fehler beim Erstellen des Steuerelements für GridWeb




## **Öffentliche API und rückwärts inkompatible Änderungen**


 Im Folgenden finden Sie eine Liste aller Änderungen, die an der öffentlichen API vorgenommen wurden, z. B. hinzugefügte, umbenannte, entfernte oder veraltete Mitglieder, sowie alle nicht abwärtskompatiblen Änderungen, die an Aspose.Cells for .NET vorgenommen wurden das Aspose.Cells Support-Forum.



Fügt die Shape.TextDirection-Eigenschaft hinzu

 Ruft die Richtung des Textflusses für die Form ab/legt sie fest.



 Fügt die HTMLLoadOptions.ConvertFormulasData-Eigenschaft hinzu

 Gibt an, ob eine Zeichenfolge in eine Formel konvertiert werden soll, wenn der mit dem Zeichen „=“ beginnende Zeichenfolgenwert eine Formelzeichenfolge ist. Der Standardwert ist „false“.



 Fügt die HtmlSaveOptions.ImageOptions-Eigenschaft hinzu

 Holt/Setzt Optionen für das Rendern beim Speichern von HTML-Dateien.



 Veraltet die HtmlSaveOptions.ExportChartImageFormat-Eigenschaft

 Verwendet stattdessen HtmlSaveOptions.ImageOptions für Bildformateinstellungen beim Speichern von HTML-Dateien.


