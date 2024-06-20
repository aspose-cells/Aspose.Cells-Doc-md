---
title: Veri Bulma veya Arama
type: docs
weight: 120
url: /tr/java/find-or-search-data/
---

{{% alert color="primary" %}} 

Microsoft Excel'de kullanıcılar belirli veri içeren hücreleri arayabilirler. Örneğin, **Düzenle**'ye tıklayıp ardından **Bul** seçeneğiyle Arama iletişim kutusunu açabilirler. Kullanıcı bir değer girer ve ardından aramak için **Tamam**'a tıklar. Excel eşleşen alanları vurgular.

**Belirli bir değer içeren hücreleri bulmak için Arama iletişim kutusu kullanımı** 

![todo:image_alt_text](find-or-search-data_1.png)

Bu örnekte, arama değeri "Portakallar"dır.

Aspose.Cells, geliştiricilere verilen bir değeri içeren hücreleri bulmak için çalışma sayfasındaki hücreler içinde arama yapma olanağı sağlar.

{{% /alert %}} 
## **Belirli Veri İçeren Hücreleri Bulma**
Aspose.Cells, bir Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir koleksiyon olan [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)'ı içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir.

[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) saati, çalışma sayfasındaki tüm hücreleri temsil eden bir koleksiyon olan [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)'i sağlar. [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonu, kullanıcı tarafından belirtilen veriyi içeren hücreleri bulmak için birkaç yöntem sağlar. Bunlardan birkaçı aşağıda daha ayrıntılı olarak tartışılmıştır.

Tüm bulma yöntemleri, belirtilen arama değerini içeren hücre referanslarını döndürür.
## **Formül İçeren Bulma**
Geliştiriciler, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunun [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) yöntemini çağırarak çalışma sayfasında belirtilen formülü bulabilir. [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) yöntemine [FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType)'ı [LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS) olarak ayarlama ve bu parametreyi [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) yöntemine parametre olarak geçirme.

Genellikle [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) yöntemi iki veya daha fazla parametre alır:

- Aranacak Nesne: çalışma sayfasında bulunması gereken bir nesneyi temsil eder.
- Önceki Hücre: aynı formülle önceki hücreyi temsil eder. Bu parametre, başlangıçtan itibaren arama yapılırken null olarak ayarlanabilir.
- Bulma Seçenekleri: Bulma kriterlerini temsil eder. Aşağıdaki örneklerde, arama yöntemlerini pratik etmek için aşağıdaki çalışma sayfası verileri kullanılır:

**Örnek çalışma sayfası verileri** 

![todo:image_alt_text](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **Stringler İçin Arama**
Dize değeri içeren hücreleri aramak kolay ve esnektir. Başlangıç karakteri ile başlayan dize içeren hücreler için arama yapmak veya karakterler kümesiyle başlayan dize içeren hücreler için arama yapmak gibi farklı arama yöntemleri bulunmaktadır.
### **Belirli Karakterlerle Başlayan Stringler İçin Arama**
Dizelerdeki ilk karakteri aramak için [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunun [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) yöntemini çağırın, [FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType)'ı [LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH) olarak ayarlayın ve bu parametre olarak [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) yöntemine geçirin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **Belirli Karakterlerle Biten Stringler İçin Arama**
Aspose.Cells ayrıca belirli karakterlerle biten dizeleri bulabilir. Dizelerin son karakterlerini aramak için [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunun [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) yöntemini çağırın, [FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType)'ı [LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH) olarak ayarlayın ve bu parametre olarak [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) yöntemine geçirin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **Düzenli İfadelerle Arama: RegEx Özelliği**
Düzenli bir ifade, belirli karakterlerin, kelimelerin veya desenlerin eşleştirilmesi (belirtilmesi ve tanınması) için kısa ve esnek bir yöntem sağlar.

Örneğin, abc-*~~xyz~~ düzenli ifade deseni "abc-123-xyz", "abc-985-xyz" ve "abc-pony-xyz" dizelerini eşleştirir. * joker karakterdir, bu nedenle desen, "abc" ile başlayan ve "-xyz" ile biten herhangi bir diziyi eşleştirir, ortadaki karakterlere bakılmaksızın.

Aspose.Cells, düzenli ifadelerle arama yapmanıza olanak tanır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **Gelişmiş Konular**
- [Belirli stile sahip hücreleri bulma](/cells/tr/java/find-cells-with-specific-style/)
- [Orijinal Değerler Kullanarak Veri Arama](/cells/tr/java/search-data-using-original-values/)
