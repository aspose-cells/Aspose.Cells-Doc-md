---
title: Cells biçimlendirme
type: docs
weight: 50
url: /tr/cpp/cells-formatting/
---
## **Biçim Cell veya Aralık Cells**
 Hücreyi veya hücre aralığını biçimlendirmek istiyorsanız Aspose.Cells,[Stil](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_style)sınıf. Bu sınıfı kullanarak hücrenin veya hücre aralığının tüm biçimlendirmesini gerçekleştirebilirsiniz. IStyle sınıfıyla gerçekleştirilebilecek biçimlendirmeyle ilgili bazı şeyler şunlardır:

- Hücrenin dolgu rengini ayarla
- Hücrenin metin kaydırmasını ayarlama
- Üst, sol, alt ve sağ kenarlıklar gibi hücrelerin kenarlıklarını ayarlayın.
- Yazı tipi rengini, yazı tipi boyutunu, yazı tipi adını, üst çizgiyi, kalın, italik, altı çizili vb. ayarlayın.
- Metin yatay veya dikey hizalamasını sağa, sola, yukarıya, aşağıya, ortaya vb. olarak ayarlayın.

 Tek bir hücrenin stilini ayarlamak istiyorsanız, lütfen[ICell->SetIStyle()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#afa3d5b2aa5e90b286effc9e92de59dd5) yöntemi ve bir hücre aralığının stilini ayarlamak istiyorsanız, lütfen[IRange->ApplyIStyle()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#aaad6703b803565b674999bbaf5eed3a0)yöntem.
## **Basit kod**
 Aşağıdaki örnek kod, çalışma sayfasının C4 hücresini çeşitli şekillerde biçimlendirir ve ekran görüntüsü,[çıktı excel dosyası](21266438.xlsx) referansınız için onun tarafından oluşturulmuştur.

![yapılacaklar:resim_alternatif_metin](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells.cpp" >}}
