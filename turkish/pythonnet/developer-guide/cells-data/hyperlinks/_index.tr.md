---
title: Excel veya OpenOffice a Hyperlink Ekleme
linktitle: Hyperlinkleri Yönetme
type: docs
weight: 45
url: /tr/python-net/insert-hyperlinks-to-excel/
description: Aspose.Cells for Python via .NET kitaplığıyla MS Excel kullanmadan Excel dosyasına hyperlink ekleme yöntemi.
keywords: Python Excel Kütüphanesi, Python Excel e Hyperlink Ekleme, Python Hyperlink Ekleme veya Ekleme, Bir URL ye Bağlantı Ekleme veya İçine Ekleme, Hücreye Bağlantı Ekleme, Harici Dosyaya Bağlantı Ekleme
---

{{% alert color="primary" %}} 

Bir bağlantı, iki varlık arasında bir bağlantı oluşturmak için kullanılır. Herkes, özellikle web sitelerinde bağlantıların kullanımı hakkında bilgilidir.
Aspose.Cells for Python via .NET kullanarak geliştiriciler Microsoft Excel dosyalarında farklı türde hyperlinkler oluşturabilirler. Bu konu, Aspose.Cells for Python via .NET tarafından desteklenen hyperlink türlerini ve bunların Excel dosyalarında nasıl kullanılabileceğini tartışmaktadır.

{{% /alert %}} 
## **Hyperlinkleri Nasıl Eklenir**
Aspose.Cells for Python via .NET, geliştiricilere API veya tasarımcı elektronik tablolar (hyperlinklerin manuel olarak oluşturulduğu ve Aspose.Cells for Python via .NET'nin diğer elektronik tablolara aktarıldığı elektronik tablolar) kullanarak Excel dosyalarına hyperlinkler eklemelerine olanak tanır.

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişime izin veren bir [WorksheetCollection](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, Excel dosyalarına farklı hyperlinkler eklemek için farklı metotlar sağlar.

## **Bir URL'ye Bağlantı Ekleme**
[Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, bir [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) koleksiyonuna sahiptir. [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) koleksiyonundaki her öğe, bir [Hyperlink](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink) için bir temsil eder. [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) metoduyla URL'lere hyperlinkler ekleyin. [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) metodu aşağıdaki parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu bağlantı aralığındaki sütun sayısı
- URL, URL adresi.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToURL-1.py" >}}

{{% alert color="primary" %}} 

Yukarıdaki örnekte, bir hiper bağlantı boş bir hücre olan **A1**'e eklenir. Bu tür durumlarda, hücre boşsa, URL adresi de boş hücreye değeri olarak eklenir. Hücre dolu değilse ve bir hiper bağlantı eklenmişse, hücrenin değeri düz metin olarak görünür. Onu bir hiper bağlantı gibi görünmesini sağlamak için o hücreye uygun biçimlendirme ayarlarını uygulayın.

{{% /alert %}} 

## **Aynı Dosya Üzerinde Bir Hücreye Bağlantı Eklemek**
Excel dosyasındaki hücrelere [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) koleksiyonunun [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) yöntemini çağırarak hiper bağlantı eklemek mümkündür. [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) yöntemi iç ve dış bağlantılar için çalışır. Aşırı yüklenmiş yöntemin bir versiyonu aşağıdaki parametreleri alır:

- Hücre adı, hyperlink'in eklenmesi gereken hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef hücrenin adresi.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToAnotherCell-1.py" >}}

## **Dış Bir Dosyaya Bağlantı Eklemek**
Dış Excel dosyalarına [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) koleksiyonunun [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) yöntemini çağırarak hiper bağlantı eklemek mümkündür. [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) yöntemi aşağıdaki parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef harici Excel dosyasının adresi.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToExternalFile-1.py" >}}

## **Gelişmiş Konular**
- [Görüntü Bağlantılarını Eklemek](/cells/tr/python-net/add-image-hyperlinks/)
- [Bağlantı Türünü Algılamak](/cells/tr/python-net/detect-hyperlink-type/)
- [Çalışma Sayfasının Bağlantılarını Düzenleme](/cells/tr/python-net/editing-hyperlinks-of-worksheet/)
- [Aralıktaki Bağlantıları Al](/cells/tr/python-net/get-hyperlinks-in-range/)

{{< app/cells/assistant language="python-net" >}}
