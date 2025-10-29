---
title: تغيير مسار الملف المطلق لمصدر بيانات الرابط الخارجي باستخدام C++
linktitle: تغيير المسار المطلق لملف مصدر بيانات الرابط الخارجي
type: docs
weight: 290
url: /ar/cpp/change-the-absolute-path-of-external-link-data-source-file/
description: تغيير المسار المطلق لملف مصدر البيانات الخارجي في Aspose.Cells باستخدام C++.
---

## سيناريوات الاستخدام المحتملة

إذا كنت ترغب في تغيير المسار المطلق لملف مصدر البيانات الخارجي، فالرجاء استخدام طريقة [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/). في البداية، سيتم تعيين هذه الخاصية إلى المسار الذي تم تحميل ملف إكسل منه. ولكن يمكنك تعيينها إلى سلسلة فارغة أو تحديد مسار مجلد محلي أو مسار شبكة بعيد. كلما قمت بتغيير هذه الخاصية، سيتم أيضًا تغيير مسار ملف مصدر البيانات الخارجي.

## تغيير المسار المطلق لملف مصدر بيانات الرابط الخارجي

يفتح الكود النموذجي التالي ملف إكسل [عينة](5115146.xlsx) الذي يحتوي على رابط خارجي. يطبع أولاً مصدر البيانات الخارجي والذي يعرض المسار البعيد، ثم يزيل المسار البعيد ويطبع مرة أخرى، المرة الثانية، يطبع مصدر البيانات الخارجي مع المسار المحلي. ثم يغير طريقة [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/) إلى مسار محلي وبعيد، ويطبع مصدر البيانات الخارجي مرة أخرى، وتتغير القيم في مخرجات وحدة التحكم.

إليك مخرجات وحدة التحكم أو التصحيح بعد تنفيذ الكود النموذجي أعلاه مع [ملف Excel العيني](5115146.xlsx).

{{< highlight cpp >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
