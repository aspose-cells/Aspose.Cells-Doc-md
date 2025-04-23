---
title: Web Adresinden Bağlantılı Bir Resim Eklemek
type: docs
weight: 450
url: /tr/net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

Bazen bir elektronik tabloya (http://) web'den bir resim eklemeniz gerekebilir. Bunu yapmak için resmin URL'sini belirtin ve resim, Microsoft Excel'de her açıldığında indirilir. Resim fiziksel olarak Excel belgesine gömülmez, ancak bir web kaynağına işaret eder.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de (örneğin 2007):

1. **Ekle** menüsünü tıklayın ve **Resim**'i seçin.
1. Resim Ekle iletişim kutusunda resmin web adresini belirtin.

## **Aspose.Cells for .NET Kullanımı**

Aspose.Cells for .NET, [**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture) kullanarak bağlantılı bir resim eklemeyi destekler. Bu yöntem bir [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) nesnesi döndürür.

Aşağıdaki örnek, bir elektronik tabloya hücre referansı üzerinden bağlantılı resim eklemenin nasıl yapılacağını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
