---
title: Aspose.Cells for .NET 22.2 Versionshinweise
type: docs
weight: 11
url: /de/net/aspose-cells-for-net-22-2-release-notes/
---
{{% alert color="primary" %}}

 Diese Seite enthält Versionshinweise für[Aspose.Cells for .NET 22.2](https://www.nuget.org/packages/Aspose.Cells/22.2.0).

{{% /alert %}}

|**Taste**|**Zusammenfassung**|**Kategorie**|
|:- |:- |:- |
|CELLSNET-50332| Extrahieren Sie alle NameCollections eines bestimmten Arbeitsblatts|
|CELLSNET-50353|Fügen Sie die Eigenschaft StandardHeightInch in der Klasse Cells hinzu|
|CELLSNET-50152| Verschiedene Formatierungs- und andere Probleme beim Rendern von Formen in PDF- und HTML-Dateien von Excel|
|CELLSNET-50300|Einige Formen werden bei der Konvertierung von Excel in PDF nicht richtig gerendert|
|CELLSNET-50301|Ungültiger Wert für externe Referenz im DataSource-Feld der Pivot-Tabelle|
|CELLSNET-50241|Regression: CSV-zu-PDF-Konvertierung funktioniert nicht|
|CELLSNET-50268|Leeres CellsArea-Array, das für CSV/TSV-Dateien zurückgegeben wird|
|CELLSNET-50269|Finnische Sprache - Bei als Prozent formatierten Zahlen fehlt das Leerzeichen vor dem Prozentzeichen|
|CELLSNET-50333|Aspose.cell Arbeitsmappen-Überarbeitungsprotokolle konnten nicht erfasst werden|
|CELLSNET-50239|Fehlende Seite nach Konvertierung einer Excel-Datei in PDF|
|CELLSNET-50255|Cell Der Typ ist nach dem Exportieren in HTML und dem erneuten Laden des exportierten HTML-Codes falsch|
|CELLSNET-50266|Chart.ToImage() Thread-Sicherheitsproblem|
|CELLSNET-50302|Regression: Konvertierung in HTML-Zahlen wird nicht korrekt gerendert|
|CELLSNET-50328|Cell Hintergrund wird nach der Konvertierung in pdf schwarz|
|CELLSNET-50225|Die Diagrammlegende wird beim Speichern von Excel in PDF zurückgesetzt|
|CELLSNET-50247|Durch das Einfügen von Zeilen in das Blatt verlieren die Reihen der Diagramme ihre XWerte|
|CELLSNET-50295|Chart.SetChartDataRange(area, false) erkennt verbundene Zellen nicht|
|CELLSNET-50308|Bereich bis PNG: Ausgabe nicht wie erwartet|
|CELLSNET-50240| Ungeschützte OLE-Objekte auf einem geschützten Blatt werden nach dem Speichern geschützt|
|CELLSNET-50273|Erkennen Sie das Dateiformat einer speziellen HTML-Datei|
|CELLSNET-50294|ActiveX-Steuerungsschaltflächen werden in Shapes konvertiert und die Datei ist für XLS zu XLSM und dann zurück zu XLS beschädigt|
|CELLSNET-50340|Beim Konvertieren bestimmter Dateien in HTML fehlen Zeilen in Tabellenspalten|
|CELLSNET-50286|Cells.RemoveDuplicates wirft „System.IndexOutOfRangeException: Index lag außerhalb der Grenzen des Arrays“|
|CELLSNET-50270|Die Eingabezeichenfolge hatte nicht das richtige Format. Ausnahme beim Öffnen einer XLS-Datei|
|CELLSNET-50271|Das Format dieser Datei wird nicht unterstützt oder Sie geben kein korrektes Format an. Ausnahme beim Öffnen einer XLS-Datei|
|CELLSNET-50293|ExportXml mit XML-Zuordnung löst „NullReferenceException“ für eine andere komplexe Datei aus|
|CELLSNET-50352|NullReferenceException beim Konvertieren der XLSM-Datei in XLS|

## **Öffentliche API und rückwärts inkompatible Änderungen**

Im Folgenden finden Sie eine Liste aller Änderungen, die an der öffentlichen API vorgenommen wurden, z. B. hinzugefügte, umbenannte, entfernte oder veraltete Mitglieder, sowie alle nicht abwärtskompatiblen Änderungen, die an Aspose.Cells for .NET vorgenommen wurden das Aspose.Cells Support-Forum.

### **Veraltet die Methode Cells.AddAddInFunction().**

Bitte verwenden Sie stattdessen WorksheetCollection.RegisterAddInFunction() Methoden.

### **Fügt die NameCollection.Filter()-Methode und die NameScopeType-Aufzählung hinzu.**

Ruft die definierten Namen nach Bereich ab.

### **Fügt MsoDrawingType.Timeline-Aufzählung hinzu.**

Stellt den Objekttyp der Timeline-Zeichnung dar.
