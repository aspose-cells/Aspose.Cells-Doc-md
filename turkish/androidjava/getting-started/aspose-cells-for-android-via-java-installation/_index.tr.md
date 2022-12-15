---
title: Aspose.Cells for Android via Java Kurulum
type: docs
weight: 30
url: /tr/java/aspose-cells-for-android-via-java-installation/
---
## **sistem gereksinimleri**
Aspose.Cells for Android via Java, platformdan bağımsızdır ve Android Runtime ortamının kurulu olduğu herhangi bir platformda kullanılabilir ve Android OS 2.0 veya üstünü çalıştıran Android sistemlerinde çalışır. Şu anda, bileşen aşağıdakilerle test edilmiştir:

- Android 5.1 v 22
## **Aspose.Cells for Android via Java'i Maven Deposundan yükleyin**
1. Derlemenize maven deposunu ekleyin.gradle
1. Bağımlılık olarak 'Aspose.Cells for Android via Java' JAR'ı ekleyin

{{< highlight "java" >}}

 // 1. Add maven repository into your build.gradle 

repositories {

    mavenCentral()

    maven { url "http://repository.aspose.com/repo/" }

}

// 2. Add 'Aspose.Cells for Android via Java' JAR as a dependency

dependencies {

    ...

    ...

    compile (group: 'com.aspose', name: 'aspose-cells', version: '20.6', classifier: 'android.via.java')

}

{{< /highlight >}}
## **Nasıl kullanılır Aspose.Cells for Android via Java**
Bu konu, Android Studio IDE'de Aspose.Cells for Android via Java'i kurmak için gerekli adımlar konusunda size yol gösterecektir, makinenizde zaten Android Studio'nun en son sürümünün yüklü olduğunu ve ayrıca Aspose.Cells for Android via Java paketinin en son sürümünü edindiğinizi varsayarsak.

{{% alert color="primary" %}} 

Android Studio'yu henüz yüklemediyseniz, önce Android Studio'nun kurulumunu edinmeniz ve makinenize yüklemeniz gerekir. Android Studio'nun en son sürümünü adresinden indirebilirsiniz.[burada](https://developer.android.com/studio/index.html#win-bundle) oysa IDE'nin nasıl kurulacağına ilişkin ayrıntılar mevcuttur[burada](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

 Aspose.Cells for Android via Java paket adresinden indirilebilir.[burada](https://downloads.aspose.com/cells/androidjava). Lütfen unutmayın, Aspose.Cells for Android via Java'in her bir sürüm paketi, aşağıda ayrıntıları verildiği gibi temel olarak 2 dosyadan oluşur.

- **aspose-hücreleri-xxxjar** Aspose.Cells for Android via Java API'den tüm ad alanlarını içeren ana kitaplık dosyasıdır.
- **aspose-cells-xxx-libs.apk** Aspose.Cells for Android via Java API tarafından sunulan şifreleme ve şifre çözme olanakları için kullanılan 3. taraf bcprov-jdk15-146.jar'ı içeren APK'dır.

{{% /alert %}} 
### **Android Studio'da Aspose.Cells for Android via Java ile Başlarken**
Android Studio IDE yüklendikten sonra, aşağıda gösterildiği gibi Dosya > Yeni > Yeni Proje'ye tıklayın.

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_1.png)

Aşağıda gösterildiği gibi Android Studio'nun Karşılama Ekranından da yeni bir proje oluşturabilirsiniz.

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_2.png)

Ardından, proje dosyalarını depolamak için uygulama adını, etki alanını ve konumu belirtmeniz istenecektir. Varsayılan değerleri seçiminize göre değiştirmeyi veya olduğu gibi bırakmayı seçebilir ve İleri'ye tıklayabilirsiniz.

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_3.png)

Bir sonraki adımda, uygulamanızı barındırmak/çalıştırmak istediğiniz Android Cihazı belirtmeniz gerekir. Seçildikten sonra İleri düğmesine tıklayın.

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_4.png)

Şimdi önceden tanımlanmış bir şablon listesinden Aktiviteyi seçmeniz gerekiyor. Gösterimi basit tutmak için aşağıda gösterildiği gibi Boş Etkinlik şablonunu seçtik.

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_5.png)

Tüm varsayılan ayarları olduğu gibi koruyacağımız için Etkinliği Özelleştir iletişim kutusunda Bitir düğmesine tıklayın.

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_6.png)

Önceki adımda Bitir düğmesine tıkladığınız anda, IDE aşağıda gösterildiği gibi projeyi oluşturmaya başlayacaktır. Bitmesine izin verin veya İptal düğmesine tıklayın.

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_7.png)

Artık proje IDE'ye yüklenmiştir, ancak, proje dosyalarının tüm hiyerarşisini görüntüleyebilmek için görünümü Proje olarak değiştirmek isteyebilirsiniz. Görünümü değiştirmek için lütfen aşağıdaki anlık görüntüyü kontrol edin.

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_8.png)

 Görünümü Proje olarak değiştirdikten sonra,**yapı.gradle** düzenleyicide dosya ve aşağıdaki parçacığı aşağıda gösterildiği gibi yapıştırın.

{{< highlight "java" >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_9.png)

Ardından Aspose.Cells for Android via Java Jar'ı projeye ekleyeceğiz. Aşağıda ayrıntıları verilen 2 önemli adım vardır.

-  Aspose.Cells for Android via Java Jar'ı manuel olarak şuraya kopyalayın:**\app\libs** dosya.
- Aspose.Cells for Android via Java Jar as Library'yi aşağıda gösterildiği gibi modüle ekleyin.

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_10.png)

Aspose.Cells for Java.Android Jar'ı kütüphane olarak eklemek istediğiniz modülü seçmeniz istenecektir. Lütfen uygun olanı seçin ve Tamam'ı tıklayın.

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_11.png)

 APK dosyasını da projeye eklemeniz gerekiyor. APK'yı şuraya kopyalamanız gerekir:**\app\src\main\varlıklar**dosya. Ana klasörün altında varlıklar klasörünüz yoksa, Proje görünümünde ana düğüme sağ tıklayarak bir tane oluşturabilirsiniz. Yeni > Klasör > Varlık Klasörü'nü seçin.

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_12.png)

APK projeye eklendikten sonra proje tarafından yüklenmesi gerekir. APK'yı aşağıdaki gibi yüklemenin 2 yolu vardır.

- Aşağıda sağlanan parçacığı kullanarak APK'yı özel bir uygulama sınıfına yükleyin ve özel uygulama sınıfını AndroidManifest.xml dosyasına kaydedin.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- APK'yı MainActivity'nin OnCreate yöntemine yükleyin.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

Artık kodu yazmaya hazırız. Gösterimin anlaşılmasını kolaylaştırmak için, düzene bir Düğme parçacığı ekledik ve tıklama olayını aşağıdaki gibi işleyeceğiz.

{{< highlight "java" >}}

 private class TestTask extends AsyncTask<Void, String, Boolean> {

    @Override

    protected Boolean doInBackground(Void... params) {

        Boolean result = false;

        Workbook book = new Workbook();

        Worksheet sheet = book.getWorksheets().get(0);

        Cells cells = sheet.getCells();

        Cell cell = cells.get("A1");

        cell.putValue("Hello World!");

        try {

            book.save(SD_PATH + "output.xlsx");

        } catch (Exception e) {

            e.printStackTrace();

        }

        return result;

    }

}

{{< /highlight >}}

Uygulamayı IDE arayüzündeki oynat düğmesini kullanarak (veya SHIFT + F10 kullanarak) çalıştırdığınızda, öykünücü uygulamayı aşağıda gösterildiği gibi yükleyecektir.

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_13.png)

Öykünücü üzerindeki düğmeyi tıklatmak, öykünücünün harici depolama klasöründe yeni bir elektronik tablo oluşturmak için kodu yürütür. Dosyaya aşağıda gösterildiği gibi Android Cihaz Monitöründen erişebilirsiniz.

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_14.png)

![yapılacaklar:resim_alternatif_Metin](aspose-cells-for-android-via-java-installation_15.png)


