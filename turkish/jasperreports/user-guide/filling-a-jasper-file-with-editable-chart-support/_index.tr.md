---
title: Düzenlenebilir Grafik Desteğiyle .jasper Dosyasını Doldurma
type: docs
weight: 10
url: /tr/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports, XLS dosyasına dışa aktarılabilir olmadan önce .jasper dosyasının .jrprint veya JasperPrint nesnesine doldurulmasını gerektirir. .jrxml dosyası için herhangi bir değişiklik gerekmez. Doldurma işlemi, grafiklerin içsel temsillerini JasperPrint nesnesine depolar, ardından bu nesne düzenlenebilir grafikler oluşturmak için kullanılır. 

{{% /alert %}} 

Raporu nasıl dolduracağınızın detaylı açıklaması için lütfen JasperReports belgelerini okuyun.

İşte bir örnek:

**Java**

{{< highlight csharp >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
