---  
title: كيفية التحكم في شريط علامات التبويب للورقة باستخدام Node.js عبر C++  
linktitle: كيفية التحكم في شريط علامة الورقة  
type: docs  
weight: 600  
url: /ar/nodejs-cpp/how-to-control-sheet-tab-bar/  
description: تعلم كيف تتحكم في شريط علامات تبويب الورقة باستخدام Aspose.Cells for Node.js via C++.  
keywords: كيفية التحكم في شريط علامات التبويب للورقة باستخدام Node.js عبر C++، تشغيل شريط علامات التبويب للورقة باستخدام Node.js عبر C++، ضبط شريط علامات التبويب للورقة باستخدام Node.js عبر C++, التحكم في شريط علامات التبويب للورقة باستخدام Node.js عبر C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  
عند الحاجة إلى ضبط عرض شريط ورقة Excel، تحتاج إلى معرفة كيفية التحكم في شريط علامات التبويب للورقة، مثل إخفاء أو عرض شريط علامات التبويب، تغيير عرض علامة التبويب، تحديد أول علامة تبويب مرئية، وغيرها. تدعم Aspose.Cells for Node.js via C++ هذه الميزات. توفر Aspose.Cells الخصائص والطرق التالية لمساعدتك على تحقيق أهدافك.

- [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)
- [**WorkbookSettings.getSheetTabBarWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getSheetTabBarWidth--)
- [**WorkbookSettings.getFirstVisibleTab()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getFirstVisibleTab--)

## **كيفية التحكم في شريط تبويب ورقة العمل باستخدام Aspose.Cells for Node.js via C++**  
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل.
1. إضافة بيانات إلى الخلايا في ورقة العمل الأولى.
1. عرض علامة الورقة وتعيين عرض شريط التبويب.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the newly added worksheet
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

// Display the sheet tab and set the width of the tab bar
workbook.getSettings().setShowTabs(true);
workbook.getSettings().setSheetTabBarWidth(150);

workbook.save("out.xlsx");
```

معاينة ملف النتائج:  
<br>  
<image src="result.png" width="70%" />  


{{< app/cells/assistant language="nodejs-cpp" >}}
