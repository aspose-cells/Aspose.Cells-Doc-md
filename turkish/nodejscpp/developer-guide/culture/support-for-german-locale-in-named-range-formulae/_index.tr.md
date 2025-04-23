---  
title: Node.js ve C++ kullanarak Almanca Bölge Desteği ile Adlandırılmış Aralık Formülleri  
linktitle: Adlandırılmış Aralık Formüllerinde Alman Locale Desteği  
type: docs  
weight: 60  
url: /tr/nodejs-cpp/support-for-german-locale-in-named-range-formulae/  
description: Aspose.Cells for Node.js via C++ kullanarak adlandırılmış aralık formüllerinde Almanca bölgesini nasıl destekleyeceğinizi öğrenin.  
---  

İngilizce formüller adlandırılmış bölgede yazılır. Bu Excel dosyasını, sistem Almanca bölgesine yapılandırılmış bir ortamda açabilirsiniz, ancak formüller Almancaya çevrilecektir. Aşağıdaki örnek bu özelliği gösterir; ancak, Excel'in Almanca kurulu olması ve sistem bölgesinin de Almanca olması gerekir.  

Bu özelliği test etmek için örnek dosya aşağıdaki bağlantıdan indirilebilir:  

[sampleNamedRangeTest.xlsm](73990165.xlsm)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
const fs = require("fs");

const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNamedRangeTest.xlsm");
const outputFilePath = path.join(dataDir, "sampleOutputNamedRangeTest.xlsm");

const wb = new AsposeCells.Workbook();
wb.save(sourceFilePath);

const name = "HasFormula";
const value = "=GET.CELL(48, INDIRECT(\"ZS\",FALSE))";

const wbSource = new AsposeCells.Workbook(sourceFilePath);
const wsCol = wbSource.getWorksheets();

const nameIndex = wsCol.getNames().add(name);
const namedRange = wsCol.getNames().get(nameIndex);
namedRange.setRefersTo(value);

wbSource.save(outputFilePath);
```  

