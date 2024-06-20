---
title: Veri Bulma veya Arama
type: docs
weight: 50
url: /tr/net/find-or-search-data/
description: Belirli veriler içeren hücreleri içeren çalışma sayfasındaki hücreleri bulma veya arama konusunda Aspose.Cells for .NET API sı aracılığıyla nasıl hücreleri arayacağınızı öğrenin.
keywords: Veri Bulma, Veri Arama, Formül İçeren Hücreleri Bulma, Formül İçeren Hücreleri Arama, FindOptions Kullanarak Veri veya Formülleri Bulma, FindOptions Kullanarak Veri veya Formülleri Arama, Belirtilmiş Dize Değeri veya Sayı İçeren Hücreleri Bulma veya Arama, Belirtilmiş veriler içeren hücreleri bulma veya arama
---

{{% alert color="primary" %}}

Microsoft Excel, kullanıcılara belirli verileri içeren bir çalışma sayfasında hücreleri bulmalarına izin verir.

{{% /alert %}}

## **Belirli Verileri İçeren Hücreleri Bulma**

### **Microsoft Excel Kullanımı**

Microsoft Excel, kullanıcıların belirli verileri içeren bir çalışma sayfasında hücreleri bulmasına izin verir. Microsoft Excel'de **Düzenle**'yi seçerseniz, arama değerini belirleyebileceğiniz bir iletişim kutusu göreceksiniz.

Burada, "Portakallar" değerini arıyoruz. Aspose.Cells, ayrıca belirli değerleri içeren hücreleri bulmayı sağlar.

### **Aspose.Cells Kullanımı**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonunu sağlar. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu, kullanıcı tarafından belirtilen verileri içeren bir çalışma sayfasındaki hücreleri bulmak için birkaç yöntem sağlar. Bu yöntemlerden bazıları aşağıda daha detaylı olarak tartışılmıştır.

{{% alert color="primary" %}}

Tüm Bul yöntemleri, belirtilen verileri içeren hücrelerin referanslarını döndürür.

{{% /alert %}}

## **Formül İçeren Hücreleri Bulma**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonunun [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) yöntemini çağırarak çalışma sayfasındaki belirli bir formülü bulabilirler. Genellikle, [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) yöntemi üç parametre alır:

- **Object:** Aranacak nesne. Türü int, double, DateTime, string, bool olmalıdır.
- **Önceki hücre:** Aynı nesneye sahip önceki hücre. Aramaya başlangıçtan itibaren arıyorsanız bu parametre null olarak ayarlanabilir.
- FindOptions: Gerekli nesneyi bulmak için seçenekler.

Aşağıdaki örnekler, bulma yöntemlerini uygulamak için çalışma sayfası verilerini kullanır:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **FindOptions Kullanarak Veri veya Formülleri Bulma**

Çeşitli [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) ile [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonunun [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) yöntemi kullanılarak belirli değerleri bulmak mümkündür. Genellikle, [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) yöntemi aşağıdaki parametreleri kabul eder:

- **Arama değeri**, aranmak istenen veri veya değer.
- **Önceki hücre**, aynı değere sahip son hücre. Aramaya başlangıçtan itibaren arıyorsanız bu parametre null olarak ayarlanabilir.
- **Bul seçenekleri**, bul seçenekleri.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Belirli Dize Değeri veya Numarası İçeren Hücreleri Bulma**

Belirli dize değerlerin bulunması, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonunda bulunan aynı [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) yöntemiyle çeşitli [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) ile çağrılabilir.

[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) ve [**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) özelliklerini belirtin. Aşağıdaki örnek kod, bu özellikleri kullanarak hücrelerde dize sayısının başında, ortasında veya sonunda bulunması için nasıl kullanılacağını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **Gelişmiş Konular**
- [Belirli Stile Sahip Hücreleri Bulma](/cells/tr/net/find-cells-with-specific-style/)
- [Hücre Değerinin Tek Tırnak İşareti ile Başlayıp Başlamadığını Bulma](/cells/tr/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Orijinal Değerler Kullanarak Veri Arama](/cells/tr/net/search-data-using-original-values/)
