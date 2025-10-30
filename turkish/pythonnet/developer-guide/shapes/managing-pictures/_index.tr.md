---
title: Resim Yönetimi
type: docs
weight: 10
url: /tr/python-net/managing-pictures/
---

Aspose.Cells for Python via .NET geliştiricilerin çalışma sayfalarına resim eklemesine izin verir. Ayrıca, bu resimlerin konumlandırılması da çalışma zamanı kontrol edilebilir, bu konu ilerleyen bölümlerde daha detaylı olarak ele alınacaktır.

Bu makale, resim eklemenin ve belirli hücrelerin içeriğini gösteren bir resmin nasıl eklenmesinin açıklamasını içerir.

## **Resim Ekleme**

Bir elektron mikroskobuna resim eklemek çok kolaydır. Sadece birkaç satır kod gerektirir:
Basitçe, [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) noktasal nesnesinde kapsüllenmiş olan [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) nesnesinin [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) metodunu çağırın. [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) metodu aşağıdaki parametreleri alır:

- **Sol üst satır dizini**, sol üst sütunun dizini.
- **Sol üst sütun dizini**, sol üst sütunun dizini.
- **Resim dosya adı**, yol bilgisi ile birlikte resim dosyasının adı.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-AddingPictures-1.py" >}}

## **Resim Konumlandırma**

Aspose.Cells for Python via .NET kullanarak resimlerin konumlandırmasını kontrol etmenin iki olası yolu vardır:

- Oransal konumlandırma: satır yüksekliği ve genişliğine oranla bir konum tanımlayın.
- Mutlak konumlandırma: resmin sayfaya yerleştirileceği kesin konumu tanımlayın, örneğin, hücrenin sol üstünden 40 piksel ve altından 20 piksel aşağıda.

### **Oransal Konumlandırma**

Geliştiriciler, resimleri [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) nesnesinin [**upper_delta_x**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_x) ve [**upper_delta_y**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_y) özelliklerini kullanarak satır yüksekliğine ve sütun genişliğine oransal olarak konumlandırabilirler. Bir [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) nesnesi, resmin dizinini geçirerek [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) koleksiyonundan alınabilir. Bu örnek, bir resmi F6 hücresine yerleştirir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.py" >}}

### **Mutlak Konumlandırma**

Geliştiriciler, resimleri [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) nesnesinin [**left**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/left) ve [**top**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/top) özelliklerini kullanarak mutlak olarak da konumlandırabilirler. Bu örnek, resmi F6 hücresine sol üstten 60 piksel ve üstten 10 piksel uzaklığa yerleştirir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.py" >}}

## **Hücre Referansına Dayalı Resim Ekleme**

Aspose.Cells for Python via .NET, bir çalışma sayfası hücresinin içeriğini bir şekil olarak görüntülemenize olanak tanır. Resmi, görüntülemek istediğiniz verilerin bulunduğu hücreye bağlayabilirsiniz. Hücre veya hücre aralığı grafik nesnesine bağlı olduğu için, o hücre veya hücre aralığında yaptığınız değişiklikler otomatik olarak grafik nesnesinde görünür.

Resmi [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) nesnesine kapsüllenmiş olan [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) koleksiyonunun [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) yöntemini çağırarak çalışma sayfasına ekleyin. [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) nesnesinin [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) özelliğini kullanarak hücre aralığını belirtin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PictureCellReference-1.py" >}}

## **Gelişmiş Konular**
- [Hücre Metni ile Koşullu İkon Takımı Ekle](/cells/tr/python-net/add-conditional-icons-set-with-the-cell-text/)
- [Web Adresinden Bağlantılı Resim Ekle](/cells/tr/python-net/insert-a-linked-picture-from-web-address/)
- [Hücre Referansına Dayalı Resim Ekle](/cells/tr/python-net/insert-a-picture-based-on-cell-reference/)
- [Bir URL'den Web Resmi Yükleyerek Excel Çalışma Sayfasına Ekleyin](/cells/tr/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="python-net" >}}
