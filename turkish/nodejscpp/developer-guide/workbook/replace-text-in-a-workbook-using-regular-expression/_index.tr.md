---  
title: Node.js ve C++ kullanarak çalışma kitabındaki metni Regular Expression ile değiştirme  
linktitle: Düzenli İfade Kullanarak Bir Çalışma Kitabındaki Metni Değiştirme  
type: docs  
weight: 90  
url: /tr/nodejs-cpp/replace-text-in-a-workbook-using-regular-expression/  
description: Node.js ve C++ kullanarak çalışma kitabında metni düzenli ifade kullanarak değiştirme.  
---  

Aspose.Cells, çalışma kitabında metni düzenli ifadeyle değiştirme özelliği sunar. Bunun için API, [**ReplaceOptions**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions) sınıfının [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) özelliğini sağlar. [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) özelliğinin **true** olarak ayarlanması, aranacak anahtarın bir düzenli ifade olacağını gösterir.

Aşağıdaki kod parçacığı, [örnek Excel dosyası](101089318.xlsx) kullanılarak [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) özelliğinin kullanımını gösterir. Aşağıdaki kod parçası tarafından oluşturulan [çıktı dosyası](101089319.xlsx) referans olması için eklenmiştir.

## **Örnek Kod**

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
