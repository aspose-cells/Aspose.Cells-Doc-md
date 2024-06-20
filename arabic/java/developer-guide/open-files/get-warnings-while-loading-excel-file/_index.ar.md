---
title: الحصول على تحذيرات أثناء تحميل ملف إكسل
type: docs
weight: 60
url: /ar/java/get-warnings-while-loading-excel-file/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان يحاول المستخدم تحميل دفتر العمل الذي يكون غير صالح إلى حد ما ولكنه قابل للتحميل. في مثل هذه الحالة، يقوم Aspose.Cells بإلقاء تحذيرات أثناء تحميل دفتر العمل. يمكنك التقاط هذه التحذيرات من خلال تنفيذ واجهة [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) وتعيين خاصية [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback).

## **الحصول على تحذيرات أثناء تحميل ملف إكسل**

يشرح الكود العيني التالي كيفية الحصول على التحذيرات أثناء تحميل ملف Excel. يقوم الكود بتحميل [ملف Excel العيني](sampleDuplicateDefinedName.xlsx) الذي يلقي التحذير [**DuplicateDefinedName**](https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME) أثناء التحميل. بعد ذلك يتم التقاط هذا التحذير بواسطة الطريقة [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning(com.aspose.cells.WarningInfo)) التي تطبع رسائل التحذير على وحدة التحكم. يتم حفظ دفتر العمل بعد ذلك كـ [ملف Excel الناتج](outputDuplicateDefinedName.xlsx). إذا قمت بفتح ملف Excel العيني في Microsoft Excel، سيعرض لك هذا التحذير كما هو موضح في هذا اللقط. يرجى أيضًا التحقق من إخراج وحدة التحكم للكود الناتج أدناه لمزيد من الفهم.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **مخرجات الوحدة**

إليك مخرجات وحدة التحكم للكود أعلاه عند تنفيذه مع [ملف إكسل عيني](sampleDuplicateDefinedName.xlsx) المقدم.

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
