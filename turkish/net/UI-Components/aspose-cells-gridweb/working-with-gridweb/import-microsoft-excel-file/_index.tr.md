---
title: Microsoft Excel Dosyasını İçe Aktar
type: docs
weight: 40
url: /tr/net/import-microsoft-excel-file/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop, Aspose.Cells.GridWeb kontrolü gibi, Microsoft Excel dosyalarını - veriler, biçimlendirme, grafikler, resimler vb. ile birlikte - ancak web uygulamalarında açabilir ve yükleyebilir. Bu konu nasıl yapılacağını açıklar.

{{% /alert %}} 
## **Excel Dosyalarını İçe Aktar**
### **Dosyadan İçe Aktar**
Aspose.Cells.GridWeb kontrolünü kullanarak bir Excel dosyasını açmak için:

1. Aspose.Cells.GridWeb denetimini bir web formuna ekleyin.
1. Dosya yolunu belirterek Excel dosyasını içe aktarın.
1. Uygulamayı çalıştırın.

{{% alert color="primary" %}} 

 Denetimi bir web formuna nasıl ekleyeceğinizi bilmiyorsanız, bkz.[GridWeb'i Web Formuna Ekleme](/cells/tr/net/add-gridweb-to-web-form/).

{{% /alert %}} 

Bir web formuna Aspose.Cells.GridWeb kontrolü eklendiğinde, kontrol otomatik olarak başlatılır ve forma varsayılan bir boyutta eklenir. Aspose.Cells.GridWeb kontrol nesnesi oluşturmanıza gerek yok, tek yapmanız gereken kontrolü sürükleyip bırakmak ve kullanmaya başlamak.

Ancak, içeriği bir Excel dosyasından Aspose.Cells.GridWeb denetimine yüklemek için, Excel dosyasının yolunu belirtmek üzere ImportExcelFile yöntemini çağırmanız gerekir. Bundan sonra, Aspose.Cells.GridWeb kontrolü dosyayı belirtilen yoldan otomatik olarak bulur ve içeriğini görüntüler. Bir Excel dosyasının içeriğini yükleyen bir kod parçacığı aşağıda verilmiştir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


Yukarıdaki kod parçasını istediğiniz gibi kullanabilirsiniz. Örneğin, bir web formu yüklendiğinde Excel dosyasını otomatik olarak yüklemek için bu kodu formun Page_Load olayına ekleyin. Bir butona tıklandığında dosyanın açılmasını istiyorsanız web formuna bir buton ekleyin ve butonun Click olayının altına yukarıdaki kodu yazın.

**Bir düğmeye tıklandığında bir Excel dosyası yüklenir** 

![yapılacaklar:resim_alternatif_Metin](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

Dosya sisteminiz NTFS ise, ASPNET veya Herkes kullanıcı hesaplarına okuma erişimi izni vermelisiniz, aksi takdirde çalışma zamanında erişim engellendi istisnası alırsınız.

{{% /alert %}} 
### **Akıştan İçe Aktar**
Aspose.Cells.GridWeb denetimi, Excel dosyalarını dosyadan açmanın yanı sıra Excel dosyalarını bir akıştan yükleyebilir. Dosyayı bir akış olarak kullanmak, her türlü dosya erişimini veya paylaşım ihlali sorunlarını engellemek için daha iyi bir yaklaşımdır çünkü bu yaklaşım, akışı kapatarak dosyalara olan tüm bağlantıların kapatılmasını sağlar.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
