---
title: Bir Excel Dosyasını Açma
type: docs
weight: 10
url: /tr/net/opening-an-excel-file/
---
{{% alert color="primary" %}} 

Aspose.Cells Grid Suite'in benzersiz bir özelliği, Excel dosyalarıyla uyumlu olmasıdır. Bu konuda, kullanıcıların Aspose.Cells.GridDesktop kontrolünü kullanarak Windows uygulamalarında Excel dosyalarını nasıl açabileceklerini göstereceğiz.

{{% /alert %}} 
## **Giriş**
 Aspose.Cells.GridDesktop kullanarak bir Excel dosyasını açmak için, içinde GridDesktop Control bulunan bir masaüstü uygulaması oluşturmanız gerekir. Windows formunuza Aspose.Cells.GridDesktop kontrolünü nasıl ekleyeceğinizi bilmiyorsanız, o zaman başvurmalısınız.[Aspose.Cells.GridDesktop nasıl kullanılır?](/cells/tr/net/how-to-use-aspose-cells-griddesktop/)

Aspose.Cells.GridDesktop, bir Excel dosyasını açmak için aşağıdaki üç farklı yolu sunar.

1. **Dosyadan Açma**
1. **CSV dosyası açılıyor**
1. **Akıştan Açma**
## **Excel Dosyasını Açma**
Bu örnekte bir masaüstü uygulaması oluşturun ve aşağıdakileri yapın.

- Forma bir GridControl Denetimi ekleyin.
- Metin özellikleri aşağıdaki gibi ayarlanmış üç düğme ekleyin:
  - **Excel Dosyasını Aç**
  - **CSV Dosyasını Aç**
  - **Akıştan aç**
### **Dosyadan Açma**
 İçeriği bir Excel dosyasından Aspose.Cells.GridDesktop kontrolüne yüklemek için, Excel dosyasının yolunu belirtmek üzere bir kontrol yöntemi çağırmanız gerekecektir. Bundan sonra, Aspose.Cells.GridDesktop kontrolü dosyayı belirtilen yoldan otomatik olarak bulur ve içeriğini görüntüler. Bir Excel dosyasının içeriğini yüklemek için kod parçacığı aşağıdaki örnekte verilmiştir. Tıklama olayını oluşturun**Excel Dosyasını Aç** butonuna basın ve içine aşağıdaki kodu yapıştırın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


Yukarıdaki kod parçacığı, geliştiriciler tarafından istedikleri şekilde kullanılabilir. Örneğin, bir Windows formu yüklendiğinde otomatik olarak bir Excel dosyası yüklemek istiyorsanız, bu kodu Formunuzun Load olayı altına ekleyebilirsiniz.
### **CSV dosyası açılıyor**
Aspose.Cells.GridDesktop kontrolü, CSV dosyasının yüklenmesini de destekler. Tıklama olayını oluşturun**CSV Dosyasını Aç** butonuna basın ve içine aşağıdaki kodu yapıştırın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **Akıştan Açma**
 Yukarıdaki tartışmamızda, dosya yolunu kullanarak bir Excel dosyasını yükleme hakkında tartıştık, ancak Aspose.Cells.GridDesktop kontrolü bir akıştan Excel dosyası yüklemeyi de destekler. Tıklama olayını oluşturun**Akıştan aç** butonuna basın ve içine aşağıdaki kodu yapıştırın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



Dosyayı bir akış olarak kullanmak, her türlü dosya erişimini veya paylaşım ihlali sorunlarını engellemek için daha iyi bir yaklaşımdır çünkü bu yaklaşım, akışı kapatarak dosyalara olan tüm bağlantıların kapatılmasını sağlar.

{{% alert color="primary" %}} 

ÖNEMLİ: Tartışılması gereken önemli bir nokta, Aspose.Cells.GridDesktop kontrolünün ayrıca bir Excel dosyasının içeriğini Grid'e yüklemek için kullanılan LoadFromExcel adlı bir yöntemi içermesidir. Ancak, bu yöntem artık geçerliliğini yitirmiştir. Bu nedenle, tüm geliştiricilerin eski yöntemden daha sağlam ve verimli olan ImportExcelFile yöntemini kullanmaları önerilir.

{{% /alert %}}
