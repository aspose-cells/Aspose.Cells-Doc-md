---
title: Hücre Referansına Dayalı Bir Resim Eklemek
type: docs
weight: 150
url: /tr/python-net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Bazen, boş bir resimle karşılaşırsınız ve hücredeki verileri veya içerikleri göstermek için hücre referansı ayarlamanız gerekir. Aspose.Cells for Python via .NET bu özelliği (Microsoft Excel 2010) destekler.

{{% /alert %}}

## Hücre Referansına Dayalı Bir Resim Eklemek

Aspose.Cells for Python via .NET, bir çalışma sayfası hücresinin içeriğini bir resim şekli olarak görüntülemeyi destekler. Resmi, göstermek istediğiniz veriyi içeren hücreye bağlayabilirsiniz. Hücre veya hücre aralığı grafiğe bağlı olduğu için, bu hücre veya hücre aralığındaki verilerde yaptığınız değişiklikler otomatik olarak grafik nesnesinde görünür. Bir resmi çalışma sayfasına eklemek için [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture)  yöntemini çağırın; bu yöntem [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)  topluluğunun (nesne içinde kapsüllenmiş olan [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)) bir üyesidir. Hücre aralığını [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula)  özelliğiyle belirtin; bu [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)  nesnesinin.

### Kod Örneği

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertPictureCellReference-1.py" >}}
