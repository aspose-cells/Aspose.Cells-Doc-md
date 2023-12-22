---
title: Cells Hizalamasını Değiştirin ve Mevcut Biçimlendirmeyi Koruyun
description: Hücre hizalamasını değiştirmek ve mevcut biçimlendirmeyi korumak için Aspose.Cells kitaplığını kullanın
keywords: Aspose.Cells, C#, Cell alignment, preserve existing formatting
type: docs
weight: 340
url: /tr/net/change-cells-alignment-and-keep-existing-formatting/
---
##  **Olası Kullanım Senaryoları**

Bazen birden çok hücrenin hizalamasını değiştirmek, ancak aynı zamanda mevcut biçimlendirmeyi de korumak isteyebilirsiniz. Aspose.Cells bunu şunu kullanarak yapmanıza olanak sağlar:[**StilFlag.Hizalamalar**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) mülk. Bunu *true** olarak ayarlarsanız, hizalamada değişiklikler gerçekleşir, aksi halde gerçekleşmez. Lütfen aklınızda bulundurun,[**StilBayrak**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) nesne parametre olarak iletilir[**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)Biçimlendirmeyi aslında bir hücre aralığına uygulayan yöntem.

##  **Cells Hizalamasını Değiştirin ve Mevcut Biçimlendirmeyi Koruyun**

 Aşağıdaki örnek kod,[örnek Excel dosyası](67338585.xlsx) , aralığı oluşturur ve onu yatay ve dikey olarak ortalayarak hizalar ve mevcut biçimlendirmeyi olduğu gibi korur. Aşağıdaki ekran görüntüsü örnek Excel dosyasını karşılaştırır ve[Excel dosyasının çıktısı](67338586.xlsx) ve hücrelerin artık yatay ve dikey olarak ortaya hizalanması dışında hücrelerin mevcut tüm formatlarının aynı olduğunu gösterir.

![yapılacak şey:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

##  **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
