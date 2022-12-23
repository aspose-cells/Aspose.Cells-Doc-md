---
title: Çalışma Sayfasına Koşullu Biçimlendirme Uygula
type: docs
weight: 40
url: /tr/cpp/apply-conditional-formatting-in-worksheet/
---
## **Olası Kullanım Senaryosu**
 Aspose.Cells, Formül, Ortalamanın Üstünde, Renk Skalası, Veri Çubuğu, Simge Seti, Top10 vb. Gibi her türlü Koşullu Biçimlendirmeyi eklemenize olanak tanır.[IBiçim Koşulu](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition)Seçtiğiniz koşullu biçimlendirmeyi uygulamak için gerekli tüm yöntemleri içeren sınıf. İşte birkaç Get yönteminin listesi.

- [GetIAboveAverage()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#aff550fd834cd78967ec440492ff012d5)
- [GetIRColorScale()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a3348a7c447dc564ceabc22c9c89bd6f5)
- [GetIDataBar()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a4415a87833c41386ed1595e742485e07)
- [GetIIconSet()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a011b2c7dbaaf671819d09f5d1df865e3)
- [GetITop10()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a64388aaf1b43811f5ee1ee3090c9bd4a)
## **Çalışma Sayfasına Koşullu Biçimlendirme Uygula**
 Aşağıdaki örnek kod, A1 ve B2 hücrelerinde Cell Değer koşullu biçimlendirmesinin nasıl ekleneceğini gösterir. Lütfen bkz[çıktı excel dosyası](23167004.xlsx) kod tarafından oluşturulan ve kodun üzerindeki etkisini açıklayan aşağıdaki ekran görüntüsü[çıktı excel dosyası](23167004.xlsx). A2 ve B2 hücresine 100'den büyük bir değer koyarsanız, A1 ve B2 hücresindeki Kırmızı dolgu rengi kaybolacaktır.

![yapılacaklar:resim_alternatif_metin](apply-conditional-formatting-in-worksheet_1.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet.cpp" >}}
