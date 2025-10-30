---
title: OData Bağlantı Bilgilerini Nasıl Alınır
type: docs
weight: 60
url: /tr/python-net/how-to-get-odata-connection-information/
---

## **OData Bağlantı Bilgilerini Alın**

Geliştiricilerin bazen OData bilgisini Excel dosyasından çıkarması gerekebilir. Aspose.Cells for Python via .NET, Excel dosyasındaki DataMashup bilgisini döndüren [**Workbook.data_mashup**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/data_mashup) özelliği sağlar. Bu bilgi, [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup) sınıfı tarafından temsil edilir. [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup) sınıfı, [**power_query_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup/power_query_formulas) özelliği aracılığıyla [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/) koleksiyonunu döner. Buradan [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/), [**PowerQueryFormula**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformula) ve [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulaitem) ile erişim sağlayabilirsiniz.

Aşağıdaki kod parçası, bu sınıfları kullanarak OData bilgisini almayı göstermektedir.

Aşağıdaki kod parçasında kullanılan Kaynak dosyası, referansınız için ekte bulunmaktadır.

[Kaynak Dosyası](96928098.xlsx)

### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-GetOdataDetails-1.py" >}}

### **Konsol Çıktısı**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
