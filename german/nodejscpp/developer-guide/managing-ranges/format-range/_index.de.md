---  
title: Formatbereiche mit Node.js über C++  
linktitle: Bereiche formatieren  
type: docs  
weight: 105  
url: /de/nodejs-cpp/how-to-format-a-range/  
description: Erfahren Sie, wie Sie einen Zellenbereich in Excel mit Aspose.Cells for Node.js via C++ formatieren.  
---  

## **Mögliche Verwendungsszenarien**  
Wenn Sie einen Stil auf einen Bereich anwenden möchten, können Sie die Bereichsformatierung verwenden.  

## **Wie formatiert man einen Bereich in Excel**  

Um einen Zellenbereich in Excel zu formatieren, können Sie die von Excel bereitgestellten integrierten Formatierungsoptionen verwenden. So formatieren Sie einen Zellenbereich direkt in Excel:  

1. Öffnen Sie Excel und öffnen Sie die Arbeitsmappe, die den zu formatierenden Bereich enthält.  

2. Wählen Sie den zu formatierenden Zellenbereich aus. Sie können klicken und ziehen, um den Bereich auszuwählen, oder Sie können Tastenkombinationen wie Umschalttaste + Pfeiltasten verwenden, um die Auswahl zu erweitern.  

3. Wenn der Bereich ausgewählt ist, klicken Sie mit der rechten Maustaste auf den ausgewählten Bereich und wählen Sie "Zellen formatieren" im Kontextmenü aus. Alternativ können Sie zum Start-Tab im Excel-Ribbon gehen, auf die Dropdown-Liste "Format" in der Gruppe "Zellen" klicken und "Zellen formatieren" auswählen.  

4. Das Dialogfeld "Zellen formatieren" wird angezeigt. Hier können Sie verschiedene Formatierungsoptionen auswählen, die auf den ausgewählten Bereich angewendet werden sollen. Sie können beispielsweise den Schriftstil, die Schriftgröße, die Schriftfarbe, das Zahlenformat, die Rahmen, die Hintergrundfarbe usw. ändern. Erkunden Sie die verschiedenen Registerkarten im Dialogfeld, um auf verschiedene Formatierungsoptionen zuzugreifen.  

5. Nachdem Sie die gewünschten Formatierungsänderungen vorgenommen haben, klicken Sie auf die Schaltfläche "OK", um die Formatierung auf den ausgewählten Bereich anzuwenden.  

## **So formatieren Sie einen Bereich mit Node.js**  

Um einen Bereich mit Aspose.Cells for Node.js via C++ zu formatieren, können Sie die folgenden Methoden verwenden:  
1. [Range.applyStyle(style, flag)](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.setStyle(style)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  
3. [Range.setStyle(style)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  

## **Beispielcode**  
In diesem Beispiel erstellen wir eine Excel-Arbeitsmappe, fügen einige Beispieldaten hinzu, greifen auf das erste Arbeitsblatt zu und definieren zwei Bereiche ("A1:C3" und "A4:C5"). Dann erstellen wir neue Stile, setzen verschiedene Formatierungsoptionen (z.B. Schriftfarbe, Fett) und wenden den Stil auf den Bereich an. Schließlich speichern wir die Arbeitsmappe in eine neue Datei.  
<br>  
![todo:image_alt_text](format-range.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const ws = workbook.getWorksheets().get(0);

const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Access the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Define the range
const range = worksheet.getCells().createRange("A1:C3");

// Apply formatting to the range
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Red);
style.getFont().setIsBold(true);

const flag = new AsposeCells.StyleFlag();
flag.setFont(true);
range.applyStyle(style, flag);

// Define the range
const range2 = worksheet.getCells().createRange("A4:C5");

// Apply formatting to the range
const style2 = workbook.createStyle();
style2.getFont().setColor(AsposeCells.Color.Blue);
style2.getFont().setIsItalic(true);
range2.setStyle(style2);

// Save the modified workbook
workbook.save("output.xlsx");
```  

