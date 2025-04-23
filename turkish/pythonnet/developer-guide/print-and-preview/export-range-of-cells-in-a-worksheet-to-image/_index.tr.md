---
title: Çalışma Sayfasındaki Hücre Aralığını Bir Görüntüye Aktarma
type: docs
weight: 60
url: /tr/python-net/export-range-of-cells-in-a-worksheet-to-image/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells for Python via .NET kullanarak çalışma sayfası resmi oluşturabilirsiniz. Ancak, bazen, yalnızca belirli bir hücre aralığını resme aktarmak isteyebilirsiniz. Bu durumda, bunu nasıl yapacağınızı anlatan makale.

## **Bir Çalışma Sayfasındaki Hücre Aralığını Görüntüye Aktar**

Bir aralığın görüntüsünü almak için yazdırma alanını istenen aralığa ayarlayın ve tüm kenar boşluklarını sıfıra ayarlayın. Ayrıca [**ImageOrPrintOptions.one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/one_page_per_sheet) değerini **true** olarak ayarlayın. Aşağıdaki kod, D8:G16 aralığından bir görüntü alır. Koddaki kullanılan örnek Excel dosyasının ekran görüntüsü aşağıdadır. Kodu herhangi bir Excel dosyasıyla deneyebilirsiniz.

## **Örnek Excel Dosyası ve Dışa Aktarılan Görüntü Ekran Görüntüsü**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Kod çalıştırıldığında yalnızca D8:G16 aralığının bir görüntüsü oluşturulur.

**![todo:image_alt_text](Output-Image.png)**

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ExportRangeOfCellsInWorksheetToImage-1.py" >}}

