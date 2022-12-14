---
title: Biçim Boyacısını Kullanma
type: docs
weight: 80
url: /tr/net/using-format-painter/
---
{{% alert color="primary" %}} 

Biçim ressamı, MS Excel'in Aspose.Cells.GridDesktop'ta uyarlanmış özelliğidir. Bu çok güzel bir özellik. Henüz bu özelliği kullanmamış kişiler için, biçim ressamı, kullanıcıların herhangi bir odaklanmış hücrenin biçimlendirme ayarlarını başka bir hücreye uygulamasına olanak tanır. Bu özelliğin uygulanması çok basittir. Bu başlıkta onu da ele alacağız.

{{% /alert %}} 
## **Biçim Boyacısını Kullanma**
 özelliği**Biçim boyacısı** kullanıcıların, biçimlendirme ayarlarını diğer hücrelere uygulamak istediğiniz bir hücreyi seçmesini ve ardından aramasını gerektirir.**StartFormatPainter** yöntem**IzgaraMasaüstü**. Aşağıdaki gibi iki format ressamı modu vardır:

- **Biçim Boyacısını Bir Kez Kullanmak**
- **Format Boyacısını Her Zaman Kullanmak**
### **Biçim Boyacısını Bir Kez Kullanmak**
 Geliştiriciler, odaklanmış bir hücrenin biçimlendirme ayarlarını tek bir hücreye uygulamak için yalnızca bir kez biçim ressamı özelliğini kullanmak isterlerse, bunu çağırarak yapabilirler.**StartFormatPainter** yöntem ve geçen bir**yanlış** buna değer. Bu**yanlış** değer, format ressamının resim yapmasını sonsuza kadar yasaklayacaktır.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **Format Boyacısını Her Zaman Kullanmak**
Format ressamını kullanmak, formatlama ayarlarını birden fazla hücreye uygulamamız gerektiğinde her zaman yararlı bir özelliktir. Geliştiriciler bu özelliği yalnızca arayarak elde edebilir**StartFormatPainter** yöntem ve geçen bir**doğru** buna değer.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


 Bu tür bir format ressamı, biz onu durdurmadıkça sonsuza kadar resim yapmaya devam eder. Bu nedenle, format ressamının her zaman resim yapmasını durdurmak için basitçe arayabiliriz**EndFormatPainter** yöntemi**IzgaraMasaüstü**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
