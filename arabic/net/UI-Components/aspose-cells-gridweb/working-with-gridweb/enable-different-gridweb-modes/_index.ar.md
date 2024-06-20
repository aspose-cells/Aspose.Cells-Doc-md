---
title: تمكين وضعيات مختلفة لتحكم GridWeb
type: docs
weight: 60
url: /ar/net/aspose-cells-gridweb/enable-different-gridweb-modes/
keywords: GridWeb,EditMode,SessionMode
description: يقدم هذا المقال كيفية العمل مع EditMode وSessionMode في GridWeb.
---

{{% alert color="primary" %}} 

 يصف هذا المقال أوضاع Aspose.Cells.GridWeb المختلفة. يتم تفصيل هذه الأوضاع بشكل منطقي بسبب ميزاتها وسلوكياتها المختلفة. لقد حددنا عدة أنواع من الأوضاع:

- وضع التحرير
- وضع العرض
- وضع الجلسة
- وضع بدون جلسة

كل هذه الأوضاع لها خصائصها الخاصة. يمكن للمطورين العمل مع Aspose.Cells.GridWeb في أي وضع وفقًا لاحتياجاتهم. سنلقي نظرة على كل وضع أدناه.

{{% /alert %}} 
## **وضع التحرير**
بشكل افتراضي، تكون عنصر التحكم Aspose.Cells.GridWeb في وضع التحرير. في وضع التحرير، يمكنك تحرير أو تعديل محتوى الجدول بالكامل باستخدام جميع الميزات التي يقدمها عنصر التحكم Aspose.Cells.GridWeb. تتضمن هذه الميزات:

- حفظ محتوى الجدول في ملفات Microsoft Excel.
- تقديم البيانات إلى خادم.
- حساب الصيغ.
- التراجع عن الإجراءات السابقة أو التخلص منها.
- إدارة الصفوف والأعمدة.
- قص ونسخ أو لصق البيانات.
- تنسيق الخلايا إلخ.

**عنصر التحكم GridWeb في وضع التحرير** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

يمكن للمطورين أيضًا التبديل إلى وضع التحرير بشكل برمجي عن طريق تعيين خاصية EditMode لعنصر التحكم GridWeb إلى true.

المثال أدناه يوضح كيفية تمكين وضع التحرير بشكل برمجي.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

عندما ينقر المستخدم على زر **التراجع**, يُعيد جعل GridWeb إلى حالته السابقة (الحالة قبل آخر عملية إرجاع إلى الخادم). إنه لا يلغي الإجراءات السابقة واحدة تلو الأخرى.

{{% /alert %}} 
## **وضع العرض**
عندما يكون عنصر تحكم GridWeb في وضع العرض، لا يمكن للمستخدمين تحرير أو تعديل محتوى الجدول، مما يعني أن المستخدمين يمكنهم فقط عرض محتوى الجدول. هذا هو السبب في تسمية هذا الوضع بوضع العرض. في وضع العرض، تكون بعض الأزرار (إرسال، حفظ والتراجع) مخفية والقائمة التي تظهر عند النقر بزر الماوس الأيمن تحتوي فقط على خيار النسخ.

عنصر تحكم GridWeb في وضع العرض 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

إذا كان المطورون يرغبون في أن يقوم مستخدموهم بعرض البيانات فقط، فيمكنهم التبديل إلى وضع العرض برمجياً عن طريق تعيين خاصية EditMode لعنصر تحكم GridWeb إلى قيمة خاطئة.

المثال أدناه يوضح كيفية تمكين وضع العرض برمجياً



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

حتى في وضع العرض، يمكن للمستخدمين تغيير ارتفاع وعرض الصفوف والأعمدة.

{{% /alert %}} 
## **وضع الجلسة**
يحتوي عنصر تحكم GridWeb في Aspose.Cells على بيانات الجدول في جلسة المستخدم لخادم الويب بين كل طلبات مستخدم الويب. يعني ذلك أن عنصر تحكم GridWeb يعمل دائمًا في وضع الجلسة افتراضيًا. ومع ذلك، إذا لم تكن تعمل في وضع الجلسة، فقم بتشغيله عن طريق تعيين خاصية SessionMode لعنصر تحكم GridWeb إلى SessionMode.Session.

المثال أدناه يوضح كيفية تمكين وضع الجلسة برمجيًا



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **وضع بدون جلسة**
لقد ناقشنا بالفعل أن نهج وضع الجلسة يوفر أفضل أداء من خلال استخدام جلسة مستخدم لتحميل وتخزين بيانات الجدول. ومع ذلك، فإنه يستهلك ذاكرة الخادم. لذا، إذا كان هناك عدد كبير من المستخدمين المتزامنين فإن مشاكل ذاكرة الوصول المتعدد قد تنشأ. لتوفير ذاكرة الخادم ودعم عدد كبير من المستخدمين المتزامنين، يُرجى النظر في وضع بدون جلسة.

يمكن تشغيل وضع بدون جلسة عن طريق تعيين خاصية SessionMode لعنصر تحكم GridWeb إلى SessionMode.ViewState.

المثال أدناه يوضح كيفية تمكين وضع بدون جلسة برمجيًا



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

مهم: عندما يتم تعيين خاصية SessionMode لـ GridWeb إلى SessionMode.ViewState، يقوم الجدول بتخزين البيانات في ViewState الصفحة. وهذا يعني أن الصفحة المقدمة أكبر، وتستهلك مزيداً من حركة المرور عبر الشبكة.

{{% /alert %}} {{% alert color="primary" %}} 

إذا كنت ترغب في استخدام خادم SQL أو StateServer للحفاظ على الجلسات، فاستخدم وضع الجلسة. يدعم عنصر تحكم GridWeb تسلسل بياناته إلى SQL Server أو StateServer.

يرجى التحقق من المقالة التالية لمزيد من المساعدة.

- [ عند عمل GridWeb عندما يكون وضع حالة جلسة ASP.NET هو SQL Server](/cells/ar/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
