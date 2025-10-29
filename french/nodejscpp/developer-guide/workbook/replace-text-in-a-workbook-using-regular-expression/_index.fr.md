---  
title: Remplacer du texte dans un classeur en utilisant une expression régulière avec Node.js via C++  
linktitle: Remplacer du texte dans un classeur en utilisant une expression régulière  
type: docs  
weight: 90  
url: /fr/nodejs-cpp/replace-text-in-a-workbook-using-regular-expression/  
description: Remplacer du texte dans un classeur en utilisant une expression régulière dans Node.js via C++.  
---  

Aspose.Cells propose la fonctionnalité de remplacer du texte dans un classeur en utilisant une expression régulière. Pour cela, l'API fournit la propriété [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) de la classe [**ReplaceOptions**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions). La définition de [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) sur **true** indique que la clé recherchée sera une expression régulière.

Le code ci-dessous démontre l'utilisation de la propriété [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) en utilisant le [fichier Excel d'exemple](101089318.xlsx). Le [fichier de sortie](101089319.xlsx) généré par ce code est joint pour référence.

## **Code d'exemple**

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
