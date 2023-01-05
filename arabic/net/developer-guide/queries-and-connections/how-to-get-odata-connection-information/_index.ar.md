---
title: كيفية الحصول على معلومات اتصال OData
type: docs
weight: 60
url: /ar/net/how-to-get-odata-connection-information/
---
## **احصل على معلومات اتصال OData**

 قد تكون هناك حالات يحتاج فيها المطورون إلى استخراج معلومات OData من ملف Excel. يوفر Aspose.Cells ملف[**المصنف**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup) الخاصية التي تُرجع معلومات DataMashup الموجودة في ملف Excel. يتم تمثيل هذه المعلومات من قبل[**داتا ماتشوب**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) صف دراسي. ال[**داتا ماتشوب**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)فئة توفر[**صيغ PowerQueryFormulas**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) الخاصية التي تعيد[**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) مجموعة. من[**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction)، يمكنك الوصول إلى[**PowerQueryFormula**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) و[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

يوضح مقتطف التعليمات البرمجية التالي استخدام هذه الفئات لاسترداد معلومات OData.

تم إرفاق ملف المصدر المستخدم في مقتطف الشفرة التالي للرجوع إليه.

[مصدر الملف](96928098.xlsx)

### **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **إخراج وحدة التحكم**

اسم الاتصال: الطلبات

الاسم: المصدر

القيمة: OData.Feed ("https://services.odata.org/V3/Northwind/Northwind.svc/" ، فارغ ، [التنفيذ = "2.0"])

الاسم: Orders_table

القيمة: المصدر {[Name = "Orders"، Signature = "table"]} [Data]