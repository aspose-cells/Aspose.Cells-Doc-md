---  
title: تنسيق النطاقات باستخدام Node.js عبر C++  
linktitle: تنسيق النطاقات  
type: docs  
weight: 105  
url: /ar/nodejs-cpp/how-to-format-a-range/  
description: تعلم كيفية تنسيق نطاق خلايا في Excel باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  
عندما تحتاج إلى تطبيق نمط على النطاق، يمكنك استخدام تنسيق النطاق.  

## **كيفية تنسيق نطاق في إكسل**  

لتنسيق مجموعة من الخلايا في إكسل، يمكنك استخدام الخيارات المدمجة للتنسيق المقدمة من إكسل. إليك كيف يمكنك تنسيق مجموعة من الخلايا مباشرة في إكسل:  

1. افتح إكسل وافتح المصنف الذي يحتوي على النطاق الذي تريد تنسيقه.  

2. حدد النطاق من الخلايا التي تريد تنسيقها. يمكنك النقر وسحب لتحديد النطاق، أو يمكنك استخدام اختصارات لوحة المفاتيح مثل Shift + مفاتيح الأسهم لتوسيع التحديد.  

3. بمجرد تحديد النطاق، انقر بزر الماوس الأيمن على النطاق المحدد واختر "تنسيق الخلايا" من القائمة المنسدلة. بالإضافة إلى ذلك، يمكنك الانتقال إلى علامة التبويب الرئيسية في الشريط في إكسل، انقر فوق القائمة المنسدلة "تنسيق" في مجموعة "الخلايا"، واختر "تنسيق الخلايا".  

4. ستظهر نافذة "تنسيق الخلايا". هنا، يمكنك اختيار خيارات التنسيق المختلفة لتطبيقها على النطاق المحدد. على سبيل المثال، يمكنك تغيير نمط الخط، حجم الخط، لون الخط، تنسيق الأرقام، الحدود، لون الخلفية، إلخ. استكشاف علامات التبويب المختلفة في نافذة الحوار للوصول إلى خيارات التنسيق المختلفة.  

5. بعد إجراء التغييرات في التنسيق المطلوب، انقر على زر "موافق" لتطبيق التنسيق على النطاق المحدد.  

## **كيفية تنسيق نطاق باستخدام Node.js**  

لتنسيق النطاق باستخدام Aspose.Cells for Node.js via C++، يمكنك استخدام الطرق التالية:  
1. [Range.applyStyle(style, flag)](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.setStyle(style)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  
3. [Range.setStyle(style)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  

## **الكود المثالي**  
في هذا المثال، نقوم بإنشاء دفتر عمل Excel، إضافة بعض البيانات العينية، الوصول إلى ورقة العمل الأولى، وتعريف نطاقين ("A1:C3" و "A4:C5"). ثم نقوم بإنشاء أنماط جديدة، وضبط خيارات التنسيق المختلفة (مثل لون الخط، والنص العريض)، وتطبيق النمط على النطاق. وأخيرًا، نحفظ دفتر العمل في ملف جديد.  
<br>  
![todo:image_alt_text](format-range.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const ws = workbook.getWorksheets().get(0);

const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Access the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Define the range
const range = worksheet.getCells().createRange("A1:C3");

// Apply formatting to the range
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Red);
style.getFont().setIsBold(true);

const flag = new AsposeCells.StyleFlag();
flag.setFont(true);
range.applyStyle(style, flag);

// Define the range
const range2 = worksheet.getCells().createRange("A4:C5");

// Apply formatting to the range
const style2 = workbook.createStyle();
style2.getFont().setColor(AsposeCells.Color.Blue);
style2.getFont().setIsItalic(true);
range2.setStyle(style2);

// Save the modified workbook
workbook.save("output.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
