---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 17.1.0
type: docs
weight: 380
url: /ar/java/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

تصف هذه الوثيقة التغييرات في واجهة برمجة تطبيقات Aspose.Cells من الإصدار 16.12.0 إلى 17.1.0 التي قد تكون مثيرة لاهتمام مطوري الوحدات/التطبيقات. تتضمن ليس فقط الطرق العامة الجديدة والمحدثة والطرق العامة التي تمت إضافتها وإزالتها وتغيير الفصول الخلفية في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **الدعم لرسوم بيانية Excel 2016**
لقد أضافت واجهات برنامج التطبيقات Aspose.Cells دعم بضع رسوم بيانية لبرنامج Excel 2016 عن طريق تعزيز تعداد الرسم البياني. تمت إضافة الحقول الجديدة التالية مع إصدار Aspose.Cells 17.1.0.

- ChartType.BOX_WHISKER: السلسلة مرتبة على شكل صندوق وفتيل.
- ChartType.FUNNEL: السلسلة مرتبة على شكل قمع.
- ChartType.PARETO_LINE: السلسلة مرتبة على شكل خطوط باريتو.
- ChartType.SUNBURST: السلسلة مرتبة على شكل نجمة الشمس.
- ChartType.TREEMAP: السلسلة مرتبة على شكل مخطط الشجرة.
- ChartType.WATERFALL: السلسلة مرتبة على شكل شلال مائي.
- ChartType.HISTOGRAM: السلسلة مرتبة على شكل هيستوغرام.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [قراءة أنواع رسوم بيانية Excel 2016](/cells/ar/java/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **تمت إضافة Setter لخاصية LoadFilter.LoadDataFilterOptions.**
لقد أضاف Aspose.Cells 17.1.0 Setter لخاصية LoadFilter.LoadDataFilterOptions لاستبدال المتغير المثيل m_LoadDataFilterOptions. قد يقوم المستخدمون بتغيير خاصية LoadDataFilterOptions في تنفيذهم الخاص لفئة LoadFilter لتغيير سلوك تحميل ملفات القالب.

فيما يلي سيناريو استخدام بسيط.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [تصفية القوالب المخصصة](/cells/ar/java/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **تمت إضافة خاصية SignificantDigits في CellsHelper**
أضاف Aspose.Cells 17.1.0 خاصية SignificantDigits من فئة CellsHelper والتي تسمح بالحصول على عدد الأرقام الكبيرة أو تعيينها لقيم رقمية في ورقة البيانات. القيمة الافتراضية لخاصية CellsHelper.SignificantDigits هي 17 وذلك فقط إذا كان ينطبق تخزين النتيجة في تنسيق ملف XLSX.

إليك سيناريو بسيط لتوضيح استخدام خاصية CellsHelper.SignificantDigits

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [ضبط عدد الأرقام الكبيرة](/cells/ar/java/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **تمت إضافة خاصية Color في GlowEffect**
أضاف Aspose.Cells 17.1.0 خاصية Color في GlowEffect والتي يمكن استخدامها لاسترداد لون تأثير اللمعان.

تستخدم القصاصة التالية خاصية Color في GlowEffect

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [قراءة لون تأثير اللمعان في الشكل](/cells/ar/java/read-color-of-the-shape-s-glow-effect/)
{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **تمت إضافة خصائص PaperWidth و PaperHeight في PageSetup**
أضاف Aspose.Cells 17.1.0 الخصائص PaperWidth و PaperHeight لفئة PageSetup. تُمثل خصائص PageSetup.PaperWidth و PageSetup.PaperHeight نوع double تمثل عرض وارتفاع الورق بوحدة البوصة مع مراعاة توجيه الصفحة.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [استرداد حجم ورقة العمل](/cells/ar/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **تمت إضافة خاصية CheckCustomNumberFormat في WorkbookSettings**
أضاف Aspose.Cells 17.1.0 خاصية CheckCustomNumberFormat لفئة WorkbookSettings. CheckCustomNumberFormat مفيدة في التحقق مما إذا تم تعيين خاصية Style.Custom بشكل صحيح أم لا. في حالة تم تعيين خاصية Style.Custom بشكل غير صحيح، أي بأن القيمة لا تتوافق مع النمط الصحيح ثم ستقوم واجهات برمجة التطبيقات لـ Aspose.Cells برمي CellsException مع رسالة مناسبة.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [التحقق من التنسيق الخاص](/cells/ar/java/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **تمت إضافة حقل PERCENTAGE في DisplayUnitType**
أضاف Aspose.Cells 17.1.0 أيضاً حقل PERCENTAGE لتعداد DisplayUnitType. حقل DisplayUnitType.PERCENTAGE يشير إلى أن القيم في الرسم البياني يجب أن تقسم على 0.01.
## **تمت إزالة واجهات برمجة التطبيقات**
### **تمت إزالة المتغير المثيل m_LoadDataFilterOptions**
تمت إزالة المتغير المثيل m_LoadDataFilterOptions في هذا الإصدار. من المستحسن استخدام خاصية LoadFilter.LoadDataFilterOptions بدلاً من ذلك.
