---
title: عام API التغييرات في Aspose.Cells 8.4.2
type: docs
weight: 150
url: /ar/net/public-api-changes-in-aspose-cells-8-4-2/
---
{{% alert color="primary" %}} 

 يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.4.1 إلى 8.4.2 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/net/public-api-changes-in-aspose-cells-8-4-2/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **آلية إنشاء المخطط المحسن**
كشفت الفئة Aspose.Cells.Charts.Chart طريقة SetChartDataRange لتسهيل مهمة إنشاء المخطط. تقبل طريقة SetChartDataRange معلمتين ، حيث تكون المعلمة الأولى من سلسلة النوع التي تحدد منطقة الخلية التي يتم من خلالها رسم سلسلة البيانات. المعلمة الثانية هي من النوع المنطقي الذي يحدد اتجاه الرسم ، أي ؛ ما إذا كنت تريد رسم سلسلة بيانات المخطط من نطاق من قيم الخلايا حسب الصف أو الأعمدة.

يوضح مقتطف التعليمات البرمجية التالي كيفية إنشاء مخطط عمودي مع بضعة أسطر من التعليمات البرمجية بافتراض أن بيانات سلسلة مخطط الرسم البياني موجودة في نفس ورقة العمل من الخلية A1 إلى D4.

**C#**

{{< highlight "csharp" >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **الطريقة VbaModuleCollection.Add added**
كشف Aspose.Cells for .NET 8.4.2 طريقة VbaModuleCollection.Add لإضافة وحدة نمطية جديدة لـ VBA إلى مثيل المصنف. تقبل طريقة VbaModuleCollection.Add معلمة من نوع ورقة العمل لإضافة وحدة نمطية خاصة بورقة العمل.

يوضح مقتطف الشفرة التالي كيفية استخدام طريقة VbaModuleCollection.Add.

**C#**

{{< highlight "csharp" >}}

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


### **طريقة التحميل الزائد Cells.CopyColumns المضافة**
كشف Aspose.Cells for .NET 8.4.2 عن نسخة محملة بشكل زائد من Cells.CopyColumns لتكرار أعمدة المصدر على الوجهة. تقبل الطريقة المكشوفة حديثًا 5 معلمات في المجموع ، حيث تكون المعلمات الأربعة الأولى هي نفسها الخاصة بالطريقة الشائعة Cells.CopyColumns. ومع ذلك ، فإن المعلمة الأخيرة من النوع int تحدد عدد أعمدة الوجهة التي يجب تكرار أعمدة المصدر عليها.

يوضح مقتطف التعليمات البرمجية التالي كيفية استخدام طريقة Cells.CopyColumns المكشوفة حديثًا.

**C#**

{{< highlight "csharp" >}}

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


### **تمت إضافة حقول التعداد PasteType.Default & PasteType.DefaultExceptBorders**
مع إصدار v8.4.2 ، أضاف Aspose.Cells API حقلي تعداد جديدين لـ PasteType كما هو مفصل أدناه.

- PasteType.Default: يعمل بشكل مشابه لوظيفة "الكل" في Excel للصق مجموعة من الخلايا.
- PasteType.DefaultExceptBorders: يعمل بشكل مشابه لوظيفة "الكل باستثناء الحدود" في Excel للصق نطاق الخلايا.

يوضح نموذج التعليمات البرمجية التالي استخدام حقل PasteType.Default.

**C#**

{{< highlight "csharp" >}}

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

بدءًا من إصدار for .NET for .NET Aspose.Cells 8.4.2 ، قدم التعداد PasteType.All يتصرف بشكل مختلف مقارنة بوظيفة "الكل" في Excel للصق نطاق الخلايا. الآن ، يقوم PasteType.All أيضًا بنسخ عرض العمود إلى النطاق الوجهة بدلاً من وظيفة "الكل" في Excel. لتقليد سلوك "الكل" في Excel ، يرجى استخدام PasteType.Default.

{{% /alert %}}
