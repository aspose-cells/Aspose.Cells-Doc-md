---
title: Golang ile C++ üzerinden Excel veya OpenOffice e Hipermetin Bağlantıları Ekleyin
linktitle: Hyperlinkleri Yönetme
type: docs
weight: 45
url: /tr/go-cpp/insert-hyperlinks-to-excel/
description: MS Excel kullanmadan Aspose.Cells kütüphanesi ile Excel dosyasına nasıl bağlantı eklenir.
keywords: Excel e Hyperlink Ekleme, Bağlantı Ekleme, URL ye Bağlantı Ekleme, Bir Hücreye Bağlantı Ekleme, Bir Dış Dosyaya Bağlantı Ekleme
---

{{% alert color="primary" %}} 

Bir bağlantı, iki varlık arasında bir bağlantı oluşturmak için kullanılır. Herkes, özellikle web sitelerinde bağlantıların kullanımı hakkında bilgilidir.
Aspose.Cells kullanarak, geliştiriciler Microsoft Excel dosyalarında farklı türde bağlantılar oluşturabilir. Bu konu, Aspose.Cells tarafından desteklenen bağlantı türlerini ve bunların Excel dosyalarımızda nasıl kullanılabileceğini tartışmaktadır.

{{% /alert %}} 

## **Hyperlinkler Ekleme**
Aspose.Cells, geliştiricilerin hem API kullanarak hem de tasarımcı tabloları (manuel olarak bağlantıların oluşturulduğu ve Aspose.Cells'in diğer tablolara aktarım için kullanıldığı tablolar) ile bağlantılar eklemesine olanak tanır.

 Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, Excel dosyalarına farklı bağlantılar eklemek için çeşitli yöntemler sağlar.

## **URL'ye Bağlantı Ekleme**
 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı, bir [GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/) koleksiyonunu içerir. [GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/) koleksiyonundaki her öğe bir [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/) temsil eder. URL’lere hiperlink eklemek için, [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) koleksiyonunun [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) metodunu çağırın. [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) metodu aşağıdaki parametreleri alır.

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, URL adresi.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks.go" >}}
{{% alert color="primary" %}} 

Yukarıdaki örnekte, bir hiper bağlantı boş bir hücre olan **A1**'e eklenir. Bu tür durumlarda, hücre boşsa, URL adresi de boş hücreye değeri olarak eklenir. Hücre dolu değilse ve bir hiper bağlantı eklenmişse, hücrenin değeri düz metin olarak görünür. Onu bir hiper bağlantı gibi görünmesini sağlamak için o hücreye uygun biçimlendirme ayarlarını uygulayın.

{{% /alert %}} 

## **Aynı Dosyadaki Bir Hücreye Bağlantı Ekleme**
 Aynı Excel dosyasındaki hücrelere hiperlink eklemek için [Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/) koleksiyonunun [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) metodunu çağırabilirsiniz. [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) metodu hem dahili hem de harici hiperlinkler için çalışır. Aşırı yüklenmiş metodun bir versiyonu aşağıdaki parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef hücrenin adresi.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks-1.go" >}}
## **Harici Bir Dosyaya Bağlantı Ekleme**
 Harici Excel dosyalarına hiperlink eklemek için [Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/) koleksiyonunun [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) metodunu çağırabilirsiniz. [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) metodu aşağıdaki parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef harici Excel dosyasının adresi.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks-2.go" >}}
## **Gelişmiş Konular**
- [Görüntü Bağlantılarını Eklemek](/cells/tr/cpp/add-image-hyperlinks/)
- [Bağlantı Türünü Algılamak](/cells/tr/cpp/detect-hyperlink-type/)
- [Çalışma Sayfasının Bağlantılarını Düzenleme](/cells/tr/cpp/editing-hyperlinks-of-worksheet/)
- [Aralıktaki Bağlantıları Al](/cells/tr/cpp/get-hyperlinks-in-range/)
