---
title: تحقق من صحة ورقة العمل بأكملها بدلاً من الخلايا المحدثة فقط
type: docs
weight: 140
url: /ar/net/validate-entire-worksheet-instead-of-only-the-updated-cells/
---
## **سيناريوهات الاستخدام الممكنة**
بشكل افتراضي ، يتحقق GridWeb من صحة الخلايا المحدثة فقط ولا يتحقق من صحة ورقة العمل بأكملها. ومع ذلك ، إذا كنت تريد التحقق من صحة ورقة العمل بأكملها على جانب العميل قبل طلب نشر GridWeb إلى الخادم ، فيجب عليك تعيين متغير needValidateall داخل acwmain.js إلى true.
## **تحقق من صحة ورقة العمل بأكملها بدلاً من الخلايا المحدثة فقط**
تعرض لقطة الشاشة التالية متغير needValidateall في acwmain.js. يرجى تعيينها على "true" والآن سيقوم GridWeb بالتحقق من صحة ورقة العمل بأكملها وليس فقط الخلايا المحدثة.

![ما يجب القيام به: image_بديل_نص](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)
