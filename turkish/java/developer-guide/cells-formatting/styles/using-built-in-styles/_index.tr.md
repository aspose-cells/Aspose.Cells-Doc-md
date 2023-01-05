---
title: Yerleşik Stilleri Kullanma
type: docs
weight: 480
url: /tr/java/using-built-in-styles/
---
{{% alert color="primary" %}} 

Aspose.Cells, elektronik tablo belgesindeki bir hücreyi biçimlendirmek için çok sayıda yeniden kullanılabilir stil koleksiyonu sağlar. Çalışma kitabımızda yerleşik stilleri kullanabilir ve ayrıca özel stiller oluşturabiliriz.

{{% /alert %}} 
## **Yerleşik Stiller nasıl kullanılır?**
 yöntem[Workbook.createBuiltinStyle](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#createBuiltinStyle\(int\) ) ve sınıf[Yerleşik Stil Türü](https://reference.aspose.com/cells/java/com.aspose.cells/BuiltinStyleType)yeniden kullanılabilir stiller oluşturmayı kolaylaştırır. İşte olası tüm yerleşik stillerin bir listesi:

- [YİRMİ_YÜZDE_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_1)
- [YİRMİ_YÜZDE_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_2)
- [YİRMİ_YÜZDE_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_3)
- [YİRMİ_YÜZDE_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_4)
- [YİRMİ_YÜZDE_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_5)
- [YİRMİ_YÜZDE_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_6)
- [KIRK_YÜZDE_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_1)
- [KIRK_YÜZDE_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_2)
- [KIRK_YÜZDE_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_3)
- [KIRK_YÜZDE_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_4)
- [KIRK_YÜZDE_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_5)
- [KIRK_YÜZDE_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_6)
- [ALTMIŞ_YÜZDE_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_1)
- [ALTMIŞ_YÜZDE_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_2)
- [ALTMIŞ_YÜZDE_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_3)
- [ALTMIŞ_YÜZDE_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_4)
- [ALTMIŞ_YÜZDE_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_5)
- [ALTMIŞ_YÜZDE_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_6)
- [ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_1)
- [ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_2)
- [ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_3)
- [ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_4)
- [ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_5)
- [ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_6)
- [KÖTÜ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#BAD)
- [HESAPLAMA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CALCULATION)
- [KONTROL_HÜCRE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CHECK_CELL)
- [VİRGÜL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA)
- [COMMA_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA_1)
- [PARA BİRİMİ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY)
- [CURRENCY_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY_1)
- [AÇIKLAYICI_METİN](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#EXPLANATORY_TEXT)
- [İYİ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#GOOD)
- [HEADER_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_1)
- [HEADER_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_2)
- [HEADER_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_3)
- [HEADER_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_4)
- [KÖPRÜ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HYPERLINK)
- [FOLLOWED_HYPERLINK](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FOLLOWED_HYPERLINK)
- [GİRİŞ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#INPUT)
- [BAĞLANTILI_HÜCRE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#LINKED_CELL)
- [DOĞAL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NEUTRAL)
- [NORMAL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NORMAL)
- [NOT](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NOTE)
- [ÇIKTI](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#OUTPUT)
- [YÜZDE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#PERCENT)
- [BAŞLIK](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TITLE)
- [TOPLAM](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TOTAL)
- [UYARI_TEXT](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#WARNING_TEXT)
- [ROW_LEVEL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ROW_LEVEL)
- [COLUMN_LEVEL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COLUMN_LEVEL)

Aşağıdaki kod, yerleşik stillerin nasıl kullanılacağını gösterir.

![yapılacaklar:resim_alternatif_metin](using-built-in-styles_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingBuiltinStyles-UsingBuiltinStyles.java" >}}
