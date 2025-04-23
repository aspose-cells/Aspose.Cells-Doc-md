---
title: كيفية الحصول على معلومات اتصال OData
type: docs
weight: 60
url: /ar/python-net/how-to-get-odata-connection-information/
---

## **الحصول على معلومات اتصال OData**

هناك حالات قد يحتاج فيها المطورون إلى استخراج معلومات OData من ملف إكسل. توفر Aspose.Cells لبايثون via .NET الخاصية [**Workbook.data_mashup**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/data_mashup) التي تُرجع معلومات DataMashup الموجودة في ملف الإكسل. تمثل هذه المعلومات بواسطة فئة [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup). توفر فئة [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup) الخاصية [**power_query_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup/power_query_formulas) التي تُرجع مجموعة [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/). من [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/)، يمكنك الوصول إلى [**PowerQueryFormula**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformula) و[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulaitem).

توضح مقتطفات الشفرة التالية استخدام هذه الفئات لاسترداد معلومات OData.

الملف المصدر المستخدم في مقطع الكود التالي مرفق للرجوع إليه.

[الملف المصدر](96928098.xlsx)

### **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-GetOdataDetails-1.py" >}}

### **مخرجات الوحدة**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}

