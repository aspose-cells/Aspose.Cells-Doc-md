---
title: Web Adresinden Bağlantılı Bir Resim Eklemek
type: docs
weight: 50
url: /tr/java/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

Bazen bir elektronik tabloya (http://) web'den bir resim eklemeniz gerekebilir. Bunu yapmak için resmin URL'sini belirtin ve resim, Microsoft Excel'de her açıldığında indirilir. Resim fiziksel olarak Excel belgesine gömülmez, ancak bir web kaynağına işaret eder.

{{% /alert %}}

## **Web Adresinden Bağlantılı Bir Resim Eklemek**

### **Microsoft Excel Kullanımı**

Microsoft Excel'de (örneğin 2007):

1. **Ekle** menüsünü tıklayın ve **Resim**'i seçin.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_1.png)

1. Resim Ekle iletişim kutusunda resmin web adresini belirtin. 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_2.png)

Resim eklenir.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_3.png)

### **Aspose.Cells for Java Kullanımı**

Aspose.Cells for Java, bir bağlantılı resim eklemeyi [**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)) yöntemini destekler.

Yöntem bir [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) nesnesi döndürür.

Aşağıdaki örnek, bir elektronik tabloya hücre referansı üzerinden bağlantılı resim eklemenin nasıl yapılacağını göstermektedir.

Kodu çalıştırdıktan sonra, oluşturulan Excel dosyasında birinci çalışma sayfasında bağlantılı bir resim bulunur.

**Çıkış dosyası** 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
