---  
title: معاينة دفتر العمل باستخدام Node.js عبر C++  
linktitle: معاينة دفتر العمل 
type: docs  
weight: 70  
url: /ar/nodejs-cpp/workbook-and-worksheet-preview/  
description: يدعم Aspose.Cells الطباعة والمعاينة المسبقة لملفات Excel بدون تثبيت Microsoft Excel باستخدام Node.js عبر C++.  
---  

## **معاينة الطباعة**  

قد توجد حالات يكون فيها من الضروري تحويل ملفات Excel التي تحتوي على ملايين الصفحات إلى PDF أو صور. سيستهلك معالجة مثل هذه الملفات وقتًا وموارد كثيرة. في مثل هذه الحالات، قد تكون ميزة معاينة الطباعة للكتاب وورقة العمل مفيدة. قبل تحويل مثل هذه الملفات، يمكن للمستخدم فحص إجمالي عدد الصفحات ثم اتخاذ قرار بشأن ما إذا كان سيتم تحويل الملف أم لا. يركز هذا المقال على استخدام فصلي [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) لمعرفة الإجمالي الكلي للصفحات.  

يوفر Aspose.Cells ميزة المعاينة المسبقة للطباعة. لهذا، توفر الـ API فصلي [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/). لإنشاء معاينة الطباعة للكتاب بأكمله، قم بإنشاء نسخة من فئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) عن طريق تمرير كائنات [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) إلى الباني. توفر فئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) طريقة [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--) التي تُرجع عدد الصفحات في المعاينة المُولدة. مماثلة لفئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)، يُستخدم فئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) لإنشاء معاينة طباعة لورقة عمل محددة. لإنشاء معاينة الطباعة لورقة العمل، قم بإنشاء نسخة من فئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) عن طريق تمرير كائنات [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) إلى الباني. توفر فئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) أيضًا طريقة [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--) التي تُرجع عدد الصفحات في المعاينة المُولدة.  

يوضح مقتطف الشفرة التالي استخدام فصلي [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) باستخدام [ملف إكسل النموذجي](94896177.xlsx).  

### **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const filePath = path.join(sourceDir, "Book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const imgOptions = new AsposeCells.ImageOrPrintOptions();
const preview = new AsposeCells.WorkbookPrintingPreview(workbook, imgOptions);
console.log("Workbook page count: " + preview.getEvaluatedPageCount());

const preview2 = new AsposeCells.SheetPrintingPreview(workbook.getWorksheets().get(0), imgOptions);
console.log("Worksheet page count: " + preview2.getEvaluatedPageCount());
```  

يُظهر ما يلي الناتج الذي تم توليده عن طريق تنفيذ الكود أعلاه.  

### **مخرجات الوحدة**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **مواضيع متقدمة**  
- [تكوين الخطوط لعرض جداول البيانات](/cells/ar/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [تحويل ورقة العمل إلى صورة - إزالة الفراغات حول البيانات](/cells/ar/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [تحويل الورقة العمل إلى صورة والورقة العمل إلى صورة حسب الصفحة](/cells/ar/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [تحويل ورقة العمل إلى صورة باستخدام خيارات الصورة أو الطباعة](/cells/ar/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [تصدير مجموعة من الخلايا في ورقة عمل إلى صورة](/cells/ar/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [تصدير ورقة العمل أو الرسم البياني إلى صورة بعرض وارتفاع مطلوبين](/cells/ar/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [استخراج الصور من أوراق العمل باستخدام خيارات الصورة أو الطباعة](/cells/ar/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [إنشاء مصغرة لورقة العمل](/cells/ar/nodejs-cpp/generate-thumbnail-of-the-worksheet/)  
- [إخراج صفحة فارغة عند عدم وجود شيء للطباعة](/cells/ar/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [إعداد الصفحة وخيارات الطباعة](/cells/ar/nodejs-cpp/page-setup-and-printing-options/)  
- [تقديم تسلسل من الصفحات باستخدام خصائص PageIndex وPageCount لخيارات الصورة أو الطباعة](/cells/ar/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [عرض الورقة العمل إلى سياق رسومي](/cells/ar/nodejs-cpp/render-worksheet-to-graphic-context/)  
- [تحديد مجموعة خطوط فردية أو خاصة لتقديم الدفتر](/cells/ar/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)   

