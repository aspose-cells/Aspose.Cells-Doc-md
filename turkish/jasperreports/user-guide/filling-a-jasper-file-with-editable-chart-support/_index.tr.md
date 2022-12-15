---
title: Bir .jasper Dosyasını Düzenlenebilir Grafik Desteğiyle Doldurma
type: docs
weight: 10
url: /tr/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---
{{% alert color="primary" %}} 

 Aspose.Cells for JasperReports, bir .jasper dosyasının bir XLS dosyasına aktarılabilmesi için önce bir .jrprint veya JasperPrint nesnesine doldurulmasını gerektirir. .jrxml dosyası için herhangi bir değişiklik yapılması gerekmez. Doldurma prosedürü, grafiklerin dahili temsillerini, daha sonra düzenlenebilir grafikler oluşturmak için kullanılan JasperPrint nesnesine depolar.

{{% /alert %}} 

Bir raporun nasıl doldurulacağına ilişkin ayrıntılı açıklama için lütfen JasperReports belgelerini okuyun.

İşte bir örnek:

**Java**

{{< highlight "csharp" >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
