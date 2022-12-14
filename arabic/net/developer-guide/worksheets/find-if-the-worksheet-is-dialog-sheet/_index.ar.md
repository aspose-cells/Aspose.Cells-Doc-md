---
title: اكتشف ما إذا كانت ورقة العمل هي ورقة حوار
type: docs
weight: 90
url: /ar/net/find-if-the-worksheet-is-dialog-sheet/
---
## **سيناريوهات الاستخدام الممكنة**

ورقة الحوار هي تنسيق قديم للورقة يحتوي على مربع حوار. يمكن إدراج هذه الورقة بواسطة إصدار أقدم من Microsoft Excel ، على سبيل المثال 2003 كما هو موضح في لقطة الشاشة هذه. يمكن أيضًا إدراجه مع VBA في الإصدارات الأحدث مثل Microsoft Excel 2016.

![ما يجب القيام به: image_بديل_نص](find-if-the-worksheet-is-dialog-sheet_1.png)

يمكنك معرفة ما إذا كانت الورقة عبارة عن ورقة حوار أو نوع آخر من الأوراق به[**نوع ورقة العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)تم توفير الخاصية بواسطة Aspose.Cells. إذا تم إرجاع قيمة التعداد[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype)اذن هذا يعني انك تتعامل مع ورقة حوار.

## **اكتشف ما إذا كانت ورقة العمل هي ورقة حوار**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](64716820.xlsx) الذي يحتوي على ورقة حوار. يتحقق من ملف[**نوع ورقة العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)الممتلكات تقارن مع[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) ثم يطبع الرسالة. يرجى الاطلاع على إخراج وحدة التحكم لعينة التعليمات البرمجية الواردة أدناه للحصول على مزيد من المساعدة.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
