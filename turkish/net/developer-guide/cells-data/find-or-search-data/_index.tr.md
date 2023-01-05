---
title: Veri Bul veya Ara
type: docs
weight: 50
url: /tr/net/find-or-search-data/
---
{{% alert color="primary" %}}

Microsoft Excel, kullanıcıların bir çalışma sayfasında belirtilen verileri içeren hücreleri bulmasına olanak tanır.

{{% /alert %}}

## **Belirtilen Verileri İçeren Cells'i Bulma**

### **Microsoft Excel'i kullanma**

 Microsoft Excel, kullanıcıların bir çalışma sayfasında belirtilen verileri içeren hücreleri bulmasına olanak tanır. eğer seçersen**Düzenlemek** dan**Bulmak** Microsoft Excel'deki menü, arama değerini belirtebileceğiniz bir iletişim kutusu göreceksiniz.

Burada "Portakal" değerini arıyoruz. Aspose.Cells, geliştiricilerin çalışma sayfasında belirtilen değerleri içeren hücreleri bulmasına da olanak tanır.

### **Aspose.Cells'i kullanma**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon. bu[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)toplama, kullanıcı tanımlı verileri içeren bir çalışma sayfasındaki hücreleri bulmak için çeşitli yöntemler sağlar. Bu yöntemlerden birkaçı aşağıda daha ayrıntılı olarak ele alınmıştır.

{{% alert color="primary" %}}

Tüm Bul yöntemleri, aranacak belirtilen verileri içeren hücrelerin başvurularını döndürür.

{{% /alert %}}

## **Bir Formül İçeren Cells'i Bulmak**

 Geliştiriciler, çalışma sayfasında belirli bir formülü arayarak bulabilirler.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonun[**Bulmak**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) yöntem. Tipik olarak,[**Bulmak**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)yöntem üç parametre kabul eder:

- **Nesne:**Aranacak nesne. Tür int,double,DateTime,string,bool olmalıdır.
- **Önceki hücre:**Aynı nesneye sahip önceki hücre. Baştan arama yapılıyorsa bu parametre null olarak ayarlanabilir.
- FindOptions: Gerekli nesneyi bulma seçenekleri.

Aşağıdaki örnekler, bulma yöntemlerini uygulamak için çalışma sayfası verilerini kullanır:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **FindOptions kullanarak Veri veya Formül Bulma**

 kullanarak belirtilen değerleri bulmak mümkündür.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonun[**Bulmak**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) yöntem ile çeşitli[**Seçenekleri Bul**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . Tipik olarak,[**Bulmak**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)yöntem aşağıdaki parametreleri kabul eder:

- **arama değeri**, aranacak veri veya değer.
- **Önceki hücre**, aynı değeri içeren son hücre. Bu parametre, baştan arama yapılırken null olarak ayarlanabilir.
- **Seçenekleri bul**, bulma seçenekleri.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Belirtilen Dizi Değerini veya Numarasını İçeren Cells'i Bulma**

 Aynı dizeyi çağırarak belirtilen dize değerlerini bulmak mümkündür.[**Bulmak**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) bulunan yöntem[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu ile çeşitli[**Seçenekleri Bul**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 belirtin[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) ve[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) özellikler. Aşağıdaki örnek kod, bu özelliklerin, belirli sayıda dizeye sahip hücreleri bulmak için nasıl kullanılacağını göstermektedir.**başlangıç** ya da**merkez** ya da**son** hücre dizisinin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **ileri konular**
- [Belirli Tarza Sahip Cells'i Bulun](/cells/tr/net/find-cells-with-specific-style/)
- [Hücre değerinin tek tırnak işaretiyle başlayıp başlamadığını bulun](/cells/tr/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Orijinal Değerleri Kullanarak Veri Arama](/cells/tr/net/search-data-using-original-values/)
