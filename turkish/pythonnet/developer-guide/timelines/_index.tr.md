---
title: Zaman Çizelgesi Ekle
linktitle: Zaman çizelgeleri
type: docs
weight: 170
url: /tr/python-net/create-timeline/
description: Aspose.Cells for Python via .NET numaralı telefondan nasıl zaman çizelgesi oluşturulacağını öğrenin.
---
##  **Olası Kullanım Senaryoları**

Filtreleri tarihleri gösterecek şekilde ayarlamak yerine, tarihe/saate göre kolayca filtrelemenize ve kaydırıcı kontrolüyle istediğiniz dönemi yakınlaştırmanıza olanak tanıyan dinamik bir filtre seçeneği olan PivotTable Zaman Çizelgesi'ni kullanabilirsiniz. Microsoft Excel, bir pivot tablo seçip ardından *Ekle > Zaman Çizelgesi*'ni tıklatarak zaman çizelgesi oluşturmanıza olanak tanır. Aspose.Cells for Python via .NET ayrıca zaman çizelgesini kullanarak zaman çizelgesi oluşturmanıza da olanak tanır.[**Worksheet.timelines.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.timelines/timelinecollection/#methods)yöntem.

##  **Pivot Tabloya Zaman Çizelgesi Oluşturma**

 Lütfen aşağıdaki örnek koda bakın. Şunu yükler:[örnek Excel dosyası](input.xlsx)pivot tabloyu içerir. Daha sonra ilk temel pivot alanına dayalı olarak zaman çizelgesini oluşturur. Son olarak çalışma kitabını kaydeder.[çıkış XLSX](output.xlsx) biçim. Aşağıdaki ekran görüntüsü, çıktı Excel dosyasında Aspose.Cells for Python via .NET tarafından oluşturulan zaman çizelgesini göstermektedir.

![yapılacak şey:image_alt_text](create-timeline-to-a-pivot-table_1.png)

###  **Basit kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-CreateTimelineToPivotTable.py" >}}

