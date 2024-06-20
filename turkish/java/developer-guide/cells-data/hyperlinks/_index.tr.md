---
title: Excel veya OpenOffice a Hyperlink Ekleme
linktitle: Hyperlinkleri Yönetme
type: docs
weight: 160
url: /tr/java/insert-hyperlinks-to-excel/
---

## **Veri Bağlantılı Hyperlink Ekleme**
{{% alert color="primary" %}} 

Bir bağlantı, iki varlık arasında bir bağlantı oluşturmak için kullanılır. Herkes, özellikle web sitelerinde bağlantıların kullanımı hakkında bilgilidir.

Aspose.Cells kullanarak, geliştiriciler Microsoft Excel dosyalarında farklı türde bağlantılar oluşturabilir. Bu konu, Aspose.Cells tarafından desteklenen bağlantı türlerini ve bunların Excel dosyalarımızda nasıl kullanılabileceğini tartışmaktadır.

{{% /alert %}} 
## **Hyperlinkler Ekleme**
Aspose.Cells, üç farklı bağlantı türünü bir hücreye eklemek için kullanır:

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) adlı bir sınıf sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, Excel dosyalarına farklı hyperlinkler eklemek için farklı yöntemler sağlar.
- [Aynı dosyadaki başka bir hücreye bağlantı ekleme](/cells/tr/java/working-with-hyperlinks-to-link-data/).
- [Dış bir dosyaya bağlantı ekleme](/cells/tr/java/working-with-hyperlinks-to-link-data/).

Aspose.Cells, geliştiricilere Excel dosyalarına API veya [tasarımcı elektronik tablolar](/cells/tr/java/what-is-a-designer-spreadsheet/) (hiperbağlantıların manuel olarak oluşturulduğu elektronik tablolar ve Aspose.Cells'in bunları diğer elektronik tablolara aktarmak için kullanıldığı elektronik tablolar) kullanarak hiperbağlantılar eklemelerine izin verir.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her elektronik tabloya erişime izin veren bir [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) içerir. Elektronik tablo, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, Excel dosyalarına farklı hiperbağlantılar eklemek için farklı yöntemler sağlar.
## **URL'ye Bağlantı Ekleme**
[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) koleksiyonunu içerir. [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) koleksiyonundaki her öğe, bir [Hyperlink](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) öğesini temsil eder. [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks) koleksiyonunun [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) yöntemini çağırarak URL'lere hyperlinkler ekleyin. [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) yöntemi şu parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, URL adresi.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


Yukarıdaki örnekte, boş bir hücre, **A1**. Boş ise URL adresi de olarak eklenir. Hücre dolu değilse ve bir hyperlink eklenirse hücrenin değeri düz metin gibi görünür. Ona uygun hyperlink gibi görünmesini sağlamak için hücreye uygun biçimlendirme ayarlarını uygulayın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **Aynı Dosyadaki Bir Hücreye Bağlantı Ekleme**
[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) koleksiyonunun [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) yöntemi çağrılarak aynı Excel dosyasındaki hücrelere hyperlink eklemek mümkündür. [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) yöntemi, hem iç hem de dış hyperlinkler için çalışır. Overloaded yönteminin bir versiyonu aşağıdaki parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef hücrenin adresi.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **Harici Bir Dosyaya Bağlantı Ekleme**
[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) koleksiyonunun [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) yöntemi çağrılarak harici Excel dosyalarına hyperlink eklemek mümkündür. [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) yöntemi aşağıdaki parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef harici Excel dosyasının adresi.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **Gelişmiş Konular**
- [Görüntü Bağlantılarını Eklemek](/cells/tr/java/add-image-hyperlinks/)
- [Bağlantı Türünü Algılamak](/cells/tr/java/detect-hyperlink-type/)
- [Çalışma Sayfasının Bağlantılarını Düzenleme](/cells/tr/java/editing-hyperlinks-of-worksheet/)
- [Aralıktaki Bağlantıları Al](/cells/tr/java/get-hyperlinks-in-range/)


