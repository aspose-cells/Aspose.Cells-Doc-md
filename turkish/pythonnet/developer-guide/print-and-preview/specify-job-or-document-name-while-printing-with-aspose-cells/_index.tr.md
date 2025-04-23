---
title: Aspose.Cells ile yazdırırken İş veya Belge Adı belirtin
type: docs
weight: 270
url: /tr/python-net/specify-job-or-document-name-while-printing-with-aspose-cells/
---

{{% alert color="primary" %}}

Çalışma kitabınızı veya çalışma sayfanızı yazdırırken İş veya Belge Adını belirtebilirsiniz, bu amaçla WorkbookRender veya SheetRender nesnelerini kullanabilirsiniz. Aspose.Cells for Python via .NET, baskı sırasında İş Adını belirlemek için WorkbookRender.ToPrinter(printerName, jobName) ve SheetRender.ToPrinter(printerName, jobName) metodlarını sağlar.

{{% /alert %}}

## **Yazdırırken İş veya Belge Adını belirtin Aspose.Cells for Python via .NET ile**

Örnek kod, kaynak Excel dosyasını yükler ve ardından WorkbookRender.ToPrinter(yazıcıAdı, işAdı) ve SheetRender.ToPrinter(yazıcıAdı, işAdı) metodlarını kullanarak belirli iş veya belge adı belirterek yazıcıya gönderir.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SpecifyJobNameWhilePrinting.py" >}}
