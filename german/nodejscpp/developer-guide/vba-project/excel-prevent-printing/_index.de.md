---  
title: So verhindern Sie, dass Benutzer Excel Dateien mit Node.js über C++ drucken  
linktitle: Wie verhindert man, dass Benutzer eine Excel Datei drucken  
type: docs  
weight: 600  
url: /de/nodejs-cpp/how-to-prevent-printing-excel/  
description: Erfahren Sie, wie Sie verhindern, dass Benutzer Excel Dateien mit Aspose.Cells for Node.js via C++ drucken.  
keywords: Excel Druck, Excel Druck verhindern, wie man das Drucken von Excel verhindert, Excel Druck verhindern, das Drucken des gesamten Arbeitsmappens mit VBA verhindern  
---  

## **Mögliche Verwendungsszenarien**  
In unserer täglichen Arbeit können wichtige Informationen in der Excel-Datei enthalten sein; um die Verbreitung interner Daten zu verhindern, erlaubt die Firma keinen Druck. Dieses Dokument zeigt, wie Sie andere vom Drucken von Excel-Dateien abhalten können.  

## **Wie man das Drucken einer Datei in MS-Excel verhindert**  
Sie können den folgenden VBA-Code anwenden, um Ihre spezifische Datei vor dem Drucken zu schützen.  
1. Öffnen Sie Ihre Arbeitsmappe, die Sie anderen nicht erlauben möchten zu drucken.  
1. Wählen Sie die Registerkarte **Entwicklertools** im Excel-Ribbon und klicken Sie auf die Schaltfläche **Code anzeigen** im Abschnitt **Steuerelemente**. Alternativ können Sie die Tasten ALT + F11 drücken, um das Microsoft Visual Basic for Applications Fenster zu öffnen.  
<br>  
<img src="1.png" width=70% />  
1. Und dann im linken Projekt-Explorer doppelklicken Sie auf ThisWorkbook, um das Modul zu öffnen, und fügen Sie einige VBA-Codes hinzu.  
<br>  
<img src="2.png" width=70% />  
1. Speichern und schließen Sie dieses Codefenster, kehren Sie zum Arbeitsbuch zurück, und wenn Sie die Beispiel-Datei drucken, wird dies nicht erlaubt, und Sie erhalten folgende Warnmeldung:  
<br>  
<img src="3.png" width=70% />  

## **So verhindern Sie, dass Benutzer Excel-Dateien mit Aspose.Cells for Node.js via C++ drucken**  

Das folgende Beispiel zeigt, wie man das Drucken einer Excel-Datei durch Benutzer verhindert:  

1. Laden Sie die [Beispieldatei](sample.xlsx).  
1. Holen Sie sich das VbaModuleCollection-Objekt aus der VbaProject-Eigenschaft der Arbeitsmappe.  
1. Holen Sie sich das VbaModule-Objekt über den Namen "ThisWorkbook".  
1. Setzen Sie die Eigenschaften des VbaModule-Codes.  
1. Speichern Sie die Beispieldatei im [xlsm-Format](out.xlsm).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");

// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);
const modules = wb.getVbaProject().getModules();
modules.get("ThisWorkbook").setCodes("Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n");

wb.save("out.xlsm");
```  

