---
title: احصل على تحذيرات أثناء تحميل ملف Excel
type: docs
weight: 110
url: /ar/net/get-warnings-while-loading-excel-file/
---
## **سيناريوهات الاستخدام الممكنة**

يحاول المستخدم أحيانًا تحميل المصنف التالف إلى حد ما ولكنه قابل للتحميل. في مثل هذه الحالة ، يقوم Aspose.Cells بإصدار تحذيرات أثناء تحميل المصنف. يمكنك التقاط هذه التحذيرات من خلال تنفيذ**[IWarningCallback] (https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback)** الواجهة والإعداد**[LoadOptions.WarningCallback] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback)**خاصية.

## **احصل على تحذيرات أثناء تحميل ملف Excel**

 يوضح نموذج التعليمات البرمجية التالي كيفية الحصول على تحذيرات أثناء تحميل ملف Excel. يقوم الكود بتحميل ملف[نموذج ملف اكسل](sampleDuplicateDefinedName.xlsx) الذي يرمي**[DuplicateDefinedName] (https://reference.aspose.com/cells/net/aspose.cells/warningtype)** تحذير عند التحميل. هذا التحذير تم القبض عليه بعد ذلك**[IWarningCallback.Warning ()] (https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning)** طريقة طباعة رسائل التحذير على وحدة التحكم. ثم يحفظ الكود المصنف باسم[ملف اكسل الناتج](outputDuplicateDefinedName.xlsx)إذا قمت بفتح نموذج ملف Excel في Microsoft Excel ، فسوف يعرض لك أيضًا هذا التحذير كما هو موضح في لقطة الشاشة هذه. يرجى أيضًا التحقق من إخراج وحدة التحكم للرمز الوارد أدناه لمزيد من الفهم.

![ما يجب القيام به: image_بديل_نص](get-warnings-while-loading-excel-file_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **إخراج وحدة التحكم**

 هنا هو إخراج وحدة التحكم من الكود أعلاه عند تنفيذه مع المقدمة[نموذج ملف اكسل](sampleDuplicateDefinedName.xlsx).

{{< highlight "java" >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
