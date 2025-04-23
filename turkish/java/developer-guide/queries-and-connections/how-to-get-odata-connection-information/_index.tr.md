---
title: OData Bağlantı Bilgilerini Nasıl Alınır
type: docs
weight: 60
url: /tr/java/how-to-get-odata-connection-information/
---

## **OData Bağlantı Bilgilerini Alın**

Geliştiricilerin excel dosyasından OData bilgisi çıkarmaları gereken durumlar olabilir. Aspose.Cells, Excel dosyasında bulunan VeriMashup bilgisini döndüren [**Workbook.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup) özelliğini sağlar. Bu bilgi, DataMashup sınıfı tarafından temsil edilir. DataMashup sınıfı, PowerQueryFormulas özelliğini döndüren PowerQueryFormulaCollction koleksiyonunu sağlar. PowerQueryFormulaCollction'dan, PowerQueryFormula ve PowerQueryFormulaItem'a erişebilirsiniz.

Aşağıdaki kod parçası, bu sınıfları kullanarak OData bilgisini almayı göstermektedir.

Aşağıdaki kod parçasında kullanılan Kaynak dosyası, referansınız için ekte bulunmaktadır.

[Kaynak Dosyası](ODataSample.xlsx)

### **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Konsol Çıktısı**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
