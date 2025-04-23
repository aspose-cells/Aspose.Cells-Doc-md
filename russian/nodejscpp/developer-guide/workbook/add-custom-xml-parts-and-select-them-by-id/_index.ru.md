---  
title: Добавление пользовательских частей XML и их выбор по ID с помощью Node.js через C++  
linktitle: Добавление пользовательских XML частей и выбор их по идентификатору  
type: docs  
weight: 70  
url: /ru/nodejs-cpp/add-custom-xml-parts-and-select-them-by-id/  
description: Узнайте, как добавлять пользовательские части XML в документы Excel и выбирать их по ID с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Пользовательские части XML — это XML-данные, которые хранятся внутри документов Microsoft Excel и используются приложениями, работающими с ними. В настоящее время нет прямого способа их добавления через интерфейс Microsoft Excel. Однако их можно добавлять программно различными способами, например, с помощью VSTO, Aspose.Cells и др. Используйте метод [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) для добавления пользовательского XML-отрывка с помощью API Aspose.Cells. Также вы можете установить его ID с помощью свойства [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--). Аналогично, чтобы выбрать пользовательский XML-отрывок по ID, используйте метод [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--).  

## **Добавление пользовательских XML-частей и выбор их по идентификатору**  

Следующий пример кода сначала добавляет четыре пользовательских XML-отрывка с помощью метода [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--). Затем он устанавливает их ID с помощью свойства [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--). В конце он находит или выбирает один из добавленных пользовательских XML-отрывков с помощью метода [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--). Также посмотрите вывод консоли приведенного кода для справки.  

## **Образец кода**  

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

## **Вывод в консоль**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  

