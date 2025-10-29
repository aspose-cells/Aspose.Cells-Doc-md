---  
title: تحديث تلقائي لكائن OLE عبر Microsoft Excel باستخدام Aspose.Cells for Node.js via C++  
linktitle: تحديث كائن Ole تلقائيًا عبر Microsoft Excel باستخدام Aspose.Cells  
type: docs  
weight: 270  
url: /ar/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/  
description: تعلم كيفية تحديث كائنات OLE تلقائيًا في إكسل باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
يوفر Aspose.Cells خاصية [**OleObject.getAutoLoad()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getAutoLoad--) لتحديث كائن OLE عند فتح ملف الإكسل في Microsoft Excel. نتيجة لهذه الخاصية، سيعرض الكائن OLE الصورة الصحيحة المُولدة بواسطة Microsoft Excel.  
{{% /alert %}}  

يقوم الكود العينة التالي بتحميل [ملف الإكسل العينة](5115231.xlsx) الذي يحتوي على صورة OLE غير حقيقية. الكائن OLE هو في الواقع مستند Microsoft Word ولكن ملف الإكسل العينة يعرض صورة الحيوان بدلاً من صورة Microsoft Word. ولكن إذا فتحت [ملف الإكسل الناتج](5115225.xlsx)، سترى Microsoft Excel عرض الصورة الصحيحة لـ OLE.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from your sample excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_oleobject.xlsx"));

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Set auto load property of first ole object to true
sheet.getOleObjects().get(0).setAutoLoad(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "RefreshOLEObjects_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
