---
title: تعيين عناوين الطباعة
type: docs
weight: 30
url: /ar/net/set-print-titles/
---
## **Aspose.Cells - تعيين عناوين الطباعة**
Aspose.Cells يسمح لك بتعيين رؤوس الصفوف والأعمدة لتكرارها على كل صفحات ورقة العمل المطبوعة. للقيام بذلك ، استخدم ملف[اعداد الصفحة](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)فئة PrintTitleColumns وخصائص PrintTitleRows.

يتم تحديد الصفوف أو الأعمدة التي سيتم تكرارها عن طريق تمرير أرقام الصفوف أو الأعمدة. على سبيل المثال ، يتم تعريف الصفوف على أنها $ 1: $ 2 ويتم تعريف الأعمدة على أنها $ A: $ B.

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows= "$1:$2";

{{< /highlight >}}
## **تحميل كود الجري**
 تحميل**تعيين عناوين الطباعة** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[ضبط خيارات الطباعة](/cells/ar/net/setting-print-options/).

{{% /alert %}}
