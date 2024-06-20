---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.Cells 16.11.0
type: docs
weight: 360
url: /ar/java/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات (API) لـ Aspose.Cells من الإصدار 16.10.0 إلى الإصدار 16.11.0 التي قد تكون مثيرة لاهتمام مطوري النماذج / التطبيقات. يتضمن ليس فقط الأساليب الجديدة والمحدثة العامة والفئات المضافة والمحذوفة إلخ، بل وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells أيضًا.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم إعدادات العولمة**
أصدر Aspose.Cells 16.11.0 فئة GlobalizationSettings إلى جانب خاصية WorkbookSettings.GlobalizationSettings لفرض استخدام واجهات برمجة التطبيقات لـ Aspose.Cells لاستخدام تسميات مخصصة لإجمالي الأرقام الفرعية. تحتوي فئة GlobalizationSettings على الطرق التالية التي يمكن استبدالها في التنفيذ المخصص لإعطاء أسماء مرغوبة للتسميات **الإجمالي** و**الإجمالي الكلي**.

- GlobalizationSettings.getTotalName: يحصل على اسم الإجمالي للوظيفة.
- GlobalizationSettings.getGrandTotalName: يحصل على الإجمالي الكلي لاسم الوظيفة.

فيما يلي فئة مخصصة بسيطة توسع فئة GlobalizationSettings وتستبدل طرقها المذكورة أعلاه لإرجاع تسميات مخصصة لدالة التجميع المتوسطية.

**Java**

{{< highlight csharp >}}

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

المقتطف التالي يقوم بتحميل جدول بيانات موجود بالفعل في ورقة البيانات ويضيف الإجمالي الفرعي من النوع المتوسط إلى البيانات المتاحة بالفعل في ورقة البيانات. سيتم استدعاء فئة CustomSettings وطرق getTotalName و getGrandTotalName في وقت إضافة الإجمالي الفرعي إلى ورقة البيانات.

**Java**

{{< highlight csharp >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[] { 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

تقدم فئة GlobalizationSettings أيضًا طريقة getOtherName والتي تكون مفيدة للحصول على اسم "آخر" للرسوم البيانية الدائرية. فيما يلي سيناريو استخدام بسيط لطريقة GlobalizationSettings.getOtherName.

**Java**

{{< highlight csharp >}}

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

المقتطف التالي يقوم بتحميل جدول بيانات موجود يحتوي على رسم بياني دائري، ويقوم بتقديم الرسم البياني إلى صورة أثناء استخدام فئة CustomSettings التي تم إنشاؤها أعلاه.

**Java**

{{< highlight csharp >}}

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
أصدر Aspose.Cells 16.11.0 فئة CellsFactory التي تحتوي حاليًا على طريقة واحدة، وهي؛ createStyle. يمكن استخدام طريقة CellsFactory.createStyle لإنشاء نسخة من فئة Style دون إضافتها إلى مجموعة أنماط ورقة البيانات.

فيما يلي سيناريو استخدام بسيط لطريقة CellsFactory.createStyle.

**Java**

{{< highlight csharp >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **تمت إضافة خاصية Workbook.AbsolutePath**
أصدر Aspose.Cells 16.11.0 خاصية Workbook.AbsolutePath التي تسمح بالحصول على مسار العمل المؤقت المخزن في ملف workbook.xml أو تعيينه. تعتبر هذه الخاصية مفيدة أثناء تحديث الروابط الخارجية فقط.
### **تمت إضافة طريقة GridHyperlinkCollection.getHyperlink**
أصدر Aspose.Cells.GridWeb 16.11.0 طريقة getHyperlink إلى فئة GridHyperlinkCollection التي تسمح بالحصول على مثيل GridHyperlink عن طريق تمرير مثيل GridCell أو زوج من الأعداد الصحيحة المقابلة لمؤشرات الصف العمود.

{{% alert color="primary" %}} 

في حال عدم العثور على رابط تشعبي على الخلية المحددة، ستُعيد طريقة getHyperlink قيمة فارغة.

{{% /alert %}} 

فيما يلي سيناريو بسيط لاستخدام طريقة getHyperlink.

**Java**

{{< highlight csharp >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **واجهات برمجة التطبيق القديمة**
### **مُنشئ نمط مهجور**
يرجى استخدام طريقة createStyle من cellsFactory كبديل.
## **حذف واجهات برمجة التطبيق**
### **طريقة getConditionalStyle في Cell تم حذفها**
الرجاء استخدام طريقة getConditionalFormattingResult بدلاً من ذلك.
### **طريقة getMaxDataRowInColumn(int column) في Cells تم حذفها**
الرجاء استخدام طريقة getLastDataRow(int) كبديل.
### **خاصية Draft في PageSetup تم حذفها**
من المستحسن استخدام خاصية PrintDraft في PageSetup بدلاً من ذلك.
### **خاصية FilterColumnCollection في AutoFilter تم حذفها**
يرجى النظر في استخدام خاصية FilterColumns في AutoFilter لتحقيق نفس الهدف.
### **خاصية Rotation في TickLabels تم حذفها**
الرجاء استخدام خاصية RotationAngle في TickLabels بدلاً من ذلك.
