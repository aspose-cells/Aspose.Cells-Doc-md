---
title: Parametreli Rapor
type: docs
weight: 60
url: /tr/reportingservices/parameterized-report/
---

{{% alert color="primary" %}} 

Bir *parametreli rapor*, raporun işlendiği sırada kullanılan giriş değerlerini kabul eden bir rapordur. 

Parametreli bir rapor ile raporun çıktısını çalışma zamanındaki ayarlanan değerlere göre değiştirebilirsiniz. Raporlama Hizmetleri, iki tür parametreyi destekler: sorgu parametreleri ve rapor parametreleri. 

- **Sorgu parametreleri**, veri işleme sırasında veri seçmek veya filtrelemek için kullanılır. Bir sorgu parametresi belirtilmişse, bir rapor için veri almak üzere tamamlanması gereken bir SELECT ifadesini veya saklanmış prosedürü tamamlamak için kullanıcı veya varsayılan özellikler tarafından bir değer sağlanmalıdır.
- **Rapor parametreleri**, rapor işleme sırasında verinin farklı bir yönünü göstermek için kullanılır. Rapor parametresi genellikle büyük bir kayıt kümesini filtrelemek için kullanılır, ancak rapordaki sorgulara ve ifadelere bağlı olarak başka kullanımları olabilir.

Rapor parametreleri, raporda tanımlanır ve rapor sunucusu tarafından işlenir; sorgu parametreleri ise veri kümesi sorgusunun bir parçası olarak tanımlanır ve veritabanı sunucusunda işlenir. Aspose.Cells.Report.Designer'da sorgu parametreleri, Microsoft Query tarafından sorgu oluşturma zamanında belirtilir. 

Aspose.Cells.Report.Designer'da rapor parametreleri oluşturabilir ve sorgu parametrelerini ilgili rapor parametresine eşleyebilirsiniz. Bu şekilde, rapor parametreleri için değerler seçmek ve bunları sorguya ileterek veri kaynağından alınacak veriyi sınırlamak mümkün olur.

{{% /alert %}} 
###### **Bu bölüm şu konuları içerir:** 
- [Rapor Parametreleri Oluşturma](/cells/tr/reportingservices/creating-report-parameters/)
- [Rapor Parametrelerini Düzenleme](/cells/tr/reportingservices/modifying-report-parameters/)
- [Sorgu Parametrelerini Rapor Parametrelerine Eşleme](/cells/tr/reportingservices/mapping-query-parameters-to-report-parameters/)
