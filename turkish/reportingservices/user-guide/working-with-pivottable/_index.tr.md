---
title: PivotTable ile Çalışmak
type: docs
weight: 100
url: /tr/reportingservices/working-with-pivottable/
---
{{% alert color="primary" %}} 

 A*Pivot tablo* verileri özetleyen ve anlamlı bir şekilde sunan etkileşimli bir tablodur. SQL Server Reporting Services, bir pivot tabloyu korurken bir raporu Microsft Excel biçiminde dışa aktaramaz. Rapor kullanıcılarının, Raporlama Servislerinden Microsoft Excel'e bir pivot tablo raporu verdikleri her seferde, pivot tabloları manuel olarak oluşturmaları gerekir. Aspose.Cells for Reporting Services ile rapor tasarım zamanında bir kez pivot tablo tasarlayabilirsiniz. Rapor her çalıştırıldığında, Aspose.Cells for Reporting Services, raporu Microsoft Excel'e aktarır ve verileri pivot tabloya yeniler.

{{% /alert %}} 

Pivot tablo raporu oluşturmak için:

1. Pivot tablo için veri kaynağı olarak bir veri kümesi oluşturun.
 Aşağıda, SQL Server Reporting Services 2005 ile birlikte gelen AdventureWorks örnek veritabanını kullanıyoruz ve "satış" adında bir veri kümesi oluşturuyoruz.
Veri kümesi için SQL aşağıdaki gibidir:

**SQL**

{{< highlight "csharp" >}}

 SELECT  PC.Name AS ProdCat,

	    PS.Name AS SubCat,

	    DATEPART(yy, SOH.OrderDate) AS OrderYear,

	    'Q' + DATENAME(qq, SOH.OrderDate) AS OrderQtr,

         SUM(SOD.UnitPrice * SOD.OrderQty) AS Sales

FROM    Production.ProductSubcategory PS INNER JOIN

         Sales.SalesOrderHeader SOH INNER JOIN

         Sales.SalesOrderDetail SOD ON SOH.SalesOrderID = SOD.SalesOrderID INNER JOIN

         Production.Product P ON SOD.ProductID = P.ProductID ON PS.ProductSubcategoryID = P.ProductSubcategoryID INNER JOIN

         Production.ProductCategory PC ON PS.ProductCategoryID = PC.ProductCategoryID

WHERE   (SOH.OrderDate BETWEEN '1/1/2002' AND '12/31/2003')

GROUP BY  DATEPART(yy, SOH.OrderDate), PC.Name, PS.Name, 'Q' + DATENAME(qq, SOH.OrderDate), PS.ProductSubcategoryID



{{< /highlight >}}



{{% alert color="primary" %}} 

 Bakınız[Veri Kaynakları ve Sorgular](/cells/tr/reportingservices/data-sources-and-queries/) Aspose.Cells.Report.Designer ile veri kaynağı ve veri kümesi oluşturma hakkında daha fazla bilgi edinmek için.

{{% /alert %}} 

1.  bölümündeki talimata göre bir tablo raporu oluşturun.[Tablolu Rapor Oluşturma](/cells/tr/reportingservices/creating-tabular-report/), Aşağıda gösterildiği gibi.
 Tablo, pivot tablo için veri kaynağı olacaktır.

![yapılacaklar:resim_alternatif_metin](working-with-pivottable_1.png)




1.  Microsoft Excel'de,**Sokmak** menü, seç**İsim** ve sonra**Tanımlamak**.
1. Bir adı “satış” olarak tanımlayın.
 Adın aralığı, aşağıda gösterildiği gibi başlık başlığının ilk hücresiyle başlar ve tablo veri satırının son hücresinde biter.

![yapılacaklar:resim_alternatif_metin](working-with-pivottable_2.png)




1.  Tıklamak**Tamam** bitirmek için.
1. Pivot tablo için yeni bir sayfa oluşturun.
1.  itibaren**Veri** menü, seç**PivotTable ve PivotChart Raporu** Pivot tablo eklemek için.
 Bir iletişim kutusu görüntülenir.
1.  Seçme**Microsoft Office Excel listesi veya veritabanı** Veri kaynağı olarak ve**Pivot tablo** rapor tipi olarak
1.  Tıklamak**Sonraki** devam etmek.

![yapılacaklar:resim_alternatif_metin](working-with-pivottable_3.png)




1. İletişim kutusunda, yukarıda tanımladığınız adı "satış" olarak girin.
1.  Tıklamak**Sonraki** devam etmek.

![yapılacaklar:resim_alternatif_metin](working-with-pivottable_4.png)




1.  Tıklamak**Bitiş**. 

![yapılacaklar:resim_alternatif_metin](working-with-pivottable_5.png)




1.  Pivot tabloyu Excel'de tasarlayın.

![yapılacaklar:resim_alternatif_metin](working-with-pivottable_6.png)



 Tasarlanan pivot tablo aşağıda gösterilmiştir.

![yapılacaklar:resim_alternatif_metin](working-with-pivottable_7.png)




1.  Pivot tabloya sağ tıklayın ve seçin**Tablo Seçenekleri**.
1.  Emin olun**Açıkken yenile** seçildi.

![yapılacaklar:resim_alternatif_metin](working-with-pivottable_8.png)




1. Raporu kaydedin ve Rapor Sunucusunda yayınlayın.
1. Raporu Rapor Sunucusundan dışa aktarın.
 Sonuç aşağıda gösterilmiştir.

![yapılacaklar:resim_alternatif_metin](working-with-pivottable_9.png)
