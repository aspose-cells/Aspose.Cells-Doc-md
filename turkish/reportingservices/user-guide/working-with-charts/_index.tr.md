---
title: Grafiklerle Çalışma
type: docs
weight: 110
url: /tr/reportingservices/working-with-charts/
---

{{% alert color="primary" %}} 

Aspose.Cells Rapor şablonu Microsoft Excel grafiklerini destekler. Her bir raporu yürüttüğünüzde, grafik en güncel verilerle doldurulur. 

{{% /alert %}} 

Bir grafik rapor şablonuna eklemek için:

1. İlk olarak, grafik veri kaynağı olacak veri kümesini oluşturun.
   Aşağıda, SQL Server Reporting Services 2005 ile birlikte sevk edilen AdventureWorks örnek veritabanını kullanıyoruz ve Sales adında bir veri kümesi oluşturuyoruz.
   Bu SQL, veri kümesini tanımlar: 

**SQL**

{{< highlight csharp >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



Daha fazla bilgi için [Veri Kaynakları ve Sorgular](/cells/tr/reportingservices/data-sources-and-queries/) bölümüne başvurun.

1. [Tablo Tipi Rapor Oluşturma](/cells/tr/reportingservices/creating-tabular-report/) bölümünde verilen talimatları izleyerek bir tablo raporu oluşturun. Bu örneğimiz için oluşturduğumuz rapor aşağıdadır. Tablo, grafiğin veri kaynağıdır. 

![todo:image_alt_text](working-with-charts_1.png)




1. Microsoft Excel'de **Ekle** menüsünü tıklayın ve **Grafik**i seçin.
1. **Sonraki**'ye tıklayın. 

![todo:image_alt_text](working-with-charts_2.png)




1. **Seriler** sekmesine tıklayın. 

![todo:image_alt_text](working-with-charts_3.png)




1. **Ekle**'ye tıklayın. 

![todo:image_alt_text](working-with-charts_4.png)




1. Diyalog kutusunda, Series1 (Çeyrek serisi) değerini tablonun ilk veri alanı olarak ayarlayın.
   Örneğin, bu “CompanySales!$C$3:$C$3” şeklinde olacaktır. İlk $C$3 “Çeyrek”in ilk satır dizinidir ve ikinci $C$3, “Çeyrek”in son satır dizininin yer tutucusu ve bu, tablo verisinin gerçek satır diziniyle işlenme sırasında değiştirilecektir. Kategori(X) eksen etiketlerini “=CompanySales!$C$3:$C$3” olarak ayarlayın. 

![todo:image_alt_text](working-with-charts_5.png)




1. Başka bir seri eklemek için **Ekle**'ye tıklayın.
   Örnekte, satış serisini ekledik. 
1. Series2'nin (Satış serisi) değerini tablonun ikinci veri alanına ayarlayın.
   Örnekte, “CompanySales!$D$3:$D$3” olarak belirtilir. İlk $D$3, “Satış” ın ilk satır dizinidir ve ikinci $D$3, “Satış” ın gerçek satır dizinine, işleme zamanında tablo verileriyle değiştirilecek bir yer tutucusudur. 
1. Devam etmek için **Sonraki**'yi tıklayın. 

![todo:image_alt_text](working-with-charts_6.png)




1. İletişim kutusunda, grafik başlığını ve kategori(X) eksenini ayarlayın.
1. İşlemi tamamlamak için **Bitir**'e tıklayın. 

![todo:image_alt_text](working-with-charts_7.png)



Şablon aşağıdaki gibi görünüyor. 

![todo:image_alt_text](working-with-charts_8.png)




1. Raporu kaydedin ve Rapor Sunucusuna yayınlayın.
1. Raporu Rapor Sunucusundan dışa aktarın.
   Sonuç aşağıdaki gibidir. 

![todo:image_alt_text](working-with-charts_9.png)
