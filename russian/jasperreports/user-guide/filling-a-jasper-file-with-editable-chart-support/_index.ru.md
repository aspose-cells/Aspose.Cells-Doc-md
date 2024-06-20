---
title: Заполнение файла .jasper с поддержкой редактируемой диаграммы
type: docs
weight: 10
url: /ru/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports требует заполнения файла .jasper файлом .jrprint или объектом JasperPrint перед экспортом в файл XLS. Никаких модификаций файла .jrxml не требуется. Процедура заполнения сохраняет внутренние представления диаграмм в объекте JasperPrint, который затем используется для создания редактируемых диаграмм. 

{{% /alert %}} 

Для получения подробного описания процедуры заполнения отчета прочитайте документацию JasperReports.

Вот пример:

**Java**

{{< highlight csharp >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
