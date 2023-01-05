---
title: Çalışma Sayfası İçinde Şeklin Mutlak Konumunu Bulma
type: docs
weight: 7000
url: /tr/java/finding-absolute-position-of-shape-inside-the-worksheet/
---
{{% alert color="primary" %}}

 Bazen bir şeklin çalışma sayfasındaki mutlak konumunu bilmeniz gerekir. Aspose.Cells şunları sağlar:[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) ve[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) Bu amaç için özellikler. Bu özellikler, çalışma sayfasındaki bir şeklin mutlak konumunu piksel cinsinden döndürür.

{{% /alert %}}

## **Shape.getLeftToCorner() ve Shape.getTopToCorner() özelliklerinin açıklaması**

Bu ekran görüntüsü,[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) ve[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)özellikleri ölçer.

**Mutlak konum ölçümü**

![yapılacaklar:resim_alternatif_metin](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

Aşağıdaki örnek kod, bir çalışma sayfasındaki ilk şeklin mutlak konumunu piksel cinsinden görüntüler. Kod, konsolda aşağıdaki çıktıyı görüntüler:

{{< highlight "java" >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
