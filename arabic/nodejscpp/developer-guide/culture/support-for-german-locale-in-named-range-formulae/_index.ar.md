---  
title: دعم اللارك الألمانية في معادلات النطاق المُسمى باستخدام Node.js عبر C++  
linktitle: دعم اللغة الألمانية في صيغ النطاقات المسماة  
type: docs  
weight: 60  
url: /ar/nodejs-cpp/support-for-german-locale-in-named-range-formulae/  
description: تعلم كيفية دعم اللغة الألمانية في معادلات النطاق المُسمى باستخدام Aspose.Cells for Node.js via C++.  
---  

 تُكتب المعادلات الإنجليزية في المنطقة المسماة. يمكن فتح ملف Excel هذا في بيئة مُهيأة للغة الألمانية، ومع ذلك، ستُترجم المعادلة الإنجليزية إلى اللغة الألمانية. يوضح المثال التالي هذه الميزة، لكنه يتطلب تثبيت Excel باللغة الألمانية وتعيين اللغة والنظام على حد سواء إلى الألمانية.  

يمكن تنزيل ملف عينة لاختبار هذه الميزة من الرابط التالي:  

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

