---
title: DrawObjectEventHandler sınıfını kullanarak PDF'e işlerken DrawObject ve Bound'u alın
type: docs
weight: 70
url: /tr/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **Olası Kullanım Senaryoları**

 Aspose.Cells soyut bir sınıf sağlar[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) olan bir[**Çizmek()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)yöntem. Kullanıcı uygulayabilir[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) ve kullanmak[**Çizmek()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) almak için yöntem[**Nesne Çiz**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)ve Excel'i PDF'e veya Görüntüye dönüştürürken Bağlandı. İşte parametrelerin kısa bir açıklaması[**Çizmek()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)yöntem.

-  nesne çizmek:[**Nesne Çiz**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) oluşturulurken başlatılacak ve iade edilecektir

- x: Solu[**Nesne Çiz**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y: Üstü[**Nesne Çiz**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- genişlik: genişliği[**Nesne Çiz**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- yükseklik: Yükseklik[**Nesne Çiz**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

Excel dosyasını PDF'e dönüştürüyorsanız, kullanabilirsiniz[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)ile sınıf[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) . Benzer şekilde, Excel dosyasını Görüntüye dönüştürüyorsanız, kullanabilirsiniz.[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)ile sınıf[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **DrawObjectEventHandler sınıfını kullanarak PDF'ye işlerken DrawObject ve Bound'u alın**

 Lütfen aşağıdaki örnek koda bakın. o yükler[örnek excel dosyası](64716821.xlsx) olarak kaydeder ve[çıkış PDF](64716822.pdf). PDF'e işlerken şunu kullanır:[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)mülkiyet ve yakalar[**Nesne Çiz**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) ve Mevcut hücrelerin ve nesnelerin bağlanması, örneğin resimler vb.[**Nesne Çiz**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) type Cell ise, Bound ve StringValue değerlerini yazdırır. Ve eğer[**Nesne Çiz**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)type Image ise Bound ve Shape Name'i yazdırır. Lütfen daha fazla yardım için aşağıda verilen örnek kodun konsol çıktısına bakın.

## **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
