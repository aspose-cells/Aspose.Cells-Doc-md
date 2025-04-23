---
title: قراءة وكتابة اتصال الخارجي لملفات XLS و XLSB
type: docs
weight: 80
url: /ar/net/read-and-write-external-connection-of-xls-and-xlsb-files/
---

## **سيناريوهات الاستخدام المحتملة**

Aspose.Cells تدعم بالفعل قراءة وكتابة اتصال خارجي لملف XLSX ولكن الآن، تدعم أيضًا هذه الميزة لملفات XLSB و XLS. ومع ذلك، يكون الكود هو نفسه لجميع أنواع الصيغ.

## **قراءة وكتابة اتصال خارجي لملف XLS/XLSB**

الكود العينة التالي يحمل ملف XLSB عينة (كما يمكن تحميل ملف XLS) ويقرأ اتصاله الخارجي الأول الذي هو في الواقع اتصال قاعدة بيانات Microsoft Access. ثم يقوم بتعديل الخاصية [**DBConnection.Name**](https://reference.aspose.com/cells/net/aspose.cells.externalconnections/externalconnection/properties/name) ويحفظه كملف XLS/XLSB الناتج. تظهر اللقطة الشاشية تأثير الكود على [ملف XLSB عينة](51740722.xlsb) و [ملف XLSB الناتج](51740723.xlsb) بعد تنفيذه. يرجى أيضًا الاطلاع على إخراج الكونسول للكود العيني المعطى أدناه للإشارة.

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **الكود المثالي**

الكود التالي سيعمل لكل من ملفات XLSB و XLS عن طريق تحميل وحفظ الملفات بامتداد مناسب.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.cs" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
