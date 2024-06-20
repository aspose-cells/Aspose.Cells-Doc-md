---
title: Resim Yönetimi
type: docs
weight: 10
url: /tr/net/managing-pictures/
---

Aspose.Cells, geliştiricilere çalışma zamanında elektron mikroskobu resimlerini elektron mikroskobuna eklemelerine olanak tanır. Dahası, bu resimlerin konumu çalışma zamanında kontrol edilebilir, bu daha sonra detaylı olarak tartışılacaktır.

Bu makale, resim eklemenin ve belirli hücrelerin içeriğini gösteren bir resmin nasıl eklenmesinin açıklamasını içerir.

## **Resim Ekleme**

Bir elektron mikroskobuna resim eklemek çok kolaydır. Sadece birkaç satır kod gerektirir:
Basitçe, [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) noktasal nesnesinde kapsüllenmiş olan [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nesnesinin [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) metodunu çağırın. [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) metodu aşağıdaki parametreleri alır:

- **Sol üst satır dizini**, sol üst sütunun dizini.
- **Sol üst sütun dizini**, sol üst sütunun dizini.
- **Resim dosya adı**, yol bilgisi ile birlikte resim dosyasının adı.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **Resim Konumlandırma**

Aspose.Cells kullanarak resimlerin konumlandırılmasını kontrol etmek için iki olası yol bulunmaktadır:

- Oransal konumlandırma: satır yüksekliği ve genişliğine oranla bir konum tanımlayın.
- Mutlak konumlandırma: resmin sayfaya yerleştirileceği kesin konumu tanımlayın, örneğin, hücrenin sol üstünden 40 piksel ve altından 20 piksel aşağıda.

### **Oransal Konumlandırma**

Geliştiriciler, resimleri [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) nesnesinin [**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) ve [**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) özelliklerini kullanarak satır yüksekliğine ve sütun genişliğine oransal olarak konumlandırabilirler. Bir [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) nesnesi, resmin dizinini geçirerek [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) koleksiyonundan alınabilir. Bu örnek, bir resmi F6 hücresine yerleştirir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **Mutlak Konumlandırma**

Geliştiriciler, resimleri [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) nesnesinin [**Left**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) ve [**Top**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) özelliklerini kullanarak mutlak olarak da konumlandırabilirler. Bu örnek, resmi F6 hücresine sol üstten 60 piksel ve üstten 10 piksel uzaklığa yerleştirir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Hücre Referansına Dayalı Resim Ekleme**

Aspose.Cells, bir çalışma sayfası hücresinin içeriğini bir görüntü şeklinde görüntülemenizi sağlar. Verilerin görüntülenmesini istediğiniz hücreye bağlayabilirsiniz. Hücre veya hücre aralığı grafik nesnesine bağlandığından, o hücre veya hücre aralığındaki değişiklikler otomatik olarak grafik nesnesinde görünür.

Resmi [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nesnesine kapsüllenmiş olan [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) koleksiyonunun [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) yöntemini çağırarak çalışma sayfasına ekleyin. [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) nesnesinin [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) özelliğini kullanarak hücre aralığını belirtin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **Gelişmiş Konular**
- [Hücre Metni ile Koşullu İkon Takımı Ekle](/cells/tr/net/add-conditional-icons-set-with-the-cell-text/)
- [Web Adresinden Bağlantılı Resim Ekle](/cells/tr/net/insert-a-linked-picture-from-web-address/)
- [Hücre Referansına Dayalı Resim Ekle](/cells/tr/net/insert-a-picture-based-on-cell-reference/)
- [Bir URL'den Web Resmi Yükleyerek Excel Çalışma Sayfasına Ekleyin](/cells/tr/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

