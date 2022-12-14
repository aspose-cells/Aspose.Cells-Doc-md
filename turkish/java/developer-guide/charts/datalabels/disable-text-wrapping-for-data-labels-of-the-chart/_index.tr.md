---
title: Grafiğin Veri Etiketleri için Metin Kaydırmayı Devre Dışı Bırak
type: docs
weight: 60
url: /tr/java/disable-text-wrapping-for-data-labels-of-the-chart/
---
{{% alert color="primary" %}}

Microsoft Excel 2013, kullanıcıların bir grafiğin veri etiketleri içindeki metni kaydırmasına veya açmasına olanak tanır. Varsayılan olarak, veri etiketi metni kaydırılır.

{{% /alert %}}

Aspose.Cells şunları sağlar:[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) yöntem. Ayarlanır**Doğru** veya**Yanlış** sırasıyla veri etiketlerinde metin kaydırmayı etkinleştirmek veya devre dışı bırakmak için.

 Benzer şekilde,[**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)bir veri etiketinin zaten sarılmış olup olmadığını öğrenme yöntemi.

Bu ekran görüntüsü, veri etiketlerinin metninin sarıldığı bir grafiği içeren örnek bir Microsoft Excel dosyasını gösterir. Gördüğünüz gibi, kontrol edebilir veya temizleyebilirsiniz.**Metni şekle kaydır** Microsoft Excel 2013'te Veri Etiketlerini Biçimlendir panelinin HİZALAMA bölümündeki seçenek.

**Veri etiketlerini sarma**

![yapılacaklar:resim_alternatif_Metin](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

 Aşağıdaki örnek kod, Aspose.Cells'i kullanarak örnek Microsoft Excel dosyasını yükler ve veri etiketi metin kaydırmayı devre dışı bırakır.[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)yöntem. Kod yürütüldüğünde, grafik şöyle görünür. Daha önce sarılmış olan metin artık açılmıştır.

**Veri etiketlerini yalnızca bir satırda gösterme**

![yapılacaklar:resim_alternatif_Metin](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
