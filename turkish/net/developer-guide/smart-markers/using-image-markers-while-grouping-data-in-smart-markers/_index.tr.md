---
title: Smart Markers ta Görüntü İşaretleyicileri Nasıl Kullanılır
type: docs
weight: 30
url: /tr/net/how-to-use-image-markers-in-smart-markers/
alias: [/net/using-image-markers-while-grouping-data-in-smart-markers/]
---

## **Olası Kullanım Senaryoları**
Görüntü işaretleyicileri, templatelerde (FoxPro, Handlebars veya modern UI çerçeveleri gibi) dinamik olarak görüntüler veya görsel varlıklar ekleyen özel yer tutuculardır. Bazen, akıllı işaretleyiciler kullanarak resim eklemeniz gerekebilir. Aspose.Cells, görselleri smart markerlara eklemeyi sağlar.

## **Smart Markers'da Görüntü Parametreleri**
Resimleri yönetmek için akıllı işaretçi parametreleri.

- **Resim:HücreyeSığdır** - Resmi hücrenin satır yüksekliğine ve sütun genişliğine otomatik sığdır.
- **Resim:ÖlçekN** - Yüksekliği ve genişliği N yüzde ölçekle.
- **Resim:Genişlik:Nin&Yükseklik:Nin** - Resmi N inç yüksekliğinde ve N inç genişliğinde oluşturun. Sol ve Üst pozisyonları da belirleyebilirsiniz (puan cinsinden).

## **Smart Markers ile Görsel İşaretleyicileri Nasıl Kullanılır**
Lütfen aşağıdaki örnek kodu inceleyin, bu kod smart marker kullanarak nasıl resim ekleyeceğinizi gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}

## **Smart Markers ile Veri Gruplarken Görsel İşaretleyicileri Nasıl Kullanılır**
Aşağıdaki örnek bir çalışma kitabı oluşturur ve ardından sırasıyla D2, E2 ve F2 hücrelerine akıllı işaretçi etiketlerini ekler.

{{< highlight java >}}

&=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Daha sonra veri kaynağını veri ile doldurur ve [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) yöntemini çağırarak akıllı işaretçi etiketlerini işler. Kod, şu resimleri [moon.png](5115492.png) ve [moon2.png](5115491.png) kullanır ancak istediğiniz resmi kullanabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}

{{< app/cells/assistant language="csharp" >}}
