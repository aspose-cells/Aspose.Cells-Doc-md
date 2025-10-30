---  
title: Veri Bulma veya Arama
type: docs  
weight: 50  
url: /tr/nodejs-cpp/find-or-search-data/  
description: Aspose.Cells for Node.js via C++ API si aracılığıyla belirli verileri içeren bir çalışma sayfasında hücreleri nasıl bulacağınızı veya arayacağınızı öğrenin.  
keywords: Belirli veriyi Node.js kullanarak C++ ile bulma, Node.js kullanarak C++ ile arama, Formül içeren hücreleri Node.js kullanarak C++ ile bulma, Node.js kullanarak C++ ile arama, FindOptions kullanarak toplam veri veya formül bulma veya arama Node.js ile, Belirtilen dizgi değeri veya numarayı içeren hücreleri Node.js ile bulma veya arama, Belirtilen dizi veya sayı içeren hücreleri Node.js ile bulma veya arama  
---  

{{% alert color="primary" %}}  
Microsoft Excel, belirli veriyi içeren hücreleri bulma imkanı sağlar.  
{{% /alert %}}  

## **Belirli Verileri İçeren Hücreleri Bulma**  

### **Microsoft Excel Kullanımı**  

Microsoft Excel, belirli veriyi içeren hücreleri bulma imkanı sağlar. Microsoft Excel'de **İşle** menüsünden **Bul** seçildiğinde, arama değerini belirtebileceğiniz bir iletişim kutusu göreceksiniz.  

Burada, "Portakallar" değerini arıyoruz. Aspose.Cells, ayrıca belirli değerleri içeren hücreleri bulmayı sağlar.  

### **Aspose.Cells for Node.js via C++ kullanımıyla**  

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonunu sağlar. [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonu, kullanıcı tarafından belirlenen verileri içeren hücreleri bulmak için çeşitli yöntemler sunar. Bu yöntemlerden birkaçını detaylıca aşağıda görebilirsiniz.  

{{% alert color="primary" %}}  
Tüm Bul yöntemleri, belirtilen verileri içeren hücrelerin referanslarını döndürür.  
{{% /alert %}}  

## **Formül İçeren Hücreleri Bulma**  

Geliştiriciler, belirli bir formülü [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunun [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) yöntemiyle bulabilirler. Genellikle, [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) metodu üç parametre alır:  

- **Obje:** Aranacak nesne. Türü int, double, DateTime, string, bool olmalı.  
- **Önceki hücre:** Aynı nesneye sahip önceki hücre. Aramaya başlarken null olarak ayarlanabilir.  
- **FindOptions:** Aranan nesne için seçenekler.  

Aşağıdaki örnekler, bulma yöntemlerini uygulamak için çalışma sayfası verilerini kullanır:  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainFormula.js" >}}


## **FindOptions Kullanarak Veri veya Formülleri Bulma**  

Belirtilen değerleri, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunun [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-) metodu ve çeşitli [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions) parametrelerle bulmak mümkündür. Genellikle, [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) metodu şu parametreleri kabul eder:  

- **Arama değeri**, aranmak istenen veri veya değer.  
- **Önceki hücre**, aynı değere sahip son hücre. Aramaya başlangıçtan itibaren arıyorsanız bu parametre null olarak ayarlanabilir.  
- **Bul seçenekleri**, bul seçenekleri.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindDataUsingFindOptions.js" >}}


## **Belirli Dize Değeri veya Numarası İçeren Hücreleri Bulma**  

Belirli dizgi değerleri, aynı [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) metodunu farklı [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions) parametreleriyle çağırarak bulunabilir.  

[**FindOptions.setLookInType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookInType-lookintype-) ve [**FindOptions.setLookAtType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookAtType-lookattype-) özelliklerini belirtin. Aşağıdaki örnek kod, bu özelliklerin nasıl kullanılacağını gösterir ve hücrenin başında, ortasında veya sonunda çeşitli sayıda dizge içeren hücreleri bulmak için kullanılır.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainSpecifyString.js" >}}



## **Gelişmiş Konular**  
- [Belirli Stile Sahip Hücreleri Bulma](/cells/tr/nodejs-cpp/find-cells-with-specific-style/)  
- [Hücre Değerinin Tek Tırnak İşareti ile Başlayıp Başlamadığını Bulma](/cells/tr/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Orijinal Değerler Kullanarak Veri Arama](/cells/tr/nodejs-cpp/search-data-using-original-values/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
