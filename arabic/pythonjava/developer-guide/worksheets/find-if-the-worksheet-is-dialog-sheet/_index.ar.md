---
title: البحث عما إذا كانت ورقة العمل هي ورقة حوار
type: docs
weight: 70
url: /ar/python-java/find-if-the-worksheet-is-dialog-sheet/
---

## **سيناريوهات الاستخدام المحتملة**
ورقة الحوار هي تنسيق قديم للورقة التي تحتوي على مربع حوار. يمكن إدراج مثل هذه الورقة بواسطة إصدار أقدم من Microsoft Excel مثل 2003 كما هو موضح في لقطة الشاشة هذه. كما يمكن إدراجها مع VBA في الإصدارات الأحدث مثل Microsoft Excel 2016.

![todo:image_alt_text](DialogSheet.png)
## **العثور على ورقة العمل هل هي ورقة حوار**
يوفر Aspose.Cells for Python via Java لك القدرة على التحقق مما إذا كانت ورقة العمل هي ورقة حوار. لهذا يوفر خاصية [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type). إذا كانت [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type) تُرجع قيمة تصنيف [SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG)، فهذا يعني أنك تتعامل مع ورقة حوار.

يوضح مقتطف الكود التالي كيفية التحقق من ورقة حوار. يُظهر الناتج المُنشأ من الكود في وحدة التحكم كما هو موضح أدناه للرجوع إليه.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **مخرجات الوحدة**
{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
