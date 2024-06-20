---
title: Veri Bulma veya Arama
type: docs
weight: 50
url: /tr/python-net/find-or-search-data/
description: Belirli verileri içeren bir çalışma sayfasında hücreleri bulmayı veya aramayı Aspose.Cells for Python via .NET API si üzerinden nasıl yapacağınızı öğrenin.
keywords: Python Excel Kitaplığı, Python Veri bulma, Python Veri arama, Python Formül İçeren Hücreleri Bulma, Python Formül İçeren Hücreleri Arama, Python FindOptions Kullanarak Veri veya Formülleri Bulma, Python FindOptions Kullanarak Veri veya Formülleri Arama, Belirli Dize Değerini veya Numarayı İçeren Hücreleri Bulma veya Arama, Belirli verileri içeren hücreleri Python bulma veya arama
---

{{% alert color="primary" %}}

Microsoft Excel, kullanıcılara belirli verileri içeren bir çalışma sayfasında hücreleri bulmalarına izin verir.

{{% /alert %}}

## **Belirli Verileri İçeren Hücreleri Bulma**

### **Microsoft Excel Kullanımı**

Microsoft Excel, kullanıcıların belirli verileri içeren bir çalışma sayfasında hücreleri bulmasına izin verir. Microsoft Excel'de **Düzenle**'yi seçerseniz, arama değerini belirleyebileceğiniz bir iletişim kutusu göreceksiniz.

Burada, "Portakallar" değerini arıyoruz. Aspose.Cells, ayrıca belirli değerleri içeren hücreleri bulmayı sağlar.

### **Aspose.Cells Kullanımı**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonunu sağlar. [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonu, kullanıcı tarafından belirtilen verileri içeren bir çalışma sayfasındaki hücreleri bulmak için birkaç yöntem sağlar. Bu yöntemlerden bazıları aşağıda daha detaylı olarak tartışılmıştır.

{{% alert color="primary" %}}

Tüm Bul yöntemleri, belirtilen verileri içeren hücrelerin referanslarını döndürür.

{{% /alert %}}

## **Formül İçeren Hücreleri Bulma**

Geliştiriciler, [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonunun [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) yöntemini çağırarak çalışma sayfasındaki belirli bir formülü bulabilirler. Genellikle, [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) yöntemi üç parametre alır:

- **what:** Aranacak nesne. Türü int,double,DateTime,string,bool olmalıdır.
- **previous_cell:** Nesneyi içeren önceki hücre. Başlangıçtan itibaren arama yapılıyorsa bu parametre null olarak ayarlanabilir.
- **find_options:** Gerekli nesneyi bulmak için seçenekler.

Aşağıdaki örnekler, bulma yöntemlerini uygulamak için çalışma sayfası verilerini kullanır:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingFormula-1.py" >}}

## **FindOptions Kullanarak Veri veya Formülleri Bulma**

Çeşitli [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions) ile [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonunun [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) yöntemi kullanılarak belirli değerleri bulmak mümkündür. Genellikle, [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) yöntemi aşağıdaki parametreleri kabul eder:

- **what:**, aranacak veri veya değer.
- **previous_cell**, aynı değeri içeren son hücre. Başlangıçtan itibaren arama yapılıyorsa bu parametre null olarak ayarlanabilir.
- **find_options**, bulma seçenekleri.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingDataOrFormulasUsingFindOptions-1.py" >}}

## **Belirli Dize Değeri veya Numarası İçeren Hücreleri Bulma**

Belirli dize değerlerin bulunması, [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonunda bulunan aynı [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) yöntemiyle çeşitli [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions) ile çağrılabilir.

[**FindOptions.look_in_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_in_type/) ve [**FindOptions.look_at_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_at_type/) özelliklerini belirtin. Aşağıdaki örnek kod, bu özellikleri kullanarak hücrelerde dize sayısının başında, ortasında veya sonunda bulunması için nasıl kullanılacağını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingStringValueOrNumber-1.py" >}}

## **Gelişmiş Konular**
- [Belirli Stile Sahip Hücreleri Bulma](/cells/tr/python-net/find-cells-with-specific-style/)
- [Hücre Değerinin Tek Tırnak İşareti ile Başlayıp Başlamadığını Bulma](/cells/tr/python-net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Orijinal Değerler Kullanarak Veri Arama](/cells/tr/python-net/search-data-using-original-values/)
