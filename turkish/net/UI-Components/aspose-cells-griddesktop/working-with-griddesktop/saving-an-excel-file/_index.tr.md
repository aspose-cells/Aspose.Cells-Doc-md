---
title: Bir Excel Dosyasını Kaydetme
type: docs
weight: 20
url: /tr/net/saving-an-excel-file/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop kontrolünü kullanarak, kullanıcılar yalnızca yeni Excel dosyaları oluşturamaz, aynı zamanda mevcut olanları da yönetebilir. Ancak her iki durumda da Aspose.Cells.GridDesktop içeriğini kaydetmek gerekli olacaktır. Bu, kullanıcılarımıza Grid içeriklerini bir Excel dosyası olarak nasıl kaydedebilecekleri konusunda bilgi vermek için şimdi tartışmamızın konusu.

{{% /alert %}} 
## **giriiş**
Aspose.Cells.GridDesktop kontrolünün içeriğini bir Excel dosyası olarak kaydetmek için Aspose.Cells.GridDesktop aşağıdaki yöntemleri sağlar.

1. **Dosya Olarak Kaydetme**
1. **Akış Olarak Kaydetme**
## **Dosya kaydediliyor**
 Bir masaüstü uygulaması oluşturun ve GridControl denetimiyle forma iki düğme ekleyin. Düğmelerin metin özelliklerini şu şekilde ayarlayın:**Dosya Olarak Kaydet** ve**Akış Olarak Kaydet** sırasıyla.
### **Dosya Olarak Kaydetme**
 Tıklama olayını oluşturun**Dosya Olarak Kaydet** butonuna basın ve içine aşağıdaki kodu yapıştırın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

ÖNEMLİ: Tartışılması gereken önemli bir nokta, Aspose.Cells.GridDesktop kontrolünün ayrıca bir Excel dosyasının içeriğini Grid'e yüklemek için de kullanılan SaveToExcel adlı bir yöntemi içermesidir. Ancak, bu yöntem artık geçerliliğini yitirmiştir. Bu nedenle, tüm geliştiricilerin eskisinden daha sağlam ve verimli olan ExportExcelFile yöntemini kullanmaları önerilir.

{{% /alert %}} 
### **Akış Olarak Kaydetme**
 Bazen, geliştiricilerin Grid içeriklerini bir akışa kaydetmeleri gerekebilir (Örneğin, MemoryStream). Bu görevi kolaylaştırmak için Aspose.Cells.GridDesktop kontrolü, Grid verilerinin bir akışa kaydedilmesini de destekler. Tıklama olayını oluşturun**Akış Olarak Kaydet** butonuna basın ve içine aşağıdaki kodu yapıştırın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

ÖNEMLİ: Microsoft Excel, Excel sayfalarının maksimum 65.536 satır ve 256 sütun içerebileceğini destekler. Aspose.Cells.GridDesktop da aynı standartları takip eder. Aspose.Cells.GridDesktop kontrolünde, geliştiriciler standart sınırdan daha fazla satır ve sütun oluşturabilir, ancak ızgara verilerini bir Excel dosyasına kaydederken bir istisna atılır. Bu, yalnızca 65.536 satır ve 256 sütunda bulunan verilerin Aspose.Cells.GridDesktop kullanılarak bir Excel dosyasına kaydedilebileceği anlamına gelir.

{{% /alert %}}
