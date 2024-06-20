---
title: SVG Formatında Görüntüye Grafik Dönüştürme
type: docs
weight: 140
url: /tr/java/converting-chart-to-image-in-svg-format/
---

{{% alert color="primary" %}} 

Ölçeklenebilir Vektör Grafikleri (SVG), aynı zamanda etkileşimliliği ve animasyonu destekleyen iki boyutlu grafikler için XML tabanlı bir vektör görüntü formatıdır. SVG belirtmesi, 1999'dan beri World Wide Web Consortium (W3C) tarafından geliştirilen açık bir standarttır.

SVG görüntüleri ve davranışları, XML metin dosyalarında tanımlanır. Bu, aranabilir, dizine eklenir, betiklenir ve sıkıştırılabilir anlamına gelir. XML dosyaları olarak, SVG görüntüleri herhangi bir metin düzenleyici ile oluşturulabilir ve düzenlenebilir, ancak genellikle çizim yazılımı ile oluşturulur.

Aspose.Cells, BMP, JPEG, PNG, GIF, SVG vb. gibi çeşitli biçimlerde grafikleri imaj olarak kaydedebilir. Bu makale, grafikleri SVG imajları olarak kaydetme işlemini açıklar.

{{% /alert %}} 

Aşağıdaki örnek kod, bir grafiği SVG biçiminde bir imaja dönüştürmek için Aspose.Cells kullanımını açıklar. Kod, kaynak Excel dosyasını yükler ve ardından ilk çalışma sayfasındaki ilk grafiği SVG'ye kaydeder.

Aşağıdaki ekran görüntüsü, örnek kodla oluşturulan SVG biçimindeki dönüştürülmüş grafik imajını gösterir.

**Çıktı görüntüsü** 

![todo:image_alt_text](converting-chart-to-image-in-svg-format_1.png)

SVG'nin XML tabanlı bir biçim olması nedeniyle, çıktı grafik imajını Notepad gibi bir metin düzenleyicide açabilirsiniz, bu ekran görüntüsünde gösterildiği gibi.

**Metin düzenleyicisindeki Çıktı SCG** 

![todo:image_alt_text](converting-chart-to-image-in-svg-format_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertCharttoImageinSVGFormat-ConvertCharttoImageinSVGFormat.java" >}}
