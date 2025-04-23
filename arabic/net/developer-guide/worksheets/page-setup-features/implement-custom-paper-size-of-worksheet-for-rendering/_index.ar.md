---
title: تنفيذ حجم ورق مخصص لورقة العمل للتقديم
type: docs
weight: 70
url: /ar/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: يوضح هذا المقال كيفية استخدام عينة الشيفرة C# API أو المكتبة .NET لتعيين حجم ورق مخصص للورقة المرغوبة عند تقديم ملف إكسل إلى تنسيق ملف PDF بشكل برمجي.
keywords: تعيين حجم ورق مخصص أثناء تحويل إكسيل إلى PDF باستخدام C#
---

## **سيناريوهات الاستخدام المحتملة**

لا توجد خيارات مباشرة متاحة لإنشاء أحجام ورق مخصصة في MS Excel، ومع ذلك، يمكنك تعيين حجم ورق مخصص للورقة المرغوبة عند تقديم ملف إكسل إلى تنسيق ملف PDF. يشرح هذا المستند كيفية تعيين حجم ورق مخصص لورقة العمل باستخدام واجهات برمجة التطبيقات لAspose.Cells.

## **تنفيذ حجم ورق مخصص لورقة العمل للتقديم**

Aspose.Cells تتيح لك تنفيذ حجم الورق المرغوب لورقة العمل. يمكنك استخدام الطريقة [**CustomPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize) للفئة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) لتحديد حجم الصفحة المخصص. يوضح الشيفرة المثالية التالية كيفية تحديد حجم ورق مخصص للصفحة الأولى في دفتر العمل. الرجاء رؤية [PDF الناتج](45056028.pdf) الذي تم إنشاؤه بالشيفرة التالية للإشارة.

## **لقطة شاشة**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
{{< app/cells/assistant language="csharp" >}}
