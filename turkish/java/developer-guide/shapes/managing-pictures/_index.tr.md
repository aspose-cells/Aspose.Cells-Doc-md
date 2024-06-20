---
title: Resim Yönetimi
type: docs
weight: 10
url: /tr/java/managing-pictures/
---

Aspose.Cells, geliştiricilere çalışma zamanında elektron mikroskobu resimlerini elektron mikroskobuna eklemelerine olanak tanır. Dahası, bu resimlerin konumu çalışma zamanında kontrol edilebilir, bu daha sonra detaylı olarak tartışılacaktır.

Bu makale, resim eklemenin ve belirli hücrelerin içeriğini gösteren bir resmin nasıl eklenmesinin açıklamasını içerir.

## **Resim Ekleme**

Bir çalışma kitabına resim eklemek çok kolaydır. Sadece birkaç satır kod gerektirir.

Sadece [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) nesnesine kapsüllenmiş olan [**Pictures**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) koleksiyonunun [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) yöntemini çağırın. [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) yöntemi aşağıdaki parametreleri alır:

- **Sol üst satır dizini**, sol üst sütunun dizini.
- **Sol üst sütun dizini**, sol üst sütunun dizini.
- **Resim dosya adı**, yol bilgisi ile birlikte resim dosyasının adı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Resimlerin Konumlandırılması**

Resimler, Aspose.Cells kullanılarak aşağıdaki gibi konumlandırılabilir:

- [Mutlak Pozisyonlama](/cells/tr/java/managing-pictures/#absolute-positioning).

### **Mutlak Konumlandırma**

Geliştiriciler, resimleri [**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) ve [**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) yöntemlerini kullanarak mutlak olarak konumlandırabilirler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **Gelişmiş Konular**
- [Web Adresinden Bağlantılı Resim Ekle](/cells/tr/java/insert-a-linked-picture-from-web-address/)
- [Hücre Referansına Göre Resim Ekle](/cells/tr/java/insert-a-picture-based-on-cell-reference/)
- [URL'den Bir Web Görüntüsünü Excel Çalışma Kitabına Ekle](/cells/tr/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
