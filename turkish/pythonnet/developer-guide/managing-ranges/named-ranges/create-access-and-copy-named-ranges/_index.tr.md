---
title: Erişim Oluştur ve Adlandırılmış Aralıkları Kopyala
type: docs
weight: 200
url: /tr/python-net/create-access-and-copy-named-ranges/
description: Bu makale, Aspose.Cells for Python via .NET API sı ile Erişim Oluştur ve Adlandırılmış Aralıkları Kopyalamanın nasıl yapılacağını göstermektedir.
keywords: Python Excel Kütüphanesi, Python Erişim Oluştur ve Adlandırılmış Aralıkları Kopyala, Python Adlandırılmış Aralıklar Oluştur, Python Adlandırılmış Aralıkları Kopyala, Bir Elektronik Tablodaki Tüm Adlandırılmış Aralıklara Erişim
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

## **Aspose.Cells for Python Excel Kütüphanesi ile Adlandırılmış Aralıkla Çalışma**

Burada, görevi yerine getirmek için Aspose.Cells for Python via .NET API'sını kullanıyoruz.
Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişime izin veren bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, bir [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonu sağlar.

### **İsimlendirilmiş Aralık Oluştur**

Bir adlandırılmış aralık oluşturmak, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonunun aşırı yüklenmiş [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) yöntemini çağırarak mümkündür. [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) yönteminin tipik bir sürümü aşağıdaki parametreleri alır:

- Sol üst hücrenin adı, aralıktaki sol üst hücrenin adı.
- Sağ alt hücrenin adı, aralıktaki sağ alt hücrenin adı.

[**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) yöntemi çağrıldığında, yeni oluşturulan aralık, [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) sınıfının bir örneği olarak döner. Bu [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) nesnesini, isimlendirilmiş aralığı yapılandırmak için kullanın. Örneğin, [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/range/name) özelliğini kullanarak aralığın adını ayarlayın. Aşağıdaki örnek, B4:G14 üzerine uzanan hücrelerin adlandırılmış bir aralık oluşturmak için nasıl yapılacağını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CreateNamedRangeofCells-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-InputDataInCellsInRange-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IdentifyCellsinNamedRange-1.py" >}}

### **İsimlendirilmiş Aralıklara Eriş**

#### **Belirli Bir Adlandırılmış Aralığa Erişme**

Belirli bir adlandırılmış aralığa erişmek için [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) koleksiyonunun [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str) yöntemini çağırın. Tipik bir [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str) yöntemi, adlandırılmış aralığın adını alır ve belirtilen adlandırılmış aralığı [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) sınıfının bir örneği olarak döndürür. Aşağıdaki örnek, adına göre belirtilen bir aralığa nasıl erişileceğini göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessSpecificNamedRange-1.py" >}}

#### **Bir Elektronik Tablodaki Tüm İsimlendirilmiş Aralıklara Eriş**

Bir elektronik tablodaki tüm isimlendirilmiş aralıklara erişmek için [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) koleksiyonunun [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#) yöntemini çağırın. [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#) yöntemi, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) koleksiyonundaki tüm adlandırılmış aralık dizisini döndürür.

Aşağıdaki örnek, bir çalışma kitabındaki tüm adlandırılmış aralıklara erişmeyi gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessAllNamedRanges-1.py" >}}

### **İsimlendirilmiş Aralıkları Kopyala**

Aspose.Cells for Python via .NET, bir aralıktaki hücreleri biçimlendirmeyle birlikte başka bir aralığa kopyalamak için [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range) yöntemi sağlar.

Aşağıdaki örnek, kaynak hücre aralığını başka adlandırılmış bir aralığa kopyalamanın nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CopyNamedRanges-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
