---
title: تعيين لون علامة تبويب الورقة من Aspose.Cells
type: docs
weight: 20
url: /ar/net/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - تعيين لون علامة تبويب ورق العمل**
تسمح Aspose.Cells لك بتغيير لون علامات تبويب ورق العمل الفردية لتمييزها عن البقية. على سبيل المثال، يمكنك جعل تكاليف بلون أحمر، ومبيعات بلون أخضر، وأصول بلون أزرق، وما إلى ذلك.
### **ضبط لون علامة تبويب ورق العمل باستخدام Microsoft Excel**
1. انقر بزر الماوس الأيمن فوق علامة تبويب في ورقة العلامات في أسفل ورقة العمل الحالية.
1. حدد **لون العلامة التبويب**.
1. حدد لونًا من اللوحة.
1. انقر على **موافق**.

**C#**

{{< highlight cs >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the first worksheet in the book

Worksheet worksheet = workbook.Worksheets[0];

//Set the tab color

worksheet.TabColor = Color.Red;

//Save the Excel file

workbook.Save("AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **تعيين لون علامة تبويب ورق العمل** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [تعيين لون علامة تبويب ورق العمل](/cells/ar/net/set-worksheet-tab-color/).

{{% /alert %}}
