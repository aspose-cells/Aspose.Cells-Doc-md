---
title: البحث عما إذا كانت ورقة العمل هي ورقة حوار
type: docs
weight: 90
url: /ar/python-net/find-if-the-worksheet-is-dialog-sheet/
description: ورقة الحوار هي شكل قديم للورقة. توفر هذه المقالة تعليمات وكود عينة لتحديد برمجيًا ما إذا كانت ورقة العمل في إكسل هي ورقة حوار باستخدام مكتبة Aspose.Cells للبايثون via .NET
keywords: مكتبة برنامج إكسل للبايثون، العثور على نوع ورقة العمل لورقة الحوار، ورقة حوار في البايثون.
---

## **سيناريوهات الاستخدام المحتملة**

ورقة الحوار هي صيغة قديمة من الورقة تحتوي على مربع حوار. يمكن إدراج مثل هذه الورقة من قبل إصدار أقدم من Microsoft Excel مثل الإصدار 2003 كما هو موضح في هذه الصورة. يمكن أيضاً إدراجها باستخدام VBA في الإصدارات الأحدث مثل Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

يمكنك معرفة ما إذا كانت الورقة هي ورقة حوار أو نوع آخر من الورقة مع خاصية [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/) المُقدمة من Aspose.Cells للبايثون via .NET. إذا عادت قيمة تعدادية [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/) فهذا يعني أنك تتعامل مع ورقة حوار.

## **العثور على ورقة العمل هل هي ورقة حوار**

يحمل الكود العيني التالي الملف الإكسل العيني (64716820.xlsx) الذي يحتوي على ورقة حوار. يتحقق من الخاصية [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/)، يقارنها بـ [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/) ثم يطبع الرسالة. يرجى الاطلاع على مخرجات الكونسول في الكود العيني المعطى أدناه للمزيد من المساعدة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
