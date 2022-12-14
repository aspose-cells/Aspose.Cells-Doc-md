---
title: Yeni Veri kaynakları ve Sorgular Oluşturma
type: docs
weight: 20
url: /tr/reportingservices/creating-new-data-sources-and-queries/
---
{{% alert color="primary" %}} 

 Aspose.Cells.Report.Designer, MS Query ile entegre olur ve MS Query'yi veri kaynakları ve sorgular oluşturmak için bir araç olarak kullanır. Aspose.Cells.Report.Designer'da yeni bir veri kaynağı ve sorgu oluşturmak için aşağıdaki adımları izleyin:.

{{% /alert %}} 

Aspose.Cells.Report.Designer'da yeni bir veri kaynağı ve sorgu oluşturmak için:

1. Microsoft Excel'i açın.
1.  Tıklamak**Veri Kümesi Oluştur** Aspose.Cells.Report.Designer araç çubuğunda:

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_1.png)


Tüm veri kaynakları ve sorgular iletişim kutusunda listelenir.

1.  Bir veri kaynağı düğümü:

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_2.png)

1.  Bir veri seti düğümü:

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_3.png)

1. Ağacın kök düğümünü seçin.
1.  Tıklamak**Ekle**. 

   **Veri kaynakları ve veri kümeleri ekleme** 

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_4.png)




1.  İletişim kutusunda veri kaynağını çağırın**SQL Server** ve veri seti**EmpsSatışDetay**.
1.  Tıklamak**Sonraki**. 

   **Veri kümeleri ve veri kaynakları ekleme** 

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_5.png)



 Aspose.Cells.Report.Designer Microsoft Sorgusunu başlatır.

1.  Veri Kaynağı Seç iletişim kutusunda,**Yeni Veri Kaynağı**.
1.  Tıklamak**TAMAM**.
 Mevcut bir veri kaynağını da seçebilirsiniz.

   **Veri kaynağı seçme** 

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_6.png)




1. Bir veri kaynağı adı girin ve açılır veritabanı sürücüleri listesinden SQL Server'ı seçin.
1.  Tıklamak**Bağlamak**. 

   **Yeni bir veri kaynağı oluşturma** 

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_7.png)




1. SQL Server Oturum Açma iletişim kutusunda her öğe için uygun değeri seçin.
 Örneğin, sunucuyu yerel olarak ayarlayın, AdventureWorks veritabanını seçin ve**Güvenilir Bağlantı Kullan**.
1.  Tıklamak**TAMAM**. 

   **SQL sunucusunda oturum açma** 

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_8.png)




1.  Tıklamak**TAMAM**. 

   **Artık SQL sunucusunda oturum açtığımızı unutmayın.** 

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_9.png)



Yeni veri kaynağı,**Veri Kaynağını Seçin** diyalog

1.  Yeni veri kaynağını seçin.

   **yeni veri kaynağı** 

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_10.png)




1.  Tıklamak**TAMAM** Microsoft Sorguyu açmak için.
1.  Microsoft Sorgusunda sorgu oluşturmak için Microsoft Sorgu Yardımcısına bakın. Aşağıdaki örnekte, parametrelerle bir sorgu oluşturuyoruz.

   **sorgu oluşturma** 

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_11.png)



 SQL aşağıdaki gibidir:

**SQL**

{{< highlight "csharp" >}}

 SELECT C.FirstName + ' ' + C.LastName AS Employee,

DATEPART(Month, SOH.OrderDate) AS OrderMonthNum,

PS.Name AS SubCat,

SUM(SOD.LineTotal) AS Sales,

SOH.SalesOrderNumber,

P.Name AS Product,

SUM(SOD.OrderQty) AS OrderQty,

SOD.UnitPrice,

PC.Name AS ProdCat

FROM  Sales.SalesOrderHeader SOH ,

Sales.SalesOrderDetail SOD ,

Sales.SalesPerson SP,

HumanResources.Employee E,

Person.Contact C,

Production.Product P,

Production.ProductSubcategory PS ,

Production.ProductCategory PC

where SOH.SalesOrderID = SOD.SalesOrderID

and SOH.SalesPersonID = SP.SalesPersonID

and SP.SalesPersonID = E.EmployeeID

and E.ContactID = C.ContactID

and SOD.ProductID = P.ProductID

and P.ProductSubcategoryID = PS.ProductSubcategoryID

and PS.ProductCategoryID = PC.ProductCategoryID

and  (DATEPART(Year, SOH.OrderDate) =  ?)

AND (DATEPART(Month, SOH.OrderDate) =  ?)

AND (SOH.SalesPersonID =?)

GROUP BY    C.FirstName + ' ' + C.LastName,

DATEPART(Month, SOH.OrderDate), SOH.SalesOrderNumber,

P.Name, PS.Name, SOD.UnitPrice, PC.Name



{{< /highlight >}}


Sorgunun üç parametresi vardır: ReportYear, ReportMonth ve EmpID.

1.  Microsoft sorgusundan**Dosya** menü, seç**Aspose.Cells.Report.Designer'a Dön**. 

   **Rapor tasarımcısına dönüş** 

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_12.png)



 Yukarıda oluşturulan veri kaynağı ve sorgu iletişim kutusunda listelenir.

1.  veri kaynağını tıklayın**SQL Server** ayrıntılı bilgilerini görüntülemek için.

   **yeni veri kaynağı** 

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_13.png)




1.  Ayrıntılı bilgilerini görüntülemek için EmpSalesDetails sorgusuna tıklayın.

   **Sorgunun sql'sini görüntülemek için SQL Sekmesine tıklayın** 

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_14.png)



**Sorgunun sütunlarını görüntülemek için Sütunlar Sekmesine tıklayın** 

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_15.png)



**Sorgunun parametrelerini görüntülemek için Parametreler Sekmesine tıklayın** 

![yapılacaklar:resim_alternatif_Metin](creating-new-data-sources-and-queries_16.png)



