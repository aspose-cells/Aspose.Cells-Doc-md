---
title: Çalışma Kitabı için Özel Sayı Ondalık ve Grup Ayracı Belirt
type: docs
weight: 100
url: /tr/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Bu makale, MS Excel de Sayı ondalık ve grup ayırıcısını nasıl değiştireceğinizi ve Aspose.Cells for Java API sıyla Java kodu kullanarak değiştireceğinizi göstermektedir.
keywords: özel ondalık ayırıcı excel belirt, özel ondalık ayırıcı excel java, özel grup ayırıcı excel belirt, özel grup ayırıcı excel java belirt, özel ondalık ve grup ayırıcı excel belirt, özel ondalık ve grup ayırıcı excel java belirt, ondalık ve grup ayırıcı excel java değiştirme, ondalık ve grup ayırıcı excel değiştirme, ondalık ayırıcı excel değiştirme, ondalık ayırıcı excel java değiştirme, grup ayırıcı excel değiştirme, grup ayırıcı excel java değiştirme
---

{{% alert color="primary" %}}

Microsoft Excel'de, Ekran Görüntüsünde gösterildiği gibi **Gelişmiş Excel Seçenekleri**'nden Sistem Ayraçlarını kullanmak yerine Özel Ondalık ve Binlerce Ayraçları belirleyebilirsiniz.

Aspose.Cells, biçimlendirme/analiz için özel ayraçları ayarlamak için [**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) ve [WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) özelliklerini sağlar.

{{% /alert %}}

## **Microsoft Excel Kullanarak Özel Ayraçları Belirtme**

1. **Dosya** sekmesinde **Seçenekler**'i açın.
1. **Gelişmiş** sekmesini açın.
1. **Düzenleme Seçenekleri** bölümündeki ayarları değiştirin.

Aşağıdaki ekran görüntüsü, **Gelişmiş Excel Seçenekleri**'ni ve **Özel Ayraçları** belirtmek için bölümü vurgular.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Aspose.Cells Kullanarak Özel Ayraçları Belirtme**

Aşağıdaki örnek kod, Aspose.Cells API'sını kullanarak Özel Ayraçları belirtmenin nasıl yapıldığını göstermektedir. Bu, nokta ve boşluk olarak sırasıyla Özel Sayı Ondalık ve Grup Ayraçlarını belirtir. Bu, kod tarafından üretilen çıktı PDF'de gösterilen **123,456.789** sayısının **123 456.789** olarak gösterilmesini sağlar.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
{{< app/cells/assistant language="java" >}}
