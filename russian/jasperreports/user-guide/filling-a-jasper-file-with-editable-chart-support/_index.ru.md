---
title: Заполнение файла .jasper с поддержкой редактируемых диаграмм
type: docs
weight: 10
url: /ru/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---
{{% alert color="primary" %}} 

 Aspose.Cells for JasperReports требует, чтобы файл .jasper был заполнен объектом .jrprint или JasperPrint, прежде чем его можно будет экспортировать в файл XLS. Никаких изменений в файле .jrxml не требуется. Процедура заполнения сохраняет внутренние представления диаграмм в объекте JasperPrint, который затем используется для создания редактируемых диаграмм.

{{% /alert %}} 

Пожалуйста, прочитайте документацию JasperReports для подробного описания того, как заполнить отчет.

Вот пример:

**Java**

{{< highlight "csharp" >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
