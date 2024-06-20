---
title: البحث عما إذا كانت ورقة العمل هي ورقة حوار
type: docs
weight: 90
url: /ar/net/find-if-the-worksheet-is-dialog-sheet/
description: ورقة الحوار هي صيغة قديمة من الورقة. تقدم هذه المقالة تعليمات وشرح الكود لتحديد برمجياً ما إذا كانت ورقة Excel هي ورقة حوار بواسطة واجهة برمجة التطبيقات C# أو مكتبة .NET.
keywords: العثور على نوع ورقة العمل من نوع حوار Excel باستخدام C#، ورقة حوار C#
---

## **سيناريوهات الاستخدام المحتملة**

ورقة الحوار هي صيغة قديمة من الورقة تحتوي على مربع حوار. يمكن إدراج مثل هذه الورقة من قبل إصدار أقدم من Microsoft Excel مثل الإصدار 2003 كما هو موضح في هذه الصورة. يمكن أيضاً إدراجها باستخدام VBA في الإصدارات الأحدث مثل Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

يمكنك معرفة ما إذا كانت الورقة ورقة حوارية أم نوعًا آخر من الأوراق بوجود خاصية [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type) المقدمة من Aspose.Cells. إذا عادت قيمة تعداد [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype)، فهذا يعني أنك تتعامل مع ورقة حوار.

## **العثور على ورقة العمل هل هي ورقة حوار**

يحمل الكود العيني التالي الملف الإكسل العيني (64716820.xlsx) الذي يحتوي على ورقة حوار. يتحقق من الخاصية [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)، يقارنها بـ [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) ثم يطبع الرسالة. يرجى الاطلاع على مخرجات الكونسول في الكود العيني المعطى أدناه للمزيد من المساعدة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
