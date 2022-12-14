---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /ar/java/java-security-invalidkeyexception/
---
## **ملخص**
بشكل افتراضي ، يدعم AES مفتاح 128 بت ، إذا كنت تخطط لاستخدام مفتاح 192 بت أو 256 بت ، فسيرمي مترجم جافا استثناء حجم المفتاح غير القانوني. هذا ليس بسبب بعض الخلل في Aspose.Cells API بدلاً من ذلك بسبب الميزة المحدودة لـ JDK / JRE نفسها. ملفات السياسة الافتراضية لـ JDK / JRE معطلة بسبب قيود الاستيراد في بعض البلدان. يتعين على المستخدمين الحصول على ملفات سياسة "القوة غير المحدودة" وتثبيتها في JRE لاستخدام وظائف التشفير المتقدمة للتشفير / فك التشفير.
## **أعراض**
 قد تحصل على java.security.InvalidKeyException: حجم مفتاح غير قانوني أو معلمات افتراضية أو java.security.InvalidKeyException: حجم مفتاح غير قانوني أثناء تحميل جدول بيانات محمي.
## **المحلول**
الحل في الواقع بسيط للغاية كما هو مفصل أدناه.

1. تنزيل Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy ملفات.
1. استخرج ملفات JAR من الأرشيف الذي تم تنزيله وضعه في الدليل $ {java.home} / jre / lib / security /.
1. أعد تشغيل البرنامج.
## **روابط التحميل**
يرجى استخدام رابط التنزيل الذي يتوافق مع إصدار JDK / JRE الخاص بك.

- [Java امتداد التشفير (JCE) ملفات سياسة الولاية القضائية غير المحدودة 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java امتداد التشفير (JCE) ملفات سياسة الولاية القضائية غير المحدودة 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java امتداد التشفير (JCE) ملفات سياسة الاختصاص القضائي غير المحدودة 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
