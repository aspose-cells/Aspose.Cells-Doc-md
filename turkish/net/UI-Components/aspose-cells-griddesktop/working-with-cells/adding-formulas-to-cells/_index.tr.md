---
title: Hücreye Formül Ekleme
type: docs
weight: 30
url: /tr/net/aspose-cells-griddesktop/adding-formula-to-cell/
keywords: GridDesktop, formül
description: Bu makale, GridDesktop ta Çalışma Sayfasındaki hücreye formül eklemenin nasıl yapılacağını tanıtır.
---

{{% alert color="primary" %}} 

Bir hücre, sadece bir sayısal değer veya bazı metin gibi basit bir değer içermekle kalmaz, aynı zamanda değeri hesaplamalardan sonra belirlenecek bir formül de içerebilir. Bir hücreye bir formül uygulandığında formül kullanılır. Bu konuda, bir hücreye uygulanan bir formülü nasıl erişebileceğimizi ve değiştirebileceğimizi tartışacağız.

{{% /alert %}} 
## **Hücreye Formül Ekleme**
Hücreye formül eklemek, önceki konumuzda tartıştığımız şekilde hücrenin değerini ayarlamak gibi, yalnızca hücrelere basit değerler eklemek yerine formüller eklemektir. Geliştiriciler, bir hücrenin **Value** özelliğini kullanarak formüle erişebilir ve değiştirebilir veya aksi takdirde hücrenin **SetCellValue** metodu kullanılarak bir hücrede formül eklemek veya değiştirmek için de kullanabilir.

**ÖNEMLİ:** Bir hücrenin **Value** özelliği veya **SetCellValue** metodu kullanımı arasındaki temel fark, **Value** özelliğinin otomatik olarak Grid'in tüm formüllerinin değerlerini yeniden hesaplamak için **RunAllFormulas** metodunu çağırmasıdır. **SetCellValue** metodunu kullandığımızda geliştiricilerin formülleri ekledikten sonra **RunAllFormulas** metodu çağırması gerekli değildir. Aslında, bir çalışma sayfasındaki birçok formül eklemek istiyorsanız, formülleri ekledikten sonra sadece bir kez **RunAllFormulas** metodu çağırabilirsiniz.

Bir formül, bir dize değeri olarak bir hücreye eklenir. Ayrıca, formül yapısı MS Excel'deki formül yapısıyla uyumlu olmalıdır. Tüm formüllerin bir **Eşitlik İşareti (=)** ile başlaması gerekir.

Aşağıdaki örnekte, çalışma sayfasındaki iki hücrenin değerlerini çarparak sonucu başka bir hücrede saklayan bir formül ekledik. Son olarak **RunAllFormulas** metodu da çağrılmıştır.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



Şimdi uygulamayı çalıştırın. Formül eklenen hücreye çift tıkladığınızda, değerin aslında arka planda hesaplama yapan formülle değiştirildiğini fark edeceksiniz.

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop MS Excel'in yaygın olarak kullanılan çoğu işlevini destekler. Desteklenen işlevlerin listesi hakkında daha fazla bilgi için lütfen [buraya tıklayın.](/cells/tr/net/list-of-supported-functions/)

{{% /alert %}}
