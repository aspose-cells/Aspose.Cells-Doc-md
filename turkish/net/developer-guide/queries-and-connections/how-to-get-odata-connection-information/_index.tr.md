---
title: OData Bağlantı Bilgileri nasıl alınır?
type: docs
weight: 60
url: /tr/net/how-to-get-odata-connection-information/
---
## **OData Bağlantı Bilgilerini Alın**

 Geliştiricilerin OData bilgilerini excel dosyasından çıkarması gereken durumlar olabilir. Aspose.Cells şunları sağlar:[**Workbook.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup) Excel dosyasında bulunan DataMashup bilgilerini döndüren özellik. Bu bilgiler şu şekilde temsil edilir:[**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) sınıf. bu[**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)sınıf sağlar[**PowerQueryFormülleri**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) döndüren özellik[**PowerQueryFormulaKoleksiyon**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) Toplamak. itibaren[**PowerQueryFormulaKoleksiyon**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction), erişim sağlayabilirsiniz[**PowerQueryFormülü**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) ve[**PowerQueryFormulaÖğesi**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

Aşağıdaki kod parçacığı, OData bilgilerini almak için bu sınıfların kullanımını gösterir.

Aşağıdaki kod parçacığında kullanılan Kaynak dosyası, referansınız için eklenmiştir.

[Kaynak dosyası](96928098.xlsx)

### **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **Konsol Çıkışı**

Bağlantı Adı: Siparişler

İsim: Kaynak

Değer: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

İsim: Orders_table

Değer: Source{[Name="Orders",Signature="table"]}[Data]