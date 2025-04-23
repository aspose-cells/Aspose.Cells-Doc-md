---  
title: Kompatibilitätsprüfer in Excel mit Node.js über C++ deaktivieren  
linktitle: Kompatibilitätsprüfung in Excel deaktivieren  
type: docs  
weight: 170  
url: /de/nodejs-cpp/disable-compatibility-checker-in-excel/  
description: Erfahren Sie, wie Sie den Kompatibilitätsprüfer über die API Aspose.Cells for Node.js via C++ deaktivieren.  
keywords: Node.js Kompatibilitätsprüfer deaktivieren, Excel Kompatibilitätsprüfer in Node.js über C++, Kompatibilitätsprüfer in Arbeitsmappen deaktivieren.  
---  

## Kompatibilitätsprüfer in Excel-Tabellen in Node.js deaktivieren  

{{% alert color="primary" %}}  
Microsoft Excels Kompatibilitätsprüfer warnt, wenn das Speichern einer Datei in einem früheren Dateiformat zu Funktionsproblemen oder Qualitätsverlust führen könnte. Der Kompatibilitätsprüfer ist eine Funktion von Microsoft Office Excel 2007 und Microsoft Excel 2010.  

Wenn Sie eine Arbeitsmappe in einer früheren Version, Excel 97 bis Excel 2003, von Excel 2007 oder Excel 2010 speichern, durchsucht der Kompatibilitätsprüfer die Arbeitsmappe, um festzustellen, ob sie Funktionen enthält, die von der früheren Version nicht unterstützt werden. Um Ihnen bei Entscheidungen über den Umgang mit Kompatibilitätsproblemen zu helfen, zeigt der Kompatibilitätsprüfer Dialogfelder mit Optionen an. Er kann auch verwendet werden, um einen Bericht über Probleme in der Arbeitsmappe zu erstellen oder das Feature zu deaktivieren.  

Manchmal müssen Sie den Kompatibilitätsprüfer für eine bestimmte Tabelle deaktivieren. Mit den APIs von Aspose.Cells können Sie dies programmatisch tun, sodass Benutzer nicht durch das pop-up Fenster des Kompatibilitätsprüfers verwirrt oder frustriert werden, wenn sie die Datei in Microsoft Excel manuell erneut speichern.  
{{% /alert %}}  

## **Wie Sie den Kompatibilitätsprüfer in Microsoft Excel deaktivieren**  

Um den Kompatibilitätsprüfer in Microsoft Excel zu deaktivieren (z.B. Microsoft Excel 2007/2010):  

- (Excel 2007) Klicken Sie auf die Office-Schaltfläche, dann auf **Vorbereiten**, anschließend auf **Kompatibilitätsprüfung ausführen** und deaktivieren Sie die Option **Kompatibilität beim Speichern dieser Arbeitsmappe prüfen**.  
- (Excel 2010) Klicken Sie auf die Registerkarte **Datei**, dann auf **Info**, klicken Sie auf **Nach Problemen suchen**, klicken Sie auf **Kompatibilität prüfen** und deaktivieren Sie anschließend die Option **Kompatibilität prüfen, wenn Sie diese Arbeitsmappe speichern**.  

## **So deaktivieren Sie den Kompatibilitätsprüfer mithilfe von Aspose.Cells-APIs**  

Setzen Sie die Eigenschaft [**Workbook.getCheckCompatibility()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCheckCompatibility--) auf **false**, um den Kompatibilitätsprüfer von Microsoft Excel zu deaktivieren.  

### **Codebeispiele**  

Die folgenden Codebeispiele zeigen, wie man den Kompatibilitätsprüfer mit Aspose.Cells for Node.js via C++ deaktiviert.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Disable the compatibility checker
workbook.getSettings().setCheckCompatibility(false);

const outputFilePath = path.join(dataDir, "Output_BK_CompCheck.out.xlsx");
// Saving the Excel file
workbook.save(outputFilePath);
```  

