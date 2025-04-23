---
title: تعيين لون علامة تبويب الورقة من Aspose.Cells
type: docs
weight: 90
url: /ar/java/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - تعيين لون علامة تبويب ورق العمل**
تسمح Aspose.Cells لك بتغيير لون علامات تبويب ورق العمل الفردية لتمييزها عن البقية. على سبيل المثال، يمكنك جعل تكاليف بلون أحمر، ومبيعات بلون أخضر، وأصول بلون أزرق، وما إلى ذلك.
#### **ضبط لون علامة تبويب ورق العمل باستخدام Microsoft Excel**
1. انقر بزر الماوس الأيمن فوق علامة تبويب في ورقة العلامات في أسفل ورقة العمل الحالية.
1. حدد **لون العلامة التبويب**.
1. حدد لونًا من اللوحة.
1. انقر على **موافق**.

**Java**

{{< highlight java >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataPath + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **تحميل رمز التشغيل**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SetWorksheetTabColor.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [تعيين لون علامة ورقة العمل](/java/set-worksheet-tab-color).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
