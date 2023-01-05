---
title: Grafiklerle Çalışmak
type: docs
weight: 110
url: /tr/reportingservices/working-with-charts/
---
{{% alert color="primary" %}} 

 Aspose.Cells Rapor şablonu, Microsoft Excel grafiklerini destekler. Bir raporu her yürüttüğünüzde, grafik en son verilerle doldurulur.

{{% /alert %}} 

Rapor şablonuna bir grafik eklemek için:

1. İlk olarak, grafiğin veri kaynağı olacak veri kümesini oluşturun.
 Aşağıda, SQL Server Reporting Services 2005 ile birlikte gelen AdventureWorks örnek veritabanını kullanıyoruz ve Sales adında bir veri kümesi oluşturuyoruz.
 Bu SQL, veri kümesini tanımlar:

**SQL**

{{< highlight "csharp" >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



 Bakınız[Veri Kaynakları ve Sorgular](/cells/tr/reportingservices/data-sources-and-queries/) Aspose.Cells.Report.Designer'da bir veri kaynağının ve veri kümesinin nasıl oluşturulacağı hakkında daha fazla bilgi edinmek için.

1. bölümündeki talimatlara göre bir tablo raporu oluşturun.[Tablolu Rapor Oluşturma](/cells/tr/reportingservices/creating-tabular-report/) . Bu örnek için oluşturduğumuz rapor aşağıdadır. Tablo, grafiğin veri kaynağıdır.

![yapılacaklar:resim_alternatif_metin](working-with-charts_1.png)




1.  Microsoft Excel'de,**Sokmak** menü ve seçin**Çizelge**.
1.  Tıklamak**Sonraki**. 

![yapılacaklar:resim_alternatif_metin](working-with-charts_2.png)




1.  Tıkla**Dizi** sekme.

![yapılacaklar:resim_alternatif_metin](working-with-charts_3.png)




1.  Tıklamak**Eklemek**. 

![yapılacaklar:resim_alternatif_metin](working-with-charts_4.png)




1. İletişim kutusunda, Seri1 (Çeyrek seri) değerini tablonun ilk veri alanına ayarlayın.
 Örnekte bu, "CompanySales!$C$3:$C$3" şeklindedir. İlk $C$3, "Çeyrek"in ilk satır dizini ve ikinci $C$3, "Çeyrek"in son satır dizini için bir yer tutucudur ve işleme zamanında tablo verilerinin gerçek satır dizini ile değiştirilecektir. Category(X) ekseni etiketlerini “=CompanySales!$C$3:$C$3” olarak ayarlayın.

![yapılacaklar:resim_alternatif_metin](working-with-charts_5.png)




1.  Tıklamak**Eklemek** başka bir dizi eklemek için.
 Örnekte, satış serisini ekledik.
1. Series2 (Satış serisi) değerini tablonun ikinci veri alanına ayarlayın.
Örnekte "CompanySales!$D$3:$D$3" şeklindedir. İlk $D$3, "Sales"in ilk satır dizini ve ikinci $D$3, "Sales"in son satır dizini için bir yer tutucudur ve işleme zamanında tablo verilerinin gerçek satır dizini ile değiştirilecektir.
1.  Tıklamak**Sonraki** devam etmek.

![yapılacaklar:resim_alternatif_metin](working-with-charts_6.png)




1. İletişim kutusunda grafik başlığını ve kategori(X) eksenini ayarlayın.
1.  Tıklamak**Bitiş** işi tamamlamak için.

![yapılacaklar:resim_alternatif_metin](working-with-charts_7.png)



 Şablon aşağıdaki gibi görünüyor.

![yapılacaklar:resim_alternatif_metin](working-with-charts_8.png)




1. Raporu kaydedin ve Rapor Sunucusunda yayınlayın.
1. Raporu Rapor Sunucusundan dışa aktarın.
 Sonuç aşağıdaki gibidir.

![yapılacaklar:resim_alternatif_metin](working-with-charts_9.png)
