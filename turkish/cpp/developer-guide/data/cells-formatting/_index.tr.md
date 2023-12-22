---
title: Cells Biçimlendirme
type: docs
weight: 50
url: /tr/cpp/cells-formatting/
---
##  **Cell Biçimi veya Cells Aralığı**
 Hücreyi veya hücre aralığını biçimlendirmek istiyorsanız Aspose.Cells şunu sağlar:[Stil](https://reference.aspose.com/cells/cpp/aspose.cells/style/)sınıf. Bu sınıfı kullanarak hücrenin veya hücre aralığının tüm biçimlendirmesini gerçekleştirebilirsiniz. IStyle sınıfıyla gerçekleştirilebilecek biçimlendirmeyle ilgili bazı şeyler şunlardır:

- Hücrenin dolgu rengini ayarlama
- Hücrenin metin kaydırmasını ayarlama
- Hücrelerin kenarlıklarını üst, sol, alt ve sağ kenarlıklar vb. gibi ayarlayın.
- Yazı tipi rengini, yazı tipi boyutunu, yazı tipi adını, üzerini, kalın, italik, altı çizili vb. ayarları yapın.
- Metnin yatay veya dikey hizalamasını sağa, sola, yukarıya, aşağıya, ortaya vb. olarak ayarlayın.

 Tek bir hücrenin stilini ayarlamak istiyorsanız lütfen şunu kullanın:[Cell->SetStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) yöntemini kullanın ve bir hücre aralığının stilini ayarlamak istiyorsanız lütfen şunu kullanın:[Aralık->ApplyStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)yöntem.
##  **Basit kod**
 Aşağıdaki örnek kod, çalışma sayfasının C4 hücresini çeşitli şekillerde biçimlendirir ve ekran görüntüsü,[excel dosyasının çıktısını almak](21266438.xlsx) referansınız için onun tarafından oluşturulmuştur.

![yapılacak şey:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
