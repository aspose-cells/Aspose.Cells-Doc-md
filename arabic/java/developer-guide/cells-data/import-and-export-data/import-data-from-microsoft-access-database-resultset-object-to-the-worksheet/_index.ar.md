---
title: استيراد البيانات من Microsoft Access Database ResultSet Object إلى ورقة العمل
type: docs
weight: 200
url: /ar/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---
## **سيناريوهات الاستخدام الممكنة**
يمكن Aspose.Cells استقبال البيانات إلى أوراق العمل من عنصر ResultSet الذي يمكن تكوينه من أي قاعدة بيانات. ومع ذلك ، تقوم هذه المقالة بشكل خاص بإنشاء كائن ResultSet من قاعدة بيانات Access Microsoft. نظرًا لأن الكود هو نفسه لجميع أنواع قواعد البيانات ، فيمكنك استخدامه بشكل عام.
## **UCanAccess - مطلوب للاتصال بقاعدة بيانات الوصول Microsoft**
 الرجاء التحميل[UCanAccess](http://ucanaccess.sourceforge.net/site.html). يتضمن ملفات JAR التالية. أضفهم جميعًا في مسار الفصل.

- ucanaccess-4.0.1.jar
- كومونس لانج 2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

لمزيد من المساعدة ، يرجى زيارة هذا الرابط Stack Overflow.

- [إضافة JARs يدويًا إلى مشروعك](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **نموذج Microsoft ملف قاعدة بيانات Access 2016 المستخدم داخل نموذج التعليمات البرمجية**
تم استخدام النموذج التالي Microsoft Access 2016 Database File داخل نموذج التعليمات البرمجية. يمكنك استخدام أي ملف قاعدة بيانات أو إنشاء ملف خاص بك.

- [الطلاب](48496712.accdb)

تُظهر لقطة الشاشة التالية ملف قاعدة البيانات عند فتحه في Microsoft Access 2016.

![ما يجب القيام به: image_بديل_نص](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **استيراد البيانات من Microsoft Access Database ResultSet Object إلى ورقة العمل.**
 نموذج التعليمات البرمجية التالي تنفيذ استعلام SQL من قاعدة بيانات Access Microsoft وإنشاء كائن ResultSet. ثم يقوم باستيراد البيانات من كائن ResultSet إلى ورقة العمل باستخدام[Worksheet.getCells (). importResultSet ()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\)) طريقة. في المرة الأولى ، يستخدم فهارس الصفوف والأعمدة ثم يستخدم اسم الخلية لاستيراد البيانات إلى ورقة العمل. أخيرًا ، يحفظ المصنف كملف[إخراج ملف Excel](48496713.xlsx). تُظهر لقطة الشاشة تأثير نموذج التعليمات البرمجية على ملف Excel الناتج كمرجع.

![ما يجب القيام به: image_بديل_نص](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
