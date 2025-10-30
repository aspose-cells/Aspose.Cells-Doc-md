---
title: Verbergen von überlagerten Inhalten mit CrossHideRight beim Speichern nach HTML mit Node.js via C++
linktitle: Verbergen von überlagertem Inhalt mit CrossHideRight beim Speichern als HTML
type: docs
weight: 100
url: /de/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---


## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei in HTML speichern, können Sie verschiedene Kreuztypen für Zelltexte angeben. Standardmäßig generiert Aspose.Cells HTML gemäß Microsoft Excel. Wenn Sie den Kreuztyp jedoch auf [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) ändern, verbirgt es alle Texte auf der rechten Seite der Zelle, die überlagert oder mit dem Zelltext überlappend sind.

## **Verstecken überlagerter Inhalte mit CrossHideRight beim Speichern in Html**

Der folgende Beispielcode lädt die [Beispieldatei Excel](64716894.xlsx) und speichert sie nach [Ausgabe-HTML](64716893.zip), nachdem [**HtmlSaveOptions.getHtmlCrossStringType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getHtmlCrossStringType--) auf [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) gesetzt wurde. Der Screenshot erklärt, wie [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) die Ausgabe-HTML vom Standard beeinflusst.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.CrossHideRight);

// Save to HTML with HtmlSaveOptions
workbook.save(path.join(dataDir, "outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html"), opts);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
