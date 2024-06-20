---
title: Yeni Veri Kaynakları ve Sorgular Oluşturma
type: docs
weight: 20
url: /tr/reportingservices/creating-new-data-sources-and-queries/
---

{{% alert color="primary" %}} 

Aspose.Cells.Report.Designer, MS Query ile entegre olur ve veri kaynakları ve sorgular oluşturmak için MS Query'yi bir araç olarak kullanır. Aspose.Cells.Report.Designer'da yeni bir veri kaynağı ve sorgu oluşturmak için aşağıdaki adımları izleyin: 

{{% /alert %}} 

Aspose.Cells.Report.Designer'da yeni bir veri kaynağı ve sorgu oluşturmak için:

1. Microsoft Excel'i açın.
1. Aspose.Cells.Report.Designer araç çubuğundaki **DataSet Oluştur**'a tıklayın: 

![todo:image_alt_text](creating-new-data-sources-and-queries_1.png)


Tüm veri kaynakları ve sorgular iletişim kutusunda listelenir. 

1. Bir veri kaynağı düğümü: 

![todo:image_alt_text](creating-new-data-sources-and-queries_2.png)

1. Bir veri kümesi düğümü: 

![todo:image_alt_text](creating-new-data-sources-and-queries_3.png)

1. Ağacın kök düğümünü seçin.
1. **Ekle**'ye tıklayın. 

   **Veri kaynakları ve veri kümesi ekleme** 

![todo:image_alt_text](creating-new-data-sources-and-queries_4.png)




1. İletişim kutusunda veri kaynağını **SqlServer** ve veri kümesini **EmpsSalesDetail** olarak adlandırın.
1. **Sonraki**'ye tıklayın. 

   **Veri kümeleri ve veri kaynakları ekleme** 

![todo:image_alt_text](creating-new-data-sources-and-queries_5.png)



Aspose.Cells.Report.Designer, Microsoft Query'yi başlatır. 

1. Yeni Veri Kaynağı'nı seçmek için Choose Data Source iletişim kutusunda **Yeni Veri Kaynağı**'nı seçin.
1. **Tamam**'a tıklayın.
   Ayrıca mevcut bir veri kaynağını da seçebilirsiniz. 

   **Veri kaynağı seçme** 

![todo:image_alt_text](creating-new-data-sources-and-queries_6.png)




1. Bir veri kaynağı adı girin ve veritabanı sürücüleri açılır listesinden SQL Server'ı seçin.
1. **Bağlan**'a tıklayın. 

   **Yeni veri kaynağı oluşturma** 

![todo:image_alt_text](creating-new-data-sources-and-queries_7.png)




SQL Server Giriş iletişim kutusunda, her öğe için uygun değeri seçin.
   Örneğin, sunucuyu yerel olarak ayarlayın, AdventureWorks veritabanını seçin ve **Güvenilir Bağlantı Kullan**'ı seçin.
1. **Tamam**'a tıklayın. 

   **SQL sunucusuna giriş yapma** 

![todo:image_alt_text](creating-new-data-sources-and-queries_8.png)




1. **Tamam**'a tıklayın. 

   **Şimdi SQL sunucusuna giriş yaptığımıza dikkat edin** 

![todo:image_alt_text](creating-new-data-sources-and-queries_9.png)



Yeni veri kaynağı, **Veri Kaynağı Seç** iletişim kutusunda görünür. 

1. Yeni veri kaynağını seçin. 

   **Yeni veri kaynağı** 

![todo:image_alt_text](creating-new-data-sources-and-queries_10.png)




1. Microsoft Query'yi açmak için **Tamam**'ı tıklayın.
1. Microsoft Query'de bir sorgu oluşturmak için Microsoft Query Yardımcısı'na başvurun. Aşağıdaki örnekte, parametrelerle bir sorgu oluşturuyoruz. 

   **Sorgu oluşturma** 

![todo:image_alt_text](creating-new-data-sources-and-queries_11.png)



SQL aşağıdaki gibidir: 

**SQL**

{{< highlight csharp >}}

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


Sorguda üç parametre bulunmaktadır: RaporYılı, RaporAyı ve EmpID.

1. Microsoft Query'nin **Dosya** menüsünden **Aspose.Cells.Report.Designer**'a **Geri Dön**'ü seçin. 

   **Rapor tasarımcısına dönme** 

![todo:image_alt_text](creating-new-data-sources-and-queries_12.png)



Yukarıda oluşturulan veri kaynağı ve sorgu, iletişim kutusunda listelenmiştir. 

1. Ayrıntılı bilgilerini görmek için veri kaynağı **SqlServer**'ı tıklayın. 

   **Yeni veri kaynağı** 

![todo:image_alt_text](creating-new-data-sources-and-queries_13.png)




1. Ayrıntılı bilgilerini görmek için sorgu EmpSalesDetails'ı tıklayın. 

   **Sorgu için SQL Sekmesini tıklayın** 

![todo:image_alt_text](creating-new-data-sources-and-queries_14.png)



**Sorgunun sütunlarını görüntülemek için Sütunlar Sekmesini tıklayın** 

![todo:image_alt_text](creating-new-data-sources-and-queries_15.png)



**Sorgunun parametrelerini görüntülemek için Parametreler Sekmesini tıklayın** 

![todo:image_alt_text](creating-new-data-sources-and-queries_16.png)



