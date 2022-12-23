---
title: احصل على تحذيرات أثناء تحميل ملف Excel
type: docs
weight: 60
url: /ar/java/get-warnings-while-loading-excel-file/
---
## **سيناريوهات الاستخدام الممكنة**

يحاول المستخدم أحيانًا تحميل المصنف التالف إلى حد ما ولكنه قابل للتحميل. في مثل هذه الحالة ، يقوم Aspose.Cells بإصدار تحذيرات أثناء تحميل المصنف. يمكنك التقاط هذه التحذيرات من خلال تنفيذ**[IWarningCallback] (https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback)** الواجهة والإعداد**[LoadOptions.WarningCallback] (https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback)**خاصية.

## **احصل على تحذيرات أثناء تحميل ملف Excel**

 يوضح نموذج التعليمات البرمجية التالي كيفية الحصول على تحذيرات أثناء تحميل ملف Excel. يقوم الكود بتحميل ملف[نموذج ملف اكسل](sampleDuplicateDefinedName.xlsx) الذي يرمي**[DuplicateDefinedName] (https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME)** تحذير عند التحميل. هذا التحذير تم القبض عليه بعد ذلك**[IWarningCallback.Warning ()] (https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning (com.aspose.cells.WarningInfo))** طريقة طباعة رسائل التحذير على وحدة التحكم. ثم يحفظ الكود المصنف باسم[ملف اكسل الناتج](outputDuplicateDefinedName.xlsx)إذا قمت بفتح نموذج ملف Excel في Microsoft Excel ، فسوف يعرض لك أيضًا هذا التحذير كما هو موضح في لقطة الشاشة هذه. يرجى أيضًا التحقق من إخراج وحدة التحكم للرمز الوارد أدناه لمزيد من الفهم.

![ما يجب القيام به: image_بديل_نص](get-warnings-while-loading-excel-file_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **إخراج وحدة التحكم**

 هنا هو إخراج وحدة التحكم من الكود أعلاه عند تنفيذه مع المقدمة[نموذج ملف اكسل](sampleDuplicateDefinedName.xlsx).

{{< highlight "java" >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
