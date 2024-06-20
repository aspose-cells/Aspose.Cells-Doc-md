---
title: OData Bağlantı Bilgilerini Nasıl Alınır
type: docs
weight: 60
url: /tr/net/how-to-get-odata-connection-information/
---

## **OData Bağlantı Bilgilerini Alın**

Geliştiricilerin excel dosyasından OData bilgilerini çıkarmak zorunda kaldığı durumlar olabilir. Aspose.Cells, Excel dosyasında bulunan DataMashup bilgilerini döndüren [**Workbook.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup) özelliğini sağlar. Bu bilgi, [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) sınıfı tarafından temsil edilir. [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) sınıfı, [**PowerQueryFormulas**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) özelliğini döndüren [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) koleksiyonunu sağlar. [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) ile, [**PowerQueryFormula**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) ve [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem) 'e erişebilirsiniz.

Aşağıdaki kod parçası, bu sınıfları kullanarak OData bilgisini almayı göstermektedir.

Aşağıdaki kod parçasında kullanılan Kaynak dosyası, referansınız için ekte bulunmaktadır.

[Kaynak Dosyası](96928098.xlsx)

### **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **Konsol Çıktısı**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
