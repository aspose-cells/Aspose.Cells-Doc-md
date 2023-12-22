---
title: التحقق من صحة ورقة العمل بأكملها بدلاً من الخلايا المحدثة فقط
type: docs
weight: 80
url: /ar/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---
##  **سيناريوهات الاستخدام المحتملة**
افتراضيًا، يقوم GridWeb بالتحقق من صحة الخلايا المحدثة فقط ولا يتحقق من صحة ورقة العمل بأكملها. ومع ذلك، إذا كنت تريد التحقق من صحة ورقة العمل بأكملها من جانب العميل قبل أن يقوم GridWeb بنشر الطلب إلى الخادم، فيجب عليك تعيين المتغير needValidateall داخل acwmain.js إلى true.
##  **التحقق من صحة ورقة العمل بأكملها بدلاً من الخلايا المحدثة فقط**
تعرض لقطة الشاشة التالية المتغير needValidateall في acwmain.js. يرجى تعيينه على "صحيح" والآن سيقوم GridWeb بالتحقق من صحة ورقة العمل بأكملها وليس فقط الخلايا المحدثة.

![ما يجب القيام به:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


