---  
title: ملحقات الويب  إضافات Office باستخدام Node.js عبر C++  
linktitle: الإضافات الإلكترونية للويب  إضافات Office  
type: docs  
weight: 130  
url: /ar/nodejs-cpp/web-extensions-office-add-ins/  
---  

ملحقات الويب توسع تطبيقات Office وتتفاعل مع محتوى مستندات Office. تضيف ملحقات الويب وظائف إضافية إلى عميل Office لتحسين تجربة المستخدم وزيادة الإنتاجية.

توفر Aspose.Cells أيضًا القدرة على العمل مع ملحقات الويب.

## **إضافة ملحق ويب**

 يمكنك إضافة إضافات الويب (إضافات Office) في إكسل بالنقر على علامة التبويب **إدراج** ثم النقر على رابط **المتجر** / **الحصول على الإضافات**. في مربع الإضافات، تصفح الإضافة التي تريدها وأضفها.

توفر Aspose.Cells أيضًا ميزة إضافة إضافات الويب باستخدام فئتي [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) و [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane). يوضح نموذج الكود التالي استخدام فئتي [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) و [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane) لإضافة إضافة ويب إلى ملف إكسل. يرجى مراجعة ملف إكسل الناتج [ملف الإكسل الناتج](89849869.xlsx) باستخدام الكود للمراجعة.

### **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const outDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook();

const extensions = workbook.getWorksheets().getWebExtensions();
const taskPanes = workbook.getWorksheets().getWebExtensionTaskPanes();

const extensionIndex = extensions.add();
const taskPaneIndex = taskPanes.add();

const extension = extensions.get(extensionIndex);
extension.getReference().setId("wa104379955");
extension.getReference().setStoreName("en-US");
extension.getReference().setStoreType(AsposeCells.WebExtensionStoreType.OMEX);

const taskPane = taskPanes.get(taskPaneIndex);
taskPane.setIsVisible(true);
taskPane.setDockState("right");
taskPane.setWebExtension(extension);

workbook.save(path.join(outDir, "AddWebExtension_Out.xlsx"));
```

## **الوصول إلى معلومات ملحق الويب**

توفر Aspose.Cells القدرة على الوصول إلى معلومات إضافات الويب في ملف إكسل. يوضح مثال الكود التالي كيف يمكن الوصول إلى معلومات الإضافة عن طريق تحميل ملف إكسل العينة [ملف إكسل عينة](89849870.xlsx). يرجى الاطلاع على مخرجات وحدة التحكم التي تم إنشاؤها بواسطة الكود للمراجعة.

### **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load sample Excel file
const filePath = path.join(sourceDir, "WebExtensionsSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const taskPanes = workbook.getWorksheets().getWebExtensionTaskPanes();

for (let i = 0; i < taskPanes.getCount(); i++) {
const taskPane = taskPanes.get(i);
console.log("Width: " + taskPane.getWidth());
console.log("IsVisible: " + taskPane.isVisible());
console.log("IsLocked: " + taskPane.isLocked());
console.log("DockState: " + taskPane.getDockState());
console.log("StoreName: " + taskPane.getWebExtension().getReference().getStoreName());
console.log("StoreType: " + taskPane.getWebExtension().getReference().getStoreType());
console.log("WebExtension.Id: " + taskPane.getWebExtension().getId());
}
```

### **مخرجات الوحدة**

{{< highlight javascript >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
