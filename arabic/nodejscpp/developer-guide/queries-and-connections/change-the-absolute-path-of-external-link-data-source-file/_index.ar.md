---
title: غير مسار مصدر بيانات الرابط الخارجي بشكل مطلق باستخدام Node.js عبر C++
linktitle: تغيير المسار المطلق لملف مصدر بيانات الرابط الخارجي
type: docs
weight: 290
url: /ar/nodejs-cpp/change-the-absolute-path-of-external-link-data-source-file/
description: تعلم كيفية تغيير المسار المطلق لملف مصدر البيانات الخارجي باستخدام Aspose.Cells for Node.js via C++. 
---

## سيناريوات الاستخدام المحتملة

إذا كنت تريد تغيير المسار المطلق لملف مصدر البيانات الخارجي، يرجى استخدام خاصية [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--). في البداية، سيتم تعيين هذه الخاصية إلى المسار الذي تم تحميل ملف Excel منه. لكن يمكنك تعيينه إلى سلسلة فارغة، أو يمكنك تعيينه إلى مسار مجلد محلي أو مسار شبكة بعيد. كلما قمت بتغيير هذه الخاصية، سيتم أيضًا تغيير مسار ملف مصدر البيانات الخارجي.

## تغيير المسار المطلق لملف مصدر بيانات الرابط الخارجي

يُحمّل المثال التالي ملف Excel عينة يحتوي على رابط خارجي. يطبع أولاً مصدر البيانات للرابط الخارجي الذي يعرض المسار البعيد. ثم يزيل المسار البعيد ويطبع مرة أخرى؛ هذه المرة، يعرض مصدر البيانات بالرابط المحلي. ثم يغير خاصية [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--) إلى مسار محلي وعن بُعد ويطبع مصدر البيانات مرة أخرى، ويُعكس التغييرات في إخراج وحدة التحكم.

إليك الإخراج من وحدة التحكم أو التصحيح بعد تنفيذ المثال أعلاه مع ملف Excel العينة  الخاص بنا.

{{< highlight javascript >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
