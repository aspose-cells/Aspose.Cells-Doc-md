---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /tr/net/aspose-cells-net-for-php/
---

## **Başlarken**

### **Giriş**

### **Sistem Gereksinimleri ve Desteklenen Platformlar**

#### **Sistem Gereksinimleri**

**Aspose.Cells .NET'i PHP için kullanmak için aşağıdaki sistem gereksinimleri bulunmaktadır:**

- PHP ve PHP Yöneticisi yüklü IIS.
- Aspose.Total APIs.
- Aspose.Cells, Interop dll ve tlb dosyası.

#### **Desteklenen Platformlar**

**Aşağıdakiler desteklenen platformlardır:**

- PHP 5.3 veya üzeri
- Windows işletim sistemi

### **İndirme ve Yapılandırma**

#### **Gerekli Kütüphaneleri İndirme**

Aşağıda belirtilen gerekli kütüphaneleri indirin. Bu, Aspose.Cells Java for PHP örneklerini yürütmek için gereklidir.

- [İndirme Bölümünden Aspose.Cells for .NET (DLL veya MSI) dosyalarını indirin](https://downloads.aspose.com/cells/net)
- [Aspose.Cells for .NET interop dll 'yi indirin](https://downloads.aspose.com/cells/net)

Eğer MSI sürümünü indirirseniz, varsayılan olarak C:\Program Dosyaları (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0 klasöründe bulunan Aspose.Cells.dll dosyasını bulacaksınız.
Ancak DLL sürümünü indirdiyseniz, onu çıkarabilir ve ardından Aspose.Cells.dll dosyasını .NET 2.0 klasöründen c:\temp klasörünüze kolaylıkla kopyalayabilirsiniz.
Benzer şekilde, interop zip dosyasını çıkarın ve Aspose.Inteop.dll dosyasını c:\temp 'e kopyalayın

#### **Sosyal Kodlama Sitelerinden Örnekleri İndirme**

Aşağıda belirtilen sosyal kodlama sitelerinde çalıştırılan örneklerin indirilebilir sürümleri bulunmaktadır:

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP Examples**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Windows Platformunda kaynak kodunun yapılandırılması**

Kullanırken kaynak kodunu açmak ve genişletmek için lütfen aşağıdaki basit adımları izleyin:

##### **1. Örneğin Aspose.Cells.dll ve Aspose.Cells.Interop.dll dosyalarını kaydedin.**

{{< highlight java >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. PHP'de COM ve DOTNET uzantılarını etkinleştirin.**

IIS'de PHP Yöneticisini açın ve ardından 'Uzantı'yı Etkinleştir'e tıklayın. php_com_dotnet.dll 'yi bulun ve etkin olduğundan emin olun.

##### **3. Aspose.Cells .NET for PHP Örneklerini Yapılandırma**

###### **Yöntem 1**

[github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP) 'den PHP örneklerini klonlayın
ve aşağıdaki komutu çalıştırın

{{< highlight java >}}

 composer install

{{< /highlight >}}

###### **Yöntem 2**

PHP Projesinin composer.json dosyasına aşağıdaki satırları ekleyin

{{< highlight java >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

ve kurulum komutunu çalıştırın

{{< highlight java >}}

 composer install

{{< /highlight >}}

To read about composer visit <https://getcomposer.org/>

### **Destek Uzat ve Katkıda Bulun**

#### **Destek**

Aspose'un ilk günlerinden itibaren, müşterilerimize sadece iyi ürünler sunmanın yeterli olmayacağını biliyorduk. Ayrıca iyi bir hizmet sunmamız gerekiyordu. Kendi geliştiricileri olduğumuz için, teknik bir sorun veya yazılımdaki bir tuhaflık sizi yapmanız gereken şeyden alıkoyduğunda ne kadar sinir bozucu olduğunu anlıyoruz. Sorunları çözmek için buradayız, onları yaratmak için değil.

Bu nedenle ücretsiz destek sunuyoruz. Ürünlerimizi kullanan herkes, bunları satın almış olsun veya değerlendirme yapılıyor olsun, tam dikket ve saygıyı hak ediyor.

Aspose.Cells .NET for PHP ile ilgili herhangi bir sorunu veya öneriyi aşağıdaki platformlardan birini kullanarak bildirebilirsiniz:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Genişletme ve Katkı Sağlama**

Aspose.Cells .NET for PHP açık kaynaklıdır ve kaynak kodu aşağıda listelenen ana sosyal kodlama sitelerinde mevcuttur. Geliştiriciler, kaynak kodunu indirerek yeni özellikler önererek veya ekleyerek veya mevcut olanları iyileştirerek katkıda bulunmaya teşvik edilir, böylece diğerlerinin de bundan faydalanabilmesi sağlanır.

#### **Kaynak Kodu**

En son kaynak kodunu aşağıdaki konumlardan birinden edinebilirsiniz

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Örnek Kod Örnekleri**

Bu bölüm aşağıdaki konuları içerir

- [PHP Programcı Kılavuzu](/cells/tr/net/php-programmers-guide/)
  - [PHP'de Dosyalarla Çalışma](/cells/tr/net/working-with-files-in-php/)
    - [PHP'de Dosya İşleme Özellikleri](/cells/tr/net/file-handling-features-in-php/)
      - [PHP'de Dosyaları Açma](/cells/tr/net/opening-files-in-php/)
      - [PHP'de Dosyaları Kaydetme](/cells/tr/net/saving-files-in-php/)
    - [PHP'de Yardımcı Özellikler](/cells/tr/net/utility-features-in-php/)
      - [PHP'de Dosyaları Şifreleme](/cells/tr/net/encrypting-files-in-php/)
      - [PHP'de Excel'den PDF'ye Dönüştürme](/cells/tr/net/excel-to-pdf-conversion-in-php/)
      - [PHP'de Belge Özelliklerini Yönetme](/cells/tr/net/managing-document-properties-in-php/)
      - [PHP'de Çalışma Sayfasını Resme Dönüştürme](/cells/tr/net/worksheet-to-image-conversion-in-php/)
  - [PHP'de Formüllerle Çalışma](/cells/tr/net/working-with-formulas-in-php/)
    - [PHP'de Formülleri Hesaplama](/cells/tr/net/calculating-formulas-in-php/)
  - [PHP'de Çalışma Sayfalarıyla Çalışma](/cells/tr/net/working-with-worksheets-in-php/)
    - [PHP'de Yönetim Özellikleri](/cells/tr/net/management-features-in-php/)
      - [PHP'de Çalışma Sayfalarını Yönetme](/cells/tr/net/managing-worksheets-in-php/)
        - [PHP'de Mevcut Bir Excel Dosyasına Çalışma Sayfaları Ekleme](/cells/tr/net/add-worksheets-to-existing-excel-file-in-php/)
        - [PHP'de Yeni Bir Excel Dosyasına Çalışma Sayfaları Ekleme](/cells/tr/net/add-worksheets-to-new-excel-file-in-php/)
        - [PHP'de Sayfa Dizini Kullanarak Çalışma Sayfalarını Kaldırma](/cells/tr/net/removing-worksheets-using-sheet-index-in-php/)
        - [PHP'de Sayfa Adını Kullanarak Çalışma Sayfalarını Kaldırma](/cells/tr/net/removing-worksheets-using-sheet-name-in-php/)
