---
title: Köprüleri Excel veya OpenOffice'e Ekleme
linktitle: Köprüleri Yönetme
type: docs
weight: 160
url: /tr/java/insert-hyperlinks-to-excel/
---
## **Bağlantı Verilerine Köprü Ekleme**
{{% alert color="primary" %}} 

İki varlık arasında bir bağlantı oluşturmak için bir köprü kullanılır. Herkes, özellikle web sitelerinde, hiper bağlantıların kullanımına aşinadır.

Aspose.Cells'i kullanan geliştiriciler, Microsoft Excel dosyalarında farklı türden köprüler oluşturabilir. Bu konuda, Aspose.Cells tarafından hangi tür köprülerin desteklendiği ve bunların Excel dosyalarımızda nasıl kullanılabileceği açıklanmaktadır.

{{% /alert %}} 
## **Köprü Ekleme**
Aspose.Cells kullanılarak bir hücreye üç tür köprü eklenebilir:

- [Bir URL'ye bağlantı ekleme](/cells/tr/java/working-with-hyperlinks-to-link-data/).
- [Aynı dosyadaki başka bir hücreye bağlantı ekleme](/cells/tr/java/working-with-hyperlinks-to-link-data/).
- [Harici bir dosyaya bağlantı ekleme](/cells/tr/java/working-with-hyperlinks-to-link-data/).

 Aspose.Cells, geliştiricilerin Excel dosyalarına API veya[tasarımcı elektronik tabloları](/cells/tr/java/what-is-a-designer-spreadsheet/)(köprülerin manuel olarak oluşturulduğu ve bunları diğer elektronik tablolara aktarmak için Aspose.Cells'in kullanıldığı elektronik tablolar).

Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)class, Excel dosyalarına farklı köprüler eklemek için farklı yöntemler sağlar.
## **Bir URL'ye Bağlantı Ekleme**
 bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf bir içerir[köprüler](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) Toplamak. İçindeki her öğe[köprüler](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) koleksiyon temsil eder[köprü](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) . Çağırarak URL'lere köprüler ekleyin[köprüler](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks) koleksiyonun[Eklemek](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )yöntem. bu[Eklemek](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) yöntemi aşağıdaki parametreleri alır:

- Cell adı, köprünün ekleneceği hücrenin adı.
- Satır sayısı, bu köprü aralığındaki satır sayısı.
- Sütun sayısı, bu köprü aralığının sütun sayısı
- URL, URL adresi.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


 Yukarıdaki örnekte, boş bir hücredeki bir URL'ye köprü eklenir,**A1**Bu gibi durumlarda, bir hücre boşsa URL adresi de o boş hücreye değer olarak eklenir. Hücre boş değilse ve bir köprü eklenirse, hücrenin değeri düz metin gibi görünür. Köprü gibi görünmesini sağlamak için ilgili hücreye uygun biçimlendirme ayarlarını uygulayın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **Aynı Dosyada Cell'e Bağlantı Ekleme**
 Aynı Excel dosyasındaki hücrelere köprüler eklemek mümkündür.[köprüler](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) koleksiyonun[Eklemek](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )yöntem. bu[Eklemek](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) yöntemi hem iç hem de dış köprüler için çalışır. Aşırı yüklenmiş yöntemin bir sürümü aşağıdaki parametreleri alır:

- Cell adı, köprünün ekleneceği hücrenin adı.
- Satır sayısı, bu köprü aralığındaki satır sayısı.
- Sütun sayısı, bu köprü aralığındaki sütun sayısı.
- URL, hedef hücrenin adresi.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **Harici Dosyaya Bağlantı Ekleme**
 Dış Excel dosyalarına köprüler eklemek mümkündür.[köprüler](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) koleksiyonun[Eklemek](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )yöntem. bu[Eklemek](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) yöntemi aşağıdaki parametreleri alır:

- Cell adı, köprünün ekleneceği hücrenin adı.
- Satır sayısı, bu köprü aralığındaki satır sayısı.
- Sütun sayısı, bu köprü aralığındaki sütun sayısı.
- URL, hedefin adresi, harici Excel dosyası.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **ileri konular**
- [Resim Köprüleri Ekle](/cells/tr/java/add-image-hyperlinks/)
- [Köprü Türünü Algıla](/cells/tr/java/detect-hyperlink-type/)
- [Çalışma Sayfasının Köprülerini Düzenleme](/cells/tr/java/editing-hyperlinks-of-worksheet/)
- [Menzildeki Köprüleri Alın](/cells/tr/java/get-hyperlinks-in-range/)


