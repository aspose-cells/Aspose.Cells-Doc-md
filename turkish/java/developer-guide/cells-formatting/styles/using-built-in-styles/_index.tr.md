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
 [Workbook.createBuiltinStyle](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#createBuiltinStyle-int-) ve [BuiltinStyleType](https://reference.aspose.com/cells/java/com.aspose.cells/BuiltinStyleType) sınıfları, tekrar kullanılabilir stiller oluşturmayı kolaylaştırır. İşte tüm olası yerleşik stillerin listesi:

- [TWENTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-1)
- [TWENTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-2)
- [TWENTY_PERCENT_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-3)
- [TWENTY_PERCENT_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-4)
- [TWENTY_PERCENT_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-5)
- [TWENTY_PERCENT_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-6)
- [FORTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-1)
- [FORTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-2)
- [KIRK_YÜZDE_VURGULAMA_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-3)
- [KIRK_YÜZDE_VURGULAMA_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-4)
- [KIRK_YÜZDE_VURGULAMA_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-5)
- [KIRK_YÜZDE_VURGULAMA_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-6)
- [ALTMIŞ_YÜZDE_VURGULAMA_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-1)
- [ALTMIŞ_YÜZDE_VURGULAMA_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-2)
- [ALTMIŞ_YÜZDE_VURGULAMA_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-3)
- [ALTMIŞ_YÜZDE_VURGULAMA_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-4)
- [ALTMIŞ_YÜZDE_VURGULAMA_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-5)
- [ALTMIŞ_YÜZDE_VURGULAMA_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-6)
- [ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-1)
- [ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-2)
- [ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-3)
- [ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-4)
- [ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-5)
- [ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-6)
- [KÖTÜ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#BAD)
- [HESAPLAMA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CALCULATION)
- [HÜCREYİ_KONTROL_ET](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CHECK-CELL)
- [VİRGÜLLÜ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA)
- [VİRGÜLLÜ_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA-1)
- [PARA_BİRİMİ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY)
- [PARA_BİRİMİ_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY-1)
- [AÇIKLAYICI_METİN](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#EXPLANATORY-TEXT)
- [İYİ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#GOOD)
- [BAŞLIK_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-1)
- [BAŞLIK_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-2)
- [BAŞLIK_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-3)
- [BAŞLIK_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-4)
- [HYPERBAĞLANTI](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HYPERLINK)
- [TAKİP_EDİLEN_HYPERBAĞLANTI](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FOLLOWED-HYPERLINK)
- [GİRİŞ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#INPUT)
- [BAĞLI_HÜCRE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#LINKED-CELL)
- [NÖTR](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NEUTRAL)
- [NORMAL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NORMAL)
- [NOT](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NOTE)
- [ÇIKIŞ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#OUTPUT)
- [YÜZDE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#PERCENT)
- [BAŞLIK](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TITLE)
- [TOPLAM](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TOTAL)
- [UYARI_METNİ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#WARNING-TEXT)
- [SATIR_SEVİYESİ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ROW-LEVEL)
- [SÜTUN_SEVİYESİ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COLUMN-LEVEL)

Aşağıdaki kod yerleşik stillerin nasıl kullanılacağını göstermektedir.

![todo:image_alt_text](using-built-in-styles_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingBuiltinStyles-UsingBuiltinStyles.java" >}}
{{< app/cells/assistant language="java" >}}
