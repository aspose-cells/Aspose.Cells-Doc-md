---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.Cells 8.6.3
type: docs
weight: 230
url: /ar/java/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات العامة لـ Aspose.Cells من الإصدار 8.6.2 إلى 8.6.3 التي قد تكون مهمة لمطوري الوحدات / التطبيقات. يشمل هذا ليس فقط الطرق العامة الجديدة والمحدثة ، والفئات المضافة ، ولكن أيضاً وصفًا لأي تغييرات في السلوك في خلفية Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم تحليل HTML أثناء استيراد البيانات**
إن إصدار Aspose.Cells for Java لواجهة برمجة التطبيقات API قد عرض خاصية ImportTableOptions.setHtmlString التي توجه الواجهة لتحليل علامات HTML أثناء استيراد البيانات إلى الورقة العمل وتعيين النتيجة المحللة كقيمة خلية. يرجى ملاحظة أن واجهات برمجة التطبيقات Aspose.Cells توفر بالفعل خاصية Cell.setHtmlString لأداء هذه المهمة على خلية واحدة، ومع ذلك، أثناء استيراد البيانات بالجملة، توجه الواجهة ImportTableOptions.setHtmlString (عند تعيينها إلى القيمة true) لمحاولة تحليل جميع علامات HTML المدعومة وتعيين النتائج المحللة للخلايا المقابلة.

فيما يلي سيناريو الاستخدام الأبسط.

**Java**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **أضافت Workbook.createBuiltinStyle الأسلوب**
Aspose.Cells for Java 8.6.3 قد عرضت الواجهة Workbook.createBuiltinStyle التي يمكن استخدامها لإنشاء كائن من فئة النمط الذي يتوافق مع أحد ال[أنماط المضمنة المقدمة من تطبيق Excel](/cells/ar/java/using-built-in-styles/). تقبل واجهة Workbook.createBuiltinStyle الثابت من تعداد BuiltinStyleType. يرجى ملاحظة، مع الإصدارات السابقة من واجهات برمجة التطبيقات Aspose.Cells، كان بإمكان إنجاز نفس المهمة عبر واجهة StyleCollection.createBuiltinStyle ولكن مع حذف إصدارات Aspose.Cells APIs الأخيرة لفئة StyleCollection لذا يمكن النظر إلى الواجهة Workbook.createBuiltinStyle المعرضة حديثاً كبديل لتحقيق الهدف نفسه.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **أضيفت خاصية LoadDataOption.OnlyVisibleWorksheet**
Aspose.Cells for Java 8.6.3 قد أظهرت خاصية LoadDataOption.OnlyVisibleWorksheet التي عند تعيينها إلى true ستؤثر على آلية التحميل لواجهة Aspose.Cells for Java API، ونتيجة لذلك ستتم تحميل الأوراق العمل المرئية فقط من جدول بيانات معطاة.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadDataOption

LoadDataOption loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.setOnlyVisibleWorksheet(true);

//Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.setLoadDataOptions(loadDataOptions);

//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

Workbook book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **واجهات برمجة التطبيق القديمة**
### **واجهات برمجة التطبيقات المهجورة**
كبديل للواجهة الWorksheet.copyConditionalFormatting، يُفضل استخدام أي من طرق Cells.copyRows أو Range.copy.
### **تفضل استخدام خاصية Cells.LastCell كبديل عن الخاصية Cells.End.**
يرجى استخدام خاصية Cells.LastCell كبديل لخاصية Cells.End.
{{< app/cells/assistant language="java" >}}
