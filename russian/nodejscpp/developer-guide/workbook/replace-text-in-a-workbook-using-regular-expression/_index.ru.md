---  
title: Замена текста в рабочей книге с помощью регулярных выражений через Node.js с использованием C++  
linktitle: Замена текста в книге с использованием регулярных выражений  
type: docs  
weight: 90  
url: /ru/nodejs-cpp/replace-text-in-a-workbook-using-regular-expression/  
description: Замена текста в рабочей книге с помощью регулярного выражения в Node.js через C++.  
---  

Aspose.Cells предоставляет возможность замена текста в рабочей книге с использованием регулярных выражений. Для этого API обеспечивает свойство [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) класса [**ReplaceOptions**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions). Установка [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) в значение **true** означает, что искомый ключ будет регулярным выражением.

Следующий фрагмент кода демонстрирует использование свойства [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) на примере [пример файла Excel](101089318.xlsx). [Выходной файл](101089319.xlsx), созданный этим кодом, прикреплен для ознакомления.

## **Образец кода**

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
