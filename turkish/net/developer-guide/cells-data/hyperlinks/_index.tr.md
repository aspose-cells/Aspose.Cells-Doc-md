---
title: Excel veya OpenOffice a Hyperlink Ekleme
linktitle: Hyperlinkleri Yönetme
type: docs
weight: 45
url: /tr/net/insert-hyperlinks-to-excel/
description: Aspose.Cells kütüphanesi kullanılarak Excel dosyasına nasıl bağlantı eklenir.
keywords: Excel e Hyperlink Ekleme, Bağlantı Ekleme, URL ye Bağlantı Ekleme, Bir Hücreye Bağlantı Ekleme, Bir Dış Dosyaya Bağlantı Ekleme
---

{{% alert color="primary" %}} 

Bir bağlantı, iki varlık arasında bir bağlantı oluşturmak için kullanılır. Herkes, özellikle web sitelerinde bağlantıların kullanımı hakkında bilgilidir.
Aspose.Cells kullanarak, geliştiriciler Microsoft Excel dosyalarında farklı türde bağlantılar oluşturabilir. Bu konu, Aspose.Cells tarafından desteklenen bağlantı türlerini ve bunların Excel dosyalarımızda nasıl kullanılabileceğini tartışmaktadır.

{{% /alert %}} 
## **Hyperlinkler Ekleme**
Aspose.Cells, geliştiricilere Excel dosyalarına bağlantı ekleme olanağı tanır. Bu, API veya tasarımcı elektronik tablolar kullanılarak yapılabilir(elle bağlantılar oluşturulan elektronik tablolar ve Aspose.Cells'in bunları diğer elektronik tablolara aktarmak için kullanılması).

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) adlı bir sınıf sağlar. [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir [WorksheetCollection](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, Excel dosyalarına farklı hiperbağlantı eklemek için farklı yöntemler sağlar.
## **URL'ye Bağlantı Ekleme**
[Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) koleksiyonunu içerir. [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) koleksiyonundaki her öğe bir [Hyperlink](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) temsil eder. URL'lere hiperbağlantı eklemek için [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) koleksiyonunun [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) yöntemini çağırarak ekleyin. [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) yöntemi şu parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu bağlantı aralığındaki sütun sayısı
- URL, URL adresi.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

Yukarıdaki örnekte, bir hiper bağlantı boş bir hücre olan **A1**'e eklenir. Bu tür durumlarda, hücre boşsa, URL adresi de boş hücreye değeri olarak eklenir. Hücre dolu değilse ve bir hiper bağlantı eklenmişse, hücrenin değeri düz metin olarak görünür. Onu bir hiper bağlantı gibi görünmesini sağlamak için o hücreye uygun biçimlendirme ayarlarını uygulayın.

{{% /alert %}} 
## **Aynı Dosyadaki Bir Hücreye Bağlantı Ekleme**
Aynı Excel dosyasındaki hücrelere hiperbağlantı eklemek mümkündür, [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) koleksiyonunun [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) yöntemini çağırarak. [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) yöntemi, hem iç hem de dış hiperbağlantılar için çalışır. Aşırı yüklenmiş yöntemin bir sürümü şu parametreleri alır:

- Hücre adı, hyperlink'in eklenmesi gereken hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef hücrenin adresi.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **Harici Bir Dosyaya Bağlantı Ekleme**
Harici Excel dosyalarına hiperbağlantı eklemek mümkündür, [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) koleksiyonunun [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) yöntemini çağırarak. [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) yöntemi şu parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef harici Excel dosyasının adresi.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **Gelişmiş Konular**
- [Görüntü Bağlantılarını Eklemek](/cells/tr/net/add-image-hyperlinks/)
- [Bağlantı Türünü Algılamak](/cells/tr/net/detect-hyperlink-type/)
- [Çalışma Sayfasının Bağlantılarını Düzenleme](/cells/tr/net/editing-hyperlinks-of-worksheet/)
- [Aralıktaki Bağlantıları Al](/cells/tr/net/get-hyperlinks-in-range/)

{{< app/cells/assistant language="csharp" >}}
