---
title: عام API التغييرات في Aspose.Cells 8.6.3
type: docs
weight: 230
url: /ar/java/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.6.2 إلى 8.6.3 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة ، ولكن أيضًا وصف أي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم HTML التحليل أثناء استيراد البيانات**
كشف هذا الإصدار من Aspose.Cells for Java API السمة ImportTableOptions.setHtmlString التي توجه API لتحليل علامات HTML أثناء استيراد البيانات إلى ورقة العمل وتعيين النتيجة المحللة كقيمة خلية. يرجى ملاحظة أن واجهات برمجة التطبيقات Aspose.Cells توفر بالفعل السمة Cell.setHtmlString لأداء هذه المهمة لخلية واحدة ، ومع ذلك ، أثناء استيراد البيانات بكميات كبيرة ، تحاول السمة ImportTableOptions.setHtmlString (عند تعيينها إلى true) تحليل جميع علامات ومجموعات HTML المدعومة النتائج التي تم تحليلها للخلايا المقابلة.

هنا هو أبسط سيناريو استخدام.

**Java**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **تمت إضافة أسلوب Workbook.createBuiltinStyle**
 كشف Aspose.Cells for Java 8.6.3 طريقة Workbook.createBuiltinStyle التي يمكن استخدامها لإنشاء كائن من فئة Style يتوافق مع أحد[الأنماط المضمنة التي يوفرها تطبيق Excel](/cells/ar/java/using-built-in-styles/)يقبل أسلوب Workbook.createBuiltinStyle ثابتًا من التعداد BuiltinStyleType. يرجى ملاحظة أنه مع الإصدارات السابقة من واجهات برمجة التطبيقات Aspose.Cells ، يمكن إنجاز نفس المهمة عبر أسلوب StyleCollection.createBuiltinStyle ولكن نظرًا لأن الإصدارات الأخيرة من واجهات برمجة التطبيقات Aspose.Cells قد أزالت فئة StyleCollection ، وبالتالي يمكن اعتبار طريقة Workbook.createBuiltinStyle التي تم الكشف عنها حديثًا كنهج بديل لـ تحقيق نفس الشيء.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **تمت إضافة خاصية LoadDataOption.OnlyVisibleWorksheet**
كشف Aspose.Cells for Java 8.6.3 خاصية LoadDataOption.OnlyVisibleWorksheet التي عند ضبطها على true ستؤثر على آلية التحميل Aspose.Cells for Java API ، ونتيجة لذلك سيتم تحميل أوراق العمل المرئية فقط من جدول بيانات معين.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **أسلوب Worksheet.copyConditionalFormatting قديم**
كبديل لطريقة Worksheet.copyConditionalFormatting ، يُنصح باستخدام أي من أساليب Cells.copyRows أو Range.copy.
### **الملكية Cells. انتهى متقادم**
من فضلك استخدم Cells.LastCell الملكية كبديل للملكية Cells.End.
