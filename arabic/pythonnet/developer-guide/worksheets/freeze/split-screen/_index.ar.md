---
title: شاشة مقسمة لورقة العمل في إكسيل
linktitle: شاشة مقسمة
type: docs
weight: 190
url: /ar/python-net/how-to-split-screen-of-excel-worksheet
description: في هذا المقال، ستتعلم كيفية عرض صفوف و/أو أعمدة معينة في ألواح منفصلة عن طريق تقسيم ورقة العمل إلى جزأين أو أربعة أجزاء برمجياً باستخدام Aspose.Cells لـ Python via .NET APIs.
keywords: مكتبة إكسل بايثون، بايثون تجميد الصفوف العلوية، بايثون تجميد الصف العلوي، بايثون تقسيم ورقة العمل عمودياً على الأعمدة، بايثون تقسيم ورقة العمل أفقياً على الصفوف، بايثون تقسيم ورقة العمل إلى أربعة أجزاء، بايثون كيفية إزالة التقسيم.
---

## **مقدمة**

في هذا المقال، سوف نتعلم كيفية عرض صفوف و/أو أعمدة معينة في لوحات منفصلة عن طريق تقسيم ورقة العمل إلى قسمين أو أربعة أجزاء. عند العمل مع مجموعات بيانات كبيرة، نحتاج إلى رؤية بعض المناطق من نفس ورقة العمل في وقت واحد لمقارنة مجموعات بيانات مختلفة. يمكن أن تلبي وظيفة الشاشة المقسمة احتياجاتك.

## **كيفية تقسيم الشاشة في إكسيل**
لتقسيم ورقة عمل إلى جزئين أو أربعة أجزاء، اتبع الخطوات التالية:

1. حدد الصف / العمود / الخلية قبل المكان الذي تريد وضع التقسيم فيه.
2. على علامة التبويب عرض، في مجموعة النوافذ، انقر فوق زر التقسيم.

**![شاشة مقسمة](Split-Screen.png)**

## **كيفية تقسيم ورقة العمل عمودياً على الأعمدة**

لفصل منطقتين في جدول البيانات بشكل عمودي، حدد العمود إلى اليمين من العمود الذي ترغب في ظهور التقسيم فيه، ثم انقر فوق زر التقسيم في Excel.

من السهل تقسيم ورقة العمل عمودياً على الأعمدة برمجياً باستخدام Aspose.Cells لـ Python via .NET، نحتاج فقط إلى اختيار خلية واحدة في الصف العلوي كخلية نشطة، ثم
تقسيم باستخدام الطريقة [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Vertically-Split.py" >}}

## **كيفية تقسيم ورقة العمل أفقياً على الصفوف**
لفصل نافذة Excel أفقياً، حدد الصف أسفل الصف الذي ترغب في ظهور التقسيم فيه في Excel.

من السهل تقسيم ورقة العمل أفقياً على الصفوف برمجياً باستخدام Aspose.Cells لـ Python via .NET، نحتاج فقط إلى اختيار خلية واحدة في العمود الأيسر كخلية نشطة، ثم
تقسيم باستخدام الطريقة [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Horizontally-Split.py" >}}

## **كيفية تقسيم ورقة العمل إلى أربعة أجزاء**
لعرض أربعة أقسام مختلفة من نفس ورقة البيانات بشكل متزامن، قم بتقسيم الشاشة الخاصة بك عمودياً وأفقياً في Excel.

من السهل تقسيم ورقة العمل عمودياً على الأعمدة برمجياً باستخدام Aspose.Cells لـ Python via .NET، نحتاج فقط إلى اختيار خلية واحدة غير موجودة في الصف الأول والعمود الأول كخلية نشطة، ثم
تقسيم باستخدام الطريقة [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Split-Four.py" >}}

## **كيفية إزالة التقسيم**
لإزالة تقسيم ورقة العمل، فقط انقر مرة أخرى فوق زر التقسيم.

توفر Aspose.Cells لـ Python via .NET طريقة [**Worksheet.remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split/) لإزالة إعدادات التقسيم.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Remove-Split.py" >}}
