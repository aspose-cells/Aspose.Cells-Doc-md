---
title: Dahili Stiller Kullanma
type: docs
weight: 480
url: /tr/java/using-built-in-styles/
---

{{% alert color="primary" %}} 

Aspose.Cells, bir elektronik tablo belgesinde bir hücreyi biçimlendirmek için tekrar kullanılabilir stillerin geniş bir koleksiyonunu sağlar. Kitabımızda dahili stilleri kullanabilir ve ayrıca özel stiller oluşturabiliriz.

{{% /alert %}} 
## **Dahili Stilleri Nasıl Kullanılır**
[Workbook.createBuiltinStyle](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#createBuiltinStyle\(int\)) yöntemi ve [BuiltinStyleType](https://reference.aspose.com/cells/java/com.aspose.cells/BuiltinStyleType) sınıfı tekrar kullanılabilir stiller oluşturmayı uygun hale getirir. İşte tüm olası dahili stillerin bir listesi:

- [TWENTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_1)
- [TWENTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_2)
- [TWENTY_PERCENT_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_3)
- [TWENTY_PERCENT_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_4)
- [TWENTY_PERCENT_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_5)
- [TWENTY_PERCENT_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_6)
- [FORTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_1)
- [FORTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_2)
- [KIRK_YÜZDE_VURGULAMA_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_3)
- [KIRK_YÜZDE_VURGULAMA_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_4)
- [KIRK_YÜZDE_VURGULAMA_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_5)
- [KIRK_YÜZDE_VURGULAMA_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_6)
- [ALTMIŞ_YÜZDE_VURGULAMA_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_1)
- [ALTMIŞ_YÜZDE_VURGULAMA_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_2)
- [ALTMIŞ_YÜZDE_VURGULAMA_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_3)
- [ALTMIŞ_YÜZDE_VURGULAMA_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_4)
- [ALTMIŞ_YÜZDE_VURGULAMA_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_5)
- [ALTMIŞ_YÜZDE_VURGULAMA_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_6)
- [ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_1)
- [ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_2)
- [ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_3)
- [ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_4)
- [ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_5)
- [ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_6)
- [KÖTÜ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#BAD)
- [HESAPLAMA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CALCULATION)
- [HÜCREYİ_KONTROL_ET](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CHECK_CELL)
- [VİRGÜLLÜ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA)
- [VİRGÜLLÜ_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA_1)
- [PARA_BİRİMİ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY)
- [PARA_BİRİMİ_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY_1)
- [AÇIKLAYICI_METİN](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#EXPLANATORY_TEXT)
- [İYİ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#GOOD)
- [BAŞLIK_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_1)
- [BAŞLIK_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_2)
- [BAŞLIK_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_3)
- [BAŞLIK_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_4)
- [HYPERBAĞLANTI](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HYPERLINK)
- [TAKİP_EDİLEN_HYPERBAĞLANTI](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FOLLOWED_HYPERLINK)
- [GİRİŞ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#INPUT)
- [BAĞLI_HÜCRE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#LINKED_CELL)
- [NÖTR](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NEUTRAL)
- [NORMAL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NORMAL)
- [NOT](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NOTE)
- [ÇIKIŞ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#OUTPUT)
- [YÜZDE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#PERCENT)
- [BAŞLIK](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TITLE)
- [TOPLAM](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TOTAL)
- [UYARI_METNİ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#WARNING_TEXT)
- [SATIR_SEVİYESİ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ROW_LEVEL)
- [SÜTUN_SEVİYESİ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COLUMN_LEVEL)

Aşağıdaki kod yerleşik stillerin nasıl kullanılacağını göstermektedir.

![todo:image_alt_text](using-built-in-styles_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingBuiltinStyles-UsingBuiltinStyles.java" >}}
