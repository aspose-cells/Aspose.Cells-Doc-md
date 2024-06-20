---
title: Biçim Boyacısını Kullanma
type: docs
weight: 80
url: /tr/net/aspose-cells-griddesktop/use-format-painter/
keywords: GridDesktop,format painter
description: Bu makale, GridDesktop taki biçim boyacısını tanıtıyor.
---

{{% alert color="primary" %}} 

Biçim boyacısı, MS Excel'in bir özelliğidir ve Aspose.Cells.GridDesktop'ta benimsenmiştir. Bu çok güzel bir özellik. Bu özelliği henüz kullanmamış olanlar için, biçim boyacısı, kullanıcıların odaklı olduğu herhangi bir hücrenin biçimlendirme ayarlarını başka bir hücreye uygulamalarına izin verir. Bu özelliğin uygulanması çok basittir. Bu konuda bahsedeceğiz.

{{% /alert %}} 
## **Biçim Boyacısını Kullanma**
**Biçim Boyacısı** özelliği, kullanıcıların başka hücrelere uygulamak istedikleri biçimlendirme ayarlarını seçmelerini ve ardından **GridDesktop**'ın **StartFormatPainter** yöntemini çağırmalarını gerektirir. Biçim boyacısının iki modu şunlardır:

- **Format Boyacısını Bir Kez Kullanmak**
- **Format Boyacısını Her Zaman Kullanmak**
### **Format Boyacısını Bir Kez Kullanmak**
Geliştiriciler, yalnızca bir kez bir hücreye odaklanmıştaki biçimlendirme ayarlarını tek bir hücreye uygulamak istediklerinde, bunu yapabilirler.  **StartFormatPainter** yöntemini çağırarak ve ona bir **false** değeri iletmek. Bu **false** değeri, format boyacısının sürekli boyama yapmasını engelleyecektir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **Format Boyacısını Her Zaman Kullanmak**
Format boyacısını her zaman kullanmak, birden fazla hücreye biçimlendirme ayarları uygulamamız gerektiğinde yararlı bir özelliktir. Geliştiriciler, sadece **StartFormatPainter** yöntemini çağırarak ve ona bir **true** değeri ileterek bu özelliği elde edebilirler.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


Bu tür bir format boyacısı, durdurana kadar sürekli boyama yapmaya devam eder. Bu nedenle, format boyacısını sürekli boyamaktan durdurmak için, sadece **GridDesktop**'nin **EndFormatPainter** yöntemini çağırabiliriz.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
