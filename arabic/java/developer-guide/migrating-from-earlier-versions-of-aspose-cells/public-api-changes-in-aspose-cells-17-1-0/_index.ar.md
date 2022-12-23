---
title: API عام تغييرات في Aspose.Cells 17.1.0
type: docs
weight: 380
url: /ar/java/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 16.12.0 إلى 17.1.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم مخططات Excel 2016**
أضافت واجهات برمجة تطبيقات Aspose.Cells دعمًا لبعض مخططات Excel 2016 من خلال تحسين تعداد ChartType. تمت إضافة الحقول الجديدة التالية بإصدار Aspose.Cells 17.1.0.

- ChartType.BOX_WHISKER: تم وضع السلسلة على هيئة مربع وشعيرات.
- ChartType.FUNNEL: تم وضع السلسلة كقمع.
- ChartType.PARETO_LINE: تم وضع السلسلة كخطوط باريتو.
- ChartType.SUNBURST: تم وضع السلسلة على شكل انفجار شمس.
- ChartType.TREEMAP: تم تخطيط السلسلة كخريطة شبكية.
- ChartType.WATERFALL: تم وضع السلسلة على شكل شلال.
- ChartType.HISTOGRAM: تم تخطيط السلسلة كرسم بياني.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[قراءة أنواع مخططات Excel 2016](/cells/ar/java/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **تمت إضافة أداة ضبط لخاصية LoadFilter.LoadDataFilterOptions**
قام Aspose.Cells 17.1.0 بإضافة أداة ضبط للخاصية LoadFilter.LoadDataFilterOptions لاستبدال متغير نسخة m_LoadDataFilterOptions. قد يقوم المستخدمون بتغيير الخاصية LoadDataFilterOptions في التطبيق الخاص بهم لفئة LoadFilter لتغيير سلوك تحميل ملفات القوالب.

هنا سيناريو استخدام بسيط.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[تصفية القالب المخصص](/cells/ar/java/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 class CustomLoadFilter extends LoadFilter {

	public void startSheet(Worksheet sheet) {

		if (sheet.getName().equals("NoCharts")) {

			//Load everything and filter charts

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CHART);

		}

		if (sheet.getName().equals("NoShapes")) {

			//Load everything and filter shapes

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.SHAPE);

		}

		if (sheet.getName().equals("NoConditionalFormatting")) {

			//Load everything and filter conditional formatting

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CONDITIONAL_FORMATTING);

		}

	}

}

{{< /highlight >}}
### **تمت إضافة خاصية CellsHelper.SignificantDigits**
كشف Aspose.Cells 17.1.0 خاصية SignificantDigits من فئة CellsHelper والتي تسمح بالحصول على أو تعيين عدد الأرقام المعنوية للقيم الرقمية في جدول بيانات. القيمة الافتراضية للخاصية CellsHelper.SignificantDigits هي 17 في حين أنها قابلة للتطبيق فقط إذا كان لابد من تخزين النتيجة في تنسيق ملف XLSX.

فيما يلي سيناريو بسيط لتوضيح استخدام خاصية CellsHelper.SignificantDigits.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[تحديد عدد الأرقام المهمة](/cells/ar/java/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **تمت إضافة خاصية GlowEffect.Color**
أضاف Aspose.Cells 17.1.0 خاصية GlowEffect.Color التي يمكن استخدامها لاسترداد لون تأثير التوهج.

يستخدم المقتطف التالي خاصية GlowEffect.Color.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[قراءة لون توهج الشكل](/cells/ar/java/read-color-of-the-shape-s-glow-effect/)
{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Read the source Excel file

Workbook book = new Workbook(dir + "sample.xlsx");

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access the first shape

Shape shape = sheet.getShapes().get(0);

//Read the glow effect color

GlowEffect glow = shape.getGlow();

CellsColor color = glow.getColor();

{{< /highlight >}}
### **تمت إضافة خصائص PageSetup.PaperWidth و PaperHeight**
قام Aspose.Cells 17.1.0 بعرض خصائص PaperWidth و PaperHeight لفئة PageSetup. تعد خصائص PageSetup.PaperWidth & PageSetup.PaperHeight من النوع المزدوج الذي يمثل عرض الورق وارتفاعه بوحدة البوصة مع مراعاة اتجاه الصفحة.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[استرجاع حجم ورق ورقة العمل](/cells/ar/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **تمت إضافة خاصية WorkbookSettings.CheckCustomNumberFormat**
قام Aspose.Cells 17.1.0 بإضافة الخاصية CheckCustomNumberFormat إلى فئة WorkbookSettings. يعتبر CheckCustomNumberFormat مفيدًا في التحقق مما إذا كانت الخاصية Style.Custom قد تم تعيينها بشكل صحيح أم لا. في حالة تعيين الخاصية Style.Custom بشكل غير صحيح ، أي ؛ القيمة لا تتوافق مع النمط الصالح ، فإن واجهات برمجة التطبيقات Aspose.Cells ستلقي CellsException بالرسالة المناسبة.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[التحقق من Forma المخصص](/cells/ar/java/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Set CheckCustomNumberFormat property to true

book.getSettings().setCheckCustomNumberFormat(true);

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access a cell

Cell cell = sheet.getCells().get("B5");

//Insert a value to the cell

cell.putValue(2347);

//Access cell's style

Style style = cell.getStyle();



//Set Custom property to an invalid pattern

style.setCustom("ggg @ fff");

//Set the modified style to the cell

cell.setStyle(style);

{{< /highlight >}}
### **تمت إضافة DisplayUnitType.PERCENTAGE الحقل**
قام Aspose.Cells 17.1.0 أيضًا بتعريض حقل PERCENTAGE لتعداد DisplayUnitType. يشير الحقل DisplayUnitType.PERCENTAGE إلى أن القيم على الرسم البياني ستُقسَّم على 0.01.
## **إزالة واجهات برمجة التطبيقات**
### **تمت إزالة متغير المثيل m_LoadDataFilterOptions**
قام هذا الإصدار بإزالة متغير مثيل m_LoadDataFilterOptions. يُنصح باستخدام الخاصية LoadFilter.LoadDataFilterOptions بدلاً من ذلك.
