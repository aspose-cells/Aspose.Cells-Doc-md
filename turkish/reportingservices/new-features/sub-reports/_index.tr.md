---
title: Alt raporlar
type: docs
weight: 20
url: /tr/reportingservices/sub-reports/
---
{{% alert color="primary" %}} 

Tablo grubu satırına Alt Rapor Gömme desteği ekledik. Biçim:

&=subreport{ReportName=raporunuzun adı; parametre1 adı = parametre1 değeri; parametre2 adı = parametre2 değeri;......} 

{{% /alert %}} 
### **Örnek**
**Tablodaki bir alt rapor** 

![yapılacaklar:resim_alternatif_Metin](sub-reports_1.png)

 Örnekte alt raporun adı “Satış Siparişi Detayı”dır. Bir parametresi vardır,*Satış sipariş numarası* . parametrenin değeri*EmpSalesDetail.SalesOrderNumber.*
#### **Alt Raporların kullanımına ilişkin kısıtlamalar**
- Alt rapor, Aspose.Cells.Reporting Services Designer aracıyla tasarlanmalıdır.
- Alt Rapor, yalnızca tablo grubu satırına gömülebilir ve grup satırı, Alt Rapor dışında başka öğeler içeremez. Tablo ayrıntı satırlarına veya alt bilgi satırlarına bir Alt Raporun gömülmesine izin verilmez.
- Şu anda birden fazla düzeyi iç içe yerleştirme desteklenmemektedir. Alt Rapor, katıştırılmış rapor içeremez.
