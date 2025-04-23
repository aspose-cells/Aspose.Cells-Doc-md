---
title: DrawObjectEventHandler sınıfını kullanarak PDF ye render ederken DrawObject ve Bound almak
type: docs
weight: 70
url: /tr/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) isimli soyut bir sınıf sunar, kullanıcı [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) metodunu uygulayabilir ve Excel dosyasını PDF veya görüntüye render ederken [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) metodunu kullanarak DrawObject ve Bound alabilir. Aşağıdaki, [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) metodunun parametrelerinin kısa bir açıklaması yer almaktadır.

- drawObject: Render edilirken [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) başlatılır ve döndürülür

- x: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)'nın solu

- y: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)'nın üstü

- width:[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)'nın genişliği

- height: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)'nın yüksekliği

Eğer Excel dosyasını PDF'e render ediyorsanız, [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) ile [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) sınıfını kullanabilirsiniz. Benzer şekilde, eğer Excel dosyasını Görüntüye render ediyorsanız, [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler) ile [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) sınıfını kullanabilirsiniz.

## **DrawObjectEventHandler sınıfını kullanarak PDF'ye render ederken DrawObject ve Bound almak**

Lütfen aşağıdaki örnek kodu inceleyin. [Örnek Excel dosyasını](64716821.xlsx) yükler ve [çıktı PDF'sini](64716822.pdf) kaydeder. PDF'ye render ederken, [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) özelliğini kullanır ve mevcut hücrelerin ve nesnelerin (örneğin görüntüler) DrawObject ve Bound değerlerini yakalar. Eğer [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) tipi Hücre ise, Bound ve StringValue'yi yazdırır. Ve eğer [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) tipi Görüntü ise, Bound ve Şekil Adını yazdırır. Daha fazla yardım için aşağıdaki örnek kodun konsol çıktısına bakınız.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
