---
title: Android via Java için Aspose.Cells Kurulumu
type: docs
weight: 30
url: /tr/java/aspose-cells-for-android-via-java-installation/
---

## **Sistem Gereksinimleri**
Android via Java için Aspose.Cells platformdan bağımsızdır ve Android Çalışma Zamanı ortamının kurulu olduğu herhangi bir platformda kullanılabilir ve Android OS 2.0 veya daha yüksek sürümünde çalışır. Şu anda, bileşen şunlarla test edilmiştir:

- Android 5.1 v 22
## **Aspose.Cells for Android via Java'ü Maven Deposundan Yükle**
1. maven deposunu **build.gradle** dosyanıza ekleyin. 
1. 'Aspose.Cells for Android via Java' JAR'ı bağımlılık olarak ekleyin.

{{< highlight java >}}

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
## **Android via Java için Aspose.Cells'ı Nasıl Kullanılır**
Bu konu, Aspose.Cells for Android via Java'ün Android Studio IDE'de kurulmasını ayarlamak için gerekli adımları rehberlik edecektir, varsayıyoruz ki makinenizde zaten Android Studio'nun en son sürümünü yüklediniz ve ayrıca en son sürüm Aspose.Cells for Android via Java'ü edindiniz.

{{% alert color="primary" %}} 

Eğer henüz Android Studio'yu yüklemediyseniz, öncelikle Android Studio'nun kurulumunu edinip makinenize yüklemeniz gerekmektedir. Android Studio'nun en son sürümünü [buradan](https://developer.android.com/studio/index.html#win-bundle) indirebilirken, IDE'nin nasıl kurulacağına ilişkin detaylar [burada](https://developer.android.com/studio/install.html) bulunmaktadır.

{{% /alert %}} {{% alert color="primary" %}} 

Aspose.Cells for Android via Java paketi [buradan](https://downloads.aspose.com/cells/androidjava) indirilebilir. Lütfen dikkat edin, Aspose.Cells for Android via Java'ün her yayın paketi genellikle aşağıda detaylandırıldığı gibi 2 dosyadan oluşmaktadır.

- **aspose-cells-x.x.x.jar** Aspose.Cells for Android via Java API'den tüm namespace'leri içeren ana kütüphane dosyasıdır.
- **aspose-cells-x.x.x-libs.apk** Aspose.Cells for Android via Java API tarafından sunulan şifreleme ve şifre çözme imkanlarını kullanmak üzere kullanılan 3. taraf bcprov-jdk15-146.jar'ı içeren APK'dir.

{{% /alert %}} 
### **Android Studio'da Aspose.Cells for Android via Java ile Başlarken**
Android Studio IDE yüklendiğinde, aşağıda gösterildiği gibi Dosya > Yeni > Yeni Proje'ye tıklayın.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_1.png)

Ayrıca, Android Studio'nun Hoşgeldiniz Ekranından yeni bir proje oluşturabilirsiniz, aşağıda gösterildiği gibi.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_2.png)

Daha sonra, uygulama adı, alan ve projeyi depolayacağınız konumu belirtmek üzere isteneceksiniz. Varsayılan değerleri değiştirmeyi veya olduğu gibi bırakmayı seçebilir ve Sonraki'ye tıklayabilirsiniz.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_3.png)

Bir sonraki adımda, uygulamanızı barındırmak/çalıştırmak istediğiniz Android Cihazını belirtmelisiniz. Seçildikten sonra, İleri düğmesine tıklayın.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_4.png)

Şimdi önceden tanımlanmış şablonlar listesinden Etkinliği seçmeniz gerekmektedir. Gösterimi basit tutmak için, aşağıda boş Etkinlik şablonunu seçtik.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_5.png)

Tüm varsayılan ayarları olduğu gibi bıraktığımızdan, Etkinlik özelleştirme ile İleri düğmesine tıklayın.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_6.png)

Önceki adımdaki Bitir düğmesine tıklar tıklamaz IDE projeyi oluşturmaya başlayacaktır, izin verin ya da İptal düğmesine tıklayın.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_7.png)

Artık proje IDE'de yüklendi, ancak proje dosyalarının tam hiyerarşisini görebilmek için Görünümü Projeye değiştirmek isteyebilirsiniz. Görünümü değiştirmek için lütfen aşağıdaki görüntüyü kontrol edin.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_8.png)

Görünümü Projeye değiştirdikten sonra, editörde **build.gradle** dosyasını bulup yükle ve aşağıdaki parçacığı yapıştırın.

{{< highlight java >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_9.png)

Sonraki olarak, Aspose.Cells for Android via Java Jar'ı projeye ekleyeceğiz. Aşağıda detaylandırıldığı gibi 2 önemli adım bulunmaktadır.

- Aspose.Cells for Android via Java Jar'ı manuel olarak **\app\libs** klasörüne kopyalayın.
- Aspose.Cells for Android via Java Jar'ı modüle kütüphane olarak ekleyin, aşağıda gösterildiği gibi.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_10.png)

Aspose.Cells for Java.Android Jar'ı bir kitaplığa eklemek istediğiniz modülü seçmek için uygun şekilde seçileceğiniz ve Tamam'ı tıklamanız istenecektir.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_11.png)

Ayrıca, APK dosyasını projeye eklemeniz de gerekiyor. APK'yi **\app\src\main\assets** klasörüne kopyalamalısınız. Main klasörünün altında assets klasörünüz yoksa, Project görünümünde main düğmesine sağ tıklayarak bir tane oluşturabilirsiniz. Yeni > Klasör > Asset Klasörü seçeneğini belirleyin.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_12.png)

APK projeye eklenince, projede yüklenmesi gerekiyor. APK'yı yüklemenin 2 yolu bulunmaktadır.

- Özel bir uygulama sınıfında aşağıdaki kod parçasını kullanarak APK'yı yükleyin ve özel uygulama sınıfını AndroidManifest.xml'e kaydedin.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- APK'yı MainActivity'in OnCreate yönteminde yükleyin.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

Şimdi kod yazmaya hazırız. Gösterimi anlaşılır tutmak için bir Button bileşenini düzene ekledik ve tıklama etkinliğini aşağıdaki gibi ele alacağız.

{{< highlight java >}}

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

IDE arabirimindeki oynatma düğmesiyle (veya SHIFT + F10 kullanarak) uygulamayı çalıştırdığınızda, simulatör aşağıda gösterildiği gibi uygulamayı yükleyecektir.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_13.png)

Simülatördeki düğmeye tıklamak, simulatörün dış depolama klasörüne yeni bir elektronik tablo oluşturmak için kodu yürütecektir. Dosyaya aşağıda gösterildiği gibi Android Cihazı İzleyicisi'nden erişebilirsiniz.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_14.png)

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_15.png)


