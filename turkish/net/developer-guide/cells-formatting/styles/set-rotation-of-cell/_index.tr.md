---
title: Cell Metni Nasıl Döndürülür
type: docs
weight: 80
url: /tr/net/how-to-rotate-text-of-cell/
description: C# kodu, Cell metnini Aspose.Cells for .NET API ile döndürmek için
keywords: c# rotate text of Cell, c# programmatically rotate text of Cell in workbook, programmatically set cell rotation angle in workbook, c# how to rotate text of Cell in excel
---
##  **Cell Metnini Aspose.Cells'de Döndür**

Aspose.Cells, geliştiricilerin Excel elektronik tablolarıyla programlı olarak çalışmasına olanak tanıyan güçlü bir .NET ve Java bileşenidir. Aspose.Cells'in sağladığı özelliklerden biri, metin yönünü özelleştirmenize ve verilerinizin görsel sunumunu iyileştirmenize olanak tanıyan hücreleri döndürme yeteneğidir. Bu belgede Aspose.Cells'i kullanarak hücreleri nasıl döndüreceğimizi inceleyeceğiz.

##  **Excel'de Cell Metni Nasıl Döndürülür**
Excel'de bir hücreyi döndürmek için aşağıdaki adımları kullanabilirsiniz:
1. Excel'i açın ve döndürmek istediğiniz hücreyi veya hücre aralığını seçin.
1. Seçilen hücrelere sağ tıklayın ve içerik menüsünden "Cells Biçimlendir" seçeneğini seçin. Alternatif olarak, Excel şeridindeki "Giriş" sekmesine gidebilir, "Cells" grubundaki "Biçim" açılır menüsüne tıklayıp "Cells'i Biçimlendir"i seçebilirsiniz.
1. "Biçim Cells" iletişim kutusunda "Hizalama" sekmesine gidin.
1. "Yönlendirme" bölümünün altında metni döndürme seçeneklerini göreceksiniz. İstediğiniz dönme açısını derece cinsinden doğrudan "Derece" kutusuna girebilirsiniz. Pozitif değerler metni saat yönünün tersine döndürür, negatif değerler ise metni saat yönünde döndürür.
<br>
![yapılacak şey:image_alt_text](alignment.png)
1. İstediğiniz rotasyonu seçtikten sonra değişiklikleri uygulamak için "Tamam"ı tıklayın. Seçilen hücre(ler) artık seçtiğiniz dönüş açısına veya yönüne göre döndürülecektir.

##  **Aspose.Cells API kullanılarak Cell Metni Nasıl Döndürülür**

[**Stil.DöndürmeAçısı**](https://reference.aspose.com/cells/net/aspose.cells/style/rotationangle/) özelliği hücreleri döndürmeyi kolaylaştırır. Aspose.Cells'deki hücreleri döndürmek için şu adımları uygulamanız gerekir:
1. Excel Çalışma Kitabını Yükle
<br>
 Öncelikle Aspose.Cells numaralı telefonu kullanarak Excel çalışma kitabını yüklemeniz gerekiyor. Mevcut bir Excel dosyasını açmak veya yeni bir dosya oluşturmak için Workbook sınıfını kullanabilirsiniz.

1. Çalışma Sayfasına Erişim
<br>
Çalışma kitabı yüklendikten sonra hücreleri döndürmek istediğiniz çalışma sayfasına erişmeniz gerekir. Çalışma sayfasına dizinine veya adına göre erişebilirsiniz.

1. Cell metnini döndür
<br>
 Artık çalışma sayfasına erişiminiz olduğuna göre, istediğiniz hücrelerin Stil nesnesini değiştirerek hücreleri döndürebilirsiniz. Stil nesnesi, döndürme dahil çeşitli biçimlendirme seçeneklerini ayarlamanıza olanak tanır.

1. Çalışma Kitabını Kaydet
<br>
Hücreleri döndürdükten sonra, değiştirilen çalışma kitabını Kaydet yöntemini kullanarak tekrar bir dosyaya veya akışa kaydedebilirsiniz.

##  **C# Örnek Kod**

Lütfen aşağıdaki koda bakın, bir çalışma kitabı nesnesi oluşturur ve birkaç hücre için farklı dönüş açıları ayarlar. Ekran görüntüsü örnek kodun yürütülmesinden sonraki sonucu gösterir.
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-rotate-text.cs" >}}
