---  
title: Sostituisci testo in un workbook usando espressioni regolari con Node.js tramite C++  
linktitle: Sostituire il testo in un libro di lavoro utilizzando le espressioni regolari  
type: docs  
weight: 90  
url: /it/nodejs-cpp/replace-text-in-a-workbook-using-regular-expression/  
description: Sostituisci testo in un workbook usando espressioni regolari in Node.js tramite C++.  
---  

Aspose.Cells fornisce la funzionalità di sostituire testo in un workbook usando un’espressione regolare. Per questo, l’API fornisce la proprietà [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) della classe [**ReplaceOptions**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions). Impostare [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) su **true** indica che la chiave cercata sarà un’espressione regolare.

 Il seguente frammento di codice dimostra l'uso della proprietà {0} usando il {2} esempio di file Excel. Il {3} generato dal frammento di codice di seguito è allegato come riferimento.

## **Codice di Esempio**

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

{{< app/cells/assistant language="nodejs-cpp" >}}
