---
title: Çalışma Sayfasında Koşullu Biçimlendirme Uygulayın
type: docs
weight: 40
url: /tr/cpp/apply-conditional-formatting-in-worksheet/
---

## **Olası Kullanım Senaryosu**
Aspose.Cells, Formül, Ortalamanın Üzerinde, Renk Ölçeği, Veri Çubuğu, Simge Seti, İlk10, vb. gibi tüm Koşullu Biçimlendirme türlerini eklemenize olanak tanır. Istediğiniz koşullu biçimlendirme uygulamanız için gerekli tüm yöntemlere sahip olan [FormatCondition](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/) sınıfını sağlar. İşte bazı Get yöntemlerinin listesi.

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
## **Çalışma Sayfasında Koşullu Biçimlendirme Uygulayın**
Aşağıdaki örnek kod, A1 ve B2 hücrelerinde bir Hücre Değer koşullu biçimlendirme nasıl eklenir gösterir. Lütfen kod tarafından oluşturulan [çıktı excel dosyasını](23167004.xlsx) ve aşağıdaki ekran görüntüsünü kontrol edin. A2 ve B2 hücresine 100'den büyük bir değer girerseniz, A1 ve B2 hücresinden kırmızı dolgu rengi kaybolacaktır.

![todo:image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
