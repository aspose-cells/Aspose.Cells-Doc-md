---
title: كيفية الحصول على معلومات اتصال OData
type: docs
weight: 60
url: /ar/net/how-to-get-odata-connection-information/
---

## **الحصول على معلومات اتصال OData**

قد تكون هناك حالات حيث يحتاج المطورون إلى استخراج معلومات OData من ملف Excel. توفر Aspose.Cells خاصية [**Workbook.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup) التي تُرجع معلومات DataMashup الموجودة في ملف Excel. يُمثل هذه المعلومات من خلال الفئة [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup). توفر الفئة [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) خاصية [**PowerQueryFormulas**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) التي ترجع مجموعة [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction). من [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction)، يمكنك الوصول إلى [**PowerQueryFormula**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) و [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

توضح مقتطفات الشفرة التالية استخدام هذه الفئات لاسترداد معلومات OData.

الملف المصدر المستخدم في مقطع الكود التالي مرفق للرجوع إليه.

[الملف المصدر](96928098.xlsx)

### **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **مخرجات الوحدة**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
