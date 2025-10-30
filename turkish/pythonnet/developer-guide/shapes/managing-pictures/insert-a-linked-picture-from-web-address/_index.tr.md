---
title: Web Adresinden Bağlantılı Bir Resim Eklemek
type: docs
weight: 450
url: /tr/python-net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

Bazen bir elektronik tabloya (http://) web'den bir resim eklemeniz gerekebilir. Bunu yapmak için resmin URL'sini belirtin ve resim, Microsoft Excel'de her açıldığında indirilir. Resim fiziksel olarak Excel belgesine gömülmez, ancak bir web kaynağına işaret eder.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de (örneğin 2007):

1. **Ekle** menüsünü tıklayın ve **Resim**'i seçin.
1. Resim Ekle iletişim kutusunda resmin web adresini belirtin.

## **Aspose.Cells for Python via .NET Kullanılarak**

Aspose.Cells for Python via .NET, [**ShapeCollection.add_linked_picture(int upper_left_row, int upper_left_column, int height_pixels, int width_pixels, str source_full_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_linked_picture) kullanarak bağlı bir resim eklemeyi destekler. Yöntem bir [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) nesnesi döndürür.

Aşağıdaki örnek, bir elektronik tabloya hücre referansı üzerinden bağlantılı resim eklemenin nasıl yapılacağını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertLinkedPicture-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
