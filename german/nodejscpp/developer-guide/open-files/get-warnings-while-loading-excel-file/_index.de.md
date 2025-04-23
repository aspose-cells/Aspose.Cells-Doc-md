---
title: Warnungen beim Laden einer Excel Datei mit Node.js über C++ erhalten
linktitle: Warnungen beim Laden einer Excel Datei erhalten
type: docs
weight: 110
url: /de/nodejs-cpp/get-warnings-while-loading-excel-file/
description: Erfahren Sie, wie Sie beim Laden einer Excel Datei mit Aspose.Cells for Node.js via C++ Warnungen erfassen können. Behandeln Sie beschädigte, aber ladbare Arbeitsmappen effektiv.
---

## **Mögliche Verwendungsszenarien**

Manchmal versucht der Benutzer, eine Arbeitsmappe zu laden, die irgendwie beschädigt, aber dennoch ladbar ist. In solchen Fällen gibt Aspose.Cells Warnungen beim Laden der Arbeitsmappe aus. Sie können diese Warnungen abfangen, indem Sie die Schnittstelle [**IWarningCallback**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback) implementieren und die Eigenschaft [**LoadOptions.getWarningCallback()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getWarningCallback--) setzen.

## **Warnungen beim Laden von Excel-Dateien erhalten**

Der folgende Beispielcode erklärt, wie man Warnungen beim Laden einer Excel-Datei erhält. Der Code lädt die [Beispiel-Excel-Datei](sampleDuplicateDefinedName.xlsx), bei der beim Laden eine [**DuplicateDefinedName**](https://reference.aspose.com/cells/nodejs-cpp/warningtype)-Warnung ausgelöst wird. Diese Warnung wird dann von der Methode [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback/#warning-warninginfo-) abgefangen, die die Warnmeldungen auf der Konsole ausgibt. Der Code speichert anschließend die Arbeitsmappe als [Ausgabe-Excel-Datei](outputDuplicateDefinedName.xlsx). Wenn Sie die Beispiel-Excel-Datei in Microsoft Excel öffnen, wird diese Warnung ebenfalls angezeigt, wie in diesem Screenshot. Bitte überprüfen Sie auch die Konsolenausgabe des unten angegebenen Codes für ein besseres Verständnis.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Beispielcode**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Implement IWarningCallback interface to catch warnings while loading workbook
class WarningCallback extends AsposeCells.IWarningCallback {
    warning(warningInfo) {
        if (warningInfo.getType() === AsposeCells.WarningType.DuplicateDefinedName) {
            console.log("Duplicate Defined Name Warning: " + warningInfo.getDescription());
        }
    }
}

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create load options and set the WarningCallback property 
// to catch warnings while loading workbook
const options = new AsposeCells.LoadOptions();
options.setWarningCallback(new WarningCallback());

// Load the source excel file
const book = new AsposeCells.Workbook(path.join(dataDir, "sampleDuplicateDefinedName.xlsx"), options);

// Save the workbook 
book.save(path.join(dataDir, "outputDuplicateDefinedName.xlsx"));
```

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Codes bei Ausführung mit der bereitgestellten [Beispiel-Excel-Datei](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
