---
title: Alt Rapor
type: docs
weight: 90
url: /tr/reportingservices/sub-report/
---
{{% alert color="primary" %}} 

Bir alt rapor, bir tablo öğesine gömülebilir. Biçim şöyledir: &=subreport{ReportName=raporunuzun adı; parametre1 adı = parametre1 değeri; parametre2 adı = parametre2 değeri; ...}

**Rapor tanımındaki bir alt rapor** 

![yapılacaklar:resim_alternatif_metin](sub-report_1.png)

Örnekte alt raporun adı “Satış Siparişi Detayı”dır. SalesOrderNumber adında bir parametresi vardır. Parametrenin değeri EmpSalesDetail.SalesOrderNumber şeklindedir.
### **Alt Raporlarla İlgili Kısıtlamalar**
1. Alt rapor Aspose.Cells.ReportingServices Designer ile tasarlanmalıdır.
1. Alt rapor, yalnızca tablo grubu satırına gömülebilir ve grup satırı, alt rapor dışında herhangi bir öğe içeremez. Tablo ayrıntı satırlarına veya alt bilgi satırlarına bir alt raporun yerleştirilmesine izin verilmez.
1. Şu anda birden fazla düzeyi iç içe yerleştirme desteklenmemektedir. Alt rapor, katıştırılmış bir rapor içeremez.

{{% /alert %}} 
###### **Bu bölüm aşağıdaki konuları içerir:**
- [Tablo Öğesi Oluşturma](/cells/tr/reportingservices/creating-table-item/)
- [Alt Rapor Öğesi Ekle](/cells/tr/reportingservices/add-sub-report-item/)
