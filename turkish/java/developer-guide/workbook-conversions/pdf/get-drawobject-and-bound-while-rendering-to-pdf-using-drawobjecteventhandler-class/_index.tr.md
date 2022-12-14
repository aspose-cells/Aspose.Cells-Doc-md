---
title: DrawObjectEventHandler sınıfını kullanarak PDF'ye işlerken DrawObject ve Bound'u alın
type: docs
weight: 60
url: /tr/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells soyut bir sınıf sağlar[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) olan bir[**Berabere()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) yöntem. Kullanıcı uygulayabilir[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)ve kullanmak[**Berabere()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) elde etme yöntemi[**Nesne Çiz**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)ve**Ciltli**Excel'i PDF veya Görüntüye dönüştürürken. İşte parametrelerin kısa bir açıklaması[**Berabere()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) yöntem.

-  nesne çizmek:[**Nesne Çiz**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)oluşturulurken başlatılacak ve iade edilecektir

- x: Solu[**Nesne Çiz**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y: Üstü[**Nesne Çiz**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- genişlik: genişliği[**Nesne Çiz**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- yükseklik: Yükseklik[**Nesne Çiz**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

Excel dosyasını PDF'ye dönüştürüyorsanız, kullanabilirsiniz[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)ile sınıf[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). Benzer şekilde, Excel dosyasını Görüntüye dönüştürüyorsanız, kullanabilirsiniz.[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)ile sınıf[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **DrawObjectEventHandler sınıfını kullanarak PDF'ye işlerken DrawObject ve Bound'u alın**

Lütfen aşağıdaki örnek koda bakın. o yükler[örnek excel dosyası](64716843.xlsx)olarak kaydeder ve[çıktı PDF](64716842.pdf). PDF'ye dönüştürürken,[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler)mülkiyet ve yakalar[**Nesne Çiz**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) ve**Ciltli** varolan hücrelerin ve nesnelerin, örneğin resimler vb. DrawObject türü Cell ise, Bound ve StringValue değerlerini yazdırır. DrawObject türü Image ise Bound ve Shape Name'i yazdırır. Lütfen daha fazla yardım için aşağıda verilen örnek kodun konsol çıktısına bakın.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
