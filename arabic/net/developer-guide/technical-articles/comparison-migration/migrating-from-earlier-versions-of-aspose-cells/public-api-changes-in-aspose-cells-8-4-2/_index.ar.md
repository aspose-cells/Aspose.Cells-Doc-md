---
title: تغيرات واجهة برمجة التطبيقات العامة في Aspose.Cells 8.4.2
type: docs
weight: 150
url: /ar/net/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

يوصف هذا المستند التغييرات التي طرأت على واجهة برمجة التطبيقات في Aspose.Cells من الإصدار 8.4.1 إلى 8.4.2 التي قد تكون مثيرة للاهتمام لمطوري الوحدات/التطبيقات. يشمل ذلك ليس فقط الطرق العامة الجديدة والمحدثة، ولكن أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **آلية إنشاء المخططات المحسنة**
فصحت صنف Aspose.Cells.Charts.Chart عن طريقة SetChartDataRange لتسهيل مهمة إنشاء الرسم البياني. تقبل طريقة SetChartDataRange معلماتين، حيث تكون المعلمة الأولى من نوع سلسلة تحدد منطقة الخلية التي سيتم من خلالها رسم سلاسل البيانات. المعلمة الثانية من نوع بوليان تحدد توجيه الرسم البياني، وهل يجب رسم سلاسل بيانات الرسم البياني من مجموعة قيم الخلايا حسب الصف أو حسب الأعمدة.

يظهر الشق المشفر التالي كيفية إنشاء مخطط عمودي ببضع أسطر من الشيفرة بشرط أن بيانات سلسلة مخططها موجودة على نفس ورقة العمل من الخلية A1 إلى D4.

**C#**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **أضيفت طريقة VbaModuleCollection.Add**
فصحت Aspose.Cells for .NET 8.4.2 طريقة VbaModuleCollection.Add لإضافة وحدة VBA جديدة إلى مثيل الدفتر. تقبل طريقة VbaModuleCollection.Add معلمة من نوع ورقة العمل لإضافة وحدة محددة لورقة العمل.

توضح كود مقتطف التالي كيفية استخدام طريقة VbaModuleCollection.Add.

**C#**

{{< highlight csharp >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add VBA module for first worksheet

int idx = workbook.VbaProject.Modules.Add(worksheet);

//Access the VBA Module, set its name and code

Aspose.Cells.Vba.VbaModule module = workbook.VbaProject.Modules[idx];

module.Name = "TestModule";

module.Codes = "Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub";

//Save the workbook

workbook.Save(output, SaveFormat.Xlsm);

{{< /highlight >}}


### **تمت إضافة طريقة Cells.CopyColumns متعددة الحمولة**
فصحت Aspose.Cells for .NET 8.4.2 النسخة المتعددة الحمولة لطريقة Cells.CopyColumns لتكرار أعمدة المصدر على الوجهة. تقبل الطريقة المفتوحة حديثًا 5 معلمات في المجموع، حيث تكون الأرباع المعلمة الأولى مثل الطريقة الشائعة Cells.CopyColumns. ومع ذلك، تحدد المعلمة الأخيرة من نوع int عدد أعمدة الوجهة التي يجب تكرار أعمدة المصدر عليها.

توضح كود مقتطف التالي كيفية استخدام طريقة Cells.CopyColumns المفتوحة حديثًا.

**C#**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.CopyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **تمت إضافة حقول التعداد PasteType.Default وPasteType.DefaultExceptBorders**
مع إصدار v8.4.2، قام API Aspose.Cells بإضافة 2 حقل تعداد جديد لـ PasteType كما هو مفصل أدناه.

- PasteType.Default: يعمل بشكل مماثل لوظيفة "الكل" في Excel لصق مجموعة من الخلايا.
- PasteType.DefaultExceptBorders: يعمل بشكل مماثل لوظيفة "الكل باستثناء الحدود" في Excel لصق مجموعة من الخلايا.

يوضح الكود العيني التالي استخدام حقل PasteType.Default.

**C#**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Create source & destination ranges

Range source = cells.CreateRange("A1:B6");

Range destination = cells.CreateRange("D1:E6");

//Copy the source range onto the destination range with everything except column widths

destination.Copy(source, new PasteOptions() { PasteType = PasteType.Default });

//Save the workbook

workbook.Save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

بدءًا من إصدار Aspose.Cells for .NET 8.4.2، يتصرف حقل التعداد PasteType.All بشكل مختلف عن وظيفة "الكل" في Excel لصق مجموعة من الخلايا. الآن، يقوم PasteType.All أيضًا بنسخ أعراض الأعمدة على مجموعة الوجهة بدلاً من وظيفة "الكل" في Excel. من أجل تقليد سلوك "الكل" في Excel، يرجى استخدام PasteType.Default.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
