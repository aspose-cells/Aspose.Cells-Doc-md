---
title: Microsoft Excel Dosyasını Dışa Aktar
type: docs
weight: 50
url: /tr/net/export-microsoft-excel-file/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb kontrolü kullanılarak GUI modundaki web sitelerinde yeni Microsoft Excel dosyaları oluşturmak veya mevcut Microsoft Excel dosyalarını değiştirmek mümkündür. Dosyalar daha sonra Excel dosyalarına kaydedilebilir. Aspose.Cells.GridWeb, etkin bir çevrimiçi hesap tablosu düzenleyicisi olarak hizmet verir. Bu konuda kılavuz içeriğinin Excel dosyalarına nasıl kaydedileceği açıklanmaktadır.

{{% /alert %}} 
## **Excel Dosyalarını Dışa Aktarma**
### **Dosya Olarak Dışa Aktar**
Aspose.Cells.GridWeb kontrolünün içeriğini bir Excel dosyası olarak kaydetmek için:

1. Aspose.Cells.GridWeb denetimini web formunuza ekleyin.
1. Çalışmanızı belirtilen bir yolda bir Excel dosyası olarak kaydedin.
1. Uygulamayı çalıştırın.

{{% alert color="primary" %}} 

 Web formunuza Aspose.Cells.GridWeb kontrolünü nasıl ekleyeceğinizi bilmiyorsanız, o zaman başvurmalısınız.[GridWeb'i Web Formuna Ekleme](/cells/tr/net/add-gridweb-to-web-form/)

{{% /alert %}} 

Windows formuna Aspose.Cells.GridWeb denetimi eklendiğinde, denetim otomatik olarak başlatılır ve forma varsayılan boyutta eklenir. Aspose.Cells.GridWeb kontrol nesnesi oluşturmanıza gerek yok, tek yapmanız gereken kontrolü sürükleyip bırakmak ve kullanmaya başlamak.

Aşağıdaki kod örneği, ızgara içeriğinin bir Excel dosyasına nasıl kaydedileceğini gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

Dosya sisteminiz NTFS ise, ASPNET veya Herkes kullanıcı hesaplarına okuma/yazma erişimi verin, aksi takdirde çalışma zamanında erişim engellendi istisnası alırsınız.

{{% /alert %}} 

Yukarıdaki kod parçacığı birkaç şekilde kullanılabilir. Yaygın bir yol, tıklandığında ızgara içeriğini bir Excel dosyasına kaydeden bir düğme eklemektir. Aspose.Cells.GridWeb görev için daha kolay bir yaklaşım sunar. Aspose.Cells.GridWeb'de SaveCommand adında bir olay var. Yukarıdaki kod parçacığı, SaveCommand olayının olay işleyicisine eklenebilir ve bu, kullanıcıların Aspose.Cells.GridWeb'in dahili**Kaydetmek** buton.

**GridWeb'in SaveCommand olayı** 

![yapılacaklar:resim_alternatif_Metin](export-microsoft-excel-file_1.jpg)

**GridWeb'in yerleşik Kaydet düğmesini tıklatarak kılavuz içeriğini Excel'e kaydetme** 

![yapılacaklar:resim_alternatif_Metin](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

 Visual Studio'da çalışıyorsanız, SaveCommand olayının olay işleyicisini, olaya çift tıklayarak kolayca oluşturabilirsiniz.**Özellikleri** bölmesi. Bu konuda daha fazla bilgi edinmek için lütfen bkz.[GridWeb Events ile Çalışma](/cells/tr/net/working-with-gridweb-events/)

{{% /alert %}} 
### **Akış Olarak Dışa Aktar**
Izgara içeriğini bir akışa (örneğin, MemoryStream) kaydetmek de mümkündür.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
