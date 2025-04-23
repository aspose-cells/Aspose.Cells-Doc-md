---
title: البحث عما إذا كانت ورقة العمل هي ورقة حوار
type: docs
weight: 100
url: /ar/java/find-if-the-worksheet-is-dialog-sheet/
---

## **سيناريوهات الاستخدام المحتملة**

ورقة الحوار هي تنسيق قديم للورقة التي تحتوي على مربع حوار. يمكن إدراج مثل هذه الورقة بواسطة إصدار أقدم من Microsoft Excel مثل 2003 كما هو موضح في لقطة الشاشة هذه. كما يمكن إدراجها مع VBA في الإصدارات الأحدث مثل Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

يمكنك معرفة ما إذا كانت الورقة هي ورقة حوار أو نوع آخر من الورقة باستخدام [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) خاصية المقدمة من Aspose.Cells. إذا عادت قيمة التعداد [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)، فإن ذلك يعني أنك تتعامل مع ورقة حوار.

## **العثور على ورقة العمل هل هي ورقة حوار**

يقوم الكود المصدري التالي بتحميل [ملف إكسل عيني](64716841.xlsx) الذي يحتوي على ورقة حوار. يقوم بفحص [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) الخاصية ويقارنها بـ [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG) ثم يقوم بطباعة الرسالة. يرجى الرجوع إلى إخراج الوحدة التحكم للكود المصدري العيني المعطى أدناه للحصول على مزيد من المساعدة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
