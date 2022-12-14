---
title: قراءة وكتابة الاتصال الخارجي لملف XLSB أو XLS
type: docs
weight: 80
url: /ar/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---
## **سيناريوهات الاستخدام الممكنة**

يدعم Aspose.Cells بالفعل قراءة وكتابة الاتصال الخارجي لملف XLSX ولكنه يدعم الآن أيضًا هذه الميزة لملف XLSB و XLS. ومع ذلك ، فإن الرمز هو نفسه لكلا النوعين من التنسيق.

## **قراءة وكتابة الاتصال الخارجي لملف XLSB / XLS**

نموذج التعليمات البرمجية التالي يقوم بتحميل نموذج ملف XLSB (يمكن أيضًا تحميل XLS) ويقرأ أول اتصال خارجي وهو بالفعل Microsoft Access DB Connection. ثم يقوم بتعديل ملف[**الاسم**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name)الخاصية ويحفظها كملف إخراج XLSB. تظهر لقطة الشاشة تأثير الكود على[نموذج لملف XLSB](51740743.xlsb)و[إخراج ملف XLSB](51740742.xlsb)بعد تنفيذه. يرجى أيضًا الاطلاع على إخراج وحدة التحكم لعينة التعليمات البرمجية الواردة أدناه للحصول على مرجع.

![ما يجب القيام به: image_بديل_نص](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **عينة من الرموز**

يجب أن يعمل الكود التالي لكل من XLSB و XLS عن طريق تحميل وحفظ الملفات بامتداد مناسب.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
