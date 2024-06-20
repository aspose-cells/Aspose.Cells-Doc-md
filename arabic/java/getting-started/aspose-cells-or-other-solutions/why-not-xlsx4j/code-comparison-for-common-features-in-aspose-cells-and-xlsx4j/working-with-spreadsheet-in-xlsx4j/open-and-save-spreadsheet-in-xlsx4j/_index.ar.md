---
title: فتح وحفظ جدول بيانات في xlsx4j
type: docs
weight: 40
url: /ar/java/open-and-save-spreadsheet-in-xlsx4j/
---

## **Aspose.Cells - فتح وحفظ جدول بيانات**
يستخدم المطورون Aspose.Cells لفتح الملفات لأغراض مختلفة. على سبيل المثال، فتح ملف لاسترجاع البيانات منه، أو استخدام ملف تصميم جدول بيانات محدد مسبقًا لتسريع عملية التطوير الخاصة بك. تسمح Aspose.Cells للمطورين بفتح أنواع مختلفة من الملفات الأصلية وهذه الملفات الأصلية يمكن أن تكون تقارير Microsoft Excel، SpreadsheetML، ملفات CSV أو ملفات محددة بفواصل. 

**تُتيح Aspose.Cells للمطورين إنشاء ملفات Excel من البداية باستخدام واجهة برمجة التطبيقات المرنة الخاصة بها. بمجرد أن تنشئ ملفات Excel، فإنه سيتعين عليك أيضًا حفظ سجل العمل الخاص بك (الملف). توفر Aspose.Cells مجموعة متنوعة من الطرق لحفظ هذه الملفات.

**Java**

{{< highlight java >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j - فتح وحفظ جدول بيانات**
المثال أدناه يوضح كيفية فتح وحفظ جداول البيانات باستخدام xlsx4j.

**Java**

{{< highlight java >}}

 String inputfilepath  = dataDir + "pivot.xlsm";

boolean save = true;

String outputfilepath = dataDir + "pivot-rtt-xlsx4j.xlsm";

// Open a document from the file system

// 1. Load the Package

OpcPackage pkg = OpcPackage.load(new java.io.File(inputfilepath));

// Save it

if (save) {

    SaveToZipFile saver = new SaveToZipFile(pkg);

    saver.save(outputfilepath);

}

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/opensavespreadsheet)
