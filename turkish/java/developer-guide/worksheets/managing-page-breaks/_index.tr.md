---
title: Sayfa Kesmelerinin Yönetimi
type: docs
weight: 30
url: /tr/java/managing-page-breaks/
---

{{% alert color="primary" %}}

Sayfa kesmesi, metnin bir sayfanın bittiği ve bir sonrakinin başladığı yerdir. Microsoft Excel, çalışma sayfasında herhangi bir seçili hücreye sayfa kesmeleri ekleyebilir.
Sayfa, sayfa kesme eklenen hücrede biter ve sayfa kesmesinden sonra tüm veriler bir sonraki sayfada yazdırılır. Basitçe, sayfa kesmeleri çalışma sayfalarını birden çok sayfaya böler. Aspose.Cells, iki tür sayfa kesmesini destekler:

- yatay
- dikey.

Bu makale, Aspose.Cells kullanarak çalışma sayfalarına yatay veya dikey sayfa kesmeleri nasıl ekleyeceğinizi açıklar.

{{% /alert %}}

## **Aspose.Cells & Sayfa Kesmeleri**

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir ve çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Sayfa kesmelerini eklemek için, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) ve [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) özelliklerini kullanın.

[**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) ve [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) özellikleri aslında birkaç sayıda sayfa kesmesi içerebilecek koleksiyonlardır. Her koleksiyon, yatay ve dikey sayfa kesmelerini yönetmek için birçok yöntem içerir. Bu yöntemlerin nasıl kullanıldığı aşağıda tartışılmaktadır.

## **Sayfa Kesmeleri Eklemek**

Bir çalışma sayfasına sayfa kesmesi eklemek için, [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) ve [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) koleksiyonlarının **Ekle** yöntemlerini çağırarak belirtilen hücreye dikey ve yatay sayfa kesmeleri ekleyin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

Sayfa kesmeleri önizleme veya yazdırma önizleme modlarında, bu sayfa kesmelerinin nasıl çalıştığını görebilirsiniz.

{{% /alert %}}

## **Tüm Sayfa Kesmelerini Temizleme**

Bir çalışma sayfasındaki tüm sayfa kesmelerini temizlemek için, [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) ve [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) koleksiyonlarının **Temizle** yöntemlerini çağırın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Belirli Sayfa Kesmesini Kaldırma**

Çalışma sayfasından belirli bir sayfa kesmesini kaldırmak için, [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) ve [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) koleksiyonlarının **removeAt** yöntemini çağırın. Her **removeAt** yöntemi, kaldırılacak sayfa kesmesinin endeksini alacaktır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**Bilmeniz gereken önemli**: Sayfa ayarlarında [**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) ve [**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide-) değil, sayfa bölme ayarlarını etkiler, bu nedenle çalışma sayfasını yazdırırken, sayfa bölme ayarları dikkate alınmaz; dosyada mevcut olsalar da.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
