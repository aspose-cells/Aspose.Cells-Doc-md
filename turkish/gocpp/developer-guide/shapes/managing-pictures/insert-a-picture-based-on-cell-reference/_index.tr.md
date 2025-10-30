---
title: Golang ve C++ kullanarak Hücre Referansına Dayalı Resim Ekleyin
linktitle: Hücre Referansına Dayalı Bir Resim Eklemek
type: docs
weight: 150
url: /tr/go-cpp/insert-a-picture-based-on-cell-reference/
description: Aspose.Cells for C++ kullanarak hücre referansına göre nasıl resim eklenir öğrenin.
---

{{% alert color="primary" %}}

Bazen boş bir resminiz vardır ve resimde verileri veya içeriği bir hücre referansı belirleyerek göstermek istersiniz. Aspose.Cells bu özelliği destekler (Microsoft Excel 2010).

{{% /alert %}}

## Hücre Referansına Dayalı Bir Resim Eklemek

Aspose.Cells, bir resim şeklinde bir çalışma sayfası hücresindeki içeriği görüntülemenin destekler. Resmi, istemci tarafı uygulamasında kullanılan kolay Aspose.Cells API'sinin bir yöntemi olan [**AddPicture**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpicture_int_int_int_int_stream/) yöntemini çağırarak çalışma sayfasına ekleyebilirsiniz. Hücre aralığını, [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) nesnesinin [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) özelliğini kullanarak belirtin.

### Kod Örneği

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertAPictureBasedOnCellReference.go" >}}
