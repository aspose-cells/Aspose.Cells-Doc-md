---  
title: إضافة أجزاء XML مخصصة وتحديدها بواسطة المعرف باستخدام Node.js عبر C++  
linktitle: إضافة أجزاء XML مخصصة وتحديدها حسب الهوية  
type: docs  
weight: 70  
url: /ar/nodejs-cpp/add-custom-xml-parts-and-select-them-by-id/  
description: تعلّم كيفية إضافة أجزاء XML مخصصة إلى مستندات إكسل وتحديدها بواسطة المعرف باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

أجزاء XML المخصصة هي بيانات XML المخزنة داخل مستندات Microsoft Excel وتستخدم بواسطة التطبيقات التي تتعامل معها. لا توجد طريقة مباشرة لإضافتها باستخدام واجهة مستخدم Microsoft Excel في الوقت الحالي. ومع ذلك، يمكنك إضافتها برمجياً بطرق متنوعة، على سبيل المثال، باستخدام VSTO، باستخدام Aspose.Cells، وغيرها. يرجى استخدام [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) إذا كنت تريد إضافة جزء XML مخصص باستخدام API الخاص بـ Aspose.Cells. يمكنك أيضًا ضبط معرفه باستخدام الخاصية [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--). بالمثل، إذا أردت تحديد جزء XML مخصص بواسطة المعرف، يمكنك استخدام طريقة [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--).  

## **إضافة أجزاء XML مخصصة وتحديدها حسب الهوية**  

يقوم الرمز النموذجي التالي أولاً بإضافة أربعة أجزاء XML مخصصة باستخدام طريقة [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--). ثم يعين معرفاتها باستخدام الخاصية [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--). وأخيرًا، يحدد أو يختار أحد أجزاء XML المخصصة المضافة باستخدام طريقة [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--). يرجى أيضًا مراجعة مخرجات وحدة التحكم للرمز أدناه للمرجعية.  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Some data in the form of byte array.
// Please use correct XML and Schema instead.
const btsData = new Uint8Array([1, 2, 3]);
const btsSchema = new Uint8Array([1, 2, 3]);

// Create four custom xml parts.
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);

// Assign ids to custom xml parts.
wb.getCustomXmlParts().get(0).setID("Fruit");
wb.getCustomXmlParts().get(1).setID("Color");
wb.getCustomXmlParts().get(2).setID("Sport");
wb.getCustomXmlParts().get(3).setID("Shape");

// Specify search custom xml part id.
let srchID = "Fruit";
srchID = "Color";
srchID = "Sport";

// Search custom xml part by the search id.
const cxp = wb.getCustomXmlParts().selectByID(srchID);

// Print the found or not found message on console.
if (cxp.isNull()) {
console.log(`Not Found: CustomXmlPart ID ${srchID}`);
} else {
console.log(`Found: CustomXmlPart ID ${srchID}`);
}

console.log("AddCustomXMLPartsAndSelectThemByID executed successfully.");
```  

## **مخرجات الوحدة**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  

