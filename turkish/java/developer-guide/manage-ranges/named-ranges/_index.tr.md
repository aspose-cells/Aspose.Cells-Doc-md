---
title: Adlandırılmış Aralıklar
type: docs
weight: 40
url: /tr/java/named-ranges/
---

{{% alert color="primary" %}} 

Genellikle sütun ve satır etiketleri tek tek hücrelere atıfta bulunmak için kullanılır. Hücreleri, hücre aralıklarını, formülleri veya sabit değerleri temsil etmek için açıklayıcı isimler oluşturmak mümkündür. **Ad** kelimesi, bir hücreyi, hücre aralığını, formülü veya sabit bir değeri temsil eden karakter dizisine atıfta bulunabilir. Bir aralığa ad atamak, o aralığa adıyla atıfta bulunabileceğiniz anlamına gelir. Satışlar!C20:C30 gibi anlaşılması zor aralıklara referans vermek için Products gibi anlaşılır isimler kullanın. Formüllerde etiketler aynı çalışma sayfasındaki verilere atıfta bulunmak için kullanılabilir; başka bir çalışma sayfasındaki bir aralığı temsil etmek istiyorsanız bir isim kullanabilirsiniz. *Adlandırılmış aralıklar, özellikle liste kontrolleri, özet tablolar, grafikler vb. için kaynak aralığı olarak kullanıldığında Microsoft Excel'in en güçlü özelliklerinden biridir.*

{{% /alert %}} 
## **Bir Adlandırılmış Aralık Oluşturma**
### **Microsoft Excel Kullanımı**
Aşağıdaki adımlar, Microsoft Excel ile hücre veya hücre aralığına ad verme işlemini tanımlar. Bu yöntem, Microsoft Office Excel 2003, Microsoft Excel 97, 2000 ve 2002 için geçerlidir.

1. Adlandırmak istediğiniz hücreyi veya hücre aralığını seçin.
1. Formül çubuğunun sol ucundaki Ad Kutusu'na tıklayın.
1. Hücrelerin adını yazın.
1. ENTER tuşuna basın.

{{% alert color="primary" %}} 

Hücre içeriğini değiştirirken hücreye ad veremezsiniz.

{{% /alert %}} 
### **Aspose.Cells Kullanımı**
Burada görevi yapmak için Aspose.Cells API'sını kullanıyoruz.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) adlı bir sınıf sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) içerir. Bir çalışma sayfası [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunu sağlar.

Hücrelerin adlarını oluşturmak için [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunun aşırı yüklenmiş [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) metodunu çağırarak isimlendirilmiş bir aralık oluşturmak mümkündür. Genellikle [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) metodunun aşağıdaki parametreleri almasını beklersiniz:

- Sol üst hücrenin adı, aralıktaki sol üst hücrenin adı.
- Sağ alt hücrenin adı, aralıktaki sağ alt hücrenin adı.

[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) metodu çağrıldığında, [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) sınıfının bir örneği olarak yeni oluşturulan adlandırılmış aralık döner.

Aşağıdaki örnek, B4:G14'ten genişleyen hücrelerin adlandırılmış bir aralık oluşturmayı gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **Çalışma Kitabındaki Tüm Adlandırılmış Aralıklara Erişme**
Çalışma kitabındaki tüm adlandırılmış aralıklara erişmek için [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) koleksiyonunun [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\)) metodunu çağırın. [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\)) metodu, [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) içindeki tüm adlandırılmış aralıkların bir dizisini döndürür.

Aşağıdaki örnek, bir çalışma kitabındaki tüm adlandırılmış aralıklara erişmeyi gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **Belirli Bir Adlandırılmış Aralığa Erişme**
Belirli bir aralığa erişmek için [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) koleksiyonunun [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\)) metodunu çağırın. Tipik bir [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\)) metodu, adlandırılmış aralığın adını alır ve belirtilen adlandırılmış aralığı [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) sınıfının bir örneği olarak döndürür.

Aşağıdaki örnek, adı verilen bir aralığa erişmeyi gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **Adlandırılmış Bir Aralıktaki Hücreleri Belirleme**
Aspose.Cells kullanarak, bir aralıktaki bireysel hücrelere veri ekleyebilirsiniz. Varsayalım ki, A1:C4 gibi adlandırılmış bir hücre aralığınız var. Bu durumda, matris 4 * 3 = 12 hücre oluşturacak ve bireysel hücreler sıralı bir şekilde düzenlenecektir. Aspose.Cells size, aralıktaki bireysel hücrelere erişmek için [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) sınıfının bazı kullanışlı özelliklerini sağlar. Aşağıdaki yöntemleri kullanarak, aralıktaki hücreleri belirleyebilirsiniz:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow), adlandırılmış aralıktaki ilk satırın dizinini döndürür.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn), adlandırılmış aralıktaki ilk sütunun dizinini döndürür.

Aşağıdaki örnek, belirtilen bir aralıktaki hücrelere bazı değerler girmeyi gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **Adı Verilen Aralıktaki Hücrelere Veri Girişi**
Aspose.Cells kullanarak, bir aralıktaki bireysel hücrelere veri ekleyebilirsiniz. Varsayalım ki, H1:J4 gibi adlandırılmış bir hücre aralığınız var. Bu durumda, matris 4 * 3 = 12 hücre oluşturacak ve bireysel hücreler sıralı bir şekilde düzenlenecektir. Aspose.Cells size, aralıktaki bireysel hücrelere erişmek için [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) sınıfının bazı kullanışlı özelliklerini sağlar. Aşağıdaki özellikleri kullanarak, aralıktaki hücreleri belirleyebilirsiniz:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow), adlandırılmış aralıktaki ilk satırın dizinini döndürür.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn), adlandırılmış aralıktaki ilk sütunun dizinini döndürür.

Aşağıdaki örnek, belirtilen bir aralıktaki hücrelere bazı değerler girmeyi gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **Aralıklara Biçim Verme...Arka Plan Rengi ve Yazı Tipi Özniteliklerini Belirleme**
Biçimlendirme uygulamak için [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) nesnesine stil ayarlarını belirlemek için [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnesini tanımlayın ve onu [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) nesnesine uygulayın.

Aşağıdaki örnek, belirli bir aralığa katı dolgu rengi (gölgeleme rengi) ve yazı tipi ayarları belirlemeyi gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **Aralıklara Biçim Verme...Adlandırılmış Bir Aralığa Kenarlık Eklenmesi**
Tek bir hücre yerine bir hücreler aralığına kenarlık eklemek mümkündür. [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) nesnesi, bir hücre aralığına kenarlık eklemek için aşağıdaki parametreleri alarak [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) metodunu sağlar:

- borderStyle: kenarlık türü, [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType) numaralandırmasından seçilir.
- borderColor: kenarlığın çizgi rengi, [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) numaralandırmasından seçilir.

Aşağıdaki örnek, bir aralığa kenarlık eklemeyi gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


Yukarıdaki kodun çalıştırılmasından sonra aşağıdaki çıktı üretilecektir: 

![todo:image_alt_text](named-ranges_1.png)
#### **Bir Aralıktaki Hücrelere Stil Uygula**
Bazen, bir [Aralık](https://reference.aspose.com/cells/java/com.aspose.cells/range)'taki hücrelere stil uygulamak isteyebilirsiniz. Bunun için, aralıktaki hücreleri iterasyonla dolaşabilir ve hücreye stili uygulamak için [Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) yöntemini kullanabilirsiniz.

Aşağıdaki örnek, bir Aralıktaki hücrelere stil uygulamanın nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **Adlandırılmış Bir Aralığı Kaldır**
Aspose.Cells, [NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\)) yöntemini kullanarak aralığın adını silmek için ve aralığın içeriğini temizlemek için [Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)) yöntemini kullanır.
Aşağıdaki örnek, bir adlandırılmış aralığı içeriği ile birlikte kaldırmanın nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


borderColors 
