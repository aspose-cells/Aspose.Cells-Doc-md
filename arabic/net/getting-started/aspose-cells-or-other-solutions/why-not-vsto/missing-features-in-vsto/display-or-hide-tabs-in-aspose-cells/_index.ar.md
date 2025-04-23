---
title: عرض أو إخفاء علامات تبويب في Aspose.Cells
type: docs
weight: 80
url: /ar/net/display-or-hide-tabs-in-aspose-cells/
---

{{% alert color="primary" %}} 

إذا نظرت عن كثب في أسفل ملف Microsoft Excel، سترى عددًا من الضوابط. تشمل هذه:

- ألسنة الصفحات.
- أزرار تمرير الألسنة.

تمثل ألسنة الصفحات الأوراق العمل في ملف الإكسل. انقر على أي علامة تبويب للانتقال إلى تلك الورقة العمل. كلما زاد عدد الأوراق العمل في الدفتر الحسابي، زادت ألسنة الصفحة. إذا كان لديك عدد جيد من الأوراق العمل في دفتر العمل، يلزمك الأزرار للتنقل خلالها. لذا، يوفر مايكروسوفت إكسل أزرار تمرير الألسنة للتمرير من خلال ألسنة الصفحات.

**علامات الورقة وأزرار تمرير العلامة التبويبية** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_1.png)

باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية علامات الجدول وأزرار التمرير في ملفات Excel. 

{{% /alert %}} 

أدناه مثال كامل يفتح ملف Excel (book1.xls)، يخفي علامات تبويبه ويحفظ الملف المعدل بوصفه output.xls.

يمكنك أن ترى أن ملف Book1.xls يحتوي على علامات تبويب في الشكل أدناه. بعد تنفيذ كود المثال، تم إخفاء الألسنة، كما يمكنك رؤية من لقطة الشاشة للملف output.xls أدناه.

**Book1.xls: ملف Excel قبل أي تعديل** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: ملف Excel بعد التعديل** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **السيطرة على عرض شريط التبويب**
**C#**

{{< highlight csharp >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
