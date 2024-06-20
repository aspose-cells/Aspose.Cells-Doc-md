---
title: Excel Dosyası Açma
type: docs
weight: 10
url: /tr/net/aspose-cells-griddesktop/openg-an-excel-file/
keywords: GridDesktop, aç, dosya
description: Bu makale, GridDesktop ta dosya nasıl açılacağını tanıtır.
---

{{% alert color="primary" %}} 

Aspose.Cells Grid Suite'nin benzersiz bir özelliği, Excel dosyalarıyla uyumluluğudur. Bu konuda, kullanıcıların Aspose.Cells.GridDesktop kontrolünü kullanarak Windows uygulamalarında Excel dosyalarını nasıl açabileceğini göstereceğiz.

{{% /alert %}} 
## **Giriş**
Aspose.Cells.GridDesktop kullanarak Excel dosyasını açmak için bir masaüstü uygulaması oluşturmanız gerekmektedir. Windows formunuza Aspose.Cells.GridDesktop kontrolünü nasıl ekleyeceğiniz hakkında bilgi sahibi değilseniz, [Aspose.Cells.GridDesktop'ı nasıl kullanırım?](/cells/tr/net/how-to-use-aspose-cells-griddesktop/) başlıklı konuya bakmalısınız.

Aspose.Cells.GridDesktop, bir Excel dosyasını açmak için aşağıdaki üç farklı yol sağlar.

1. **Dosyadan Açma**
1. **CSV Dosyasını Açma**
1. **Akıştan Açma**
## **Excel Dosyası Açma**
Bu örnekte bir masaüstü uygulaması oluşturun ve aşağıdakileri yapın.

- Forma bir GridControl Kontrolü ekleyin.
- Metin özellikleri aşağıdaki gibi ayarlanmış üç düğme ekleyin:
  - **Excel Dosyası Aç**
  - **CSV Dosyası Aç**
  - **Akıştan Aç**
### **Dosyadan Açma**
Bir Excel dosyasından içeriği Aspose.Cells.GridDesktop kontrolüne yüklemek için, kontrolün bir yöntemini çağırmanız gerekecek. Bundan sonra, Aspose.Cells.GridDesktop kontrolü belirtilen yoldan dosyayı otomatik olarak bulacak ve içeriğini gösterecektir. Bir Excel dosyasının içeriğini yükleme kod örneği aşağıdaki örnekte verilmiştir. **Excel Dosyası Aç** düğmesinin Click olayını oluşturun ve aşağıdaki kodu yapıştırın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


Yukarıdaki kod örneği, geliştiricilerin istedikleri gibi kullanabileceği bir kod örneğidir. Örneğin, bir Windows form yüklenirken bir Excel dosyasını otomatik olarak yüklemek istiyorsanız, bu kodu Form'un Load olayı altına ekleyebilirsiniz.
### **CSV dosyası açma**
Aspose.Cells.GridDesktop kontrolü, CSV dosyasını yükleme işlemi de destekler. **CSV Dosyası Aç** düğmesinin Click olayını oluşturun ve aşağıdaki kodu yapıştırın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **Akıştan Açma**
Yukarıdaki tartışmamızda, bir Excel dosyasını dosya yolunu kullanarak yükleme konusunu ele aldık ancak Aspose.Cells.GridDesktop kontrolü aynı zamanda akıştan da Excel dosyası yükleme işlemini destekler. **Akıştan Aç** düğmesinin Click olayını oluşturun ve aşağıdaki kodu yapıştırın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



Dosyayı bir akış olarak kullanmak, herhangi bir türde dosya erişimi veya paylaşım ihlali sorunlarını engellemek için daha iyi bir yaklaşımdır çünkü bu yaklaşım, akışı kapatılarak dosyalara olan tüm bağlantıları kapatmayı garanti altına almaktadır.

{{% alert color="primary" %}} 

ÖNEMLİ: Tartışılması gereken önemli bir nokta, Aspose.Cells.GridDesktop kontrolünün aynı zamanda LoadFromExcel adında eski model olan bir yöntem içerdiğidir. Ancak, bu yöntem artık kullanımdan kaldırılmıştır. Bu nedenle, tüm geliştiricilerin eski model olan yerine daha güçlü ve verimli olan ImportExcelFile yöntemini kullanmaları önerilmektedir.

{{% /alert %}}
