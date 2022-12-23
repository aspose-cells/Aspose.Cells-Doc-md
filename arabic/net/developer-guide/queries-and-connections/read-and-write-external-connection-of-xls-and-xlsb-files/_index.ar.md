---
title: قراءة وكتابة التوصيل الخارجي لملفات XLS و XLSB
type: docs
weight: 80
url: /ar/net/read-and-write-external-connection-of-xls-and-xlsb-files/
---
## **سيناريوهات الاستخدام الممكنة**

يدعم Aspose.Cells بالفعل قراءة وكتابة الاتصال الخارجي لملف XLSX ولكنه الآن يدعم هذه الميزة لملف XLSB و XLS. ومع ذلك ، فإن الكود هو نفسه لجميع أنواع التنسيقات.

## **قراءة وكتابة الوصلة الخارجية لملف XLS/XLSB**

 يقوم نموذج التعليمات البرمجية التالي بتحميل نموذج ملف XLSB (يمكن أيضًا تحميل XLS) ويقرأ أول اتصال خارجي وهو في الواقع Microsoft Access DB Connection. ثم يقوم بتعديل ملف[**الاسم**](https://reference.aspose.com/cells/net/aspose.cells.externalconnections/externalconnection/properties/name) الخاصية ويحفظها كملف الإخراج XLS/XLSB. تظهر لقطة الشاشة تأثير الكود على[عينة ملف XLSB](51740722.xlsb) و[ملف الإخراج XLSB](51740723.xlsb) بعد تنفيذه. يرجى أيضًا الاطلاع على إخراج وحدة التحكم لعينة التعليمات البرمجية الواردة أدناه للحصول على مرجع.

![ما يجب القيام به: image_بديل_نص](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **عينة من الرموز**

يجب أن يعمل الكود التالي لكل من ملفات XLSB و XLS عن طريق تحميل وحفظ الملفات بالملحق المناسب.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.cs" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
