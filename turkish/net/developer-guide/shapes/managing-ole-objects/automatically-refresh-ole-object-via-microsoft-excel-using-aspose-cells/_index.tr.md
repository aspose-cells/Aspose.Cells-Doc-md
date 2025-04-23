---
title: Aspose.Cells kullanarak Microsoft Excel üzerinden OLE nesnesini otomatik olarak yenileyin
type: docs
weight: 270
url: /tr/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel'de excel dosyası açıldığında OLE nesnesini yenilemek için [**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload) özelliğini sağlar. Bu özellik sayesinde OLE nesnesi, Microsoft Excel tarafından oluşturulan doğru OLE görüntüsünü gösterecektir.

{{% /alert %}}

Aşağıdaki örnek kod, gerçek dışı bir OLE görüntüsüne sahip olan [örnek excel dosyasını](5115231.xlsx) yükler. OLE nesnesi aslında bir Microsoft Word belgesidir ancak örnek excel dosyası, Microsoft Word görüntüsü yerine hayvan görüntüsünü göstermektedir. Ancak [çıktı excel dosyasını](5115225.xlsx) açarsanız, Microsoft Excel'in doğru OLE görüntüsünü gösterdiğini göreceksiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
