---  
title: Node.js ile C++ kullanımıyla Font Ayarları  
linktitle: Font Ayarları  
description: Aspose.Cells, hücrelerin yazı tipi ayarlarını yapılandırmanıza imkan tanıyan, hücre stilleri ve özellikleriyle çalışmaya uygun bir Node.js kütüphanesidir. Bu makale, Aspose.Cells kütüphanesini kullanarak hücre font ayarlarının nasıl yapılacağını tanıtacaktır.  
keywords: Aspose.Cells, Cells, Yazı Tipi Ayarları, Stiller, Özellikler, Node.js C++ ile  
type: docs  
weight: 30  
url: /tr/nodejs-cpp/cells-font-settings/  
---  

{{% alert color="primary" %}}  
Bir metnin görünümü, font ayarlarını değiştirerek kontrol edilebilir. Font ayarları, yazı tiplerinin adı, stili, boyutu, rengi ve diğer efektlerini içerebilir. Microsoft Excel gibi, Aspose.Cells de hücrelerin font ayarlarını yapılandırmayı destekler.  
{{% /alert %}}  

## **Font Ayarlarını Yapılandırma**  

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sunar; bu, bir Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, her sayfaya erişimi sağlayan [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir sayfa, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ise, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonunu sağlar. [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfı nesnesini temsil eder.  

Aspose.Cells, [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) ve [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) metodlarını sağlar; bunlar, hücrenin biçimlendirme stilini almak ve ayarlamak içindir. [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) sınıfı ise, font ayarlarını yapılandırmak için özellikler sağlar.  

### **Yazı Tipi Adını Ayarlama**  

Geliştiriciler, herhangi bir fontu hücre içeriğine uygulamak için [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) nesnesinin [setName](https://reference.aspose.com/cells/nodejs-cpp/font/#setName-string-) metodunu kullanabilir.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontName.js" >}}


### **Yazı Tipi Stilini Kalın Yapma**  

Geliştiriciler, [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) nesnesinin [**setIsBold**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsBold-boolean-) metodunu **true** olarak ayarlayarak metni kalın yapabilir.   

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetBoldStyle.js" >}}



### **Yazı Tipi Boyutunu Ayarlama**  

Yazı tipi boyutunu [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) nesnesinin [**setSize**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSize-number-) metoduyla ayarlayın.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontSize.js" >}}


### **Yazı Tipi Rengini Ayarlama**  

Yazı tipi rengini [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) nesnesinin [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-) metodunu kullanarak ayarlayın. Renkleri, Node.js'in bir parçası olan Renk enumundan herhangi biriyle seçin ve [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-) metoduna atayın.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontColor.js" >}}


### **Yazı Tipi Altı Çizgi Türünü Ayarlama**  

[**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) nesnesinin [**setUnderline**](https://reference.aspose.com/cells/nodejs-cpp/font/#setUnderline-fontunderlinetype-) metodunu kullanarak metni altına çizin. Aspose.Cells, [**FontUnderlineType**](https://reference.aspose.com/cells/nodejs-cpp/fontunderlinetype) enumeration'unda çeşitli önceden tanımlanmış yazı tipi alt çizgi türleri sunar.  

|**Yazı Tipi Altı Çizgi Tipleri**|**Açıklama**|  
| :- | :- |  
|Accounting|Tek hesap çizgisi|  
|Double|Çift çizgi|  
|DoubleAccounting|Çift hesap çizgisi|  
|None|Çizgi yok|  
|Single|Tek çizgi|  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontUnderline.js" >}}


### **Üstü Çizili Etkiyi Ayarlama**  

 [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) nesnesinin [**setIsStrikeout**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsStrikeout-boolean-) metodunu **true** olarak ayarlayarak çizili uygula.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}


### **Üst Simge Etkisini Ayarlama**  

 [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) nesnesinin [**setIsSubscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSubscript-boolean-) metodunu **true** olarak ayarlayarak alt simge uygula.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}



### **Yazı Tipi Üzerine Üst Simge Efekti Ayarlama**  

Geliştiriciler, [**setIsSuperscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSuperscript-boolean-) yöntemini [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) nesnesi üzerinde **true** olarak ayarlayarak üst simge efektini uygulayabilir.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetSuperscript.js" >}}


## **Gelişmiş Konular**  
- [Yazı Tipi Üzerine Üst Simge ve Abone Etkileri Uygulama](/cells/tr/nodejs-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [Bir Elektronik Tablo veya Çalışma Kitabında Kullanılan Yazı Tiplerinin Listesini Alın](/cells/tr/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)  


