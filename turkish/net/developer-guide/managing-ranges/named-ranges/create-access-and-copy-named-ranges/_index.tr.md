---
title: Erişim Oluşturma ve Adlandırılmış Aralıkları Kopyalama
type: docs
weight: 200
url: /tr/net/create-access-and-copy-named-ranges/
---
## **Giriş**

Normalde, sütun ve satır etiketleri, tek tek hücrelere atıfta bulunmak için kullanılır. Hücreleri, hücre aralıklarını, formülleri veya sabit değerleri temsil etmek için tanımlayıcı adlar oluşturmak mümkündür. Kelime**isim** bir hücreyi, hücre aralığını, formülü veya sabit değeri temsil eden bir karakter dizisine atıfta bulunabilir. Bir aralığa ad atamak, o hücre aralığına kendi adıyla atıfta bulunulabileceği anlamına gelir. Sales!C20:C30 gibi anlaşılması zor aralıklara atıfta bulunmak için Ürünler gibi anlaşılması kolay adlar kullanın. Etiketler, aynı çalışma sayfasındaki verilere atıfta bulunan formüllerde kullanılabilir; başka bir çalışma sayfasındaki bir aralığı temsil etmek istiyorsanız, bir ad kullanabilirsiniz. *Adlandırılmış aralıklar, özellikle liste kontrolleri, pivot tablolar, grafikler vb. için kaynak aralık olarak kullanıldığında Microsoft Excel'in en güçlü özelliklerinden biridir.

## **Microsoft Excel Kullanarak Adlandırılmış Aralıkla Çalışma**

### **Adlandırılmış Aralıklar Oluştur**

 Aşağıdaki adımlar, kullanılarak bir hücrenin veya hücre aralığının nasıl adlandırılacağını açıklar.**Excel** . Bu yöntem için geçerlidir**Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** ve**2002**.

1. Adlandırmak istediğiniz hücreyi, hücre aralığını seçin.
1.  Tıkla**İsim kutusu** formül çubuğunun sol ucunda.
1. Hücrelerin adını yazın.
1. Enter tuşuna basın.

{{% alert color="primary" %}}

Hücre içeriğini değiştirirken hücreye isim veremezsiniz.

{{% /alert %}}

## **Aspose.Cells Kullanarak Adlandırılmış Aralıkla Çalışma**

Burada görevi yapmak için Aspose.Cells API kullanıyoruz.
 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Toplamak.

### **Adlandırılmış Aralık Oluştur**

 Aşırı yüklemeyi çağırarak adlandırılmış bir aralık oluşturmak mümkündür.[**Yaratma Aralığı**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Toplamak. tipik bir versiyonu[**Yaratma Aralığı**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) yöntem aşağıdaki parametreleri alır:

- Sol üst hücrenin adı, aralıktaki sol üst hücrenin adı.
- Sağ alt hücrenin adı, aralıktaki sağ alt hücrenin adı.

 Ne zaman[**Yaratma Aralığı**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) yöntem çağrıldığında, yeni oluşturulan aralığı bir örnek olarak döndürür.[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range) sınıf. Bunu kullan[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range) adlandırılmış aralığı yapılandırmak için nesne. Örneğin, kullanarak aralığın adını ayarlayın.[**İsim**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name) Emlak. Aşağıdaki örnek, B4:G14'ün üzerine uzanan adlandırılmış bir hücre aralığının nasıl oluşturulacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **Adlandırılmış Aralıktaki Cells'e Veri Girin**

Modeli izleyerek bir aralığın tek tek hücrelerine veri ekleyebilirsiniz.

- **C#**: Aralık[satır,sütun]
- **VB**: Aralık(satır,sütun)

A1:C4'ü kapsayan adlandırılmış bir hücre aralığınız olduğunu varsayalım. Matris 4 * 3 = 12 hücre yapar. Ayrı aralık hücreleri sırayla düzenlenir: Aralık[0,0], Aralık[0,1], Aralık[0,2], Aralık[1,0], Aralık[1,1], Aralık[1,2], Menzil[2,0], Menzil[2,1], Menzil[2,2], Menzil[3,0], Menzil[3,1], Menzil[3,2].

Aralıktaki hücreleri tanımlamak için aşağıdaki özellikleri kullanın:

- FirstRow, adlandırılmış aralıktaki ilk satırın dizinini döndürür.
- FirstColumn, adlandırılmış aralıktaki ilk sütunun dizinini döndürür.
- RowCount, adlandırılmış aralıktaki toplam satır sayısını döndürür.
- ColumnCount, adlandırılmış aralıktaki toplam sütun sayısını döndürür.

Aşağıdaki örnek, belirli bir aralığın hücrelerine bazı değerlerin nasıl girileceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **Adlandırılmış Aralıkta Cells'i tanımlayın**

Modeli izleyerek bir aralığın tek tek hücrelerine veri ekleyebilirsiniz:

- **C#**: Aralık[satır,sütun]
- **VB**: Aralık(satır,sütun)

A1:C4'ü kapsayan adlandırılmış bir aralığınız varsa. Matris 4 * 3 = 12 hücre yapar. Ayrı aralık hücreleri sırayla düzenlenir: Aralık[0,0], Aralık[0,1], Aralık[0,2], Aralık[1,0] ,Aralık[1,1], Aralık[1,2], Menzil[2,0], Menzil[2,1], Menzil[2,2], Menzil[3,0], Menzil[3,1], Menzil[3,2].

Aralıktaki hücreleri tanımlamak için aşağıdaki özellikleri kullanın:

- FirstRow, adlandırılmış aralıktaki ilk satırın dizinini döndürür.
- FirstColumn, adlandırılmış aralıktaki ilk sütunun dizinini döndürür.
- RowCount, adlandırılmış aralıktaki toplam satır sayısını döndürür.
- ColumnCount, adlandırılmış aralıktaki toplam sütun sayısını döndürür.

Aşağıdaki örnek, belirli bir aralığın hücrelerine bazı değerlerin nasıl girileceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **Adlandırılmış Aralıklara Erişim**

#### **Belirli Bir Adlandırılmış Aralığa Erişin**

 Ara[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) koleksiyonun[**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) belirtilen ada göre bir aralık elde etme yöntemi. tipik[**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) yöntem, adlandırılmış aralığın adını alır ve belirtilen adlandırılmış aralığı,[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range) sınıf. Aşağıdaki örnek, adına göre belirtilen bir aralığa nasıl erişileceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **Bir Elektronik Tablodaki Tüm Adlandırılmış Aralıklara Erişin**

 Ara[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) koleksiyonun[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) bir e-tablodaki tüm adlandırılmış aralıkları alma yöntemi. bu[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) yöntem, tüm ad aralıklarının bir dizisini döndürür.[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) Toplamak.

Aşağıdaki örnek, bir çalışma kitabındaki tüm adlandırılmış aralıklara nasıl erişileceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **Adlandırılmış Aralıkları Kopyala**

 Aspose.Cells sağlar[**Aralık.Kopya()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) biçimlendirmeli bir hücre aralığını başka bir aralığa kopyalama yöntemi.

Aşağıdaki örnek, bir hücre kaynak aralığının başka bir adlandırılmış aralığa nasıl kopyalanacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
