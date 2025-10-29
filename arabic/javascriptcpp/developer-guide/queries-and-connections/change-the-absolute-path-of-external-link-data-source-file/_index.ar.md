---
title: تغيير المسار المطلق لمصدر بيانات الرابط الخارجي باستخدام JavaScript عبر C++
linktitle: تغيير المسار المطلق لملف مصدر بيانات الرابط الخارجي
type: docs
weight: 290
url: /ar/javascript-cpp/change-the-absolute-path-of-external-link-data-source-file/
description: تعلّم كيفية تغيير المسار المطلق لمصدر بيانات الرابط الخارجي باستخدام Aspose.Cells for JavaScript عبر C++. 
---

## سيناريوات الاستخدام المحتملة

إذا كنت تريد تغيير المسار المطلق لملف مصدر البيانات الخارجي، يرجى استخدام خاصية [**Workbook.absolutePath**](https://reference.aspose.com/cells/javascript-cpp/workbook/#absolutePath--). في البداية، سيتم تعيين هذه الخاصية إلى المسار الذي تم تحميل ملف Excel منه. لكن يمكنك تعيينه إلى سلسلة فارغة، أو يمكنك تعيينه إلى مسار مجلد محلي أو مسار شبكة بعيد. كلما قمت بتغيير هذه الخاصية، سيتم أيضًا تغيير مسار ملف مصدر البيانات الخارجي.

## تغيير المسار المطلق لملف مصدر بيانات الرابط الخارجي

يُحمّل المثال التالي ملف Excel عينة يحتوي على رابط خارجي. يطبع أولاً مصدر البيانات للرابط الخارجي الذي يعرض المسار البعيد. ثم يزيل المسار البعيد ويطبع مرة أخرى؛ هذه المرة، يعرض مصدر البيانات بالرابط المحلي. ثم يغير خاصية [**Workbook.absolutePath**](https://reference.aspose.com/cells/javascript-cpp/workbook/#absolutePath--) إلى مسار محلي وعن بُعد ويطبع مصدر البيانات مرة أخرى، ويُعكس التغييرات في إخراج وحدة التحكم.



{{< highlight javascript >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
