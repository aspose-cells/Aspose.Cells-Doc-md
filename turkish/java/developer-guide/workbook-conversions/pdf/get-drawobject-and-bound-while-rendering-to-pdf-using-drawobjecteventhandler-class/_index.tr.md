---
title: DrawObjectEventHandler sınıfını kullanarak PDF ye render ederken DrawObject ve Bound almak
type: docs
weight: 60
url: /tr/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, bir [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) soyut sınıf sağlar, bu sınıfın bir [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-) yöntemi bulunur. Kullanıcı, [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) uygulayabilir ve Excel'in PDF veya görüntüye render edilirken [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-) yöntemini ve [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) ve **Bound**'u alabilir. Aşağıda, [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-) yönteminin parametrelerine kısa bir açıklaması bulunmaktadır.

- drawObject: Render edilirken başlatılacak ve döndürülecek [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- x: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)'nın solu

- y: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)'nın üstü

- width:[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)'nın genişliği

- height: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)'nın yüksekliği

Eğer Excel dosyanızı PDF'ye render ediyorsanız, [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) sınıfını [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) ile kullanabilirsiniz. Benzer şekilde, Excel dosyanızı Görüntü'ye render ediyorsanız, [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) sınıfını [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) ile kullanabilirsiniz.

## **DrawObjectEventHandler sınıfını kullanarak PDF'ye render ederken DrawObject ve Bound almak**

Lütfen aşağıdaki örnek kodu inceleyin. Bu, [örnek Excel dosyasını](64716843.xlsx) yükler ve bu dosyayı [çıktı PDF'si](64716842.pdf) olarak kaydeder. PDF'ye render edilirken, [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) özelliğini kullanır ve mevcut hücrelerin ve nesnelerin (örneğin resimler vb.) **Bound**'unu ve **Bound**'unu yakalar. drawObject türü Cell ise, Bound'unu ve StringValue'sunu yazdırır. Ve eğer drawObject türü Image ise, Bound'unu ve Şekil Adını yazdırır. Yardım için lütfen aşağıdaki örnek kodun konsol çıktısına bakın.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
