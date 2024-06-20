---
title: كيفية الحصول على معلومات اتصال OData
type: docs
weight: 60
url: /ar/java/how-to-get-odata-connection-information/
---

## **الحصول على معلومات اتصال OData**

قد يكون هناك حالات حيث يحتاج المطورون إلى استخراج معلومات OData من ملف الإكسل. يوفر Aspose.Cells الخاصية [**Workbook.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup) التي تعيد معلومات DataMashup الموجودة في ملف Excel. تمثل هذه المعلومات بواسطة فئة DataMashup. توفر فئة DataMashup خاصية PowerQueryFormulas التي تعيد مجموعة PowerQueryFormulaCollction. من PowerQueryFormulaCollction، يمكنك الوصول إلى PowerQueryFormula و PowerQueryFormulaItem.

توضح مقتطفات الشفرة التالية استخدام هذه الفئات لاسترداد معلومات OData.

الملف المصدر المستخدم في مقطع الكود التالي مرفق للرجوع إليه.

[ملف المصدر](ODataSample.xlsx)

### **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **مخرجات الوحدة**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
