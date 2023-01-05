---
title: كيفية الحصول على معلومات اتصال OData
type: docs
weight: 60
url: /ar/java/how-to-get-odata-connection-information/
---
## **احصل على معلومات اتصال OData**

قد تكون هناك حالات يحتاج فيها المطورون إلى استخراج معلومات OData من ملف Excel. يوفر Aspose.Cells ملف[**المصنف**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup)الخاصية التي تُرجع معلومات DataMashup الموجودة في ملف Excel. يتم تمثيل هذه المعلومات بواسطة فئة DataMashup. توفر فئة DataMashup خاصية PowerQueryFormulas التي تُرجع مجموعة PowerQueryFormulaCollction. من PowerQueryFormulaCollction ، يمكنك الوصول إلى PowerQueryFormula و PowerQueryFormulaItem.

يوضح مقتطف التعليمات البرمجية التالي استخدام هذه الفئات لاسترداد معلومات OData.

تم إرفاق ملف المصدر المستخدم في مقتطف الشفرة التالي للرجوع إليه.

[مصدر الملف](ODataSample.xlsx)

### **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **إخراج وحدة التحكم**

اسم الاتصال: الطلبات

الاسم: المصدر

القيمة: OData.Feed ("https://services.odata.org/V3/Northwind/Northwind.svc/" ، فارغ ، [التنفيذ = "2.0"])

الاسم: Orders_table

القيمة: المصدر {[Name = "Orders"، Signature = "table"]} [Data]