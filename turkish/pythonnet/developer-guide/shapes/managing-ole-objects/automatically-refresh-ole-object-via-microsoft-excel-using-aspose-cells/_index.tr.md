---
title: Otomatik olarak OLE nesnesini yenile
type: docs
weight: 270
url: /tr/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, Microsoft Excel'de açıldığında OLE nesnesini yenilemek için [**OleObject.auto_load**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/auto_load) özelliğini sağlar. Bu özellik sayesinde, OLE nesnesi, Microsoft Excel tarafından üretilen doğru OLE resmi görüntüleyecektir.

{{% /alert %}}

Aşağıdaki örnek kod, gerçek dışı bir OLE görüntüsüne sahip olan [örnek excel dosyasını](5115231.xlsx) yükler. OLE nesnesi aslında bir Microsoft Word belgesidir ancak örnek excel dosyası, Microsoft Word görüntüsü yerine hayvan görüntüsünü göstermektedir. Ancak [çıktı excel dosyasını](5115225.xlsx) açarsanız, Microsoft Excel'in doğru OLE görüntüsünü gösterdiğini göreceksiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-RefreshOLEObjects-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
