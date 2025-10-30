---  
title: Seitenlayout und Druckoptionen mit Node.js via C++  
linktitle: Seiteneinrichtung und Druckoptionen  
type: docs  
weight: 60  
url: /de/nodejs-cpp/page-setup-and-printing-options/  
---  

{{% alert color="primary" %}}  
Manchmal müssen Entwickler die Seiteneinrichtung und die Druckeinstellungen konfigurieren, um den Druckprozess zu steuern. Die Seiteneinrichtung und Druckeinstellungen bieten verschiedene Optionen und werden von Aspose.Cells vollständig unterstützt.  

Dieser Artikel zeigt, wie man eine Konsolenanwendung in Node.js via C++ erstellt und mit wenigen Zeilen Code Seitenlayout- und Druckoptionen in einem Arbeitsblatt mit der Aspose.Cells API anwendet.  
{{% /alert %}}  

## **Arbeiten mit Seiten- und Druckeinstellungen**  

Für dieses Beispiel haben wir ein Arbeitsbuch in Microsoft Excel erstellt und Aspose.Cells verwendet, um Seitenlayout- und Druckoptionen festzulegen.  

### **Verwenden von Aspose.Cells zum Festlegen von Seiteneinrichtungsoptionen**  

Erstellen Sie zuerst ein einfaches Arbeitsblatt in Microsoft Excel. Wenden Sie dann Seiteneinrichtungsoptionen darauf an. Das Ausführen des Codes ändert die Seiteneinrichtungsoptionen, wie im Screenshot unten dargestellt.  

|**Ausgabedatei.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|  

1. Erstellen Sie ein Arbeitsblatt mit einigen Daten in Microsoft Excel:  
   1. Öffnen Sie eine neue Arbeitsmappe in Microsoft Excel.  
   1. Fügen Sie einige Daten hinzu.  
1. Legen Sie Seiteneinrichtungsoptionen fest:  
   Wenden Sie die Seiteneinrichtungsoptionen auf die Datei an. Unten ist ein Screenshot der Standardoptionen vor der Anwendung der neuen Optionen zu sehen.  

|**Standardseiteneinrichtungsoptionen.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|  

1. Laden Sie Aspose.Cells herunter und installieren Sie es:  
   1. [Herunterladen](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++.  
   1. Installieren Sie es auf Ihrem Entwicklungscomputer.  
      Alle Aspose-Komponenten arbeiten im Evaluierungsmodus, wenn sie installiert sind. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.  
1. Ein Projekt erstellen:  
   1. Starten Sie Ihre Node.js-Umgebung.  
   1. Erstellen Sie eine neue Konsolenanwendung.  
      Dieses Beispiel zeigt eine Node.js-Konsolenanwendung, aber Sie können auch die C++-Bindungen verwenden.  
1. Fügen Sie Verweise hinzu:  
   1. Dieses Beispiel verwendet Aspose.Cells, fügen Sie daher einen Verweis auf diese Komponente im Projekt hinzu. Zum Beispiel:  
      …\Program Files\Aspose\Aspose.Cells\Bin\Node.js-Cpp\Aspose.Cells.node  
1. Schreiben Sie die Anwendung, die die API aufruft:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "CustomerReport.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the orientation to Portrait
worksheet.getPageSetup().setOrientation(AsposeCells.PageOrientationType.Portrait);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Setting the paper size to A4
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Setting the print quality of the worksheet to 1200 dpi
worksheet.getPageSetup().setPrintQuality(1200);

// Setting the first page number of the worksheet pages
worksheet.getPageSetup().setFirstPageNumber(2);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_out.xlsx"));
```  

### **Druckoptionen festlegen**  

Die Seiteneinrichtungseinstellungen bieten auch mehrere Druckoptionen (auch Blattoptionen genannt), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden. Sie ermöglichen Benutzern:  

- Eine bestimmte Druckbereich eines Arbeitsblatts auswählen.
- Titel drucken.
- Gitternetzlinien drucken.
- Zeilen-/Spaltenüberschriften drucken.
- Entwurfsqualität erreichen.
- Kommentare drucken.
- Zellenfehler drucken.
- Seiteneinteilung definieren.  

Das folgende Beispiel wendet Druckoptionen auf die Datei an, die im obigen Beispiel erstellt wurde (PageSetup.xls). Der nachfolgende Screenshot zeigt die Standard-Druckoptionen, bevor neue Optionen angewendet werden.  

|**Eingabedokument**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|  
Das Ausführen des Codes ändert die Druckoptionen.  

|**Ausgabedatei**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageSetup.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

const pageSetup = worksheet.getPageSetup();

// Specifying the cells range (from A1 cell to E30 cell) of the print area
pageSetup.setPrintArea("A1:E30");

// Defining column numbers A & E as title columns
pageSetup.setPrintTitleColumns("$A:$E");

// Defining row numbers 1 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_Print_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
