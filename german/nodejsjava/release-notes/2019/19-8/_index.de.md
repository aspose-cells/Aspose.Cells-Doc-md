---
title: Aspose.Cells für Node.js über Java 19.8 Versionshinweise
type: docs
weight: 10
url: /de/nodejs-java/aspose-cells-for-node-js-via-java-19-8-release-notes/
---
{{% alert color="primary" %}} 

Diese Seite enthält Versionshinweise für Aspose.Cells für Node.js über Java 19.8.

{{% /alert %}} 

|**Taste**|**Zusammenfassung**|**Kategorie**|
|:- |:- |:- |
|CELLSJAVA-42861|Alternativtext der Form im ODS-Dateiformat konnte nicht abgerufen werden|Insekt|
|CELLSJAVA-42929|Der Diagrammtitel ändert sich bei der XLSX-zu-PDF-Konvertierung|Insekt|
|CELLSJAVA-42933|Die Grafikfarbe ändert sich beim Konvertieren von Excel-Dateien in PDF|Insekt|
|CELLSJAVA-42946|Falsche Wiedergabe von gestapelten Balkendiagrammen mit Reihen in PDF|Insekt|
|CELLSJAVA-42942|Seiten werden auf Arbeitsblattebene und nicht auf Arbeitsmappenebene gedruckt|Insekt|
|CELLSJAVA-42952|Falsche Einrückung vom oberen Rand der Zelle in einigen Wörtern|Insekt|
|CELLSJAVA-42902|Der Wasserfalldiagrammstil wird beim Kopieren der Arbeitsmappe nicht richtig kopiert|Insekt|
|CELLSJAVA-42939|Von Excel ausgelöste Warnung, wenn Workbook.getVbaProject() nur für eine Arbeitsmappe aufgerufen wird|Insekt|
|CELLSJAVA-42940|Sicherheitswarnung nach dem Entfernen aller VBA-Modulskripte|Insekt|
|CELLSJAVA-42955|Das Öffnen von VBAProject beschädigt die Arbeitsmappe|Insekt|
|CELLSJAVA-42945|Beim Speichern als HTML wird eine Ausnahme ausgelöst, wenn ExportImagesAsBase64 festgelegt ist|Ausnahme|
|CELLSJAVA-42953|NullPointerException beim Konvertieren von XLS-Dateien in HTML|Ausnahme|
|CELLSJAVA-42951|java.lang.NullPointerException ausgelöst durch comment.setHtmlNote()|Ausnahme|
|CELLSJAVA-42954|Ausnahme beim Laden und Speichern der XLSX-Datei ausgelöst|Ausnahme|
|CELLSJAVA-42957|Beim Speichern der XLSX-Datei wird ein ungültiger FontUnderlineType-Wert ausgegeben|Ausnahme|
### **Öffentliche API und rückwärts inkompatible Änderungen**
Im Folgenden finden Sie eine Liste aller Änderungen, die an der öffentlichen API vorgenommen wurden, z. B. hinzugefügte, umbenannte, entfernte oder veraltete Mitglieder, sowie alle nicht abwärtskompatiblen Änderungen, die an Aspose.Cells für Node.js über Java vorgenommen wurden , wenden Sie sich bitte an das Support-Forum Aspose.Cells.
#### **Aktualisiert die referenzierte BouncyCastle-Bibliothek auf 1.60**
Die beigefügte BouncyCastle-Bibliothek im Release-Archiv wurde auf die Version 1.60 aktualisiert. Aspose.Cells ist jedoch auch mit alten Versionen kompatibel, sodass der Benutzer weiterhin die alten Versionen wie 1.46 verwenden kann.
#### **Veraltet die HTMLLoadOptions-Klasse und fügt die HtmlLoadOptions-Klasse hinzu**
Verwenden Sie stattdessen die HtmlLoadOptions-Klasse.
#### **Veraltet die ODSLoadOptions-Klasse und fügt die OdsLoadOptions-Klasse hinzu**
Verwenden Sie stattdessen die OdsLoadOptions-Klasse.
#### **Veraltet die JSONUtility-Klasse und fügt die JsonUtility-Klasse hinzu**
Verwenden Sie stattdessen die JsonUtility-Klasse.
#### **Fügt die Schnittstelle IPageSavingCallback hinzu**
Steuerung/Fortschritt des Seitenspeichervorgangs anzeigen.
#### **Fügt die Klasse PageSavingArgs hinzu**
Info für einen Seitenspeichervorgang.
#### **Fügt die Klasse PageStartSavingArgs hinzu**
Info für eine Seite startet den Speichervorgang.
#### **Fügt die Klasse PageEndSavingArgs hinzu**
Info für eine Seite beendet den Speichervorgang.
#### **Fügt die PdfSaveOptions.PageSavingCallback-Eigenschaft hinzu**
Steuerung/Fortschritt des Seitenspeichervorgangs anzeigen.

