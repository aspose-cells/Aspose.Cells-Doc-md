---
title: قراءة وكتابة الاتصال الخارجي لملف XLSB أو XLS
type: docs
weight: 80
url: /ar/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---

## **سيناريوهات الاستخدام المحتملة**

تدعم Aspose.Cells بالفعل قراءة وكتابة الاتصال الخارجي لملفات XLSX ولكن الآن، تدعم أيضًا هذه الميزة لملفات XLSB وXLS. ومع ذلك، يكون الكود متطابقًا لكلا النوعين من التنسيق.

## **قراءة وكتابة الاتصال الخارجي لملفات XLSB/XLS**

الكود العيني التالي يحمل ملف XLSB(XLS يمكن أيضًا أن يتم تحميله) عينيًا ويقرأ اتصاله الخارجي الأول الذي هو في الواقع اتصال قاعدة بيانات Microsoft Access. يقوم بتعديل الخاصية [**DBConnection.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name) ثم يحفظه كملف XLSB ناتج. تُظهر اللقطة الشاشية تأثير الكود على [ملف XLSB عيني](51740743.xlsb) و [ملف XLSB الناتج](51740742.xlsb) بعد تنفيذه. يُرجى أيضًا رؤية الإخراج على الشاشة للكود العيني المُعطى أدناه للإشارة.

![todo:image_alt_text](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **الكود المثالي**

سيعمل الكود البعدعِ لكلا XLSB و XLS من خلال تحميل وحفظ الملفات بامتداد مناسب.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
