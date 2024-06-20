---
title: Akıllı İmler ile Veri Birleştirirken Bildirimleri Alma
type: docs
weight: 20
url: /tr/net/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells API'leri, biçimlendirme ve formüllerin [dizayn tabloları](/cells/tr/net/what-is-a-designer-spreadsheet/) içine yerleştirildiği ve ardından belirtilen Akıllı İmler'e göre verilerin doldurulması için [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) sınıfıyla çalışmak için [sağlar](https://docs.aspose.com/cells/net/smart-markers/). Bazen, hücre referansı veya işlenen belirli Akıllı İmleç hakkında bildirim almak gerekebilir. Bu, [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) özelliği ve Aspose.Cells for .NET sürümüyle beraber sunulan [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) arayüzü kullanarak başarılabilir.

{{% /alert %}} 

[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) arayüzünün kullanımını, [WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) yöntemi için geri arama işlemini tanımlamak için yeni bir sınıfı tanımlamak için aşağıdaki kod parçası gösterilmektedir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



İşlemin geri kalanı, Smart İmler içeren [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) yükleyerek ve veri kaynağını ayarlayarak işlemi içerir. Örneği basit tutmak için, yalnızca iki Akıllı İmleyi içeren önceden tanımlanmış bir dizayn tablosu kullandık. Veri kaynağı belirtilen Akıllı İmlere göre verileri birleştirmek üzere dinamik olarak oluşturulur.

|![todo:image_alt_text](getting-notifications-while-merging-data-with-smart-markers_1.png)|
| :- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
