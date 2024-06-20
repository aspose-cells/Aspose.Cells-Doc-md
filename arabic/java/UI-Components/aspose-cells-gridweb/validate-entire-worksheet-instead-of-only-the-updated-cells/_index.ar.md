---
title: التحقق من ورقة العمل بأكملها بدلاً من الخلايا المحدثة فقط
type: docs
weight: 80
url: /ar/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---

## **سيناريوهات الاستخدام المحتملة**
بشكل افتراضي ، يقوم GridWeb بالتحقق من الخلايا المحدثة فقط ولا يقوم بالتحقق من ورقة العمل بأكملها. ومع ذلك ، إذا كنت ترغب في التحقق من ورقة العمل بأكملها على الجانب العميل قبل أن يرسل GridWeb طلبًا إلى الخادم ، فيجب عليك ضبط المتغير needValidateall داخل acwmain.js على true.
## **التحقق من ورقة العمل بأكملها بدلاً من الخلايا المحدثة فقط**
الصورة الملتقطة التالية تعرض المتغير needValidateall في ملف acwmain.js. يرجى تعيينه إلى true والآن سوف يقوم GridWeb بالتحقق من صحة جدول البيانات الخاص بك بأكمله ليس فقط الخلايا المحدثة.

![todo:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


