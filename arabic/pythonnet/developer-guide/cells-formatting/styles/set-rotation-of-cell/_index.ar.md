---
title: كيفية دوران نص الخلية
type: docs
weight: 80
url: /ar/python-net/how-to-rotate-text-of-cell/
description: رمز C# لتدوير نص الخلية باستخدام Aspose.Cells لبايثون via .NET API
keywords: بايثون لتدوير نص الخلية، تدوير نص الخلية برمجياً في أحد دفاتر العمل، ضبط زاوية تدوير الخلية برمجياً، كيف تدور نص الخلية في إكسل باستخدام بايثون
---

## **تدوير نص الخلية في Aspose.Cells لبايثون via .NET**

Aspose.Cells لبايثون via .NET هو مكون قوي يعمل مع .NET و Java يتيح للمطورين العمل مع جداول البيانات من خلال البرمجة. إحدى الميزات التي يقدمها Aspose.Cells لبايثون via .NET هي القدرة على تدوير الخلايا، مما يسمح لك بتخصيص اتجاه النص وتحسين العرض البصري لبياناتك. في هذا المستند، سنستكشف كيفية تدوير الخلايا باستخدام Aspose.Cells لبايثون via .NET.

## **كيفية تدوير نص الخلية في إكسل**
يمكنك تدوير خلية في إكسل باستخدام الخطوات التالية:
1. افتح برنامج إكسل وحدد الخلية أو مجموعة من الخلايا التي ترغب في تدويرها.
1. انقر بزر الماوس الأيمن على الخلية(الخلايا) المحددة واختر "تنسيق الخلايا" من قائمة السياق. بالإضافة إلى ذلك، يمكنك الانتقال إلى علامة التبويب "الرئيسية" في شريط أدوات إكسل، انقر على القائمة المنسدلة "تنسيق" في مجموعة "الخلايا"، واختر "تنسيق الخلايا".
1. في مربع حوار "تنسيق الخلايا"، انتقل إلى علامة التبويب "توجيه".
1. في قسم "التوجيه"، سترى خيارات لتدوير النص. يمكنك إدخال زاوية التدوير المرغوبة مباشرة في مربع "الدرجات". القيم الإيجابية تدور النص باتجاه عقارب الساعة، والقيم السالبة تدور به عكس اتجاه عقارب الساعة.
<br>
![todo:image_alt_text](alignment.png)
1. بمجرد اختيار الدورة المرغوبة، انقر على "موافق" لتطبيق التغييرات. ستتم إعادة تدوير الخلية(الخلايا) المحددة الآن استنادًا إلى زاوية التدوير أو التوجيه التي اخترتها.

## **كيفية تدوير نص الخلية باستخدام Aspose.Cells لبايثون via .NET API**

تجعل خاصية [**Style.rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) من السهل تدوير الخلايا. لتدوير الخلايا في Aspose.Cells لبايثون via .NET، عليك اتباع هذه الخطوات:
1. تحميل دفتر العمل في إكسل
<br>
أولاً، تحتاج إلى تحميل دفتر العمل Excel باستخدام Aspose.Cells لبايثون via .NET. يمكنك استخدام فئة Workbook لفتح ملف Excel موجود أو إنشاء واحد جديد. 

1. الوصول إلى ورقة البيانات
<br>
بمجرد تحميل دفتر العمل، ستحتاج إلى الوصول إلى ورقة البيانات التي ترغب في تدوير الخلايا فيها. يمكنك الوصول إما إلى ورقة البيانات بمؤشرها أو اسمها. 

1. تدوير نص الخلية
<br>
الآن بعد أن لديك وصول إلى ورقة البيانات، يمكنك تدوير الخلايا عن طريق تعديل كائن الأنماط (Style) للخلايا المرغوبة. كائن الأنماط يسمح لك بتعيين مجموعة متنوعة من خيارات التنسيق، بما في ذلك التدوير. 

1. حفظ دفتر العمل
<br>
بعد تدوير الخلايا، يمكنك حفظ دفتر العمل المعدل مرة أخرى في ملف أو تيار باستخدام طريقة الحفظ.

## **كود عينة بايثون**

يرجى رؤية الكود التالي، فهو ينشئ كائن دفتر العمل ويضبط زوايا تدوير مختلفة لعدة خلايا. يوضح اللقطة الشاشة النتيجة بعد تنفيذ الكود العيني.
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Cells-rotate-text.py" >}}

