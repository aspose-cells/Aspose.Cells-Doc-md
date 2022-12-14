---
title: Cell Referansına Göre Bir Resim Ekleyin
type: docs
weight: 150
url: /tr/net/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

Bazen boş bir resminiz olur ve formül çubuğunda bir hücre referansı ayarlayarak resimdeki verileri veya içeriği göstermeniz gerekir. Aspose.Cells bu özelliği destekler (Microsoft Excel 2010).

{{% /alert %}}

## Cell Referansına Göre Resim Ekleme

Aspose.Cells, bir çalışma sayfası hücresinin içeriğinin görüntü şeklinde görüntülenmesini destekler. Resmi, görüntülemek istediğiniz verileri içeren hücreye bağlayabilirsiniz. Hücre veya hücre aralığı grafik nesnesine bağlı olduğundan, o hücre veya hücre aralığındaki verilerde yaptığınız değişiklikler otomatik olarak grafik nesnesinde görünür. çağırarak çalışma sayfasına bir resim ekleyin.[**Resim Ekle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) yöntemi[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) koleksiyon (kapsüllenmiş[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nesne). kullanarak hücre aralığını belirtin.[**formül**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) özniteliği[**Resim**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)nesne.

### Kod Örneği

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
