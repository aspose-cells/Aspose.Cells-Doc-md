---  
title: Texte in einer Arbeitsmappe mithilfe von regulären Ausdrücken mit Node.js über C++ ersetzen  
linktitle: Ersetzen von Text in einer Arbeitsmappe mittels regulären Ausdrücken  
type: docs  
weight: 90  
url: /de/nodejs-cpp/replace-text-in-a-workbook-using-regular-expression/  
description: Texte in einer Arbeitsmappe mithilfe von regulären Ausdrücken in Node.js über C++ ersetzen.  
---  

Aspose.Cells bietet die Funktion, Text in einer Arbeitsmappe mithilfe eines regulären Ausdrucks zu ersetzen. Dafür stellt die API die [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) Eigenschaft der [**ReplaceOptions**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions) Klasse bereit. Wenn Sie [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) auf **true** setzen, bedeutet dies, dass der gesuchte Schlüssel ein regulärer Ausdruck ist.

Das folgende Codebeispiel demonstriert die Verwendung der [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--)-Eigenschaft anhand der [Beispieldatei](101089318.xlsx). Die [Ausgabedatei](101089319.xlsx), die durch das folgende Codebeispiel generiert wurde, ist zur Referenz beigefügt.

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "SampleRegexReplace.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const replace = new AsposeCells.ReplaceOptions();
replace.setCaseSensitive(false);
replace.setMatchEntireCellContents(false);
// Set to true to indicate that the searched key is regex
replace.setRegexKey(true);

workbook.replace("\\bKIM\\b", "^^^TIM^^^", replace);
workbook.save(path.join(outputDir, "RegexReplace_out.xlsx"));
```  

