---
title: اضبط لون علامة تبويب ورقة العمل في xlsx4j
type: docs
weight: 60
url: /ar/java/set-worksheet-tab-color-in-xlsx4j/
---
## **Aspose.Cells - تعيين لون علامة تبويب ورقة العمل**
Aspose.Cells يسمح لك بتغيير لون علامات تبويب أوراق العمل الفردية لجعلها بارزة من البقية. على سبيل المثال ، يمكنك جعل المصاريف باللون الأحمر ، والمبيعات الخضراء ، والأصول زرقاء ، وما إلى ذلك.
### **ضبط لون علامة تبويب ورقة العمل باستخدام Microsoft Excel**
1. انقر بزر الماوس الأيمن فوق علامة تبويب في ورقة الجدولة أسفل ورقة العمل الحالية.
1. يختار**لون علامة التبويب**.
1. حدد لونًا من اللوحة.
1. انقر**نعم**.

**Java**

{{< highlight "java" >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataDir + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **تحميل كود الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/settabcolor/AsposeSetWorksheetTabColor.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[تعيين لون علامة تبويب ورقة العمل](/java/set-worksheet-tab-color).

{{% /alert %}}
