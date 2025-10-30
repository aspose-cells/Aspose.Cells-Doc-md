---
title: Hücre Biçimlendirme
type: docs
weight: 50
url: /tr/cpp/cells-formatting/
---

## **Hücre veya Hücre Aralığını Biçimlendir**
Eğer hücre veya hücre aralığını biçimlendirmek istiyorsanız, Aspose.Cells [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style/) sınıfını sağlar. Bu sınıfı kullanarak hücre veya hücre aralığının tüm biçimlendirmesini gerçekleştirebilirsiniz. IStyle sınıfı ile gerçekleştirilebilecek bazı biçimlendirme ile ilgili şeyler şunlardır

- Hücrenin dolgu rengini ayarlayın
- Hücrenin metin kaydırmasını ayarlayın
- Hücrelerin sınırlarını, üst, sol, alt ve sağ sınırlar gibi ayarlayın.
- Yazı tipi rengi, yazı tipi boyutu, yazı tipi adı, üstü çizili, kalın, eğik, altı çizili, vb. ayarlayın.
- Metni sağa, sola, yukarıya, aşağıya, ortalamaya vb. yatay veya dikey hizalamaya ayarlayın.

Tek bir hücrenin stilini ayarlamak istiyorsanız, lütfen [Cell->SetStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) yöntemini kullanın ve bir hücre aralığının stili ayarlamak istiyorsanız, lütfen [Range->ApplyStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) yöntemini kullanın.
## **Örnek Kod**
Aşağıdaki örnek kod, çalışta yaprak C4'ün hücresini çeşitli şekillerde biçimlendirir ve ekran görüntüsü [çıktı excel dosyasını](21266438.xlsx) referans için oluşturur.

![todo:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
