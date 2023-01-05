---
title: عرض أو إخفاء علامات التبويب في Aspose.Cells
type: docs
weight: 80
url: /ar/net/display-or-hide-tabs-in-aspose-cells/
---
{{% alert color="primary" %}} 

إذا نظرت عن كثب إلى الجزء السفلي من ملف Excel Microsoft ، فسترى عددًا من عناصر التحكم. وتشمل هذه:

- علامات تبويب الأوراق.
- أزرار التمرير لعلامة التبويب.

تمثل علامات تبويب الأوراق أوراق العمل في ملف Excel. انقر فوق أي علامة تبويب للتبديل إلى ورقة العمل هذه. كلما زاد عدد أوراق العمل في المصنف ، زاد عدد علامات تبويب الأوراق. إذا كان ملف Excel يحتوي على عدد جيد من أوراق العمل ، فأنت بحاجة إلى أزرار للتنقل خلالها. لذلك ، يوفر Microsoft Excel أزرار تمرير علامة التبويب للتمرير عبر علامات تبويب الأوراق.

**علامات تبويب الأوراق وأزرار التمرير لعلامة التبويب** 

![ما يجب القيام به: image_بديل_نص](display-or-hide-tabs-in-aspose-cells_1.png)

باستخدام Aspose.Cells ، يمكن للمطورين التحكم في رؤية علامات تبويب الأوراق وأزرار تمرير علامات التبويب في ملفات Excel.

{{% /alert %}} 

يوجد أدناه مثال كامل يفتح ملف Excel (book1.xls) ، ويخفي علامات التبويب الخاصة به ويحفظ الملف المعدل كـ output.xls.

يمكنك أن ترى أن ملف Book1.xls يحتوي على علامات تبويب في الشكل أدناه. بعد تنفيذ رمز المثال ، يتم إخفاء علامات التبويب ، كما ترى من لقطة شاشة ملف output.xls أدناه.

**book1.xls: ملف Excel قبل أي تعديل** 

![ما يجب القيام به: image_بديل_نص](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: ملف Excel بعد التعديل** 

![ما يجب القيام به: image_بديل_نص](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **التحكم في عرض شريط الجدولة**
**C#**

{{< highlight "csharp" >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
