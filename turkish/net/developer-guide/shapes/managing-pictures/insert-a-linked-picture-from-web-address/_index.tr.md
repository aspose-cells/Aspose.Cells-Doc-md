---
title: Web Adresinden Bağlantılı Resim Ekleme
type: docs
weight: 450
url: /tr/net/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

Bazen web'den (http://) bir çalışma sayfasına bir resim eklemeniz gerekir. Bunu yapmak için resmin URL'sini belirtin ve resim, elektronik tablo Microsoft Excel'de her açıldığında indirilecektir. Görüntü fiziksel olarak Excel belgesine gömülü değildir, ancak bir web kaynağına işaret eder.

{{% /alert %}}

## **Microsoft Excel'i kullanma**

Microsoft Excel'de (örneğin 2007):

1.  Tıkla**Sokmak** menü ve seçin**Resim**.
1. Resim Ekle iletişim kutusunda resmin web adresini belirtin.

## **Aspose.Cells for .NET'i kullanma**

 Aspose.Cells for .NET, şunu kullanarak bağlantılı bir resim eklemeyi destekler:[**ShapeCollection.AddLinkedPicture(int UpperLeftRow, int UpperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture) . Yöntem bir döndürür[**Resim**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)nesne.

Aşağıdaki örnek, bağlantılı resmin web adresinden bir çalışma sayfasına nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
