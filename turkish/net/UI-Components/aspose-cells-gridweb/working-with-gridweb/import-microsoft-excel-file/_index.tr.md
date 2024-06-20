---
title: Microsoft Excel Dosyası İçe Aktar
type: docs
weight: 40
url: /tr/net/aspose-cells-gridweb/import-microsoft-excel-file/
keywords: GridWeb, içe aktar
description: Bu makale, GridWeb de dosya içe aktarmanın nasıl yapılacağını tanıtır.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop gibi, Aspose.Cells.GridWeb kontrolü, web uygulamalarında Microsoft Excel dosyalarını - veri, biçimlendirme, grafikler, görüntüler vb. ile birlikte - açabilir ve yükleyebilir. Bu konu nasıl açıklar.

{{% /alert %}} 
## **Excel Dosyalarını İçe Aktar**
### **Dosyadan İçe Aktar**
Aspose.Cells.GridWeb kontrolünü kullanarak bir Excel dosyasını açmak için:

1. Aspose.Cells.GridWeb kontrolünü bir web formuna ekleyin.
1. Dosya yolunu belirterek Excel dosyasını içe aktarın.
1. Uygulamayı çalıştırın.

{{% alert color="primary" %}} 

Kontrolü bir web formuna nasıl ekleyeceğinizi bilmiyorsanız, [Web Formuna GridWeb Ekle](/cells/tr/net/aspose-cells-gridweb/add-gridweb-to-web-form/) sayfasına bakın.

{{% /alert %}} 

Aspose.Cells.GridWeb kontrolü bir web formuna eklendiğinde, kontrol otomatik olarak oluşturulur ve varsayılan boyutta forma eklenir. Aspose.Cells.GridWeb kontrol nesnesi oluşturmanıza gerek yoktur, yapmanız gereken tek şey kontrolü sürükleyip bırakmak ve kullanmaya başlamaktır.

Ancak, bir Excel dosyasından içeriği Aspose.Cells.GridWeb kontrolüne yüklemek için, ImportExcelFile yöntemini çağırarak Excel dosyasının yolunu belirtmeniz gerekir. Bundan sonra, Aspose.Cells.GridWeb kontrolü belirtilen yoldan dosyayı otomatik olarak bulacak ve içeriğini görüntüleyecektir. Bir Excel dosyasının içeriğini yükleyen bir kod parçası aşağıda verilmiştir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


Yukarıdaki kod parçası istediğiniz herhangi bir şekilde kullanılabilir. Örneğin, bir web form yüklendiğinde otomatik olarak bir Excel dosyası yüklemek için, bu kodu formun Page_Load olayına ekleyin. Bir dosyayı bir düğmeye tıklandığında açmak istiyorsanız, bir düğme ekleyin ve kodu düğmeye tıklandığında etkinliğinin altına yazın.

**Bir düğmeye tıklandığında Excel dosyası yüklenir** 

![todo:image_alt_text](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

Dosya sisteminiz NTFS ise, ASPNET veya Herkes kullanıcı hesaplarına okuma erişim izni vermelisiniz veya çalışma zamanında erişim reddedildi istisnası alırsınız.

{{% /alert %}} 
### **Akıştan Al**
Aspose.Cells.GridWeb kontrolü dosyadan Excel dosyalarını açmanın yanı sıra akıştan da Excel dosyalarını yükleyebilir. Bir dosyayı akış olarak kullanmak, dosyaya erişim veya paylaşım ihlali sorunlarını engellemek için daha iyi bir yaklaşımdır çünkü bu yaklaşım, akışı kapatarak dosyalara olan tüm bağlantıları kapatmayı garanti altına alır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
