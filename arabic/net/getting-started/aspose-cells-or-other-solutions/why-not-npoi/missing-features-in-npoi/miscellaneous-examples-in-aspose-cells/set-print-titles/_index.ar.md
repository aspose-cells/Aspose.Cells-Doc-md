---
title: تعيين عناوين الطباعة
type: docs
weight: 30
url: /ar/net/set-print-titles/
---

## **Aspose.Cells - تحديد عناوين الطباعة**
تتيح لك Aspose.Cells تعيين رؤوس الصفوف والأعمدة لتتكرر على جميع الصفحات لورقة بيانات مطبوعة. للقيام بذلك، استخدم فئة [PageSetup](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) الخاصة بـ PrintTitleColumns وخصائص PrintTitleRows.

يتم تعريف الصفوف أو الأعمدة التي ستتكرر عن طريق تمرير أرقامها. على سبيل المثال، يتم تعريف الصفوف كـ $1:$2 والأعمدة كـ $A:$B.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows= "$1:$2";

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **تعيين عناوين الطباعة** من أي من المواقع المذكورة أدناه للتعليم الاجتماعي للبرمجة:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

للحصول على مزيد من التفاصيل، قم بزيارة [ضبط خيارات الطباعة](/cells/ar/net/setting-print-options/).

{{% /alert %}}
