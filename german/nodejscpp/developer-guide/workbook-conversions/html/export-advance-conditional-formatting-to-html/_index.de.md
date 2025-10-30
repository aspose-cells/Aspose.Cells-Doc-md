---  
title: Exportieren von DataBar, ColorScale und IconSet Bedingte Formatierungen beim Excel zu HTML Konvertieren mit Node.js über C++  
linktitle: Datenleiste, Farbskala und IconSet Bedingte Formatierung beim Konvertieren von Excel in HTML exportieren  
type: docs  
weight: 30  
url: /de/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/  
---  

{{% alert color="primary" %}} 

Sie können DataBar-, ColorScale- und IconSet-bedingte Formatierungen beim Konvertieren Ihrer Excel-Datei in HTML exportieren. Diese Funktion wird von Microsoft Excel nur teilweise unterstützt, während Aspose.Cells for Node.js via C++ sie vollständig unterstützt.

{{% /alert %}}  

## **Datenleiste, Farbskala und IconSet-Bedingte Formatierung beim Konvertieren von Excel in HTML exportieren**  
Der folgende Screenshot zeigt die [Beispiel-Excel-Datei](5115558.xlsx) mit DataBar, ColorScale und IconSet Bedingter Formatierung. Sie können die [Beispiel-Excel-Datei](5115558.xlsx) über den angegebenen Link herunterladen.  

![todo:image_alt_text](conversion_1.png)  

Der folgende Screenshot zeigt die Aspose.Cells Ausgabe-HTML-Datei mit DataBar, ColorScale und IconSet Bedingter Formatierung. Wie Sie sehen können, sieht es genau wie die [Beispiel-Excel-Datei](5115558.xlsx) aus.  

![todo:image_alt_text](conversion_2.png)  

### **Beispielcode**  
Der folgende Beispielcode konvertiert eine Beispiel-Excel-Datei in HTML, was nur eine normale [Excel-zu-HTML-Konvertierung](/cells/de/nodejs-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml) ist.  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
