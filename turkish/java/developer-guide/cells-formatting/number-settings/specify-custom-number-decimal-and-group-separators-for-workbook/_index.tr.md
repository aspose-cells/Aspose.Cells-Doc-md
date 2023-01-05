---
title: Çalışma Kitabı için Özel Ondalık Sayı ve Grup Ayırıcıları Belirtin
type: docs
weight: 100
url: /tr/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Bu makale, Aspose.Cells for Java API kullanarak MS Excel'de ve Java koduyla Sayı ondalık ve grup ayırıcısının nasıl değiştirileceğini gösterir.
keywords: specify custom decimal separator excel, specify custom decimal separator excel java, specify custom group separator excel, specify custom group separator excel java, specify custom decimal and group separator excel, specify custom decimal and group separator excel java, change decimal and group separator excel java, change decimal and group separator excel, change decimal separator excel, change decimal separator excel java, change group separator excel, change group separator excel java
---
{{% alert color="primary" %}}

 Microsoft Excel'de, Excel'den Sistem Ayırıcıları kullanmak yerine Özel Ondalık ve Binlik Ayırıcıları belirtebilirsiniz.**Gelişmiş Excel Seçenekleri** aşağıdaki ekran görüntüsünde gösterildiği gibi.

 Aspose.Cells şunları sağlar:[**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) ve[WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) özellikleri, sayıları biçimlendirme/ayrıştırma için özel ayırıcıları ayarlamak için.

{{% /alert %}}

## **Microsoft Excel kullanarak Özel Ayırıcıları Belirtme**

1.  Açık**Seçenekler** içinde**Dosya** sekme.
1. Aç**Gelişmiş** sekme.
1.  içindeki ayarları değiştirin**Düzenleme Seçenekleri** bölüm.

Aşağıdaki ekran görüntüsü**Gelişmiş Excel Seçenekleri** ve belirtmek için bölümü vurgular**Özel Ayırıcılar**.

![yapılacaklar:resim_alternatif_metin](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Aspose.Cells kullanarak Özel Ayırıcıları Belirtme**

 Aşağıdaki örnek kod, Aspose.Cells API kullanılarak Özel Ayırıcıların nasıl belirtileceğini gösterir. Sırasıyla Özel Ondalık Sayı ve Grup Ayırıcılarını nokta ve boşluk olarak belirtir. Yani sayı**123,456.789** olarak görüntülenecek**123 456.789** kod tarafından oluşturulan PDF çıktısını gösteren ekran görüntüsünde gösterildiği gibi.

![yapılacaklar:resim_alternatif_metin](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
