---  
title: Wie man mit Node.js über C++ Drucktitel festlegt  
linktitle: Wie man Drucktitel festlegt  
type: docs  
weight: 200  
url: /de/nodejs-cpp/how-to-set-print-titles/  
description: Dieser Artikel zeigt Ihnen, wie Sie Drucktitel mit der Aspose.Cells Bibliothek für Node.js über C++ festlegen.  
keywords: Druckzeilen und spalten wiederholt drucken, Node.js Wie man Drucktitel festlegt, Drucktitel in Node.js setzen und löschen, Drucktitel in Node.js löschen, Drucktitel in Node.js hinzufügen, Drucktitel in Node.js entfernen, Drucktitel in Excel festlegen, Drucktitel in Excel löschen.  
---  

## **Mögliche Verwendungsszenarien**  

Das Festlegen von Drucktiteln in Excel stellt sicher, dass bestimmte Zeilen oder Spalten auf jeder gedruckten Seite wiederholt werden, was besonders bei großen Tabellen, die sich über mehrere Seiten erstrecken, nützlich ist. Hier sind einige Gründe, warum Sie Drucktitel festlegen könnten:  

1. Verbesserte Lesbarkeit: Drucktitel helfen den Lesern, die Daten zu verstehen, indem sie Kopfzeilen auf allen Seiten sichtbar halten, was die Interpretation der Informationen auf jeder Seite erleichtert, ohne auf die erste Seite zurückgreifen zu müssen.  

1. Professionelles Erscheinungsbild: Das konsequente Anzeigen von Kopfzeilen oder Label auf jeder Seite schafft ein professionelleres und gepflegteres Druckdokument.  

1. Verbesserte Navigation: Bei umfangreichen Daten ermöglicht das Wiederholen der Kopfzeilen auf jeder Seite eine schnellere Navigation und Referenzierung, wodurch das Hin- und Herblättern zwischen den Seiten reduziert wird.  

1. Weniger Fehler: Wenn Kopfzeilen auf jeder Seite vorhanden sind, minimieren Sie die Chancen für Missinterpretationen oder Eingabefehler, da Benutzer den Datenzusammenhang leicht erkennen können.  

1. Konsistenz: Die Sicherstellung, dass wichtige Informationen wie Spaltenüberschriften oder Zeilenbeschriftungen immer sichtbar sind, gewährleistet Konsistenz und Klarheit im gesamten Dokument.  

## **So legen Sie Drucktitel in Excel fest**  

Um Drucktitel in Excel festzulegen, folgen Sie diesen Schritten:  

1. Öffnen Sie die Registerkarte Seitenlayout: Klicken Sie auf die Registerkarte "Seitenlayout" im Menüband oben im Excel-Fenster.  
1. Zugriff auf Drucktitel: Klicken Sie im "Seiteneinrichtung"-Bereich auf "Drucktitel".  
1. Zeilen zum Wiederholen festlegen: Im Dialogfeld "Seite einrichten" gehen Sie auf die Registerkarte "Blatt". Im Abschnitt "Drucktitel" geben Sie die Zeilen an, die oben wiederholt werden sollen, indem Sie das Kästchen neben "Zeilen, die oben wiederholt werden" aktivieren und die Zeile(n) auswählen, die wiederholt werden sollen.  
1. Spalten zum Wiederholen festlegen (falls erforderlich): Ebenso können Sie die Spalten angeben, die links wiederholt werden sollen, indem Sie das Kästchen neben "Spalten, die links wiederholt werden" aktivieren und die Spalte(n) auswählen, die wiederholt werden sollen.  
<br>  
<img src="3.png" width=60% />  

1. Bestätigen und Drucken: Klicken Sie auf "OK", um die Einstellungen anzuwenden. Beim Drucken des Arbeitsblatts erscheinen die angegebenen Zeilen oder Spalten auf jeder gedruckten Seite.  

## **So entfernen Sie Drucktitel in Excel**  

Um Drucktitel in Excel zu entfernen, müssen Sie die Zeilen oder Spalten löschen, die so eingestellt sind, dass sie auf jeder Seite wiederholt werden. So geht's:  

1. Öffnen Sie die Registerkarte Seitenlayout: Klicken Sie auf die Registerkarte "Seitenlayout" im Menüband oben im Excel-Fenster.  
1. Zugriff auf Drucktitel: Klicken Sie im "Seiteneinrichtung"-Bereich auf "Drucktitel".  
1. Drucktitel entfernen: Im Dialogfeld "Seiteneinrichtung" wechseln Sie zum Reiter "Blatt". Löschen Sie den Text in den Feldern für "Zeilen, die oben wiederholt werden" und "Spalten, die links wiederholt werden", indem Sie den Inhalt löschen.  
<br>  
<img src="4.png" width=60% />  

1. Bestätigen und schließen: Klicken Sie auf "OK", um die Änderungen zu übernehmen.  

## **So legen Sie Drucktitel mit Aspose.Cells for Node.js via C++ fest**  

Um Drucktitel in einem bestimmten Arbeitsblatt festzulegen: Laden Sie zuerst die [Beispieldatei](input.xlsx) und ändern Sie dann die Eigenschaften [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) und [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) des Objekts [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) für das gewünschte Arbeitsblatt. Das Festlegen dieser Eigenschaften auf einen Range-String setzt die Drucktitel.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set rows to repeat at the top (e.g., rows 1 and 2)
worksheet.getPageSetup().setPrintTitleRows("$1:$2");

// Set columns to repeat at the left (e.g., columns A and B)
worksheet.getPageSetup().setPrintTitleColumns("$A:$B");

// Save the workbook
workbook.save("set_print_titles.pdf");
```  

Das Ausgabenergebnis:  
<br>  
<img src="1.png" width=60% />  

## **So löschen Sie Drucktitel mit Aspose.Cells for Node.js via C++**  

Um Drucktitel in einem bestimmten Arbeitsblatt zu entfernen: Laden Sie zuerst die [Beispieldatei](input.xlsx) und ändern Sie dann die Eigenschaften [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) und [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) des Objekts [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) für das gewünschte Arbeitsblatt. Das Festlegen dieser Eigenschaften auf einen leeren String löscht die Drucktitel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Clear the rows and columns set to repeat
worksheet.getPageSetup().setPrintTitleRows("");
worksheet.getPageSetup().setPrintTitleColumns("");

// Save the workbook
workbook.save("clear_print_titles.pdf");
```  

Das Ausgabenergebnis:  
<br>  
<img src="2.png" width=60% />  

{{< app/cells/assistant language="nodejs-cpp" >}}
