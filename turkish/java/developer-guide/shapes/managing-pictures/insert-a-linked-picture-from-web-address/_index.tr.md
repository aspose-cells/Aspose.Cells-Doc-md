---
title: Web Adresinden Bağlantılı Resim Ekleme
type: docs
weight: 50
url: /tr/java/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

Bazen web'den (http://) bir çalışma sayfasına bir resim eklemeniz gerekir. Bunu yapmak için resmin URL'sini belirtin ve resim, elektronik tablo Microsoft Excel'de her açıldığında indirilecektir. Görüntü fiziksel olarak Excel belgesine gömülü değildir, ancak bir web kaynağına işaret eder.

{{% /alert %}}

## **Web Adresinden Bağlantılı Resim Ekleme**

### **Microsoft Excel'i kullanma**

Microsoft Excel'de (örneğin 2007):

1.  Tıkla**Sokmak** menü ve seçin**Resim**.

![yapılacaklar:resim_alternatif_Metin](insert-a-linked-picture-from-web-address_1.png)

1.  Resim Ekle iletişim kutusunda resmin web adresini belirtin.

![yapılacaklar:resim_alternatif_Metin](insert-a-linked-picture-from-web-address_2.png)

Resim eklenir.

![yapılacaklar:resim_alternatif_Metin](insert-a-linked-picture-from-web-address_3.png)

### **Aspose.Cells for Java'i kullanma**

 Aspose.Cells for Java, yöntemi kullanarak bağlantılı bir resim eklemeyi destekler[**ShapeCollection.addLinkedPicture(int UpperLeftRow, int UpperLeftColumn, int yükseklik, int genişlik, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)).

 Yöntem bir döndürür[**Resim**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)nesne.

Aşağıdaki örnek, bağlantılı resmin web adresinden bir çalışma sayfasına nasıl ekleneceğini gösterir.

Kodu çalıştırdıktan sonra, oluşturulan Excel dosyası ilk çalışma sayfasında bağlantılı bir resim içerir.

**çıktı dosyası** 

![yapılacaklar:resim_alternatif_Metin](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
