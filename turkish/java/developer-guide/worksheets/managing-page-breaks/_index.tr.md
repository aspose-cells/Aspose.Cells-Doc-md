---
title: Sayfa Sonlarını Yönetme
type: docs
weight: 30
url: /tr/java/managing-page-breaks/
---
{{% alert color="primary" %}}

Sayfa sonu, metinde bir sayfanın bittiği ve bir sonrakinin başladığı bir yerdir. Microsoft Excel, bir çalışma sayfasında seçilen herhangi bir hücreye sayfa sonları ekleyebilir.
Sayfa, sayfa sonunun eklendiği hücrede biter ve sayfa sonundan sonraki tüm veriler bir sonraki sayfada yazdırılır. Basit bir ifadeyle, sayfa bölünmüş çalışma sayfalarını birden çok sayfaya ayırır. Aspose.Cells'i kullanarak çalışma zamanında çalışma sayfalarına sayfa sonları eklemek de mümkündür. Aspose.Cells iki tür sayfa sonunu destekler:

- yatay
- dikey.

Bu makalede, Aspose.Cells kullanılarak çalışma sayfalarına yatay veya dikey sayfa sonlarının nasıl ekleneceği açıklanmaktadır.

{{% /alert %}}

## **Aspose.Cells & Sayfa Sonları**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Bu bir Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Excel dosyasındaki her çalışma sayfasına erişim sağlar.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlayan sınıf. Sayfa sonlarını eklemek için[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[**Yatay Sayfa Sonları**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) ve[**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)özellikleri.

 bu[**Yatay Sayfa Sonları**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) ve[**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)özellikler aslında birkaç sayfa sonu içerebilen koleksiyonlardır. Her koleksiyon, yatay ve dikey sayfa sonlarını yönetmek için çeşitli yöntemler içerir. Bu yöntemlerin nasıl kullanıldığı aşağıda tartışılmaktadır.

## **Sayfa Sonları Ekleme**

 Bir çalışma sayfasına sayfa sonu eklemek için belirtilen hücreye dikey ve yatay sayfa sonları ekleyin.[**Yatay Sayfa Sonları**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) ve[**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) koleksiyonlar'**Ekle** yöntemler. Her biri**Ekle**method sayfa sonunun ekleneceği hücre adını alır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

Sayfa sonu önizleme veya baskı önizleme modlarında, bu sayfa sonlarının nasıl çalıştığını görebilirsiniz.

{{% /alert %}}

## **Tüm Sayfa Sonlarını Temizleme**

 Bir çalışma sayfasındaki tüm sayfa sonlarını temizlemek için[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) ve[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) koleksiyonlar'**Temizlemek**yöntemler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Belirli Sayfa Sonunu Kaldırma**

 Çalışma sayfasındaki belirli bir sayfa sonunu kaldırmak için[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) ve[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) koleksiyonlar'**kaldırAt** yöntemler. Her biri**kaldırAt**yöntem, kaldırılacak sayfa sonunun dizinini alacaktır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**bilmek önemli** : Sayfaya sığdır özelliklerini ayarladığınızda (yani[**Sayfalara SığdırUzun**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) ve[**Sayfalara SığdırGeniş**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)) sayfa yapısı ayarlarında, sayfa sonu ayarları etkilenir, bu nedenle, çalışma sayfasını yazdırırsanız, dosyada hala var olmalarına rağmen sayfa sonu ayarları dikkate alınmaz.

{{% /alert %}}
