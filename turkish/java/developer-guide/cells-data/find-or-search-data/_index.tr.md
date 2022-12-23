---
title: Veri Bul veya Ara
type: docs
weight: 120
url: /tr/java/find-or-search-data/
---
{{% alert color="primary" %}} 

 Microsoft Excel'de, kullanıcılar belirli verileri içeren hücreleri arayabilir. Örneğin, tıklama**Düzenlemek** ve sonra**Bulmak** Ara iletişim kutusunu açar. Kullanıcılar bir değer girer ve tıklar**Tamam** onu aramak için Excel, eşleşen alanları vurgular.

**Belirli bir değer içeren hücreleri bulmak için Bul iletişim kutusunu kullanma** 

![yapılacaklar:resim_alternatif_metin](find-or-search-data_1.png)

Bu örnekte arama değeri "Portakallar"dır.

Aspose.Cells, geliştiricilerin belirli bir değeri içerenleri bulmak için bir çalışma sayfasındaki hücreleri aramasına olanak tanır.

{{% /alert %}} 
## **Belirli Veriler İçeren Cells'i Bulma**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) , bu bir Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıf içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) , Excel dosyasındaki çalışma sayfalarının her birine erişim sağlayan bir koleksiyon. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)sınıf.

 bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf sağlar[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) , çalışma sayfasındaki tüm hücreleri temsil eden bir koleksiyon.[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)toplama, kullanıcı tanımlı verileri içeren bir çalışma sayfasındaki hücreleri bulmak için çeşitli yöntemler sağlar. Bu yöntemlerden birkaçı aşağıda daha ayrıntılı olarak ele alınmıştır.

Tüm bulma yöntemleri, belirtilen arama değerini içeren tüm hücreler için hücre başvurularını döndürür.
## **Formül İçeren Bulmak**
 Geliştiriciler, çalışma sayfasında belirli bir formülü arayarak bulabilirler.[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonun[bulmak](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\) ) yöntemini ayarlayarak[FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) ile[LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS)ve onu bir parametre olarak geçirmek[bulmak](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) yöntem.

 Tipik olarak,[bulmak](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) yöntemi iki veya daha fazla parametre kabul eder:

- Aranacak Nesne: çalışma sayfasında bulunması gereken bir nesneyi temsil eder.
- Önceki Cell: aynı formüle sahip önceki hücreyi temsil eder. Bu parametre, baştan arama yapılırken null olarak ayarlanabilir.
- Bul Seçenekleri: Bulma kriterlerini temsil eder. Aşağıdaki örneklerde, bulma yöntemlerini uygulamak için aşağıdaki çalışma sayfası verileri kullanılır:

**Örnek çalışma sayfası verileri** 

![yapılacaklar:resim_alternatif_metin](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **Dizeleri Arama**
Dize değeri içeren hücreleri aramak kolay ve esnektir. Aramanın farklı yolları vardır, örneğin, belirli bir karakterle veya karakter kümesiyle başlayan dizeleri içeren hücreleri arayın.
### **Belirli Karakterlerle Başlayan Dizeleri Arama**
 Bir dizideki ilk karakteri aramak için,[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonun[bulmak](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) yöntemini ayarlayın[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) ile[LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH)ve bunu bir parametre olarak iletin[bulmak](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) yöntem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **Belirli Karakterlerle Biten Dizeleri Arama**
 Aspose.Cells ayrıca belirli karakterlerle biten dizileri de bulabilir. Bir dizideki son karakterleri aramak için,[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonun[bulmak](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) yöntemini ayarlayın[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) ile[Tipe Bak.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH)ve bunu bir parametre olarak iletin[bulmak](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) yöntem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **Normal İfadelerle Arama: RegEx Özelliği**
Normal ifade, belirli karakterler, sözcükler veya kalıplar gibi metin dizelerini eşleştirmek (belirtmek ve tanımak) için özlü ve esnek bir yol sağlar.

Örneğin, normal ifade kalıbı abc-* ~~xyz~~ "abc-123-xyz", "abc-985-xyz" ve "abc-pony-xyz" dizileriyle eşleşir.* bir joker karakterdir, bu nedenle kalıp, ortada hangi karakterlerin olduğuna bakılmaksızın "abc" ile başlayan ve "-xyz" ile biten tüm dizelerle eşleşir.

Aspose.Cells normal ifadelerle arama yapmanızı sağlar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **ileri konular**
- [Belirli bir stile sahip hücreleri bulun](/cells/tr/java/find-cells-with-specific-style/)
- [Orijinal Değerleri Kullanarak Veri Arama](/cells/tr/java/search-data-using-original-values/)
