---  
title: Verwenden Sie Fehlerüberprüfung Optionen mit Node.js über C++  
linktitle: Verwenden von Fehlerüberprüfungsoptionen  
type: docs  
weight: 140  
url: /de/nodejs-cpp/use-error-checking-options/  
description: Erfahren Sie, wie Sie Fehlerüberprüfungsoptionen in Excel Arbeitsblättern programmatisch mit Aspose.Cells for Node.js via C++ verwenden.  
keywords: Zahl in Excel als Text speichern, indem Sie Node.js über C++ verwenden, Fehlerüberprüfungsoptionen in Excel Node.js über C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel ermöglicht es Benutzern, Fehlerprüfoptionen und -regeln zu definieren. Benutzer sehen oft Fehlerprüfungen beim Erstellen von Formeln, ein kleines Dreieck in der oberen rechten Ecke einer Zelle markiert, wenn ein Problem mit einer Zelle vorliegt. Excel bietet Informationen, die den Benutzern helfen, häufige Probleme zu korrigieren.  
{{% /alert %}}  

## **Arten von Fehlern**  

Fehler, die bedeuten, dass die Formel kein Ergebnis zurückgeben kann – wie das Teilen einer Zahl durch Null – erfordern sofortige Aufmerksamkeit und eine Fehlermeldung im Zelle. Das Klicken auf das grüne Dreieck zeigt ein Ausrufezeichen; durch Klicken öffnet sich eine Optionsliste.  

Der Fehler kann mithilfe der Optionen behoben oder ignoriert werden. Das Ignorieren eines Fehlers bedeutet, dass dieser Fehler bei weiteren Fehlerprüfungen nicht angezeigt wird.  

Aspose.Cells bietet Funktionen für Fehlerüberprüfung. Die Klasse [**ErrorCheckOption**](https://reference.aspose.com/cells/nodejs-cpp/errorcheckoption) verwaltet verschiedene Arten von Fehlerprüfungen, zum Beispiel Nummern, die als Text gespeichert sind, Formelfeld-Fehler und Validierungsfehler. Verwenden Sie die Aufzählung [**ErrorCheckType**](https://reference.aspose.com/cells/nodejs-cpp/errorchecktype), um die gewünschte Fehlerüberprüfung festzulegen.  

## **Als Text gespeicherte Zahlen**  

Gelegentlich werden Zahlen formatiert und in Zellen als Text gespeichert. Dies kann Probleme bei Berechnungen verursachen oder irreführende Sortierreihenfolgen erzeugen. Zahlen, die als Text formatiert sind, sind in der Zelle linksbündig anstelle von rechtsbündig. Wenn eine Formel, die eine mathematische Operation mit Zellen durchführen sollte, kein Ergebnis zurückgibt, überprüfen Sie die Ausrichtung in den Zellen, auf die sich die Formel bezieht - einige oder alle diese Zellen könnten als Text formatierte Zahlen sein.  

Sie können die Fehlerprüfungsoptionen verwenden, um Zahlen, die als Text gespeichert sind, schnell in echte Zahlen umzuwandeln. In Microsoft Excel 2003:  

1. Klicken Sie im Menü **Extras** auf **Optionen**.  
1. Wählen Sie den Tab Fehlerüberprüfung aus.  
   Die Option **Als Text gespeicherte Zahl** ist standardmäßig aktiviert.  
1. Deaktivieren Sie es.  

Der folgende Beispielcode zeigt, wie Sie die Option zur Fehlerprüfung von als Text gespeicherten Zahlen für ein Arbeitsblatt in der Vorlage XLS-Datei mithilfe der Aspose.Cells-APIs deaktivieren.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a workbook and opening a template spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Instantiate the error checking options
const opts = sheet.getErrorCheckOptions();

const index = opts.add();
const opt = opts.get(index);
// Disable the numbers stored as text option
opt.setErrorCheck(AsposeCells.ErrorCheckType.NumberStoredAsText, false);
// Set the range
opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

const outputFilePath = path.join(dataDir, "out_test.out.xlsx");
// Save the Excel file
workbook.save(outputFilePath);
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
