---
title: تغيير المسار المطلق لملف مصدر بيانات الرابط الخارجي
type: docs
weight: 290
url: /ar/python-net/change-the-absolute-path-of-external-link-data-source-file/
---

## سيناريوات الاستخدام المحتملة

إذا كنت ترغب في تغيير المسار المطلق لملف مصدر بيانات الرابط الخارجي، يرجى استخدام خاصية [**Workbook.absolute_path**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/absolute_path). في البداية، سيتم تعيين هذه الخاصية إلى المسار من حيث تم تحميل ملف Excel. ولكن يمكنك ضبطها لتكون سلسلة فارغة أو يمكنك ضبطها لتكون بعض مسار المجلد المحلي أو مسار الشبكة البعيدة. كلما قمت بتغيير هذه الخاصية، سيتم تغيير أيضًا مسار ملف مصدر بيانات الرابط الخارجي.

## تغيير المسار المطلق لملف مصدر بيانات الرابط الخارجي

يقوم الكود النموذجي التالي بتحميل [ملف Excel العيني](5115146.xlsx) الذي يحتوي على رابط خارجي. يقوم أولاً بطباعة مصدر بيانات الرابط الخارجي الذي يطبع المسار البعيد. ثم يقوم بإزالة المسار البعيد والطباعة مرة أخرى، وفي هذه المرة، يطبع مصدر بيانات الرابط الخارجي بالمسار المحلي. ثم يقوم بتغيير الخاصية [**Workbook.absolute_path**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/absolute_path) إلى مسار محلي وبعيد ويقوم بطباعة مصدر بيانات الرابط الخارجي مرة أخرى وتنعكس التغييرات في مخرجات وحدة التحكم.

إليك مخرجات وحدة التحكم أو التصحيح بعد تنفيذ الكود النموذجي أعلاه مع [ملف Excel العيني](5115146.xlsx).

{{< highlight java >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
