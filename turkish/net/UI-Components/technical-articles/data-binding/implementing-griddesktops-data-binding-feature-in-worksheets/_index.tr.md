---
title: Çalışma Sayfalarında GridDesktop Veri Bağlama Özelliğini Uygulama
type: docs
weight: 10
url: /tr/net/implementing-griddesktops-data-binding-feature-in-worksheets/
---
{{% alert color="primary" %}} 

Veri Bağlama, Microsoft .NET Çerçevesi tarafından sunulan heyecan verici bir özelliktir. Microsoft tarafından sunulan DataGrid kontrolünün veri bağlamayı desteklediğini biliyoruz; bu, bir DataGrid'in herhangi bir Veri Kaynağına (DataSet, DataTable ve DataView nesneleri kullanılarak) bağlanabileceği anlamına gelir. Bu özellik geliştiricilerin hayatını çok kolaylaştırdı. Aynı konsepti temel alan Aspose.Cells.GridDesktop, geliştiricilerin çalışma sayfalarını herhangi bir veri kaynağına bağlamasına olanak tanıyan veri bağlamayı da destekler. Bu makale, özelliği incelemektedir.

{{% /alert %}} 
## **Örnek Veritabanı Oluşturma**
1.  Örnekle birlikte kullanmak için örnek bir veritabanı oluşturun. Ürünler tablosu (aşağıdaki şema) ile örnek bir veritabanı oluşturmak için Microsoft Access'i kullandık.

![yapılacaklar:resim_alternatif_metin](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Ürünler tablosuna üç sahte kayıt eklenir.
   **Ürünler tablosundaki kayıtlar** 

![yapılacaklar:resim_alternatif_metin](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **Örnek Uygulama Oluşturun**
Şimdi Visual Studio'da basit bir masaüstü uygulaması oluşturun ve aşağıdakileri yapın.

1. Araç kutusundan "GridControl" Kontrolünü sürükleyin ve formun üzerine bırakın.
1. Formun altındaki araç kutusundan dört düğme bırakın ve metin özelliklerini şu şekilde ayarlayın:**Woksheet'i bağla**, **Satır ekle**, **Sırayı sil** ve**Veritabanına Güncelleme** sırasıyla.
## **Ad Alanı Ekleme ve Global Değişkenleri Bildirme**
Bu örnek bir Microsoft Access veritabanı kullandığından, kodun en üstüne System.Data.OleDb ad alanını ekleyin.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


Artık bu ad alanı altında paketlenmiş sınıfları kullanabilirsiniz.

1. Genel değişkenleri bildirin.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **DataSet'i Veritabanındaki Verilerle Doldurma**
Şimdi verileri alıp bir DataSet nesnesine doldurmak için örnek veritabanına bağlanın.

1. Örnek veritabanımıza bağlanmak için OleDbDataAdapter nesnesini kullanın ve aşağıdaki kodda gösterildiği gibi, veritabanındaki Ürünler tablosundan getirilen verilerle bir DataSet'i doldurun.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **DataSet ile Bağlama Çalışma Sayfası**
Çalışma sayfasını DataSet'in Ürünler tablosuyla bağlayın:

1. İstediğiniz bir çalışma sayfasına erişin.
1. Çalışma sayfasını DataSet'in Ürünler tablosuyla bağlayın.

 içine aşağıdaki kodu ekleyin**Bağlama Çalışma Sayfası** düğmenin tıklama olayı.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **Çalışma Sayfasının Sütun Başlıklarını Ayarlama**
İlişkili çalışma sayfası artık verileri başarıyla yüklüyor ancak sütun başlıkları varsayılan olarak A, B ve C olarak etiketleniyor. Sütun başlıklarını veritabanı tablosundaki sütun adlarına ayarlamak daha iyi olur.

Çalışma sayfasının sütun başlıklarını ayarlamak için:

1. DataSet'teki DataTable'ın (Ürünler) her sütunu için altyazıları alın.
1. Başlıkları çalışma sayfası sütunlarının başlıklarına atayın.

 yazan kodu ekleyin**Bağlama Çalışma Sayfası** Aşağıdaki kod parçacığı ile düğmenin tıklama olayı. Bunu yaparak eski sütun başlıkları (A, B ve C) ÜrünKimliği, ÜrünAdı ve ÜrünPrice ile değiştirilecektir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **Sütunların Genişliğini ve Stillerini Özelleştirme**
Çalışma sayfasının görünümünü daha da iyileştirmek için sütunların genişliğini ve stillerini ayarlamak mümkündür. Örneğin, bazen sütun başlığı veya sütun içindeki değer, hücreye sığmayan uzun sayıda karakterden oluşur. Bu tür sorunları çözmek için Aspose.Cells.GridDesktop, sütun genişliklerinin değiştirilmesini destekler.

 Aşağıdaki kodu ekleyin**Bağlama Çalışma Sayfası** buton. Sütun genişlikleri yeni ayarlara göre özelleştirilecektir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


 Aspose.Cells.GridDesktop, sütunlara özel stiller uygulanmasını da destekler. Eklenen aşağıdaki kod,**Bağlama Çalışma Sayfası** düğmesi, sütun stillerini daha görünür hale getirmek için özelleştirir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


 Şimdi uygulamayı çalıştırın ve tıklayın**Bağlama Çalışma Sayfası** Buton.
## **Satır Ekleme**
Çalışma sayfasına yeni satırlar eklemek için Worksheet sınıfı AddRow yöntemini kullanın. Bu, alta boş bir satır ekler ve veri kaynağına yeni bir DataRow eklenir (burada, DataSet'in DataTable'ına yeni bir DataRow eklenir). Geliştiriciler, AddRow yöntemini tekrar tekrar çağırarak istedikleri kadar satır ekleyebilirler. Bir satır eklendiğinde, kullanıcılar buna değerler girebilir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **Satırları Silme**
Aspose.Cells.GridDesktop, Worksheet sınıfı RemoveRow yöntemini çağırarak satırların silinmesini de destekler. Aspose.Cells.GridDesktop kullanılarak bir satırın kaldırılması, satırın dizininin silinmesini gerektirir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


 Yukarıdaki kodun eklenmesi**Sırayı sil** düğmesine basın ve uygulamayı çalıştırın. Satır kaldırılmadan önce birkaç kayıt görüntülenir. Bir satırın seçilmesi ve**Sırayı sil** düğmesi seçilen satırı kaldırır.
## **Değişiklikleri Veritabanına Kaydetme**
Son olarak, kullanıcılar tarafından çalışma sayfasında yapılan değişiklikleri veritabanına geri kaydetmek için OleDbDataAdapter nesnesinin Update yöntemini kullanın. Update yöntemi, veritabanını güncellemek için çalışma sayfasının veri kaynağını (DataSet, DataTable vb.) alır.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1.  yukardaki kodu ekle**Veritabanına Güncelleme** buton.
1. Uygulamayı çalıştırın.
1. Çalışma sayfası verileri üzerinde bazı işlemler gerçekleştirin, belki yeni satırlar ekleyebilir ve mevcut verileri düzenleyebilir veya kaldırabilirsiniz.
1.  Sonra tıklayın**Veritabanına Güncelleme** değişiklikleri veritabanına kaydetmek için.
1. Tablo kayıtlarının uygun şekilde güncellendiğini görmek için veritabanını kontrol edin.
