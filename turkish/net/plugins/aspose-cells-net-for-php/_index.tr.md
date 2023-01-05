---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /tr/net/aspose-cells-net-for-php/
---
## **Başlarken**

### **Giriş**

### **Sistem Gereksinimleri ve Desteklenen Platformlar**

#### **sistem gereksinimleri**

**Aspose.Cells .NET for PHP'i kullanmak için sistem gereksinimleri aşağıdadır:**

- PHP ve PHP Manager yüklü IIS.
- Aspose.Total API'ler.
- Aspose.Cells Interop dll ve tlb dosyası.

#### **Desteklenen Platformlar**

**Desteklenen platformlar aşağıdadır:**

- PHP 5.3 veya üstü
- Windows işletim sistemi

### **İndirin ve Yapılandırın**

#### **Gerekli Kitaplıkları İndirin**

Aşağıda belirtilen gerekli kütüphaneleri indirin. Bunlar Aspose.Cells Java for PHP örneklerini çalıştırmak için gereklidir.

- [İndirme bölümünden Aspose.Cells for .NET (DLL veya MSI) dosyalarını indirin](https://downloads.aspose.com/cells/net)
- [Aspose.Cells for .NET birlikte çalışma dll dosyasını indirin](https://downloads.aspose.com/cells/net)

MSI sürümünü indirirseniz, Aspose.Cells.dll dosyasını varsayılan olarak C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0 klasöründe bulacaksınız.
Ancak, DLL sürümünü indirdiyseniz, ayıklayabilir ve daha sonra kullanım kolaylığı için .NET 2.0 klasöründen Aspose.Cells.dll dosyasını c:\temp klasörünüze kopyalayabilirsiniz.
Benzer şekilde birlikte çalışma zip dosyasını çıkarın ve Aspose.Inteop.dll dosyasını c:\temp konumuna kopyalayın

#### **Sosyal Kodlama Sitelerinden Örnekler İndirin**

Çalışan örneklerin aşağıdaki yayınları, aşağıda belirtilen sosyal kodlama sitelerinden indirilebilir:

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP Örnekler**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Windows Platformunda kaynak kodu nasıl yapılandırılır**

Kullanırken kaynak kodunu açmak ve genişletmek için lütfen şu basit adımları izleyin:

##### **1. Hem dll hem de interop.dll dosyalarını kaydedin, örneğin Aspose.Cells.dll ve Aspose.Cells.Interop.dll.**

{{< highlight "java" >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. PHP'de COM ve DOTNET Uzantılarını etkinleştirin.**

IIS'de PHP Yöneticisi'ni açın ve ardından 'Devre Dışı Bırakma ve Uzantıyı Etkinleştir' seçeneğini tıklayın. php'yi bul_iletişim_dotnet.dll ve etkinleştirildiğinden emin olun.

##### **3. Yapılandırma Aspose.Cells .NET for PHP Örnekler**

###### **Yöntem 1**

 Klon PHP Örnekleri[github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
ve aşağıdaki komutu çalıştırın

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

###### **Yöntem 2**

PHP Projenizin besteci.json dosyasına aşağıdaki satırları ekleyin

{{< highlight "java" >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

ve kurulum komutunu çalıştırın

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

 Besteci ziyareti hakkında okumak için<https://getcomposer.org/>

### **Destek Genişletin ve Katkıda Bulunun**

#### **Destek olmak**

Aspose'in ilk günlerinden itibaren müşterilerimize sadece iyi ürünler vermenin yeterli olmayacağını biliyorduk. Ayrıca iyi hizmet vermemiz gerekiyordu. Biz de geliştiriciyiz ve teknik bir sorun veya yazılımdaki bir tuhaflık, yapmanız gerekeni yapmanızı engellediğinde bunun ne kadar sinir bozucu olduğunu anlıyoruz. Sorunları çözmek için buradayız, onları yaratmak için değil.

Bu nedenle ücretsiz destek sunuyoruz. İster satın almış olsun ister bir değerlendirme yapıyor olsun, ürünümüzü kullanan herkes, tüm dikkatimizi ve saygımızı hak ediyor.

Aspose.Cells .NET for PHP ile ilgili sorun ve önerilerinizi aşağıdaki platformlardan herhangi birini kullanarak kaydedebilirsiniz:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Genişletin ve Katkıda Bulunun**

Aspose.Cells .NET for PHP açık kaynaktır ve kaynak kodu aşağıda listelenen başlıca sosyal kodlama web sitelerinde mevcuttur. Geliştiricilerin kaynak kodunu indirmeleri ve yeni özellikler önererek veya ekleyerek veya mevcut olanları geliştirerek katkıda bulunmaları teşvik edilir, böylece diğerleri de bundan faydalanabilir.

#### **Kaynak kodu**

En son kaynak kodunu aşağıdaki konumlardan birinden alabilirsiniz.

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Örnek Kod Örnekleri**

Bu bölüm aşağıdaki konuları içerir

- [PHP Programcılar Kılavuzu](/cells/tr/net/php-programmers-guide/)
  - [PHP'de Dosyalarla Çalışmak](/cells/tr/net/working-with-files-in-php/)
    - [PHP'de Dosya İşleme Özellikleri](/cells/tr/net/file-handling-features-in-php/)
      - [Dosyaları PHP'de Açmak](/cells/tr/net/opening-files-in-php/)
      - [PHP'de Dosyaları Kaydetmek](/cells/tr/net/saving-files-in-php/)
    - [PHP'deki Yardımcı Program Özellikleri](/cells/tr/net/utility-features-in-php/)
      - [PHP'de Dosyaları Şifrelemek](/cells/tr/net/encrypting-files-in-php/)
      - [PHP'de Excel'den PDF'e Dönüştürme](/cells/tr/net/excel-to-pdf-conversion-in-php/)
      - [PHP'de Belge Özelliklerini Yönetme](/cells/tr/net/managing-document-properties-in-php/)
      - [PHP'de Çalışma Sayfasından Görüntüye Dönüştürme](/cells/tr/net/worksheet-to-image-conversion-in-php/)
  - [PHP'de Formüllerle Çalışmak](/cells/tr/net/working-with-formulas-in-php/)
    - [PHP'de Formülleri Hesaplamak](/cells/tr/net/calculating-formulas-in-php/)
  - [PHP'de Çalışma Sayfalarıyla Çalışmak](/cells/tr/net/working-with-worksheets-in-php/)
    - [PHP'de Yönetim Özellikleri](/cells/tr/net/management-features-in-php/)
      - [PHP'de Çalışma Sayfalarını Yönetme](/cells/tr/net/managing-worksheets-in-php/)
        - [PHP'de Mevcut Excel Dosyasına Çalışma Sayfaları Ekleme](/cells/tr/net/add-worksheets-to-existing-excel-file-in-php/)
        - [PHP'de Yeni Excel Dosyasına Çalışma Sayfaları Ekleme](/cells/tr/net/add-worksheets-to-new-excel-file-in-php/)
        - [PHP'de Sayfa Dizini Kullanarak Çalışma Sayfalarını Kaldırma](/cells/tr/net/removing-worksheets-using-sheet-index-in-php/)
        - [PHP'de Sayfa Adını Kullanarak Çalışma Sayfalarını Kaldırma](/cells/tr/net/removing-worksheets-using-sheet-name-in-php/)
