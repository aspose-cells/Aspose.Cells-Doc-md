---
title: تغيير المسار المطلق لملف مصدر بيانات الرابط الخارجي
type: docs
weight: 1020
url: /ar/java/change-the-absolute-path-of-external-link-data-source-file/
---

## **سيناريوهات الاستخدام المحتملة**
إذا كنت ترغب في تغيير المسار المطلق لملف مصدر بيانات الرابط الخارجي، يرجى استخدام خصائص الـ [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath). في البداية، سيتم تعيين هذه الخاصية على المسار من حيث تم تحميل ملف الإكسل. ولكن يمكنك تعيينها على سلسلة فارغة أو يمكنك تعيينها على مسار مجلد محلي أو مسار شبكة بعيدة. في كل مرة تغير في هذه الخاصية، سيتم تغيير مسار مصدر بيانات الرابط الخارجي أيضًا.
## **تقوم الكود عينة التالي بتحميل [ملف إكسل عينة](5472589.xlsx) الذي يحتوي على رابط خارجي. يقوم أولاً بطباعة مصدر بيانات الرابط الخارجي الذي يطبع المسار البعيد. ثم يقوم بإزالة المسار البعيد والطباعة مرة أخرى، وهذه المرة، يطبع مصدر بيانات الرابط الخارجي بالمسار المحلي. ثم يقوم بتغيير خاصية [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath) على مسار محلي وبعيد ويطبع مصدر بيانات الرابط الخارجي مرة أخرى وتؤخذ التغييرات في الإخراج الوحدة النمطية.**
يحمل الكود النموذجي التالي [ملف الإكسل عينة](5472589.xlsx) الذي يحتوي على رابط خارجي. يطبع أولاً مصدر البيانات من الرابط الخارجي والذي يطبع المسار البعيد. ثم يزيل المسار البعيد ويطبع مرة أخرى، وهذه المرة، يطبع مصدر البيانات من الرابط الخارجي بالمسار المحلي. ثم يغير [خاصية Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath) إلى مسار محلي وعن بعد ويطبع مرة أخرى مصدر البيانات من الرابط الخارجي وينعكس التغيير في مخرجات وحدة التحكم.
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **مخرجات الوحدة**
فيما يلي إخراج الوحدة النمطية بعد تنفيذ الكود أعلاه مع [ملف إكسل عينة](5472589.xlsx).

{{< highlight java >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
