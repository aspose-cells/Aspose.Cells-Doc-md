---
title: Microsoft Excel kullanarak OLE nesnesini otomatik olarak yenile Golang ile C++ kullanarak
linktitle: Otomatik olarak OLE nesnesini yenile
type: docs
weight: 270
url: /tr/go-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Aspose.Cells kullanarak Golang ile C++ ile OLE nesnelerini otomatik olarak yenileme yollarını öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel'de Excel dosyası açılırken OLE nesnesini yenilemek için [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/go-cpp/oleobject/getautoload/) özelliğini sağlar. Bu özellik sayesinde, OLE nesnesi Microsoft Excel tarafından oluşturulan doğru OLE görüntüsünü gösterecektir.

{{% /alert %}}

Aşağıdaki örnek kod, gerçek olmayan bir OLE görüntüsü içeren [örnek Excel dosyasını](5115231.xlsx) yükler. OLE nesnesi aslında bir Microsoft Word belgesidir, ancak örnek Excel dosyası, Microsoft Word görüntüsü yerine hayvan resmi gösterir. Ancak, [çıktı Excel dosyasını](5115225.xlsx) açarsanız, Microsoft Excel'in doğru OLE görüntüsünü gösterdiğini görürsünüz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutomaticallyRefreshOleObjectViaMicrosoftExcelUsingAsposeCells.go" >}}
