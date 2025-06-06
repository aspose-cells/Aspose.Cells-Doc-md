---
title: شاشة مقسمة لورقة العمل في إكسيل
linktitle: شاشة مقسمة
type: docs
weight: 190
url: /ar/net/how-to-split-screen-of-excel-worksheet
description: في هذه المقالة، ستتعلم كيفية عرض صفوف معينة و/أو أعمدة في نوافذ منفصلة عن طريق تقسيم ورقة العمل إلى جزئين أو أربعة أجزاء برمجياً باستخدام مكتبة C# مع واجهة برمجة تطبيقات .NET.
keywords: تجميد الصفوف الأعلى، تجميد الصف الأعلى.
---

## **مقدمة**

في هذا المقال، سوف نتعلم كيفية عرض صفوف و/أو أعمدة معينة في لوحات منفصلة عن طريق تقسيم ورقة العمل إلى قسمين أو أربعة أجزاء. عند العمل مع مجموعات بيانات كبيرة، نحتاج إلى رؤية بعض المناطق من نفس ورقة العمل في وقت واحد لمقارنة مجموعات بيانات مختلفة. يمكن أن تلبي وظيفة الشاشة المقسمة احتياجاتك.

## **كيفية تقسيم الشاشة في إكسيل**
لتقسيم ورقة عمل إلى جزئين أو أربعة أجزاء، اتبع الخطوات التالية:

1. حدد الصف / العمود / الخلية قبل المكان الذي تريد وضع التقسيم فيه.
2. على علامة التبويب عرض، في مجموعة النوافذ، انقر فوق زر التقسيم.

**![شاشة مقسمة](Split-Screen.png)**

## **تقسيم ورقة العمل عمودياً على الأعمدة**

لفصل منطقتين في جدول البيانات بشكل عمودي، حدد العمود إلى اليمين من العمود الذي ترغب في ظهور التقسيم فيه، ثم انقر فوق زر التقسيم في Excel.

من السهل تقسيم جدول العمل عمودياً على الأعمدة بشكل برمجي باستخدام Aspose.Cells for .Net، نحتاج فقط إلى تحديد خلية واحدة في الصف العلوي كخلية نشطة، ثم
تقسيم باستخدام الطريقة [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

## **تقسيم ورقة العمل أفقياً على الصفوف**
لفصل نافذة Excel أفقياً، حدد الصف أسفل الصف الذي ترغب في ظهور التقسيم فيه في Excel.

من السهل تقسيم جدول العمل أفقياً على الصفوف بشكل برمجي باستخدام Aspose.Cells for .Net، نحتاج فقط إلى تحديد خلية واحدة في العمود الأيسر كخلية نشطة، ثم
تقسيم باستخدام الطريقة [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

## **تقسيم ورقة العمل إلى أربعة أجزاء**
لعرض أربعة أقسام مختلفة من نفس ورقة البيانات بشكل متزامن، قم بتقسيم الشاشة الخاصة بك عمودياً وأفقياً في Excel.

من السهل تقسيم جدول العمل عمودياً على الأعمدة بشكل برمجي باستخدام Aspose.Cells for .Net، نحتاج فقط إلى تحديد خلية واحدة ليست في الصف الأول والعمود الأول كخلية نشطة، ثم
تقسيم باستخدام الطريقة [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

## **كيفية إزالة التقسيم**
لإزالة تقسيم ورقة العمل، فقط انقر مرة أخرى فوق زر التقسيم.

توفر Aspose.Cells for .Net طريقة [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/) لإزالة إعداد التقسيم.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}
{{< app/cells/assistant language="csharp" >}}
