---
title: تغيير المسار المطلق لملف مصدر بيانات الارتباط الخارجي
type: docs
weight: 290
url: /ar/net/change-the-absolute-path-of-external-link-data-source-file/
---
## سيناريوهات الاستخدام الممكنة

 إذا كنت تريد تغيير المسار المطلق لملف مصدر بيانات الارتباط الخارجي ، فيرجى استخدام ملحق[**المصنف**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath)منشأه. في البداية ، سيتم تعيين هذه الخاصية على المسار من حيث تم تحميل ملف Excel. ولكن يمكنك تعيينه على سلسلة فارغة أو يمكنك تعيينه على مسار مجلد محلي أو مسار شبكة بعيدة. عندما تقوم بتغيير هذه الخاصية ، سيتم أيضًا تغيير مسار ملف مصدر بيانات الارتباط الخارجي.

## تغيير المسار المطلق لملف مصدر بيانات الارتباط الخارجي

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج ملف اكسل](5115146.xlsx) الذي يحتوي على ارتباط خارجي. يقوم أولاً بطباعة مصدر بيانات الارتباط الخارجي الذي يطبع المسار البعيد. ثم يزيل المسار البعيد ويطبع مرة أخرى ، وهذه المرة يطبع مصدر بيانات الارتباط الخارجي بالمسار المحلي. ثم يغير ملف[**المصنف**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath)الخاصية إلى مسار محلي وبعيد ويطبع مصدر بيانات الارتباط الخارجي مرة أخرى وتنعكس التغييرات في إخراج وحدة التحكم.

هنا هو إخراج وحدة التحكم أو التصحيح بعد تنفيذ نموذج التعليمات البرمجية أعلاه بامتداد[نموذج ملف اكسل](5115146.xlsx).

{{< highlight "java" >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
