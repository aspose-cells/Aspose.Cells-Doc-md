﻿---
title: قائمة الصيغ
type: docs
weight: 10
url: /ar/reportingservices/formula-list/
---
**حقول التقرير**

|**اسم مجموعة** |**اسم الصيغة**|**وصف**|
|:- |:- |:- |
| المجالات العالمية| وقت التنفيذ| تاريخ ووقت بدء تشغيل التقرير.|
|| ReportServerUrl| عنوان URL لخادم التقارير الذي يتم تشغيل التقرير عليه.|
|| تقرير اسم|اسم التقرير كما تم تخزينه في قاعدة بيانات خادم التقارير.|
|| ReportFolder| المسار الكامل للمجلد الذي يحتوي على التقرير. لا يتضمن ذلك عنوان URL لخادم التقارير.|
| المستعمل| معرف المستخدم| معرّف المستخدم الذي يقوم بتشغيل التقرير.|
|| لغة| معرّف اللغة للمستخدم الذي يقوم بتشغيل التقرير.|
**حقول التقرير**

|**اسم مجموعة**|**وصف**|
|:- |:- |
| حدود| تحتوي مجموعة المعلمات على معلمات التقرير داخل التقرير. يمكن تمرير المعلمات إلى الاستعلامات أو استخدامها في عوامل التصفية أو استخدامها في وظائف أخرى تعمل على تغيير مظهر التقرير بناءً على المعلمة.|
| مجالات| تحتوي مجموعة الحقول على الحقول الموجودة ضمن مجموعة البيانات الحالية.|
| مجموعة البيانات||
**العاملين**
تُستخدم العوامل الحسابية لدمج الأرقام والمتغيرات الرقمية والحقول الرقمية والوظائف الرقمية للحصول على رقم آخر. تُستخدم عوامل المقارنة عادةً لمقارنة معاملات لشرط في بنية تحكم مثل عبارة If. تُستخدم العوامل المنطقية عادةً مع عوامل المقارنة لتوليد شروط لهياكل التحكم.

|**اسم مجموعة**|**اسم الصيغة**|**وصف**|
|:- |:- |:- |
| علم الحساب|^ | الأُس ، على سبيل المثال 2 ^ 3.|
||* | الضرب ، على سبيل المثال 2 * 3.|
||/ | التقسيم ، على سبيل المثال 2/3.|
||\\\ | قسم صحيح ، على سبيل المثال 2 \\\ 3.|
|| عصري| المعامل ، على سبيل المثال 4 Mod 3.|
||+ | الجمع ، على سبيل المثال 4 + 3.|
||- | الطرح ، على سبيل المثال 4 - 3.|
| مقارنة|< | أقل من ، على سبيل المثال 4< 3 false. |
||<= | أصغر من أو يساوي ، على سبيل المثال 4<= 3 false. |
||> | أكبر من ، على سبيل المثال 4> 3 صحيح.|
||>= | أكبر من أو يساوي ، على سبيل المثال 4> = 3 صحيح.|
||= | يساوي ، على سبيل المثال 4 = 3 خطأ.|
||<> | لا يساوي ، على سبيل المثال 4<> 3 صحيح.|
|| مثل|يقارن سلسلة بنمط. على سبيل المثال نتيجة = سلسلة مثل النمط.|
|| يكون| يقارن بين متغيرين مرجعيين للكائن ، على سبيل المثال asp is aspose.|
| سلسلة|& | يولد سلسلة سلسلة من تعبيرين.|
||+ | تجمع رقمين أو تُرجع القيمة الموجبة لتعبير رقمي. يمكن أيضًا استخدامها لسلسلة تعبيرين سلسلة.|
| منطقي / بت| و| ينفذ ارتباطًا منطقيًا على تعبيرين منطقيين ، أو اقتران بت على تعبيرين رقميين.|
|| لا| ينفذ نفيًا منطقيًا على تعبير منطقي أو نفي بت على تعبير رقمي.|
|| أو| ينفذ فصلًا منطقيًا على تعبيرين منطقيين ، أو فصل أحادي على تعبيرين رقميين.|
|| Xor| ينفذ استبعادًا منطقيًا على تعبيرين منطقيين ، أو استثناء بت على تعبيرين رقميين.|
|| و أيضا| ينفذ اقترانًا منطقيًا لدائرة قصر في تعبيرين.|
|| او اخرى|ينفذ فصلًا منطقيًا شاملاً للدائرة القصيرة على تعبيرين.|
| التحول قليلا|>> | ينفذ إزاحة حسابية لليسار على نمط بت.|
||<< | ينفذ إزاحة حسابية لليمين على نمط بت.|

