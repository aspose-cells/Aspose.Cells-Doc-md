---
title: Excel Dosyasını Kaydetme
type: docs
weight: 20
url: /tr/net/aspose-cells-griddesktop/save-an-excel-file/
keywords: GridDesktop, kaydetme, dosya
description: Bu makale, GridDesktop ta dosya nasıl kaydedilirinin nasıl sunulduğunu tanıtıyor.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop kontrolünü kullanarak, kullanıcılar yalnızca yeni Excel dosyaları oluşturmakla kalmaz, aynı zamanda mevcut olanları yönetebilirler. Ancak her iki durumda da Aspose.Cells.GridDesktop içeriğini kaydetmek gerekecektir. Bu konu, kullanıcılarımıza içeriği nasıl Excel dosyası olarak kaydedebilecekleri konusu olacaktır.

{{% /alert %}} 
## **Giriş**
Aspose.Cells.GridDesktop kontrolünün içeriğini bir Excel dosyası olarak kaydetmek için, Aspose.Cells.GridDesktop aşağıdaki yöntemleri sağlar.

1. **Dosya Olarak Kaydetme**
1. **Akışa Kaydetme**
## **Dosya Kaydetme**
Bir masaüstü uygulaması oluşturun ve formunuza bir GridControl kontrolü ile iki düğme ekleyin. İlgili düğmelerin metin özelliklerini sırasıyla **Dosya Olarak Kaydet** ve **Akışa Kaydet** olarak ayarlayın.
### **Dosya Olarak Kaydetme**
**Dosya Olarak Kaydet** düğmesinin Click olayını oluşturun ve aşağıdaki kodu yapıştırın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

ÖNEMLİ: Tartışılması gereken önemli bir nokta, Aspose.Cells.GridDesktop kontrolünün aynı zamanda LoadFromExcel adında eski model olan bir yöntem içerdiğidir. Ancak, bu yöntem artık kullanımdan kaldırılmıştır. Bu nedenle, tüm geliştiricilerin eski model olan yerine daha güçlü ve verimli olan ExportExcelFile yöntemini kullanmaları önerilmektedir.

{{% /alert %}} 
### **Akışa Kaydetme**
Geliştiricilerin bazen Grid içeriğini bir akışa (örneğin, MemoryStream) kaydetmesi gerekebilir. Bu görevi kolaylaştırmak için, Aspose.Cells.GridDesktop kontrolü ayrıca Grid verilerini bir akışa kaydetmeyi destekler. **Stream Olarak Kaydet** düğmesinin Click olayını oluşturun ve içine aşağıdaki kodu yapıştırın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

ÖNEMLİ: Microsoft Excel, Excel tablolarının maksimum 65.536 satır ve 256 sütun içerebilmesini destekler. Aspose.Cells.GridDesktop da aynı standartları izler. Aspose.Cells.GridDesktop kontrolünde, geliştiriciler standart sınırlardan daha fazla satır ve sütun oluşturabilirler ancak grid verilerini bir Excel dosyasına kaydederken, bir istisna oluşacaktır. Bu, yalnızca 65.536 satır ve 256 sütun içeren verilerin Aspose.Cells.GridDesktop kullanılarak bir Excel dosyasına kaydedilebileceği anlamına gelir.

{{% /alert %}}
