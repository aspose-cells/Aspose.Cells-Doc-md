---
title: Köprüleri Excel veya OpenOffice'e Ekleme
linktitle: Köprüleri Yönetme
type: docs
weight: 45
url: /tr/net/insert-hyperlinks-to-excel/
description: MS Excel olmadan Aspose.Cells kitaplığı ile Excel dosyasına köprüler nasıl eklenir.
---
{{% alert color="primary" %}} 

İki varlık arasında bir bağlantı oluşturmak için bir köprü kullanılır. Herkes, özellikle web sitelerinde, hiper bağlantıların kullanımına aşinadır.
Aspose.Cells'i kullanan geliştiriciler, Microsoft Excel dosyalarında farklı türden köprüler oluşturabilir. Bu konuda, Aspose.Cells tarafından hangi tür köprülerin desteklendiği ve bunların Excel dosyalarımızda nasıl kullanılabileceği açıklanmaktadır.

{{% /alert %}} 
## **Köprü Ekleme**
Aspose.Cells, geliştiricilerin API veya tasarımcı elektronik tablolarını (köprülerin manuel olarak oluşturulduğu ve Aspose.Cells'in bunları diğer elektronik tablolara aktarmak için kullanıldığı elektronik tablolar) kullanarak Excel dosyalarına köprüler eklemesine olanak tanır.

 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/net/aspose.cells/worksheet)class, Excel dosyalarına farklı köprüler eklemek için farklı yöntemler sağlar.
## **Bir URL'ye Bağlantı Ekleme**
 bu[Çalışma kağıdı](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir içerir[köprüler](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) Toplamak. İçindeki her öğe[köprüler](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) koleksiyon temsil eder[köprü](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) . Çağırarak URL'lere köprüler ekleyin[köprüler](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) koleksiyonun[Eklemek](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) yöntem. bu[Eklemek](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)yöntem aşağıdaki parametreleri alır:

- Cell adı, köprünün ekleneceği hücrenin adı.
- Satır sayısı, bu köprü aralığındaki satır sayısı.
- Sütun sayısı, bu köprü aralığındaki sütun sayısı
- URL, URL adresi.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

 Yukarıdaki örnekte, boş bir hücredeki bir URL'ye köprü eklenir,**A1**. Bu gibi durumlarda, bir hücre boşsa URL adresi de o boş hücreye değer olarak eklenir. Hücre boş değilse ve köprü eklenirse, hücrenin değeri düz metin gibi görünür. Köprü gibi görünmesini sağlamak için ilgili hücreye uygun biçimlendirme ayarlarını uygulayın.

{{% /alert %}} 
## **Aynı Dosyada Cell'e Bağlantı Ekleme**
 Aynı Excel dosyasındaki hücrelere köprüler eklemek mümkündür.[köprüler](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) koleksiyonun[Eklemek](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) yöntem. bu[Eklemek](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)yöntem hem dahili hem de harici köprüler için çalışır. Aşırı yüklenmiş yöntemin bir sürümü aşağıdaki parametreleri alır:

- Cell ad, köprünün ekleneceği hücrenin adı.
- Satır sayısı, bu köprü aralığındaki satır sayısı.
- Sütun sayısı, bu köprü aralığındaki sütun sayısı.
- URL, hedef hücrenin adresi.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **Harici Dosyaya Bağlantı Ekleme**
 Dış Excel dosyalarına köprüler eklemek mümkündür.[köprüler](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) koleksiyonun[Eklemek](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) yöntem. bu[Eklemek](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)yöntem aşağıdaki parametreleri alır:

- Cell adı, köprünün ekleneceği hücrenin adı.
- Satır sayısı, bu köprü aralığındaki satır sayısı.
- Sütun sayısı, bu köprü aralığındaki sütun sayısı.
- URL, hedefin adresi, harici Excel dosyası.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **ileri konular**
- [Resim Köprüleri Ekle](/cells/tr/net/add-image-hyperlinks/)
- [Köprü Türünü Algıla](/cells/tr/net/detect-hyperlink-type/)
- [Çalışma Sayfasının Köprülerini Düzenleme](/cells/tr/net/editing-hyperlinks-of-worksheet/)
- [Menzildeki Köprüleri Alın](/cells/tr/net/get-hyperlinks-in-range/)

