---
title: تغيير المسار المطلق لملف مصدر بيانات الارتباط الخارجي
type: docs
weight: 1020
url: /ar/java/change-the-absolute-path-of-external-link-data-source-file/
---
## **سيناريوهات الاستخدام الممكنة**
 إذا كنت تريد تغيير المسار المطلق لملف مصدر بيانات الارتباط الخارجي ، فيرجى استخدام ملحق[المصنف](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath)منشأه. في البداية ، سيتم تعيين هذه الخاصية على المسار من حيث تم تحميل ملف Excel. ولكن يمكنك تعيينه على سلسلة فارغة أو يمكنك تعيينه على مسار مجلد محلي أو مسار شبكة بعيدة. عندما تقوم بتغيير هذه الخاصية ، سيتم أيضًا تغيير مسار ملف مصدر بيانات الارتباط الخارجي.
## **تغيير المسار المطلق لملف مصدر بيانات الارتباط الخارجي**
 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج ملف اكسل](5472589.xlsx) الذي يحتوي على ارتباط خارجي. يقوم أولاً بطباعة مصدر بيانات الارتباط الخارجي الذي يطبع المسار البعيد. ثم يزيل المسار البعيد ويطبع مرة أخرى ، وهذه المرة يطبع مصدر بيانات الارتباط الخارجي بالمسار المحلي. ثم يغير ملف[المصنف](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath)الخاصية إلى مسار محلي وبعيد ويطبع مصدر بيانات الارتباط الخارجي مرة أخرى وتنعكس التغييرات في إخراج وحدة التحكم.
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **إخراج وحدة التحكم**
هنا هو إخراج وحدة التحكم أو التصحيح بعد تنفيذ نموذج التعليمات البرمجية أعلاه بامتداد[نموذج ملف اكسل](5472589.xlsx).

{{< highlight "java" >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
