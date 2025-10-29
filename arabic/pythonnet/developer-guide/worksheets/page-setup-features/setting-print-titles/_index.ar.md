---
title: تعيين عناوين الطباعة باستخدام Python.NET
linktitle: تعيين عناوين الطباعة
type: docs
weight: 200
url: /ar/python-net/how-to-set-print-titles/
description: تعرف على كيفية تكوين رؤوس الصفوف/الأعمدة المتكررة على صفحات الطباعة باستخدام Aspose.Cells for Python via .NET.
keywords: تكرار رؤوس الطباعة في بايثون، تعيين عناوين الطباعة في بايثون، مسح عناوين الطباعة في بايثون، إعداد صفحة إكسل في بايثون، طباعة أوراق العمل باستخدام Python.NET
---

## **سيناريوهات الاستخدام المحتملة**

ضبط عناوين الطباعة في إكسل يضمن تكرار صفوف أو أعمدة معينة في كل صفحة مطبوعة، وهو مفيد بشكل خاص للجداول الكبيرة التي تمتد عبر صفحات متعددة. إليك بعض الأسباب التي قد تدفعك لضبط عناوين الطباعة:

1. تحسين قابلية القراءة: تساعد عناوين الطباعة القراء على فهم البيانات من خلال إبقاء العناوين مرئية على جميع الصفحات، مما يجعل من الأسهل تفسير المعلومات على كل صفحة دون الحاجة للرجوع إلى الصفحة الأولى.

1. تقديم مظهر احترافي: عرض العناوين أو التسميات بشكل متكرر على كل صفحة يخلق مظهرًا أكثر أناقة واحترافية للمستندات المطبوعة.

1. تحسين التنقل: بالنسبة للمستندات التي تحتوي على بيانات موسعة، يساعد تكرار العناوين في كل صفحة على التنقل بسرعة والوصول إلى المعلومات، ويقلل من الحاجة للرجوع بين الصفحات.

1. تقليل الأخطاء: عندما تكون العناوين موجودة على كل صفحة، يقل احتمال سوء التفسير أو أخطاء الإدخال، حيث يمكن للمستخدمين رؤية سياق البيانات بسهولة.

1. التناسق: ضمان أن المعلومات المهمة، مثل عناوين الأعمدة أو تسميات الصفوف، دائمًا مرئية يحافظ على التناسق والوضوح Throughout المستند.

## **كيفية ضبط عناوين الطباعة في إكسل**

 لضبط عناوين الطباعة في إكسل، اتبع الخطوات التالية:

1. افتح علامة تبويب تخطيط الصفحة: انقر على علامة التبويب "تخطيط الصفحة" في الشريط أعلى نافذة إكسل.
1. الوصول إلى عناوين الطباعة: في مجموعة "إعداد الصفحة"، انقر على "عناوين الطباعة".
1. تعيين الصفوف للتكرار: في مربع حوار "إعداد الصفحة"، انتقل إلى علامة التبويب "ورقة». في قسم "عناوين الطباعة"، حدد الصفوف التي تريد تكرارها في الأعلى بالنقر على المربع بجانب "تكرار الصفوف في أعلى" واختيار الصفوف التي تريد تكرارها.
1. تعيين الأعمدة للتكرار (إن لزم الأمر): بالمثل، يمكنك تحديد الأعمدة للتكرار على اليسار عن طريق النقر على المربع بجانب "تكرار الأعمدة على اليسار" واختيار الأعمدة التي تريد تكرارها.
<br>
<img src="3.png" width=60% />

1. أكد والطباعة: انقر على "موافق" لتطبيق الإعدادات. عند طباعة ورقة العمل، ستظهر الصفوف أو الأعمدة المحددة على كل صفحة مطبوعة.

## **كيفية مسح عناوين الطباعة في إكسل**

لمسح عناوين الطباعة في إكسل، تحتاج إلى إزالة الصفوف أو الأعمدة التي تم تعيينها للتكرار على كل صفحة مطبوعة. إليك الطريقة:

1. افتح علامة تبويب تخطيط الصفحة: انقر على علامة التبويب "تخطيط الصفحة" في الشريط أعلى نافذة إكسل.
1. الوصول إلى عناوين الطباعة: في مجموعة "إعداد الصفحة"، انقر على "عناوين الطباعة".
1. مسح عناوين الطباعة: في مربع حوار "إعداد الصفحة"، انتقل إلى علامة التبويب "ورقة". امسح مربعات النص لـ "الصفوف لإعادة التكرار في الأعلى" و"الأعمدة لإعادة التكرار على اليسار" عن طريق حذف أي محتوى داخلها.
<br>
<img src="4.png" width=60% />

1. أكد وأغلق: انقر على "موافق" لتطبيق التغييرات.

## **كيفية تعيين عناوين الطباعة باستخدام Aspose.Cells**

لتعيين عناوين الطباعة في ورقة عمل محددة: أولاً، حمّل [ملف العينة](input.xlsx)، ثم قم بتعديل خصائص [**Worksheet.page_setup.print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows/) و [**Worksheet.page_setup.print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) لكائن [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/). سيساعد تعيين هذه الخصائص إلى سلسلة نطاق على تكوين عناوين الطباعة.

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set row 1 as repeating header
worksheet.page_setup.print_title_rows = "$1:$1"

# Save modified workbook
workbook.save("output.xlsx")
```

نتيجة الإخراج:
<br>
<img src="1.png" width=60% />

## **لمسح عناوين الطباعة باستخدام Aspose.Cells**

لمسح عناوين الطباعة، قم بضبط خصائص عنوان الطباعة إلى سلاسل فارغة:

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Clear existing print titles
worksheet.page_setup.print_title_rows = ""
worksheet.page_setup.print_title_columns = ""

# Save modified workbook
workbook.save("output.xlsx")
```

نتيجة الإخراج:
<br>
<img src="2.png" width=60% />

```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Set rows to repeat at the top (e.g., rows 1 and 2)
worksheet.page_setup.print_title_rows = "$1:$2"

# Set columns to repeat at the left (e.g., columns A and B)
worksheet.page_setup.print_title_columns = "$A:$B"

# Save the workbook
workbook.save("set_print_titles.pdf")
```
```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Clear the rows and columns set to repeat
worksheet.page_setup.print_title_rows = ""
worksheet.page_setup.print_title_columns = ""

# Save the workbook
workbook.save("clear_print_titles.pdf")
```
{{< app/cells/assistant language="python-net" >}}
