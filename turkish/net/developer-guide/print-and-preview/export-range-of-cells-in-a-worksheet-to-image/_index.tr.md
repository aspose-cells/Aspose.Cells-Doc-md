---
title: Çalışma Sayfasındaki Cells Aralığını Görüntüye Dışa Aktar
type: docs
weight: 60
url: /tr/net/export-range-of-cells-in-a-worksheet-to-image/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells'i kullanarak bir çalışma sayfasının görüntüsünü oluşturabilirsiniz. Ancak, bazen bir çalışma sayfasındaki yalnızca bir hücre aralığını bir görüntüye aktarmanız gerekir. Bu makalede, bunun nasıl başarılacağı açıklanmaktadır.

## **Çalışma Sayfasındaki Cells Aralığını Görüntüye Dışa Aktar**

 Bir aralığın görüntüsünü çekmek için, baskı alanını istenen aralığa ayarlayın ve ardından tüm kenar boşluklarını 0 olarak ayarlayın.[**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) ile**doğru** . Aşağıdaki kod, D8:G16 aralığının bir görüntüsünü alır. Aşağıda bir ekran görüntüsü[örnek excel dosyası](47153160.xlsx) kodunda kullanılır. Kodu herhangi bir Excel dosyasıyla deneyebilirsiniz.

## **Örnek Excel Dosyasının ve Dışa Aktarılan Resminin Ekran Görüntüsü**

**![todo:image_alt_text](çalışma sayfasındaki hücrelerin-aralığını-image_1.png'ye aktar)**

Kodun çalıştırılması, yalnızca D8:G16 aralığının bir görüntüsünü oluşturur.

**![todo:image_alt_text](Output-Image.png)**

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
