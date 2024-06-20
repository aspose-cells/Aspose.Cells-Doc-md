---
title: Alt Raporlar
type: docs
weight: 20
url: /tr/reportingservices/sub-reports/
---

{{% alert color="primary" %}} 

Bir Alt-Raporu bir Tablo grubu satırına gömecek bir desteği dahil ettik. Format şudur:

&=subreport{ReportName=your report name; parameter1 name = parameter1 value; parameter2 name = parameter2 value;......} 

{{% /alert %}} 
### **Örnek**
**Bir tabloda alt rapor** 

![todo:image_alt_text](sub-reports_1.png)

Örneğin, alt raporun adı “Satış Sipariş Detayı” dır. Bir parametreye sahiptir, *SatışSiparişNumarası*. Parametrenin değeri *EmpSatışDetay.SiparişNumarası* dır.
#### **Alt-Raporları Kullanma Kısıtlamaları**
- Alt-rapor, Aspose.Cells.Reporting Services Designer aracı ile tasarlanmalıdır.
- Alt-Rapor yalnızca tablo grup satırına gömülebilir ve grup satırı, Alt-Rapor dışında başka öğeler içeremez. Alt-Raporu tablo detay satırlarına veya altbilgi satırlarına gömmek mümkün değildir.
- Şu anda birden fazla seviye iç içe desteği bulunmamaktadır. Alt-Rapor gömülü rapor içeremez.
