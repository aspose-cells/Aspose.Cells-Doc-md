---
title: تعيين لون علامة ورقة العمل في xlsx4j
type: docs
weight: 60
url: /ar/java/set-worksheet-tab-color-in-xlsx4j/
---

## **Aspose.Cells - تعيين لون علامة تبويب ورق العمل**
تسمح Aspose.Cells لك بتغيير لون علامات تبويب ورق العمل الفردية لتمييزها عن البقية. على سبيل المثال، يمكنك جعل تكاليف بلون أحمر، ومبيعات بلون أخضر، وأصول بلون أزرق، وما إلى ذلك.
### **ضبط لون علامة تبويب ورق العمل باستخدام Microsoft Excel**
1. انقر بزر الماوس الأيمن فوق علامة تبويب في ورقة العلامات في أسفل ورقة العمل الحالية.
1. حدد **لون العلامة التبويب**.
1. حدد لونًا من اللوحة.
1. انقر على **موافق**.

**Java**

{{< highlight java >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataDir + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/settabcolor/AsposeSetWorksheetTabColor.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [تعيين لون علامة ورقة العمل](/java/set-worksheet-tab-color).

{{% /alert %}}
