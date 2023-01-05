---
title: Resimleri Yönetme
type: docs
weight: 10
url: /tr/net/managing-pictures/
---
Aspose.Cells, geliştiricilerin çalışma zamanında e-tablolara resim eklemesine olanak tanır. Ayrıca, bu resimlerin konumu, sonraki bölümlerde daha ayrıntılı olarak tartışılan çalışma zamanında kontrol edilebilir.

Bu makale, resimlerin nasıl ekleneceğini ve belirli hücrelerin içeriğini gösteren bir resmin nasıl ekleneceğini açıklar.

## **Resim Ekleme**

Bir e-tabloya resim eklemek çok kolaydır. Yalnızca birkaç satır kod alır:
 basitçe[**Eklemek**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) yöntemi[**resimler**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) koleksiyon (kapsüllenmiş[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nesne). bu[**Eklemek**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)yöntem aşağıdaki parametreleri alır:

- **Sol üst sıra dizini**, sol üst satırın dizini.
- **Sol üst sütun dizini**, sol üst sütunun dizini.
- **Resim dosyası adı**, resim dosyasının adı, yol ile tamamlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **Resimleri Konumlandırma**

Aspose.Cells'i kullanarak resimlerin konumunu kontrol etmenin iki olası yolu vardır:

- Orantılı konumlandırma: sıra yüksekliği ve genişliği ile orantılı bir konum tanımlayın.
- Mutlak konumlandırma: sayfada görüntünün ekleneceği tam konumu tanımlayın, örneğin hücrenin kenarının 20 piksel solunda ve 20 piksel altında.

### **Orantılı Konumlandırma**

 Geliştiriciler, resimleri satır yüksekliği ve sütun genişliğiyle orantılı olarak konumlandırabilir.[**ÜstDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) ve[**ÜstDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) özellikleri[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) nesne. A[**Resim**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) nesne şu adresten alınabilir:[**resimler**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)resim dizinini geçirerek koleksiyon. Bu örnek, F6 hücresine bir resim yerleştirir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **Mutlak Konumlandırma**

 Geliştiriciler ayrıca resimleri kesinlikle kullanarak konumlandırabilir.[**Sol**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) ve[**Tepe**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) özellikleri[**Resim**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)nesne. Bu örnek, F6 hücresine soldan 60 piksel ve hücrenin üstünden 10 piksel uzaklıkta bir resim yerleştirir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Cell Referansına Göre Resim Ekleme**

Aspose.Cells, bir çalışma sayfası hücresinin içeriğini bir görüntü şeklinde görüntülemenizi sağlar. Resmi, görüntülemek istediğiniz verileri içeren hücreye bağlayabilirsiniz. Hücre veya hücre aralığı grafik nesnesine bağlı olduğundan, o hücre veya hücre aralığındaki verilerde yaptığınız değişiklikler otomatik olarak grafik nesnesinde görünür.

 çağırarak çalışma sayfasına bir resim ekleyin.[**Resim Ekle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) yöntemi[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) koleksiyon (kapsüllenmiş[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nesne). kullanarak hücre aralığını belirtin.[**formül**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) özniteliği[**Resim**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)nesne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **ileri konular**
- [Cell Metniyle Ayarlanmış Koşullu Simgeler Ekleme](/cells/tr/net/add-conditional-icons-set-with-the-cell-text/)
- [Web Adresinden Bağlantılı Resim Ekleme](/cells/tr/net/insert-a-linked-picture-from-web-address/)
- [Cell Referansına Göre Bir Resim Ekleyin](/cells/tr/net/insert-a-picture-based-on-cell-reference/)
- [Bir URL'den bir Web Görüntüsünü Excel Çalışma Sayfasına Yükleme](/cells/tr/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

