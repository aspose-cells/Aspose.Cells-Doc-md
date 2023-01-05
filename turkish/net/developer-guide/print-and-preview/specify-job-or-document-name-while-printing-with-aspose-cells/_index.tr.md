---
title: Aspose.Cells ile yazdırırken İş veya Belge Adını belirtin
type: docs
weight: 270
url: /tr/net/specify-job-or-document-name-while-printing-with-aspose-cells/
---
{{% alert color="primary" %}}

WorkbookRender veya SheetRender nesnelerini kullanarak çalışma kitabınızı veya çalışma sayfanızı yazdırırken İş veya Belge Adını belirtebilirsiniz. Aspose.Cells, çalışma kitabınızı veya çalışma sayfanızı yazdırırken İş Adını belirtmek için kullanabileceğiniz WorkbookRender.ToPrinter(printerName, jobName) ve SheetRender.ToPrinter(printerName, jobName) yöntemlerini sağlar.

{{% /alert %}}

## Aspose.Cells ile yazdırırken İş veya Belge Adını belirtin

Örnek kod, kaynak Excel dosyasını yükler ve ardından WorkbookRender.ToPrinter(yazıcıAdı, işAdı) ve SheetRender.ToPrinter(yazıcıAdı, işAdı) yöntemlerini kullanarak iş veya belge adını belirterek yazıcıya gönderir.

## Basit kod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SpecifyJobWhilePrinting-SpecifyJobNameWhilePrinting.cs" >}}
