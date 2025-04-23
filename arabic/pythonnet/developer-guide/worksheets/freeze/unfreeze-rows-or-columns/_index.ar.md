---
title: إلغاء تجميد الصفوف أو الأعمدة
linktitle: إلغاء تجميد الأجزاء
type: docs
weight: 190
url: /ar/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: في هذا المقال، ستتعلم كيفية إلغاء تجميد الصفوف والأعمدة أو الألواح في أوراق عمل إكسل برمجياً باستخدام Aspose.Cells لـ Python via .NET APIs.
keywords: مكتبة إكسل بايثون، بايثون إلغاء تجميد الألواح، بايثون كيفية إلغاء تجميد الصفوف، بايثون كيفية إلغاء تجميد الأعمدة، بايثون كيفية إلغاء تجميد النافذة.
---

## **مقدمة**

في هذا المقال، سوف نتعلم كيفية إلغاء تجميد الصفوف، الأعمدة واللوحات. إذا تم تجميد أوراق العمل في ملفات Excel، نريد أحيانًا إلغاء تجميد ورقة العمل أو ضبط الصفوف والأعمدة أو اللوحات المجمدة.


## **كيفية إلغاء تجميد الصفوف أو الأعمدة في إكسل**

1. انقر على علامة التبويب عرض > تجميد الألواح > إلغاء تجميد الألواح.

**![إلغاء تجميد الألواح في إكسل](Unfreeze-Panes.png)**




## **كيفية إلغاء تجميد الصفوف، الأعمدة أو الألواح باستخدام Aspose.Cells لـ Python Excel Library**
من السهل إلغاء تجميد اللوحات مع Aspose.Cells لـ Python via .NET. يرجى استخدام طريقة [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) لإلغاء تجميد الألواح.

1. إنشاء ورقة عمل لفتح الملف المجمد.
2. إلغاء تجميد الألواح باستخدام طريقة Worksheet.UnFreezePanes().
3. حفظ الملف.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

المرفق [ملف إكسل عيني](Frozen.xlsx).
