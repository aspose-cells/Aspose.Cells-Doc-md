---
title: الحصول على تحذيرات أثناء تحميل ملف إكسل
type: docs
weight: 110
url: /ar/net/get-warnings-while-loading-excel-file/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان يحاول المستخدم تحميل دفتر العمل الذي يكون غير صالح إلى حد ما ولكنه قابل للتحميل. في مثل هذه الحالة، يقوم Aspose.Cells بإلقاء تحذيرات أثناء تحميل دفتر العمل. يمكنك التقاط هذه التحذيرات من خلال تنفيذ واجهة [**IWarningCallback**](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback) وتعيين خاصية [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback).

## **الحصول على تحذيرات أثناء تحميل ملف إكسل**

يشرح الكود العيني التالي كيفية الحصول على التحذيرات أثناء تحميل ملف Excel. يقوم الكود بتحميل [ملف Excel العيني](sampleDuplicateDefinedName.xlsx) الذي يلقي التحذير [**DuplicateDefinedName**](https://reference.aspose.com/cells/net/aspose.cells/warningtype) أثناء التحميل. بعد ذلك يتم التقاط هذا التحذير بواسطة الطريقة [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning) التي تطبع رسائل التحذير على وحدة التحكم. يتم حفظ دفتر العمل بعد ذلك كـ [ملف Excel الناتج](outputDuplicateDefinedName.xlsx). إذا قمت بفتح ملف Excel العيني في Microsoft Excel، سيعرض لك هذا التحذير كما هو موضح في هذا اللقط. يرجى أيضًا التحقق من إخراج وحدة التحكم للكود الناتج أدناه لمزيد من الفهم.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **مخرجات الوحدة**

إليك مخرجات وحدة التحكم للكود أعلاه عند تنفيذه مع [ملف إكسل عيني](sampleDuplicateDefinedName.xlsx) المقدم.

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
