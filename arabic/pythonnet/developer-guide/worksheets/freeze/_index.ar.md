---
title: تجميد الأجزاء في ورقة العمل Excel
linktitle: تجميد الأجزاء
type: docs
weight: 190
url: /ar/python-net/how-to-freeze-panes-of-excel-worksheet
description: في هذه المقالة، ستتعلم كيفية تثبيت البنرات في أوراق العمل في إكسل برمجيًا باستخدام واجهات برمجة التطبيقات Aspose.Cells للبايثون via .NET
keywords: مكتبة برنامج إكسل للبايثون، تثبيت البنرات في الإكسيل، تثبيت النافذة في البايثون.
---

## **مقدمة**

في هذا المقال، سنتعلم كيفية تثبيت الأجزاء. عندما تكون لديك كمية كبيرة من البيانات تحت عنوان مشترك، لا يمكنك رؤية العنوان عند التمرير في الورقة. وكل سجل يحتوي على العديد من البيانات. يمكنك تثبيت الأجزاء حتى تتمكن من رؤية تلك الجزء المثبت حتى عندما يتم التمرير في باقي البيانات. يمكنك رؤية الرءوس بسهولة في الصفوف العليا أو الأعمدة الأولى. تثبيت الأجزاء وإلغاء تثبيتها يغيران فقط عرض البيانات دون تغيير البيانات نفسها.

## **كيفية تثبيت البنرات في إكسيل**

**![تجميد الأجزاء في إكسل](Freeze-panes.png)**


1. إذا كنت تريد تجميد الأجزاء، تجميد الصفوف والأعمدة، فحدد أولاً خلية (مثل B2) 
2. انقر على عرض > تجميد الأجزاء.
3. في القائمة المنسدلة، انقر على تجميد الأجزاء.
4. إذا قمت بالتمرير إلى أسفل أو اليمين، فإن الصف الأول والعمود مجمدان.

**![تجميد الأجزاء](Frozen-Panes.png)**

كما يمكنك رؤية الصف الأول والعمود A من التجميد، الصف الثاني هو 32 والعمود المرئي الثاني هو D. 

تتيح لك تجميد الأجزاء رؤية البيانات الكبيرة دون الحاجة لتتبع تسمية الصف أو العمود.




## **كيفية تثبيت البنرات باستخدام مكتبة Aspose.Cells للبايثون لإكسيل**
من السهل تثبيت البنرات مع Aspose.Cells للبايثون via .NET. يرجى استخدام الطريقة [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) لتثبيت البنرات عند الخلية المحددة.
1. إنشاء دفتر العمل لفتح الملف أو إنشاء ملف فارغ.
2. تجميد الألواح باستخدام الطريقة Worksheet.FreezePanes().
3. حفظ الملف.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Pane.py" >}}

المرفق [ملف الإكسيل عينة](Freeze.xlsx).
