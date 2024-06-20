---
title: Özel Komut Düğmeleri Oluşturma
type: docs
weight: 100
url: /tr/net/aspose-cells-gridweb/create-custom-command-buttons/
keywords: GridWeb, komut düğmeleri, özel komut düğmeleri, özel
description: Bu makale, GridWeb de özel komut düğmeleri nasıl oluşturulacağını tanıtır.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb özel **Gönder**, **Kaydet** ve **Geri Al** gibi özel düğmeler içerir. Tüm bu düğmeler Aspose.Cells.GridWeb için belirli görevleri gerçekleştirir.
Özel görevleri gerçekleştiren özel düğmeler eklemek de mümkündür. Bu konu, bu özelliğin nasıl kullanılacağını açıklar.

{{% /alert %}} 
## **Özel Komut Düğmeleri Oluşturma**
Aspose.Cells.GridWeb'de özel bir komut düğmesi oluşturmak için:

1. Aspose.Cells.GridWeb denetimini web formuna ekleyin.
1. Bir çalışsayı açın.
1. CustomCommandButton sınıfının bir örneğini oluşturun.
1. Düğmenin Komutunu bir değere ayarlayın. Bu değer, düğmenin olay işleyicisinde kullanılır.
1. Düğmenin metnini ayarlayın.
1. Düğmenin görüntü URL'sini ayarlayın.
1. Son olarak, CustomCommandButton nesnesini GridWeb denetiminin CustomCommandButtons koleksiyonuna ekleyin.

{{% alert color="primary" %}} 

Özel komut düğmeleri ayrıca Visual Studio'nun Özellikler iletişim kutusunu kullanarak WYSIWYG modunda da eklenebilir.

{{% /alert %}} 

Kod parçacığının çıktısı aşağıda gösterilmiştir:

**GridWeb denetimine özel bir komut düğmesi eklendi** 

![todo:image_alt_text](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **Özel Komut Düğmesi Olay İşleme**
Özel komut düğmelerinin en önemli yönü, tıklanıldığında gerçekleştirdikleri eylemdir. Eylemi ayarlamak için, GridWeb denetiminin CustomCommand olayı için bir olay işleyici oluşturun.

CustomCommand olayı her zaman özel komut düğmesi tıklandığında tetiklenir. Bu nedenle, olay işleyicisinin, düğmeyi GridWeb denetimine eklerken ayarlanan Komutla bağlantılı belirli özel komut düğmesini tanımlaması gerekir. Son olarak, düğme tıklandığında yürütülen özel kodu ekleyin.

Aşağıdaki kod örneğinde, düğme tıklandığında A1 hücresine bir metin mesajı eklenir.

**Özel komut düğmesine tıklandığında A1 hücresine eklenen metin** 

![todo:image_alt_text](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
