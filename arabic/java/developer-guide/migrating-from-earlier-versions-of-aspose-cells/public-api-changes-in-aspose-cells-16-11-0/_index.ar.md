---
title: API عام تغييرات في Aspose.Cells 16.11.0
type: docs
weight: 360
url: /ar/java/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 16.10.0 إلى 16.11.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم إعدادات العولمة**
كشف Aspose.Cells 16.11.0 عن فئة GlobalizationSettings جنبًا إلى جنب مع خاصية WorkbookSettings.GlobalizationSettings من أجل فرض Aspose.Cells APIs لاستخدام تسميات مخصصة للمجموعات الفرعية. تحتوي فئة GlobalizationSettings على الطرق التالية التي يمكن تجاوزها في التنفيذ المخصص لإعطاء الأسماء المطلوبة للتسميات**مجموع** & **المبلغ الإجمالي**.

- GlobalizationSettings.getTotalName: الحصول على الاسم الإجمالي للوظيفة.
- GlobalizationSettings.getGrandTotalName: الحصول على الاسم الإجمالي الكلي للدالة.

فيما يلي فئة مخصصة بسيطة تعمل على توسيع فئة GlobalizationSettings وتتجاوز الأساليب المذكورة أعلاه لإرجاع تسميات مخصصة لوظيفة الدمج المتوسط.

**Java**

{{< highlight "csharp" >}}

 public class CustomSettings extends GlobalizationSettings

{    

    public String getTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "AVG";

             default:

                return super.getTotalName(functionType);

         }

    }

    public String getGrandTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "GRAND AVG";

             default:

            	 return super.getGrandTotalName(functionType);

         }



    }

}

{{< /highlight >}}

المقتطف التالي يقوم بتحميل جدول بيانات موجود ويضيف الإجمالي الفرعي لنوع المتوسط على البيانات المتوفرة بالفعل في ورقة العمل. سيتم استدعاء فئة CustomSettings وطرق getTotalName & getGrandTotalName الخاصة بها في وقت إضافة Subtotal إلى ورقة العمل.

**Java**

{{< highlight "csharp" >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[]{ 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

تقدم فئة GlobalizationSettings أيضًا طريقة getOtherName والتي تعد مفيدة للحصول على اسم ملصقات "أخرى" للمخططات الدائرية. فيما يلي سيناريو استخدام بسيط لطريقة GlobalizationSettings.getOtherName.

**Java**

{{< highlight "csharp" >}}

 public class CustomSettings extends GlobalizationSettings

{ 

	public String getOtherName()

	{

		String language = Locale.getDefault().getLanguage();

		System.out.println(language);

		switch (language)

		{

			case "en":

				return "Other";

			case "fr":

				return "Autre";

			case "de":

				return "Andere";

			//Do other cases

			default:

				return super.getOtherName();

		}

	}

}

{{< /highlight >}}

يقوم المقتطف التالي بتحميل جدول بيانات موجود يحتوي على مخطط دائري ، ويعرض المخطط للصورة أثناء استخدام فئة CustomSettings التي تم إنشاؤها أعلاه.

**Java**

{{< highlight "csharp" >}}

 //Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.getWorksheets().get(0);

//Accesses the 1st chart from the collection

Chart chart = sheet.getCharts().get(0);

//Refreshes the chart

chart.calculate();

//Renders the chart to image

chart.toImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}
### **تمت إضافة فئة CellsFactory**
كشف Aspose.Cells 16.11.0 عن فئة CellsFactory التي لها حاليًا طريقة واحدة ، وهي ؛ خلق نمط. يمكن استخدام أسلوب CellsFactory.createStyle لإنشاء مثيل لفئة Style دون إضافته إلى مجموعة أنماط المصنف.

فيما يلي سيناريو الاستخدام البسيط لطريقة CellsFactory.createStyle.

**Java**

{{< highlight "csharp" >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **تمت إضافة المصنف. خاصية AbsolutePath**
كشف Aspose.Cells 16.11.0 المصنف. تسمح الخاصية AbsolutePath بالحصول على المسار المطلق للمصنف المخزن في ملف workbook.xml أو تعيينه. هذه الخاصية مفيدة أثناء تحديث الروابط الخارجية فقط.
### **تمت إضافة أسلوب GridHyperlinkCollection.getHyperlink**
كشف Aspose.Cells.GridWeb 16.11.0 طريقة getHyperlink إلى فئة GridHyperlinkCollection التي تسمح بالحصول على مثيل GridHyperlink إما بتمرير مثيل GridCell أو زوج من الأعداد الصحيحة المقابلة لمؤشرات عمود الصف.

{{% alert color="primary" %}} 

في حالة عدم العثور على ارتباط تشعبي في الخلية المحددة ، فإن طريقة getHyperlink ستعيد قيمة خالية.

{{% /alert %}} 

فيما يلي سيناريو استخدام بسيط لطريقة getHyperlink.

**Java**

{{< highlight "csharp" >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **منشئ أسلوب قديم**
يرجى استخدام طريقة cellFactory.createStyle كبديل.
## **واجهات برمجة التطبيقات المحذوفة**
### **تم حذف Cell.getConditionalStyle Method**
الرجاء استخدام طريقة Cell.getConditionalFormattingResult بدلاً من ذلك.
### **تم حذف طريقة Cells.getMaxDataRowInColumn (عمود int)**
الرجاء استخدام طريقة Cells.getLastDataRow (int) كبديل.
### **خاصية PageSetup.Draft المحذوفة**
يُنصح باستخدام خاصية PageSetup.PrintDraft بدلاً من ذلك.
### **تم حذف خاصية AutoFilter.FilterColumnCollection**
يرجى مراعاة استخدام خاصية AutoFilter.FilterColumns لتحقيق نفس الهدف.
### **TickLabels المحذوفة. خاصية الدوران**
الرجاء استخدام خاصية TickLabels.RotationAngle بدلاً من ذلك.
