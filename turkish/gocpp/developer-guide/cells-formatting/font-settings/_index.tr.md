---
title: Font Ayarlarıyla Golang ve C++ kullanan
linktitle: Font Ayarları
type: docs
weight: 30
url: /tr/go-cpp/cells-font-settings/
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışma konusunda C++ için bir kütüphanedir. Hücrelerin yazı tipi ayarlarını destekler, kullanıcıların hücrelerin yazı tipi stilini ve özelliklerini özelleştirmelerine olanak tanır. Bu makale, Aspose.Cells kütüphanesini kullanarak hücre yazı tipi ayarlarını nasıl yapacağınızı tanıtacaktır.
keywords: Aspose.Cells, Hücreler, Font Ayarları, Stilleri, Özellikleri
---

{{% alert color="primary" %}}

Bir metnin görünüm ve hissi, yazı tipi ayarlarını değiştirerek kontrol edilebilir. Yazı tipi ayarları, isim, stil, boyut, renk ve diğer efektleri içerebilir. Microsoft Excel gibi, Aspose.Cells da hücrelerin yazı tipi ayarlarını yapılandırmayı destekler.

{{% /alert %}}

## **Font Ayarlarını Yapılandırma**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, bir Microsoft Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı bir [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonu sağlar. [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının bir nesnesini temsil eder.

Aspose.Cells, [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) sınıfının [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) ve [**SetStyle**](https://reference.aspose.com/cells/go-cpp/cell/setstyle/) yöntemlerini sağlar; bu yöntemler bir hücrenin biçimlendirme stiline getirilip alınmasında kullanılır. [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) sınıfı, font ayarlarını yapılandırmak için özellikler sağlar.

### **Yazı Tipi Adını Ayarlama**

Geliştiriciler, [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) objesinin [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) özelliğini kullanarak herhangi bir yazı tipini hücre içindeki metne uygulayabilir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings.go" >}}
### **Yazı Tipi Stilini Kalın Yapma**

Geliştiriciler, metni kalın yapmak için [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) nesnesinin [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) özelliğini **true** olarak ayarlayarak yapabilirler.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-1.go" >}}
### **Yazı Tipi Boyutunu Ayarlama**

[**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) nesnesinin [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/) özelliği ile yazı tipi boyutunu ayarlayın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-2.go" >}}
### **Yazı Tipi Rengini Ayarlama**

Yazı tipi rengini ayarlamak için [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) objesinin [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) özelliğini kullanın. C++ çerçevesinin bir parçası olan Renk enumerasyonundan herhangi bir renk seçin ve [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) özelliğine atayın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-3.go" >}}
### **Yazı Tipi Altı Çizgi Türünü Ayarlama**

[**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) nesnesinin [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) özelliğini kullanarak metni altı çizili yapın. Aspose.Cells, [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/) numaralandırmasında çeşitli önceden tanımlanmış yazı tipi altı çizgi tipleri sunar.

|**Yazı Tipi Altı Çizgi Tipleri**|**Açıklama**|
| :- | :- |
|Accounting|Tek hesap çizgisi|
|Double|Çift çizgi|
|DoubleAccounting|Çift hesap çizgisi|
|None|Çizgi yok|
|Single|Tek çizgi|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-4.go" >}}
### **Üstü Çizili Etkiyi Ayarlama**

Üstü çizili uygulamak için [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) nesnesinin [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) özelliğini **true** olarak ayarlayın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-5.go" >}}
### **Üst Simge Etkisini Ayarlama**

Abone simgesini ayarlayarak [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) nesnesinin [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) özelliğini **true** olarak ayarlayın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-6.go" >}}
### **Yazı Tipi Üzerine Üst Simge Efekti Ayarlama**

Geliştiriciler, yazı tipi üzerine üst simge efektini [**IsSuperscript**](https://reference.aspose.com/cells/go-cpp/font/issuperscript/) öğesinin [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) özelliğini **true** olarak ayarlayarak uygulayabilirler.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-7.go" >}}
## **Gelişmiş Konular**
- [Yazı Tipi Üzerine Üst Simge ve Abone Etkileri Uygulama](/cells/tr/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Bir Elektronik Tablo veya Çalışma Kitabında Kullanılan Yazı Tiplerinin Listesini Alın](/cells/tr/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
