---
title: Adlandırılmış Aralıklar
type: docs
weight: 40
url: /tr/java/named-ranges/
---
{{% alert color="primary" %}} 

Normalde, sütun ve satır etiketleri, tek tek hücrelere atıfta bulunmak için kullanılır. Hücreleri, hücre aralıklarını, formülleri veya sabit değerleri temsil etmek için tanımlayıcı adlar oluşturmak mümkündür. Kelime**isim** bir hücreyi, hücre aralığını, formülü veya sabit bir değeri temsil eden bir karakter dizisine atıfta bulunabilir. Bir aralığa ad atamak, o hücre aralığına kendi adıyla atıfta bulunulabileceği anlamına gelir. Sales!C20:C30 gibi anlaşılması zor aralıklara atıfta bulunmak için Ürünler gibi anlaşılması kolay adlar kullanın. Etiketler, aynı çalışma sayfasındaki verilere atıfta bulunan formüllerde kullanılabilir; başka bir çalışma sayfasındaki bir aralığı temsil etmek istiyorsanız, bir ad kullanabilirsiniz. *Adlandırılmış aralıklar, özellikle liste kontrolleri, pivot tablolar, grafikler vb. için kaynak aralık olarak kullanıldığında Microsoft Excel'in en güçlü özelliklerinden biridir.

{{% /alert %}} 
## **Adlandırılmış Aralık Oluşturma**
### **Microsoft Excel'i kullanma**
Aşağıdaki adımlarda, Microsoft Excel kullanılarak bir hücrenin veya hücre aralığının nasıl adlandırılacağı açıklanmaktadır. Bu yöntem Microsoft Office Excel 2003, Microsoft Excel 97, 2000 ve 2002 için geçerlidir.

1. Adlandırmak istediğiniz hücreyi, hücre aralığını seçin.
1. Formül çubuğunun sol ucundaki Ad Kutusunu tıklayın.
1. Hücrelerin adını yazın.
1. Enter tuşuna basın.

{{% alert color="primary" %}} 

Hücre içeriğini değiştirirken hücreye isim veremezsiniz.

{{% /alert %}} 
### **Aspose.Cells'i kullanma**
Burada görevi yapmak için Aspose.Cells API kullanıyoruz.

 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) Bu, bir Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf bir sağlar[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Toplamak.

 Aşırı yüklemeyi çağırarak adlandırılmış bir aralık oluşturmak mümkündür.[aralık oluştur](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak. Tipik bir versiyonu[aralık oluştur](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) yöntemi aşağıdaki parametreleri alır:

- Sol üst hücrenin adı, aralıktaki sol üst hücrenin adı.
- Sağ alt hücrenin adı, aralıktaki sağ alt hücrenin adı.

 Ne zaman[aralık oluştur](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) yöntemi çağrıldığında, yeni oluşturulan adlandırılmış aralığı örneğinin bir örneği olarak döndürür.[Menzil](https://reference.aspose.com/cells/java/com.aspose.cells/range) sınıf.

Aşağıdaki örnek, B4:G14'ün üzerine uzanan adlandırılmış bir hücre aralığının nasıl oluşturulacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **Bir Elektronik Tablodaki Tüm Adlandırılmış Aralıklara Erişme**
 Ara[GetNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) yöntemi[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) bir e-tablodaki tüm adlandırılmış aralıkları almak için. bu[GetNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) yöntemi, içindeki tüm adlandırılmış aralıkların bir dizisini döndürür.[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

Aşağıdaki örnek, bir çalışma kitabındaki tüm adlandırılmış aralıklara nasıl erişileceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **Belirli Bir Adlandırılmış Aralığa Erişin**
 Ara[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) koleksiyonun[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) ) ada göre belirtilen bir aralığı elde etme yöntemi. tipik[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) ) yöntemi, adlandırılmış aralığın adını alır ve belirtilen adlandırılmış aralığı,[Menzil](https://reference.aspose.com/cells/java/com.aspose.cells/range)sınıf.

Aşağıdaki örnek, adına göre belirtilen bir aralığa nasıl erişileceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **Adlandırılmış Aralıkta Cells'i tanımlayın**
Aspose.Cells'i kullanarak, bir aralığın tek tek hücrelerine veri ekleyebilirsiniz. Adlandırılmış bir hücre aralığınız olduğunu varsayalım. Yani, A1:C4. Böylece matris 4 * 3 = 12 hücre yapar ve bireysel aralık hücreleri sıralı olarak düzenlenir. Aspose.Cells, aralıktaki tek tek hücrelere erişmeniz için [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) sınıfının bazı kullanışlı Özelliklerini sağlar. Aralıktaki hücreleri tanımlamak için aşağıdaki yöntemleri kullanabilirsiniz:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) adlandırılmış aralıktaki ilk satırın dizinini döndürür.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)adlandırılmış aralıktaki ilk sütunun dizinini döndürür.

Aşağıdaki örnek, belirli bir aralığın hücrelerine bazı değerlerin nasıl girileceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **Adlandırılmış Aralıktaki Cells'e Veri Girin**
Aspose.Cells'i kullanarak, bir aralığın tek tek hücrelerine veri ekleyebilirsiniz. Diyelim ki, adlandırılmış bir hücre aralığınız var, yani H1:J4. Böylece matris 4 * 3 = 12 hücre yapar ve bireysel aralık hücreleri sıralı olarak düzenlenir. Aspose.Cells, aralıktaki tek tek hücrelere erişmeniz için [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) sınıfının bazı kullanışlı Özelliklerini sağlar. Aralıktaki hücreleri tanımlamak için aşağıdaki özellikleri kullanabilirsiniz:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow)adlandırılmış aralıktaki ilk satırın dizinini döndürür.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)adlandırılmış aralıktaki ilk sütunun dizinini döndürür.

Aşağıdaki örnek, belirli bir aralığın hücrelerine bazı değerlerin nasıl girileceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **Aralıkları Biçimlendir...Arka Plan Rengini ve Yazı Tipi Niteliklerini Adlandırılmış Bir Aralığa Ayarlama**
 Biçimlendirmeyi uygulamak için bir tanımlayın[stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) stil ayarlarını belirlemek ve onu nesneye uygulamak için nesne[Menzil](https://reference.aspose.com/cells/java/com.aspose.cells/range)nesne.

Aşağıdaki örnek, bir aralığa yazı tipi ayarlarıyla düz dolgu renginin (gölgeleme rengi) nasıl ayarlanacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **Aralıkları Biçimlendir...Adlandırılmış Aralığa Kenarlık Ekleme**
 Tek bir hücre yerine bir dizi hücreye kenarlık eklemek mümkündür. bu[Menzil](https://reference.aspose.com/cells/java/com.aspose.cells/range) nesne sağlar[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)hücre aralığına kenarlık eklemek için aşağıdaki parametreleri alan yöntem:

-  borderStyle: kenarlık türü,[Hücre Sınır Türü](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)numaralandırma.
-  borderColor: sınırdan seçilen kenarlığın çizgi rengi[Renk](https://reference.aspose.com/cells/java/com.aspose.cells/Color) numaralandırma.

Aşağıdaki örnek, bir aralığa anahat kenarlığının nasıl ayarlanacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


 Yukarıdaki kod yürütüldükten sonra aşağıdaki çıktı üretilecektir:

![yapılacaklar:resim_alternatif_metin](named-ranges_1.png)
#### **Aralıktaki hücrelere stil uygulama**
Bazen, bir hücredeki hücrelere bir stil uygulamak istersiniz.[Menzil](https://reference.aspose.com/cells/java/com.aspose.cells/range) . Bunun için, aralıktaki hücreler üzerinde yineleme yapabilir ve[Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) stili hücreye uygulama yöntemi.

Aşağıdaki örnek, Aralıktaki hücrelere stillerin nasıl uygulanacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **Adlandırılmış Aralığı Kaldırma**
 Aspose.Cells şunları sağlar:[NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\) ) aralığın adını silme yöntemi. Aralığın içeriğini temizlemek için şunu kullanın:[Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)) yöntem.
Aşağıdaki örnek, adlandırılmış bir aralığın içeriğiyle birlikte nasıl kaldırılacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


sınırRenkler
