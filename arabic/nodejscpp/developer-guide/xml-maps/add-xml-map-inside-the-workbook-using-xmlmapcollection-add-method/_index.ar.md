---  
title: أضف خريطة XML داخل دفتر العمل باستخدام طريقة XmlMapCollection.Add مع node.js عبر C++  
linktitle: إضافة خريطة XML داخل الدفتر باستخدام طريقة XmlMapCollection.Add  
type: docs  
weight: 10  
url: /ar/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/  
description: تعلم كيفية إضافة خريطة XML داخل دفتر العمل باستخدام طريقة XmlMapCollection.Add مع Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

توفر Aspose.Cells الطريقة [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) التي يمكنك استخدامها لاستيراد خريطة XML داخل مصنف العمل.  

## **إضافة خريطة XML داخل الكتيب باستخدام طريقة XmlMapCollection.Add**  

يقوم الكود العيني بإضافة خريطة XML داخل مصنف العمل باستخدام الطريقة [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) ويحفظه كملف إكسل [output excel file](5115434.xlsx). تظهر اللقطة الشاشية خريطة XML التي تم استيرادها من [sample.xml](5115433.xml) داخل ملف إكسل الناتج.  

![add-xml-map](add-xml-map.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Add xml map found inside the sample.xml inside the workbook
wb.getWorksheets().getXmlMaps().add(path.join(dataDir, "sample.xml"));

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```  

