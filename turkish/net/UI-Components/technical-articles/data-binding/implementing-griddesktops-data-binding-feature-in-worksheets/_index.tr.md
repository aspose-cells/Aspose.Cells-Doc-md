---
title: Bu makale, GridDesktop ta veri bağlama işlemini nasıl gerçekleştireceğinizi tanıtır.
type: docs
weight: 10
url: /tr/net/aspose-cells-griddesktop/implementing-data-binding-feature-in-worksheets/
keywords: Veri Bağlama, Microsoft .NET Framework tarafından sunulan heyecan verici bir özelliktir. Microsoft tarafından sunulan DataGrid kontrolünün veri bağlama desteğini desteklediğini biliyoruz, bu da DataGrid in herhangi bir Veri Kaynağına (DataSet, DataTable ve DataView nesnelerini kullanarak) bağlanabileceği anlamına gelir. Bu özellik geliştiricilerin hayatını çok daha kolaylaştırdı. Aynı konsepte dayanarak, Aspose.Cells.GridDesktop da veri bağlama desteği sağlar, bu da geliştiricilere çalışsayfalarını herhangi bir veri kaynağına bağlamalarını sağlar. Bu makale özelliği keşfeder.
description: Bu makale, GridDesktop ta veri bağlamayı nasıl yapacağınızı tanıtıyor.
---

{{% alert color="primary" %}} 

.NET Framework tarafından sunulan heyecan verici bir özelliktir. Microsoft tarafından sunulan DataGrid kontrolünün, DataSet, DataTable ve DataView nesnelerini kullanarak herhangi bir Veri Kaynağına bağlanma yeteneği olduğunu biliyoruz. Bu özellik geliştiricilerin işini çok kolaylaştırmıştır. Aynı konsepte dayanarak, Aspose.Cells.GridDesktop ayrıca veri bağlamayı destekler, bu da geliştiricilere çalışsayıları herhangi bir veri kaynağına bağlama imkanı sağlar. Bu makale bu özelliği keşfeder.

{{% /alert %}} 
## **Örnek Bir Veritabanı Oluşturma**
1. Örnek bir veritabanı oluşturmak için. Örnek bir veritabanı oluşturmak için Microsoft Access kullanıyoruz ve aşağıdaki şemayı içeren bir Ürünler tablosu ile örnek bir veritabanı oluşturduk. 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Ürünler tablosuna üç sahte kayıt eklenmiştir.
   Ürünler tablosundaki kayıtlar 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **Örnek Bir Uygulama Oluşturma**
Şimdi Visual Studio'da basit bir masaüstü uygulaması oluşturun ve aşağıdakileri yapın.

1. Aracı kutusundan 'GridControl' denetimini sürükleyip form üzerine bırakın.
1. Aracı kutusundan dört düğmeyi formun alt kısmına sürükleyin ve metin özelliğini sırasıyla **Çalışma Sayfasını Bağla**, **Satır Ekle**, **Satır Sil** ve **Veritabanına Güncelle** olarak ayarlayın.
## **Ad Alanı Ekleme ve Global Değişkenler Bildirme**
Bu örnek, bir Microsoft Access veritabanı kullandığından, kodun en üstüne System.Data.OleDb ad alanını ekleyin.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


Bu ad alanı altında paketlenmiş sınıfları kullanabilirsiniz.

1. Global değişkenleri bildirin.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **Veritabanından Veri Seti ile Veri Doldurma**
Şimdi örnek veritabanına bağlanarak bir Veri Seti nesnesine veri çekip doldurun.

1. OleDbDataAdapter nesnesini kullanarak örnek veritabanıyla bağlantı kurun ve veritabanındaki Ürünler tablosundan alınan verilerle bir Veri Seti doldurun, aşağıdaki kodda gösterildiği gibi.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **Çalışma Sayfasını Veri Seti ile Bağlama**
Çalışma sayfasını Veri Seti'nin Ürünler tablosuyla bağlayın:

1. İstenen çalışma sayfasına erişin.
1. Çalışma sayfasını Veri Seti'nin Ürünler tablosuyla bağlayın.

**Çalışma Sayfasını Bağla** düğmesinin tıklama olayına aşağıdaki kodu ekleyin.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **Çalışma Sayfası Sütun Başlıklarını Ayarlama**
Bağlı çalışma sayfası şu anda verileri başarıyla yüklüyor ancak sütun başlıkları varsayılan olarak A, B ve C olarak etiketlenmiştir. Veritabanı tablosundaki sütun başlıklarını sütun başlıklarına ayarlamak daha iyi olacaktır.

Çalışma sayfası sütun başlıklarını ayarlamak için:

1. Veri Seti'ndeki (Ürünler) her sütun için başlıkları alın.
1. Başlıkları çalışma sayfası sütunlarının başlıklarına atayın.

**Çalışma Sayfasını Bağla** düğmesinin tıklama olayına aşağıdaki kod parçasını ekleyin. Böylece eski sütun başlıkları (A, B ve C) ProductID, ProductName ve ProductPrice ile değiştirilecektir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **Sütunların Genişlik ve Stilini Özelleştirme**
Çalışma sayfasının görünümünü daha da iyileştirmek için sütunların genişliğini ve stilini ayarlamak mümkündür. Örneğin, bazen, sütun başlığı veya sütundaki değer hücresi içine sığmayacak uzun sayıda karakterden oluşur. Bu tür sorunları çözmek için Aspose.Cells.GridDesktop, sütunların genişliklerini değiştirmeyi destekler.

**Çalışma Sayfasını Bağla** düğmesine aşağıdaki kodu ekleyin. Sütun genişlikleri yeni ayarlamalara göre özelleştirilecektir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


Aspose.Cells.GridDesktop ayrıca sütunlara özel stiller uygulamayı destekler. **Çalışma Sayfasını Bağla** düğmesine eklenen aşağıdaki kod, sütun stillerini daha gösterişli hale getirir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


Şimdi uygulamayı çalıştırın ve **Çalışma Sayfasını Bağla** Düğmesine tıklayın.
## **Satırlar Ekleme**
Yeni satırlar eklemek için, Worksheet sınıfının AddRow yöntemini kullanın. Bu, en altta boş bir satır ekler ve bir veri kaynağına yeni bir DataRow eklenir (burada, bir DataSet'in DataTable'ına yeni bir DataRow eklenir). Geliştiriciler AddRow yöntemini tekrar tekrar çağırarak istedikleri kadar satır ekleyebilirler. Bir satır ekledikten sonra, kullanıcılar içine değer girebilir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **Satırları Silme**
Aspose.Cells.GridDesktop ayrıca Worksheet sınıfının RemoveRow yöntemini çağırarak satırları silmeyi destekler. Bir satırı silmek için Aspose.Cells.GridDesktop kullanırken silinecek satırın dizinini gerektirir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


Yukarıdaki kodu **Satırı Sil** düğmesine ekleyin ve uygulamayı çalıştırın. Bir satırın kaldırılması öncesinde birkaç kayıt görüntülenir. Bir satırı seçip **Satırı Sil** düğmesini tıkladığınızda seçilen satır kaldırılır.
## **Veritabanına Yapılan Değişikliklerin Kaydedilmesi**
Son olarak, kullanıcılar tarafından çalışsheet'te yapılan herhangi bir değişikliği veritabanına kaydetmek için OleDbDataAdapter nesnesinin Update yöntemini kullanın. Update yöntemi worksheet'in veri kaynağını (DataSet, DataTable vb.) alır ve veritabanını güncellemek için kullanır.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1. Yukarıdaki kodu **Veritabanına Güncelle** düğmesine ekleyin.
1. Uygulamayı çalıştırın.
1. Worksheet verileri üzerinde bazı işlemler yapın, belki yeni satırlar ekleyin ve mevcut verileri düzenleyin veya kaldırın.
1. Ardından **Veritabanına Güncelle**'ye tıklayarak değişiklikleri veritabanına kaydedin.
1. Tabloyu kontrol etmek için değiştirilmiş olup olmadığını görmek için.
