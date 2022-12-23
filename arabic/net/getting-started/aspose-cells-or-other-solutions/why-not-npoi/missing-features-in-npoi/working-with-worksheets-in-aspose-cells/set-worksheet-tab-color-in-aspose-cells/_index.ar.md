---
title: قم بتعيين لون علامة تبويب ورقة العمل في Aspose.Cells
type: docs
weight: 20
url: /ar/net/set-worksheet-tab-color-in-aspose-cells/
---
## **Aspose.Cells - تعيين لون علامة تبويب ورقة العمل**
Aspose.Cells يسمح لك بتغيير لون علامات تبويب أوراق العمل الفردية لجعلها بارزة من البقية. على سبيل المثال ، يمكنك جعل المصاريف باللون الأحمر ، والمبيعات الخضراء ، والأصول زرقاء ، وما إلى ذلك.
### **ضبط لون علامة تبويب ورقة العمل باستخدام Microsoft Excel**
1. انقر بزر الماوس الأيمن فوق علامة تبويب في ورقة الجدولة أسفل ورقة العمل الحالية.
1. يختار**لون علامة التبويب**.
1. حدد لونًا من اللوحة.
1. انقر**نعم**.

**C#**

{{< highlight "cs" >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the first worksheet in the book

Worksheet worksheet = workbook.Worksheets[0];

//Set the tab color

worksheet.TabColor = Color.Red;

//Save the Excel file

workbook.Save("AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**تعيين لون علامة تبويب ورقة العمل** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[تعيين لون علامة تبويب ورقة العمل](/cells/ar/net/set-worksheet-tab-color/).

{{% /alert %}}
