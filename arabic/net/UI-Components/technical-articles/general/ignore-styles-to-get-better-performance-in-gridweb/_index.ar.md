---
title: تجاهل الأنماط للحصول على أداء أفضل في GridWeb
type: docs
weight: 1060
url: /ar/net/aspose-cells-gridweb/ignorestylewithnodata
description: توضح هذه المقالة كيفية استخدام IgnoreStyleWithNoData للحصول على أداء أفضل لمكتبة Aspose.Cells.GridWeb.
keywords: performance
---
## **سيناريوهات الاستخدام الممكنة**
 يرجى استخدام[GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata)الخاصية لتحميل عدد أقل من الصفوف / الأعمدة المطلوبة من المصنف.
 
## **احصل على أداء أفضل أثناء تحميل المصنف**
 رجاء تاكد من[نموذج ملف اكسل](largerowswithstyle.xlsx) 

عند تعيين IgnoreStyleWithNoData = صحيح ؛

كما ترى ، فإنه يعرض الصفوف (إلى 15) والأعمدة (إلى L) ، ولن يعرض آخر الصفوف والأعمدة المستمرة بدون بيانات في الخلايا ، وبالتالي سيكون وقت التحميل أقل.

![المصنف بنمط التجاهل](ignorestyletrue.png)


عند تعيين IgnoreStyleWithNoData = false ؛ (القيمة الافتراضية هي false)

كما ترى ، فإنه يعرض عددًا أكبر من الصفوف (حتى 500) والأعمدة (إلى تشيكوسلوفاكيا)

من الصف 16 إلى الصف 500 ، قامت بعض الخلايا بتعيين نمط boder ، لكن الخلايا لا تحتوي على بيانات.

من العمود M إلى العمود CZ ، قامت بعض الخلايا بتعيين نمط boder ، لكن الخلايا لا تحتوي على بيانات.

![المصنف دون تجاهل النمط](ignorestylefalse.png)
 
 
 