---  
title: Byt ut text i en arbetsbok med reguljära uttryck med Node.js via C++  
linktitle: Byt ut text i en arbetsbok med hjälp av reguljärt uttryck  
type: docs  
weight: 90  
url: /sv/nodejs-cpp/replace-text-in-a-workbook-using-regular-expression/  
description: Byt ut text i en arbetsbok med reguljära uttryck i Node.js via C++.  
---  

Aspose.Cells erbjuder funktionen att byta ut text i en arbetsbok med hjälp av ett reguljärt uttryck. För detta tillhandahåller API:t [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--)-egenskapen i [**ReplaceOptions**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions)-klassen. Att ställa in [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) till **true** indikerar att den sökta nyckeln kommer att vara ett reguljärt uttryck.

Följande kodexempel visar användningen av [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--)-egenskapen med hjälp av [provfilen](101089318.xlsx). Den genererade [utdatafilen](101089319.xlsx) från kodexemplet bifogas för referens.

## **Exempelkod**

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

