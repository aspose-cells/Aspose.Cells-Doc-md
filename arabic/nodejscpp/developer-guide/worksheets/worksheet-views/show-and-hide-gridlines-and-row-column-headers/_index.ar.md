---  
title: عرض وإخفاء خطوط الشبكة وعناوين الصفوف والأعمدة باستخدام Node.js عبر C++  
linktitle: إظهار وإخفاء خطوط الشبكة ورؤوس الصف والعمود  
type: docs  
weight: 30  
url: /ar/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/  
description: يقدم هذا المقال رمزًا نموذجيًا لاستخدام واجهة برمجة التطبيقات Node.js عبر C++ لإخفاء أو إظهار خطوط الشبكة، والعناوين للأعمدة والصفوف في ورقة عمل Excel برمجياً.  
---  

{{% alert color="primary" %}}  
يدعم Aspose.Cells إخفاء وعرض خطوط الشبكة لورقة العمل التي يكون ظهورها افتراضيًا. كما يوفر التحكم في رؤوس الصف والعمود لورقة العمل.  
{{% /alert %}}  

## **إظهار وإخفاء خطوط الشبكة**  

تحتوي جميع ورقات العمل في Excel على خطوط شبكية افتراضيًا. تساعد في تحديد الخلايا بحيث يكون من السهل إدخال البيانات في خلايا معينة. تمكِّن الخطوط الشبكية من عرض ورقة العمل كمجموعة من الخلايا، حيث يمكن تحديد كل خلية بسهولة.  

### **التحكم في رؤية خطوط الشبكة**  

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، والتي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) تتيح للمطورين الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. للتحكم في ظهور خطوط الشبكة، استخدم الخاصية [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--). [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) هي خاصية بوليانية، مما يعني أنها يمكن أن تخزن فقط قيمة **true** أو **false**.  

#### **جعل خطوط الشبكة مرئية**  

اجعل خطوط الشبكة مرئية عن طريق ضبط الخاصية [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) على **true**.  

#### **إخفاء خطوط الشبكة**  

اخفِ خطوط الشبكة عن طريق ضبط الخاصية [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) على **false**.  

يوجد مثال كامل أدناه يوضح استخدام الخاصية [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) عن طريق فتح ملف Excel (book1.xls)، إخفاء خطوط الشبكة على ورقة العمل الأولى، وحفظ الملف المعدل باسم output.xls.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileData = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file data
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the grid lines of the first worksheet of the Excel file
worksheet.setIsGridlinesVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **إظهار وإخفاء رؤوس الصف والعمود**  

جميع ورقات العمل في ملف Excel مكونة من خلايا مرتبة في صفوف وأعمدة. جميع الصفوف والأعمدة لها قيم فريدة يتم استخدامها لتحديدها وتحديد الخلايا الفردية. على سبيل المثال، يتم ترقيم الصفوف - 1، 2، 3، 4، الخ. - وترتيب الأعمدة ترتيبها أبجديًا - أ، ب، ج، د، الخ. تظهر قيم الصف والعمود في الرؤوس. باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية هذه الرؤوس للصف والعمود.  

### **التحكم في رؤية ورقات العمل**  

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) تسمح للمطورين بالوصول إلى كل ورقة عمل في ملف إكسل. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة واسعة من الخصائص والطرق لإدارة ورقة العمل. للتحكم في ظهور رؤوس الصفوف والأعمدة، استخدم خاصية [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--). [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) هو خاصية من نوع Boolean، مما يعني أنه يمكنها فقط تخزين قيمة **true** أو **false**.  

#### **جعل رؤوس الصف/العمود مرئية**  

اجعل رؤوس الصفوف والأعمدة مرئية عن طريق تعيين خاصية [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) إلى **true**.  

#### **إخفاء رؤوس الصف/العمود**  

اخفِ رؤوس الصفوف والأعمدة عن طريق تعيين خاصية [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) إلى **false**.  

يوضح المثال الكامل أدناه كيفية استخدام الخاصية [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) عن طريق فتح ملف إكسل (book1.xls)، وإخفاء رؤوس الصفوف والأعمدة على ورقة العمل الأولى، وحفظ الملف المُعدّل باسم output.xls.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file path
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the headers of rows and columns
worksheet.setIsRowColumnHeadersVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
من الممكن أيضًا استخدام طريقتي [**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) و [**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) من الفئة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) لجعل صفوف وأعمدة متعددة مرئية.  
{{% /alert %}}  

