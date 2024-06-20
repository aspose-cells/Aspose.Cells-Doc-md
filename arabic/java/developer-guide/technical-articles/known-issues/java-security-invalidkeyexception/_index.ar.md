---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /ar/java/java-security-invalidkeyexception/
---

## **ملخص**
بشكل افتراضي، يدعم AES مفتاحًا بطول 128 بت، إذا كنت تخطط لاستخدام مفتاح بطول 192 بت أو 256 بت، سيرمي مترجم جافا استثناء مفتاح غير قانوني الحجم. ليس هذا بسبب خلل في واجهة برمجة التطبيقات لـ Aspose.Cells API بل بسبب ميزة محدودة لـ JDK/JRE نفسها. ملفات السياسة الافتراضية لـ JDK/JRE غير كاملة بسبب قيود الاستيراد في بعض الدول. يجب على المستخدمين الحصول على ملفات سياسة "قوة غير محدودة" وتثبيتها في JRE الخاص بهم لاستخدام وظيفة التشفير/فك التشفير المتقدمة.
## **الأعراض**
قد تحصل على java.security.InvalidKeyException: Illegal key size أو default parameters أو java.security.InvalidKeyException: Illegal key size أثناء تحميل جدول بيانات محمي. 
## **الحل**
الحل في الواقع بسيط جدًا كما هو موضح أدناه.

1. قم بتنزيل ملحق تشفير جافا (JCE) بقوة الولاية وملفات السياسة.
1. استخرج ملفات JAR من الأرشيف المحمل وضعها في ${java.home}/jre/lib/security/ الدليل.
1. أعِد تشغيل البرنامج.
## **روابط التنزيل**
الرجاء استخدام الرابط التنزيل الذي يتوافق مع إصدار JDK/JRE الخاص بك.

- [ملفات ملحق تشفير جافا (JCE) بقوة الولاية للقوانين 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [ملفات ملحق تشفير جافا (JCE) بقوة الولاية للقوانين 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [ملفات ملحق تشفير جافا (JCE) بقوة الولاية للقوانين 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
