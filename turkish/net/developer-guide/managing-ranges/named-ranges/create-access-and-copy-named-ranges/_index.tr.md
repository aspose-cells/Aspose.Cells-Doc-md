---
title: Erişim Oluştur ve Adlandırılmış Aralıkları Kopyala
type: docs
weight: 200
url: /tr/net/create-access-and-copy-named-ranges/
---

## **Giriş**

Normalde, sütun ve satır etiketleri bireysel hücrelere atıfta bulunmak için kullanılır. Hücrelere, hücre gruplarına, formüllere veya sabit değerlere temsil etmek için açıklayıcı isimler oluşturulabilir. 'İsim' kelimesi, bir hücreyi, hücre grubunu, formülü veya sabit değeri temsil eden bir karakter dizisine atıfta bulunabilir. Bir aralığa ad atamak, o hücre grubunun adı ile atıfta bulunulabilir anlamına gelir. Satırlar, eğilmesi zor olan satışlar gibi zor anlaşılabilen aralıklara atıfta bulunmak için kolay anlaşılabilir isimler kullanın. Etiketler, aynı çalışma sayfasındaki verilere atıfta bulunan formüllerde kullanılabilir; başka bir çalışma sayfasında bir aralığı temsil etmek isterseniz bir isim kullanabilirsiniz. 'Adlandırılmış aralıklar, özellikle liste denetimleri, özet tablolar, grafikler vb. için kaynak aralık olarak kullanıldığında Microsoft Excel'in en güçlü özellikleri arasındadır.

## **Microsoft Excel Kullanarak Adlandırılmış Aralık İle Çalışma**

### **Adlandırılmış Aralık Oluştur**

Aşağıdaki adımlar, **MS Excel** kullanarak bir hücreyi veya hücre aralığını adlandırmanın nasıl yapıldığını açıklar. Bu yöntem **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** ve **2002** için uygundur.

1. Adlandırmak istediğiniz hücreyi veya hücre aralığını seçin.
2. Formül çubuğunun sol ucundaki **Ad Kutusu'nu** tıklayın.
1. Hücrelerin adını yazın.
1. ENTER tuşuna basın.

{{% alert color="primary" %}}

Hücre içeriğini değiştirirken hücreye ad veremezsiniz.

{{% /alert %}}

## **Aspose.Cells Kullanarak Adlandırılmış Aralık İle Çalışma**

Burada görevi yapmak için Aspose.Cells API'sını kullanıyoruz.
Aspose.Cells, Microsoft Excel dosyasını temsil eden bir sınıf, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışsayfaya erişim sağlayan [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir. Bir çalışsayfa [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonu sağlar.

### **İsimlendirilmiş Aralık Oluştur**

Bir adlandırılmış aralık oluşturmak, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunun aşırı yüklenmiş [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) yöntemini çağırarak mümkündür. [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) yönteminin tipik bir sürümü aşağıdaki parametreleri alır:

- Sol üst hücrenin adı, aralıktaki sol üst hücrenin adı.
- Sağ alt hücrenin adı, aralıktaki sağ alt hücrenin adı.

[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) yöntemi çağrıldığında, yeni oluşturulan aralık, [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) sınıfının bir örneği olarak döner. Bu [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) nesnesini, isimlendirilmiş aralığı yapılandırmak için kullanın. Örneğin, [**Name**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name) özelliğini kullanarak aralığın adını ayarlayın. Aşağıdaki örnek, B4:G14 üzerine uzanan hücrelerin adlandırılmış bir aralık oluşturmak için nasıl yapılacağını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **Adı Verilen Aralıktaki Hücrelere Veri Girişi**

Bir aralıktaki bireysel hücrelere veri ekleyebilirsiniz. İzlenecek desen aşağıdaki gibidir

- **C#**: Range[row,column]
- **VB**: Range(row,column)

A1:C4'ü kapsayan bir isimlendirilmiş aralığınız olduğunu düşünün. Matris 4 * 3 = 12 hücre yaratır. Bireysel aralık hücreleri ardışık olarak düzenlenir: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

Aralıktaki hücreleri tanımlamak için aşağıdaki özellikleri kullanın:

- FirstRow, isimlendirilmiş aralıktaki ilk satırın indisini döndürür.
- FirstColumn, isimlendirilmiş aralıktaki ilk sütunun indisini döndürür.
- RowCount, isimlendirilmiş aralıktaki toplam satır sayısını döndürür.
- ColumnCount, isimlendirilmiş aralıktaki toplam sütun sayısını döndürür.

Aşağıdaki örnek, belirtilen bir aralıktaki hücrelere bazı değerler girmeyi gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **İsimlendirilmiş Aralıktaki Hücreleri Tanımlama**

Bir aralıktaki bireysel hücrelere veri ekleyebilirsiniz. İzlenecek desen aşağıdaki gibidir:

- **C#**: Range[row,column]
- **VB**: Range(row,column)

Eğer A1:C4'ü kapsayan bir isimlendirilmiş aralığınız varsa, matris 4 * 3 = 12 hücre yaratır. Bireysel aralık hücreleri ardışık olarak düzenlenir: Range[0,0], Range[0,1], Range[0,2], Range[1,0] ,Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

Aralıktaki hücreleri tanımlamak için aşağıdaki özellikleri kullanın:

- FirstRow, isimlendirilmiş aralıktaki ilk satırın indisini döndürür.
- FirstColumn, isimlendirilmiş aralıktaki ilk sütunun indisini döndürür.
- RowCount, isimlendirilmiş aralıktaki toplam satır sayısını döndürür.
- ColumnCount, isimlendirilmiş aralıktaki toplam sütun sayısını döndürür.

Aşağıdaki örnek, belirtilen bir aralıktaki hücrelere bazı değerler girmeyi gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **İsimlendirilmiş Aralıklara Eriş**

#### **Belirli Bir Adlandırılmış Aralığa Erişme**

Belirli bir adlandırılmış aralığa erişmek için [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) koleksiyonunun [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) yöntemini çağırın. Tipik bir [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) yöntemi, adlandırılmış aralığın adını alır ve belirtilen adlandırılmış aralığı [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) sınıfının bir örneği olarak döndürür. Aşağıdaki örnek, adına göre belirtilen bir aralığa nasıl erişileceğini göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **Bir Elektronik Tablodaki Tüm İsimlendirilmiş Aralıklara Eriş**

Bir elektronik tablodaki tüm isimlendirilmiş aralıklara erişmek için [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) koleksiyonunun [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) yöntemini çağırın. [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) yöntemi, [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) koleksiyonundaki tüm adlandırılmış aralık dizisini döndürür.

Aşağıdaki örnek, bir çalışma kitabındaki tüm adlandırılmış aralıklara erişmeyi gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **İsimlendirilmiş Aralıkları Kopyala**

Aspose.Cells, bir hücre aralığını biçimlendirmesiyle birlikte başka bir aralığa kopyalamak için [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) yöntemi sağlar.

Aşağıdaki örnek, kaynak hücre aralığını başka adlandırılmış bir aralığa kopyalamanın nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
