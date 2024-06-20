---
title: Microsoft Excel Dosyası Dışa Aktar
type: docs
weight: 50
url: /tr/net/aspose-cells-gridweb/export-microsoft-excel-file/
keywords: GridWeb,dışa aktar
description: Bu makale, GridWeb de dosya nasıl dışa aktarılırı tanıtıyor.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb denetimini kullanarak web sitelerinde GUI modunda yeni Microsoft Excel dosyaları oluşturmak veya mevcut dosyaları değiştirmek mümkündür. Dosyalar daha sonra Excel dosyalarına kaydedilebilir. Aspose.Cells.GridWeb etkili bir çevrimiçi elektronik tablo düzenleyici olarak hizmet verir. Bu konu, grid içeriğinin Excel dosyalarına kaydedilmesinin nasıl yapıldığını açıklar.

{{% /alert %}} 
## **Excel Dosyalarını Dışa Aktarma**
### **Dosya Olarak Dışa Aktar**
Aspose.Cells.GridWeb denetiminin içeriğini Excel dosyası olarak kaydetmek için:

1. Aspose.Cells.GridWeb denetimini web formunuza ekleyin.
1. Çalışmanızı belirtilen bir yola Excel dosyası olarak kaydedin.
1. Uygulamayı çalıştırın.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb denetimini web formunuza nasıl ekleyeceğinizi bilmiyorsanız, [Web Formuna GridWeb Eklemek](/cells/tr/net/aspose-cells-gridweb/add-gridweb-to-web-form/) adresine bakmalısınız.

{{% /alert %}} 

Aspose.Cells.GridWeb denetimi bir windows formuna eklendiğinde, denetim otomatik olarak başlatılır ve varsayılan boyutta forma eklenir. Bir Aspose.Cells.GridWeb denetimi nesnesi oluşturmanıza gerek yoktur, yapmanız gereken tek şey denetimi sürükleyip bırakarak kullanmaktır.

Aşağıdaki kod örneği, grid içeriğini bir Excel dosyasına kaydetmenin nasıl yapıldığını açıklar.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

Dosya sisteminiz NTFS ise, ASPNET veya Herkes kullanıcı hesaplarına okuma/yazma erişimi izni verin, aksi takdirde çalışma zamanında erişim reddedildi istisnası alırsınız.

{{% /alert %}} 

Yukarıdaki kod parçası birkaç farklı şekilde kullanılabilir. Yaygın bir yol, tıklanıldığında grid içeriğini Excel dosyasına kaydeden bir düğme eklemektir. Aspose.Cells.GridWeb, görev için daha kolay bir yaklaşım sunar. Aspose.Cells.GridWeb'in SaveCommand adında bir olayı vardır. Yukarıdaki kod parçası, kullanıcıların yerleşik **Kaydet** düğmesine tıklayarak çalışmalarını kaydetmelerine olanak tanıyan SaveCommand olayının olay işleyicisine eklenebilir.

**GridWeb'in SaveCommand olayı** 

![todo:image_alt_text](export-microsoft-excel-file_1.jpg)

**GridWeb'in yerleşik Kaydet düğmesine tıklayarak grid içeriğini Excel'e kaydetme** 

![todo:image_alt_text](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

Visual Studio'da çalışıyorsanız, **Özellikler** penceresindeki olaya çift tıklayarak Kolay Kaydet olayının olay işleyicisini kolayca oluşturabilirsiniz. Bu konu hakkında daha fazla bilgi için [GridWeb Olayları ile Çalışmak](/cells/tr/net/aspose-cells-gridweb/working-with-gridweb-events/) adresine bakınız.

{{% /alert %}} 
### **Akış Olarak Dışa Aktarma**
Grid içeriğini bir akışa (örneğin MemoryStream) kaydetmek de mümkündür.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
