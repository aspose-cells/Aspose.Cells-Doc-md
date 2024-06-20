---
title: PivotTablo İle Çalışma
type: docs
weight: 100
url: /tr/reportingservices/working-with-pivottable/
---

{{% alert color="primary" %}} 

Bir *pivot tablosu*, verileri özetleyen ve anlamlı bir şekilde sunan etkileşimli bir tablodur. SQL Server Reporting Services, bir pivot tablosunu koruyarak bir raporu Microsft Excel biçimine dışa aktaramaz. Rapor kullanıcıları, Raporlama Hizmetleri'nden Microsoft Excel'e bir pivot tablo raporu dışa aktardıklarında her seferinde manuel olarak pivot tabloları oluşturmak zorundadır. Aspose.Cells for Reporting Services ile rapor tasarım zamanında bir kez bir pivot tablo tasarlayabilirsiniz. Her defasında rapor çalıştığında, Aspose.Cells for Reporting Services raporu Microsoft Excel'e dışa aktarır ve verileri pivot tablosuna yeniler.

{{% /alert %}} 

Pivot tablo raporu oluşturmak için:

1. Pivot tablosunun veri kaynağı olarak bir veri kümesi oluşturun.
   Aşağıda, SQL Server Reporting Services 2005 ile birlikte gelirken AdventureWorks örnek veritabanını kullandık ve 'satış' adında bir veri kümesi oluşturduk.
   Veri seti için SQL aşağıdaki gibidir: 

**SQL**

{{< highlight csharp >}}

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

Lütfen [Veri Kaynakları ve Sorgular](/cells/tr/reportingservices/data-sources-and-queries/) sayfasına göz atın ve Aspose.Cells.Report.Designer ile veri kaynağı ve veri kümesi nasıl oluşturulur hakkında daha fazla bilgi edinin.

{{% /alert %}} 

1. [Tablo Raporu Oluşturma](/cells/tr/reportingservices/creating-tabular-report/) bölümündeki talimatlara göre bir tablo raporu oluşturun, aşağıdaki gibi.
   Tablo, özet tablosu için veri kaynağı olacaktır. 

![todo:image_alt_text](working-with-pivottable_1.png)




1. Microsoft Excel'de **Ekle** menüsünden **Ad** ve ardından **Tanımla**yı seçin.
1. “satış” olarak bir isim tanımlayın.
   Ad aralığı, başlık başlığının ilk hücresi ile tablo veri satırının son hücresi arasında başlar ve aşağıda gösterildiği gibi biter. 

![todo:image_alt_text](working-with-pivottable_2.png)




1. Bitirmek için **Tamam**'ı tıklayın.
1. Özet tablo için yeni bir sayfa oluşturun.
1. **Veri** menüsünden **Özet Tablo ve Özet Grafik Raporu**nu seçerek özet tablo ekleyin.
   Bir iletişim kutusu görüntülenir.
1. **Microsoft Office Excel listesi veya veritabanı**'nı veri kaynağı olarak ve **özet tablo**'yu rapor türü olarak seçin.
1. Devam etmek için **Sonraki**'yi tıklayın. 

![todo:image_alt_text](working-with-pivottable_3.png)




1. İletişim kutusuna yukarıda tanımladığınız “satış” ismini girin.
1. Devam etmek için **Sonraki**'yi tıklayın. 

![todo:image_alt_text](working-with-pivottable_4.png)




1. **Bitir**'e tıklayın. 

![todo:image_alt_text](working-with-pivottable_5.png)




1. Excel'de özet tabloyu tasarlayın. 

![todo:image_alt_text](working-with-pivottable_6.png)



Tasarlanan özet tablo aşağıda gösterilmiştir. 

![todo:image_alt_text](working-with-pivottable_7.png)




1. Özet tabloyu sağ tıklayın ve **Tablo Seçenekleri**'ni seçin.
1. **Açıkta Yenile**'nin seçili olduğundan emin olun. 

![todo:image_alt_text](working-with-pivottable_8.png)




1. Raporu kaydedin ve Rapor Sunucusuna yayınlayın.
1. Raporu Rapor Sunucusundan dışa aktarın.
   Sonuç aşağıda gösterilmektedir. 

![todo:image_alt_text](working-with-pivottable_9.png)
