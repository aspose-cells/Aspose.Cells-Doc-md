---  
title: Hücrenin metnini Nasıl Döndürülür
linktitle: Hücrenin metnini Nasıl Döndürülür  
type: docs  
weight: 80  
url: /tr/nodejs-cpp/how-to-rotate-text-of-cell/  
description: Bir hücrenin metnini programatik olarak döndürmeyi öğrenin Aspose.Cells for Node.js via C++ kullanarak.  
keywords: Node.js hücre metnini döndürmek, hücreyi programatik olarak döndürmek, çalışma kitabında hücre dönüşü açısını ayarlamak, Node.js hücre metnini döndürmek nasıl?  
---  

## **Hücre Metnini Döndürmek Aspose.Cells for Node.js via C++ ile**

Aspose.Cells, geliştiricilerin Excel elektronik tablolarıyla programatik olarak çalışmasına imkan tanıyan güçlü bir Node.js bileşenidir. Aspose.Cells’in sunduğu özelliklerden biri hücreleri döndürme yeteneğidir, böylece metnin yönünü özelleştirebilir ve görsel sunumu geliştirebilirsiniz. Bu belgede, Aspose.Cells kullanarak hücreleri nasıl döndürürüz gösterilecektir.

## **Excel'de Hücrenin Metnini Döndürme**
Bir hücreyi Excel'de döndürmek için aşağıdaki adımları kullanabilirsiniz:
1. Excel'i açın ve döndürmek istediğiniz hücreyi veya hücre aralığını seçin.
1. Seçilen hücre(ler)e sağ tıklayın ve bağlam menüsünden "Hücreleri Biçimlendir"'i seçin. Alternatif olarak, Excel şeridinde "Ana Sayfa" sekmesine gidip "Hücreler" grubundaki "Biçimlamanın" açılır menüsüne tıklayıp "Hücreleri Biçimlendir"'i seçebilirsiniz.
1. "Hücreleri Biçimlendir" iletişim kutusunda, "Hizalama" sekmesine gidin.
1. "Yönlendirme" bölümünde, metni döndürebileceğiniz seçenekleri göreceksiniz. "Derece" kutusuna istenen dönme açısını doğrudan girebilirsiniz. Pozitif değerler metni saat yönünün tersine döndürür, negatif değerler ise saat yönünde döndürür.
<br>
![todo:image_alt_text](alignment.png)
1. İstenilen yönlendirmeyi seçtikten sonra, değişiklikleri uygulamak için "Tamam"'a tıklayın. Seçilen hücre(ler) artık seçtiğiniz dönme açısına veya yönlendirmeye göre dönecektir.

## **Aspose.Cells API kullanarak Hücrenin Metnini Döndürme**

[**Style.setRotationAngle(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-) özelliği hücreleri döndürmeyi kolaylaştırır. Aspose.Cells'te hücreleri döndürmek için şu adımları izlemeniz gerekir:
1. Excel Çalışma Kitabını Yükle  
<br>
İlk olarak, mevcut bir Excel dosyasını açmak veya yeni bir tane oluşturmak için Workbook sınıfını kullanarak Excel çalışma kitabını yüklemeniz gerekir. 

1. Çalışma Sayfasına Eriş  
<br>
Çalışma kitabı yüklendikten sonra, hücreleri döndürmek istediğiniz çalışma sayfasına erişmeniz gerekir. Çalışma sayfasına endeksine veya adına göre erişebilirsiniz. 

1. Hücrenin metnini döndür  
<br>
Artık çalışma sayfasına erişiminiz olduğuna göre, istenen hücrelerin Stil objesini değiştirerek hücreleri döndürebilirsiniz. Stil objesi, dönme dahil çeşitli biçimlendirme seçeneklerini belirlemenizi sağlar. 

1. Çalışma Kitabını Kaydet  
<br>
Hücreleri döndürdükten sonra, değiştirilmiş çalışma kitabını Save metodunu kullanarak bir dosyaya veya akıma geri kaydedebilirsiniz.

## **Node.js Örnek Kodu**

Aşağıdaki kodu inceleyin, bir çalışma kitabı nesnesi oluşturur ve birkaç hücre için farklı dönüş açıları ayarlar. Ekran görüntüsü, örnek kodun çalıştırılmasının ardından sonucu gösterir.
<br>
<img src="rotation.png" width=80% />

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-SetRotationOfCell.js" >}}


