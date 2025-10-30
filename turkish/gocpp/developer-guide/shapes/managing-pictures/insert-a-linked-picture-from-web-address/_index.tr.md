---
title: Golang aracılığıyla C++ ile Web Adresinden Bir Bağlantılı Resim Ekleyin
linktitle: Web Adresinden Bağlantılı Bir Resim Eklemek
type: docs
weight: 450
url: /tr/go-cpp/insert-a-linked-picture-from-web-address/
description: Bir web adresinden bağlı resmi bir çalışma sayfasına nasıl ekleyeceğinizi öğrenin Aspose.Cells for C++ kullanarak.
---

{{% alert color="primary" %}}

Bazen bir elektronik tabloya (http://) web'den bir resim eklemeniz gerekebilir. Bunu yapmak için resmin URL'sini belirtin ve resim, Microsoft Excel'de her açıldığında indirilir. Resim fiziksel olarak Excel belgesine gömülmez, ancak bir web kaynağına işaret eder.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de (örneğin 2007):

1. **Ekle** menüsünü tıklayın ve **Resim**'i seçin.
1. Resim Ekle iletişim kutusunda resmin web adresini belirtin.

## **Aspose.Cells for C++ Kullanarak**

Aspose.Cells for C++, [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlinkedpicture/) metodunu kullanarak bağlı bir resim eklemeyi destekler. Metod, bir [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) nesnesi döndürür.

Aşağıdaki örnek, bir web adresinden bağlı bir resmi çalışma sayfasına nasıl ekleyeceğinizi gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertALinkedPictureFromWebAddress.go" >}}
