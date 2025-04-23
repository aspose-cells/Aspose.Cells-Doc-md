---
title: Çalışma Sayfasındaki Hücre Aralığını Bir Görüntüye Aktarma
type: docs
weight: 60
url: /tr/net/export-range-of-cells-in-a-worksheet-to-image/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells kullanarak bir çalışma sayfasının görüntüsünü alabilirsiniz. Ancak bazen, bir çalışma sayfasındaki yalnızca belirli bir hücre aralığını bir görüntüye aktarmanız gerekebilir. Bu makalede, bu işlemi nasıl gerçekleştireceğiniz açıklanmaktadır.

## **Bir Çalışma Sayfasındaki Hücre Aralığını Görüntüye Aktar**

Bir aralığın görüntüsünü almak için yazdırma alanını istenen aralığa ayarlayın ve tüm kenar boşluklarını sıfıra ayarlayın. Ayrıca [**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) değerini **true** olarak ayarlayın. Aşağıdaki kod, D8:G16 aralığından bir görüntü alır. Koddaki kullanılan örnek Excel dosyasının ekran görüntüsü aşağıdadır. Kodu herhangi bir Excel dosyasıyla deneyebilirsiniz.

## **Örnek Excel Dosyası ve Dışa Aktarılan Görüntü Ekran Görüntüsü**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Kod çalıştırıldığında yalnızca D8:G16 aralığının bir görüntüsü oluşturulur.

**![todo:image_alt_text](Output-Image.png)**

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
