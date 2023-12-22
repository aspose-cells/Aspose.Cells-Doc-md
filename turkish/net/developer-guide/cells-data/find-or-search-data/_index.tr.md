---
title: Veri Bul veya Ara
type: docs
weight: 50
url: /tr/net/find-or-search-data/
description: Aspose.Cells for .NET API numaralı telefondan belirtilen verileri içeren bir çalışma sayfasındaki hücreleri nasıl bulacağınızı veya arayacağınızı öğrenin.
keywords: Find data, Search data, Find Cells Containing a Formula, Search Cells Containing a Formula, Find Data or Formulas using FindOptions, Search Data or Formulas using FindOptions, Find or Search Cells Containing Specified String Value or Number, Find or Search cells contains specified data
---
{{% alert color="primary" %}}

Microsoft Excel, kullanıcıların bir çalışma sayfasında belirtilen verileri içeren hücreleri bulmasına olanak tanır.

{{% /alert %}}

##  **Belirtilen Verileri İçeren Cells Bulma**

###  **Microsoft Excel'i kullanma**

 Microsoft Excel, kullanıcıların bir çalışma sayfasında belirtilen verileri içeren hücreleri bulmasına olanak tanır. Eğer seçerseniz**Düzenlemek** itibaren**Bulmak** Microsoft Excel'deki menüde, arama değerini belirleyebileceğiniz bir iletişim kutusu göreceksiniz.

Burada "Portakal" değerini arıyoruz. Aspose.Cells ayrıca geliştiricilerin çalışma sayfasında belirtilen değerleri içeren hücreleri bulmasına da olanak tanır.

###  **Aspose.Cells'i kullanma**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)toplama, kullanıcı tarafından belirlenen verileri içeren bir çalışma sayfasındaki hücreleri bulmak için çeşitli yöntemler sağlar. Bu yöntemlerden birkaçı aşağıda daha ayrıntılı olarak tartışılmaktadır.

{{% alert color="primary" %}}

Tüm Bul yöntemleri, aranacak belirtilen verileri içeren hücrelerin referanslarını döndürür.

{{% /alert %}}

##  **Cells Formül İçeren Bulma**

 Geliştiriciler çalışma sayfasında belirli bir formülü arayarak bulabilirler.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Koleksiyonun[**Bulmak**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) yöntem. Tipik olarak,[**Bulmak**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)yöntem üç parametreyi kabul eder:

- **Nesne:**Aranacak nesne. Tür int,double,DateTime,string,bool olmalıdır.
- **Önceki hücre:**Aynı nesnenin bulunduğu önceki hücre. Başlangıçtan itibaren arama yapılıyorsa bu parametre null değerine ayarlanabilir.
- FindOptions: Gerekli nesneyi bulma seçenekleri.

Aşağıdaki örneklerde bulma yöntemlerini uygulamak için çalışma sayfası verileri kullanılmaktadır:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

##  **FindOptions Kullanarak Veri veya Formül Bulma**

 Belirtilen değerleri kullanarak bulmak mümkündür.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Koleksiyonun[**Bulmak**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) çeşitli yöntemlerle yöntem[**Seçenekleri Bul**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . Tipik olarak,[**Bulmak**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)yöntem aşağıdaki parametreleri kabul eder:

- *Arama değeri**, aranacak veri veya değer.
- *Önceki hücre**, aynı değeri içeren son hücre. Bu parametre, başlangıçtan itibaren arama yaparken null olarak ayarlanabilir.
- *Bulma seçenekleri**, bulma seçenekleri.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

##  **Belirtilen Dize Değerini veya Sayısını İçeren Cells Bulma**

 Aynısını çağırarak belirtilen dize değerlerini bulmak mümkündür.[**Bulmak**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) bulunan yöntem[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) çeşitli koleksiyonlarla[**Seçenekleri Bul**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 Belirtin[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) Ve[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) özellikler. Aşağıdaki örnek kod, çeşitli sayıda dizeye sahip hücreleri bulmak için bu özelliklerin nasıl kullanılacağını gösterir.**başlangıç** veya**merkez** veya**son** hücrenin dizesinden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

##  **İleri konular**
- [Özel Stil ile Cells'i Bul](/cells/tr/net/find-cells-with-specific-style/)
- [Hücre değerinin tek tırnak işaretiyle başlayıp başlamadığını bulma](/cells/tr/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Orijinal Değerleri Kullanarak Veri Arama](/cells/tr/net/search-data-using-original-values/)
