---
title: Aspose.Cells for Java 19.1 Versionshinweise
type: docs
weight: 120
url: /de/java/aspose-cells-for-java-19-1-release-notes/
---
{{% alert color="primary" %}} 

Diese Seite enthält Versionshinweise für Aspose.Cells for Java 19.1.

{{% /alert %}} 

|**Taste**|**Zusammenfassung**|**Kategorie**|
|:- |:- |:- |
|CELLSJAVA-41026|Unterstützung von Excel 95/5.0 (XLS-Dateien)|Neue Funktion|
|CELLSJAVA-42778|Ausnahme „Stil textRotation muss zwischen 0 und 180 liegen“ beim Laden des XLSM|Erweiterung|
|CELLSJAVA-42290|In TextBoxen in Diagrammen eingefügte Striche und Gedankenstriche werden in der PDF-Datei des Diagramms nicht richtig gerendert|Insekt|
|CELLSJAVA-42750|Die Elemente der Seitenfelder im PivotTable-Bericht können nicht abgerufen werden|Insekt|
|CELLSJAVA-42783|Problem mit durchgestrichenem Text im generierten HTML-Dateiformat|Insekt|
|CELLSJAVA-42784|Daten in einigen Zellen (z. B. G7, H7 usw.) werden nicht auf die gleiche Weise wie in der Originaldatei in der Excel-zu-HTML/Bild-Konvertierung gerendert|Insekt|
|CELLSJAVA-42797|Einige Stile werden in der HTML-Eingabe nicht gerendert|Insekt|
|CELLSJAVA-42807|Formel/Funktion "ISOWEEKNUM"-Berechnung ist nicht dasselbe wie MS Excel|Insekt|
|CELLSJAVA-42794|ODS zu XLSX - Textfarbe geändert|Insekt|
|CELLSJAVA-42795|ODS zu XLSX - Durchgestrichene Schriftart wird nicht richtig beibehalten|Insekt|
|CELLSJAVA-42796|ODS zu XLSX - Textfeldabmessungen geändert|Insekt|
|CELLSJAVA-42798|ODS -> XLSX - Hyperlink ist funktionsfähig, wird aber als Klartext angezeigt|Insekt|
|CELLSJAVA-42802|ODS zu XLSX, Prozentsätze gehen im Balkendiagramm verloren|Insekt|
|CELLSJAVA-42803|Gliederung „SummaryRowBelow“ ist beim Speichern im XLSB-Dateiformat nicht betroffen|Insekt|
|CELLSJAVA-42757|CellsException beim Konvertieren von Dateien|Ausnahme|
|CELLSJAVA-42799|Ausnahme "java.lang.ArrayIndexOutOfBoundsException: -32768" beim Laden eines XLSX-Dateiformats|Ausnahme|
|CELLSJAVA-42800|ArrayIndexOutOfBoundsException beim Laden einer Arbeitsmappe|Ausnahme|
## **Öffentliche API und rückwärts inkompatible Änderungen**
Im Folgenden finden Sie eine Liste aller Änderungen, die an der öffentlichen API vorgenommen wurden, z. B. hinzugefügte, umbenannte, entfernte oder veraltete Mitglieder, sowie alle nicht abwärtskompatiblen Änderungen, die an Aspose.Cells for Java vorgenommen wurden das Aspose.Cells Support-Forum.
### **Fügt die Methode PivotTable.ShowReportFilterPageByName(string fieldName) hinzu**
Zeigt alle Berichtsfilterseiten gemäß dem Namen von PivotField an, das PivotField muss sich in den PageFields befinden.
### **Fügt die Methode PivotTable.ShowReportFilterPageByIndex(int posIndex) hinzu**
Zeigt alle Berichtsfilterseiten gemäß dem Positionsindex in den PageFields an.
### **Fügt die Methode PivotTable.ShowReportFilterPage(PivotField pageField) hinzu**
Zeigt alle Berichtsfilterseiten nach PivotField an, das PivotField muss sich in den PageFields befinden.
### **Fügt die Klassen DataSorterKey und DataSorterKeyCollection hinzu**
Repräsentiert den Schlüssel des Datensortierers.
### **Fügt die Methode DataSorter.AddKey(Int32,SortOnType,SortOrder,Object) hinzu**
Fügt den Sortierschlüssel hinzu, z. B. Hintergrundfarbe der Zelle, Schriftfarbe.
### **Fügt die Eigenschaft Aspose.Cells.DataSorter.Keys hinzu**
Ruft alle Schlüssel des Datensortierers ab.
### **Fügt SortOnType-Aufzählung hinzu**
Repräsentiert den Typ der sortierten Daten.
### **Fügt die ODSLoadOptions-Klasse hinzu**
Stellt die Optionen zum Laden der ODS-Datei dar.
### **Fügt die HTMLLoadOptions.ProgId-Eigenschaft hinzu**
Ruft die Programm-ID zum Erstellen der Datei ab. Wird nur für MHT-Dateien verwendet.
### **Fügt die PdfSaveOptions.TextCrossType-Eigenschaft hinzu**
Ruft die Anzeige des Texttyps ab oder legt diese fest, wenn die Textbreite größer als die Zellenbreite ist.
### **Fügt TextCrossType-Enumerationsklasse hinzu**
Listet die Anzeige des Texttyps auf, wenn die Textbreite größer als die Zellenbreite ist.
### **Fügt WorksheetCollection.RegisterAddInFunction()-Methoden hinzu**
Ersatz von Cell.SetAddInFormula(), eine bequemere und effizientere Möglichkeit für Benutzer, Add-in-Funktionen hinzuzufügen und zu verwenden.
### **Veraltet die Methode Cell.SetAddInFormula()**
Bitte registrieren Sie die Add-In-Funktionen zuerst mit WorksheetCollection.RegisterAddInFunction() und setzen Sie dann stattdessen die Formel für Cell mit Cell.Formula/Cell.SetFormula().
