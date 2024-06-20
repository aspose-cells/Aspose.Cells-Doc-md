---
title: Alt Rapor
type: docs
weight: 90
url: /tr/reportingservices/sub-report/
---

{{% alert color="primary" %}} 

Bir alt rapor bir tablo öğesine yerleştirilebilir. Format şudur: &=subreport{ReportName=Rapor adınız; parametre1 adı = parametre1 değeri; parametre2 adı = parametre2 değeri; ...}

**Bir rapor tanımındaki bir alt rapor** 

![todo:image_alt_text](sub-report_1.png)

Örnekte, alt raporun adı “Satış Siparişi Detay”dır. Bir parametre vardır, SalesOrderNumber. Parametrenin değeri EmpSalesDetail.SalesOrderNumber'dir.
### **Alt Raporlar üzerindeki Kısıtlamalar**
1. Alt rapor Aspose.Cells.ReportingServices Designer ile tasarlanmalıdır.
1. Alt rapor yalnızca tablo grup satırına gömülebilir ve grup satırı alt rapor dışında herhangi bir öğe içeremez. Alt raporun tablo detay satırlarına veya altbilgi satırlarına gömülmesine izin verilmez.
1. Şu anda, birden fazla seviyede iç içe geçme desteklenmemektedir. Alt rapor gömülü bir rapor içeremez.

{{% /alert %}} 
###### **Bu bölüm şu konuları içerir:** 
- [Tablo Öğesi Oluşturma](/cells/tr/reportingservices/creating-table-item/)
- [Alt Rapor Öğesi Ekleme](/cells/tr/reportingservices/add-sub-report-item/)
