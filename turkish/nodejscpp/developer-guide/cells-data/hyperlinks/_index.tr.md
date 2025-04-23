---
title: Excel veya OpenOffice a Hyperlink Ekleme
linktitle: Hyperlinkleri Yönetme
type: docs
weight: 45
url: /tr/nodejs-cpp/insert-hyperlinks-to-excel/
description: MS Excel olmadan ilişkili bağlantıları Aspose.Cells kütüphanesi kullanarak Node.js’de nasıl ekleyeceğinizi gösteren yöntem.
keywords: Excel Node.js ye Bağlantı Ekleyin veya Girin, C++ ile Node.js üzerinden Bağlantı Ekle veya Gir, C++ ile Node.js üzerinden URL ye Bağlantı Ekle veya Gir, C++ ile Node.js üzerinden Bir Hücreye Bağlantı Ekle veya Gir, Node.js ile Bir Dış Dosyaya Bağlantı Ekleyin veya Gir
---

{{% alert color="primary" %}} 

Bir bağlantı, iki varlık arasında bir bağlantı oluşturmak için kullanılır. Herkes, özellikle web sitelerinde bağlantıların kullanımı hakkında bilgilidir.
Aspose.Cells kullanarak, geliştiriciler Microsoft Excel dosyalarında farklı türde bağlantılar oluşturabilir. Bu konu, Aspose.Cells tarafından desteklenen bağlantı türlerini ve bunların Excel dosyalarımızda nasıl kullanılabileceğini tartışmaktadır.

{{% /alert %}} 

## **Hyperlinkler Ekleme**
Aspose.Cells, geliştiricilerin hem API kullanarak hem de tasarımcı tabloları (manuel olarak bağlantıların oluşturulduğu ve Aspose.Cells'in diğer tablolara aktarım için kullanıldığı tablolar) ile bağlantılar eklemesine olanak tanır.

Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her sayfaya erişim sağlayan [WorksheetCollection](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) içerir. Bir sayfa, [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, Excel dosyalarına çeşitli bağlantılar eklemek için farklı yöntemler sunar.
## **URL'ye Bağlantı Ekleme**
[Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--) koleksiyonunu içerir. [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--) koleksiyonundaki her öğe, bir [Hyperlink](https://reference.aspose.com/cells/nodejs-cpp/hyperlink) temsil eder. URL'lere bağlantı eklemek için, [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection) koleksiyonunun [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) yöntemini çağırın. [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) yöntemi şu parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, URL adresi.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToURL.js" >}}


{{% alert color="primary" %}} 

Yukarıdaki örnekte, bir hiper bağlantı boş bir hücre olan **A1**'e eklenir. Bu tür durumlarda, hücre boşsa, URL adresi de boş hücreye değeri olarak eklenir. Hücre dolu değilse ve bir hiper bağlantı eklenmişse, hücrenin değeri düz metin olarak görünür. Onu bir hiper bağlantı gibi görünmesini sağlamak için o hücreye uygun biçimlendirme ayarlarını uygulayın.

{{% /alert %}} 
## **Aynı Dosyadaki Bir Hücreye Bağlantı Ekleme**
Aynı Excel dosyasındaki hücrelere bağlantı eklemek için, [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection) koleksiyonunun [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) yöntemini çağırabilirsiniz. [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) yöntemi hem iç hem de dış bağlantılar için çalışır. Aşırı yüklenmiş yöntemin bir versiyonu şu parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef hücrenin adresi.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToCell.js" >}}


## **Harici Bir Dosyaya Bağlantı Ekleme**
Dış Excel dosyalarına bağlantı eklemek için, [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection) koleksiyonunun [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) yöntemini çağırabilirsiniz. [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) yöntemi şu parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef harici Excel dosyasının adresi.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToExternalFile.js" >}}



## **Gelişmiş Konular**
- [Görüntü Bağlantılarını Eklemek](/cells/tr/nodejs-cpp/add-image-hyperlinks/)
- [Bağlantı Türünü Algılamak](/cells/tr/nodejs-cpp/detect-hyperlink-type/)
- [Çalışma Sayfasının Bağlantılarını Düzenleme](/cells/tr/nodejs-cpp/editing-hyperlinks-of-worksheet/)
- [Aralıktaki Bağlantıları Al](/cells/tr/nodejs-cpp/get-hyperlinks-in-range/)

