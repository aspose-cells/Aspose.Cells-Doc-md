---
title: استيراد البيانات من كائن نتائج قاعدة البيانات Microsoft Access إلى ورقة العمل
type: docs
weight: 200
url: /ar/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**
يمكن لـ Aspose.Cells استيراد البيانات إلى ورقات العمل من كائن ResultSet الذي يمكن إنشاؤه من أي قاعدة بيانات. ومع ذلك، يقوم هذا المقال على وجه التحديد بإنشاء كائن ResultSet من قاعدة بيانات Microsoft Access. نظرًا لأن الشفرة هي نفسها لجميع أنواع قواعد البيانات، يمكنك استخدامها بشكل عام.
## **UCanAccess - مطلوب للاتصال بقاعدة بيانات Microsoft Access**
الرجاء تنزيل [UCanAccess](http://ucanaccess.sourceforge.net/site.html). ويتضمن الملفات الجاهزة JAR التالية. أضفها جميعًا في المسار.

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

لمزيد من المساعدة، يرجى زيارة هذا الرابط في Stack Overflow.

- [إضافة مكتبات JAR يدويًا إلى مشروعك](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **ملف قاعدة بيانات عينة من Microsoft Access 2016 المستخدم داخل الرمز العيني**
تم استخدام ملف قاعدة بيانات عينة من Microsoft Access 2016 التالي داخل الرمز العيني. يمكنك استخدام أي ملف قاعدة بيانات أو إنشاء ملف خاص بك.

- [Students.accdb](48496712.accdb)

الصورة التالية تُظهر ملف قاعدة البيانات عند فتحه في Microsoft Access 2016.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **استيراد البيانات من مجموعة نتائج قاعدة بيانات Microsoft Access إلى الورقة العمل.**
ينفذ الكود النموذجي التالي استعلام SQL من قاعدة بيانات Microsoft Access وينشئ كائن ResultSet. ثم يستورد البيانات من كائن ResultSet إلى ورقة العمل باستخدام طريقة [Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet-java.sql.ResultSet-int-int-boolean-). في المرة الأولى، يستخدم فهارس الصف والعمود ثم يستخدم اسم الخلية لاستيراد البيانات إلى ورقة العمل. أخيرًا، يحفظ دفتر العمل كملف إكسل إخراجي [Output Excel File](48496713.xlsx). تظهر الصورة الملتقطة أثر الكود النموذجي على ملف إكسل الناتج للاطلاع.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
