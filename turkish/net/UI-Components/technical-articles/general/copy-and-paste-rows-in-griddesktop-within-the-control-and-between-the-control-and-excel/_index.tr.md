---
title: Kontrol içinde ve Kontrol ile Excel arasında GridDesktop'ta Satırları Kopyala ve Yapıştır
type: docs
weight: 70
url: /tr/net/copy-and-paste-rows-in-griddesktop-within-the-control-and-between-the-control-and-excel/
---
{{% alert color="primary" %}} 

Kontrol içinde veya kontrol ile excel arasında GridDesktop'ta satırları kopyalayıp yapıştırmayı etkinleştirmek istiyorsanız, lütfen GridDesktop.ClipboardCopyPaste özelliğini true olarak ayarlayın. Bu özelliği tasarım zamanında veya kodda ayarlayabilirsiniz. Bu özelliğin varsayılan değeri yanlıştır. Şu anda, yalnızca hücre değerlerini kopyalayıp yapıştırabilir ve hücrenin biçim, kenarlık stili vb.

{{% /alert %}} 
## **Tasarım Modunda ve Çalışma Süresinde GridDesktop.ClipboardCopyPaste özelliğinin ayarlanması**
 Aşağıdaki örnek kod, içinde GridDesktop.ClipboardCopyPaste özelliğini ayarlar.**Çalışma süresi**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-CopyAndPasteRows-1.cs" >}}
