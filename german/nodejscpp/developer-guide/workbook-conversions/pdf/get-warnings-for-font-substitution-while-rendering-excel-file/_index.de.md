---  
title: Warnungen für Schriftartensubstitution beim Rendern von Excel Dateien mit Node.js via C++ erhalten  
linktitle: Warnungen für Schriftarten ersetzen beim Rendern von Excel Dateien erhalten  
type: docs  
weight: 230  
url: /de/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/  
description: Erfahren Sie, wie Sie Warnungen für Schriftartensubstitution beim Rendern von Excel Dateien zu PDF mit Aspose.Cells for Node.js via C++ erhalten.  
---  

{{% alert color="primary" %}}  

Manchmal ersetzt Aspose.Cells beim Rendern einer Microsoft Excel-Datei in PDF Schriftarten. Aspose.Cells bietet eine Funktion, die Entwickler darüber informiert, welche bestimmte Schriftart durch eine Warnung ersetzt wurde. Dies ist eine nützliche Funktion, die Ihnen helfen kann zu erkennen, warum ein von Aspose.Cells gerendertes PDF anders aussieht als die ursprüngliche Microsoft Excel-Datei, damit Sie geeignete Maßnahmen ergreifen können. Zum Beispiel, das Installieren der fehlenden Schriftarten, damit die Rendierungsergebnisse gleich aussehen.

{{% /alert %}}  

Um Warnungen für Schriftartensubstitution beim Rendern von Excel-Dateien zu PDF zu erhalten, implementieren Sie die IWarningCallback Schnittstelle und setzen Sie die PdfSaveOptions.warningCallback Eigenschaft mit Ihrer implementierten Schnittstelle.

Der folgende Screenshot zeigt eine Quell-Excel-Datei, die wir im folgenden Code verwenden werden. Sie enthält einige Texte in den Zellen A6 und A7 in Schriftarten, die von Microsoft Excel nicht korrekt gerendert werden.

|**Nicht alle Schriftarten werden korrekt gerendert**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|  
Aspose.Cells wird die Schriftarten in den Zellen A6 und A7 durch geeignete Schriftarten ersetzen, wie unten gezeigt.

|**Ersetzte Schriftarten**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|  
## **Quelldatei herunterladen und PDF ausgeben**  
Sie können die Quelldatei und das PDF-Output von den folgenden Links herunterladen

- [source.xlsx](5112611.xlsx)  
- [output.pdf](5112616.pdf)  
## **Code**  
Der folgende Code implementiert IWarningCallback und setzt die PdfSaveOptions.warningCallback Eigenschaft auf die implementierte Schnittstelle. Jetzt wird bei jeder SchriftartSubstitution in einer Zelle eine Warnung von Aspose.Cells ausgelöst, innerhalb der WarningCallback.Warning() Methode.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class GetWarningsForFontSubstitution {
static warning(info) {
if (info.getType() === AsposeCells.WarningType.FontSubstitution) {
console.log("WARNING INFO: " + info.getDescription());
}
}

static run() {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setWarningCallback(GetWarningsForFontSubstitution);
const outputFilePath = path.join(dataDir, "output_out.pdf");
workbook.save(outputFilePath, options);
}
}
```  
## **Ergebnis**  
Nachdem die Quell-Excel-Datei in PDF konvertiert wurde, werden die Warnungen wie folgt in die Debug-Konsole ausgegeben:

{{< highlight java >}}  

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].  

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].  

{{< /highlight >}}  

{{% alert color="primary" %}}  

Wenn Ihre Tabelle Formeln enthält, ist es am besten, die Methode Workbook.calculateFormula kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
