---
title: افتح واحفظ جدول البيانات في xlsx4j
type: docs
weight: 40
url: /ar/java/open-and-save-spreadsheet-in-xlsx4j/
---
## **Aspose.Cells - فتح وحفظ جدول البيانات**
يستخدم المطورون Aspose.Cells لفتح الملفات لأغراض مختلفة. على سبيل المثال ، افتح ملفًا لاسترداد البيانات منه ، أو استخدم ملف جدول بيانات مصمم مسبقًا لتسريع عملية التطوير لديك. Aspose.Cells يسمح للمطورين بفتح أنواع مختلفة من الملفات المصدر. يمكن أن تكون ملفات المصدر هذه Microsoft تقارير Excel أو SpreadsheetML أو CSV أو ملفات محددة بعلامات جدولة.

**Aspose.Cells**يسمح للمطورين بإنشاء ملفات Excel من البداية باستخدام API. بمجرد إنشاء ملفات Excel ، ستحتاج أيضًا إلى حفظ المصنف الخاص بك (ملف). يوفر Aspose.Cells طرقًا متنوعة لحفظ هذه الملفات.

**Java**

{{< highlight "java" >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j - فتح وحفظ جدول البيانات**
يوضح المثال أدناه كيفية فتح جداول البيانات وحفظها أثناء استخدام xlsx4j.

**Java**

{{< highlight "java" >}}

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
## **تحميل كود الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/opensavespreadsheet)
