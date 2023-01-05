---
title: Resimleri Yönetme
type: docs
weight: 10
url: /tr/java/managing-pictures/
---
{{% alert color="primary" %}}

Aspose.Cells, geliştiricilerin çalışma zamanında e-tablolara resim eklemesine olanak tanır. Ayrıca, bu resimlerin konumu, sonraki bölümlerde daha ayrıntılı olarak tartışılan çalışma zamanında kontrol edilebilir.

Aspose.Cells for Java yalnızca resim formatlarını destekler: BMP, JPEG, PNG, GIF.

Örneklerde kullanılan dizinler 0'dan başlar.

{{% /alert %}}

## **Resim Ekleme**

Bir e-tabloya resim eklemek çok kolaydır. Sadece birkaç satır kod alır.

 basitçe[**Ekle**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String) ) yöntemi[**resimler**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) koleksiyon (kapsüllenmiş[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) nesne). bu[**Ekle**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) yöntemi aşağıdaki parametreleri alır:

- **Sol üst sıra dizini**, sol üst satırın dizini.
- **Sol üst sütun dizini**, sol üst sütunun dizini.
- **Resim dosyası adı**, resim dosyasının adı, yol ile tamamlayın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Resimlerin Konumlandırılması**

Resimler, Aspose.Cells kullanılarak aşağıdaki gibi konumlandırılabilir:

- [Mutlak Konumlandırma](/cells/tr/java/managing-pictures/#absolute-positioning).

### **Mutlak Konumlandırma**

 Geliştiriciler, resimleri kesinlikle kullanarak konumlandırabilir.[**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) ve[**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) yöntemleri[**Resim**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)nesne.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **ileri konular**
- [Web Adresinden Bağlantılı Resim Ekleme](/cells/tr/java/insert-a-linked-picture-from-web-address/)
- [Cell Referansına göre bir Resim Ekleme](/cells/tr/java/insert-a-picture-based-on-cell-reference/)
- [Bir URL'den Web Görüntüsünü Excel Çalışma Sayfasına Ekleme](/cells/tr/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
