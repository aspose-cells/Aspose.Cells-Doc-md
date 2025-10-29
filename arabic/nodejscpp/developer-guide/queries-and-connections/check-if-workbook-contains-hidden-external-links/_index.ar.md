---  
title: التحقق مما إذا كانت مصنف العمل يحتوي على روابط خارجية مخفية باستخدام Node.js عبر C++  
linktitle: التحقق مما إذا كانت مصفوفة العمل تحتوي على روابط خارجية مخفية  
type: docs  
weight: 230  
url: /ar/nodejs-cpp/check-if-workbook-contains-hidden-external-links/  
description: تعلم كيفية التحقق مما إذا كان مصنف العمل يحتوي على روابط خارجية مخفية باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  
في بعض الأحيان، يحتوي مصنف العمل على روابط خارجية مخفية لا يمكن عرضها في Microsoft Excel. يسترجع Aspose.Cells جميع الروابط الخارجية سواء كانت مرئية أو مخفية. ومع ذلك، يمكنك التحقق من خاصية [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--) للتحقق مما إذا كان الرابط الخارجي مرئيًا أم لا.

## **التحقق مما إذا كانت مصفوفة العمل تحتوي على روابط خارجية مخفية**  
يحمّل المثال التالي ملف Excel المصدر الذي يحتوي على روابط خارجية مخفية. لا يمكن عرض هذه الروابط في Microsoft Excel لكنها موجودة داخل المصنف. بعد طباعة خاصية [ExternalLink.getDataSource()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#getDataSource--) و [ExternalLink.isReferred()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isReferred--)، يتم طباعة خاصية [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--). في المخرجات أدناه، ترى أن جميع روابطه الخارجية غير مرئية.

### **الكود المثالي**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the external link collection of the workbook
const links = workbook.getWorksheets().getExternalLinks();

// Print all the external links and check their IsVisible property
for (let i = 0; i < links.getCount(); i++) {
console.log("Data Source: " + links.get(i).getDataSource());
console.log("Is Referred: " + links.get(i).getIsReferred());
console.log("Is Visible: " + links.get(i).getIsVisible());
console.log();
}
```  

### **مخرجات الوحدة**  
إليك مخرجات وحدة التحكم للكود العيني أعلاه عند تنفيذه مع [ملف Excel العيني المعطى](5115413.xlsx).

{{< highlight java >}}  
 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls  

Is Referred: True  

Is Visible: False  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
