---
title: Parametreli Rapor
type: docs
weight: 60
url: /tr/reportingservices/parameterized-report/
---
{{% alert color="primary" %}} 

 A*parametreli rapor* rapor işlenirken kullanılan giriş değerlerini kabul eden bir rapordur.

 Parametreli bir raporla, bir raporun çıktısını çalışma zamanında ayarlanan değerlere göre değiştirebilirsiniz. Raporlama Hizmetleri iki tür parametreyi destekler: sorgu parametreleri ve rapor parametreleri.

- **Sorgu parametreleri** veri işleme sırasında verileri seçmek veya filtrelemek için kullanılır. Bir sorgu parametresi belirtilirse, SELECT deyimini veya bir rapor için veri alan saklı yordamı tamamlamak üzere kullanıcı veya varsayılan özellikler tarafından bir değer sağlanmalıdır.
- **Rapor parametreleri**verilerin farklı bir yönünü göstermek için rapor işleme sırasında kullanılır. Bir rapor parametresi genellikle büyük bir kayıt kümesini filtrelemek için kullanılır, ancak rapordaki sorgulara ve ifadelere bağlı olarak başka kullanımları da olabilir.

 Rapor parametreleri, bir raporda tanımlanıp rapor sunucusu tarafından işlenmeleri bakımından sorgu parametrelerinden farklıdır; sorgu parametreleri ise veri kümesi sorgusunun bir parçası olarak tanımlanıp veritabanı sunucusunda işlenir. Aspose.Cells.Report.Designer'da sorgu parametreleri, Microsoft Sorgu'da sorgu oluşturma zamanında belirtilir.

Aspose.Cells.Report.Designer'da rapor parametreleri oluşturabilir ve sorgu parametrelerini karşılık gelen rapor parametresine eşleyebilirsiniz. Bu şekilde, veri kaynağından alınan verileri sınırlamak için rapor parametreleri için değerlerin seçilmesi ve bunların sorguya geçirilmesi mümkündür.

{{% /alert %}} 
###### **Bu bölüm aşağıdaki konuları içerir:**
- [Rapor Parametreleri Oluşturma](/cells/tr/reportingservices/creating-report-parameters/)
- [Rapor Parametrelerini Değiştirme](/cells/tr/reportingservices/modifying-report-parameters/)
- [Sorgu Parametrelerini Rapor Parametrelerine Eşleme](/cells/tr/reportingservices/mapping-query-parameters-to-report-parameters/)
