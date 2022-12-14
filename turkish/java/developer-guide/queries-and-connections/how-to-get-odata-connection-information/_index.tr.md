---
title: OData Bağlantı Bilgileri nasıl alınır?
type: docs
weight: 60
url: /tr/java/how-to-get-odata-connection-information/
---
## **OData Bağlantı Bilgilerini Alın**

Geliştiricilerin OData bilgilerini excel dosyasından çıkarması gereken durumlar olabilir. Aspose.Cells şunları sağlar:[**Workbook.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup)Excel dosyasında bulunan DataMashup bilgilerini döndüren özellik. Bu bilgiler DataMashup sınıfı tarafından temsil edilir. DataMashup sınıfı, PowerQueryFormulaCollction koleksiyonunu döndüren PowerQueryFormulas özelliğini sağlar. PowerQueryFormulaCollction'dan, PowerQueryFormula ve PowerQueryFormulaItem öğelerine erişebilirsiniz.

Aşağıdaki kod parçacığı, OData bilgilerini almak için bu sınıfların kullanımını gösterir.

Aşağıdaki kod parçacığında kullanılan Kaynak dosyası, referansınız için eklenmiştir.

[Kaynak dosyası](ODataSample.xlsx)

### **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Konsol Çıkışı**

Bağlantı Adı: Siparişler

İsim: Kaynak

Değer: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

İsim: Orders_table

Değer: Source{[Name="Orders",Signature="table"]}[Data]