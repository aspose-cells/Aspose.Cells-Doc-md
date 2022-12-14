---
title: Linux'ta TrueType Yazı Tiplerini Kurma
type: docs
weight: 20
url: /tr/java/how-to-install-truetype-fonts-on-linux/
---
{{% alert color="primary" %}}

En olası senaryo, elektronik tabloları PDF'ye dönüştürmek için Aspose.Cells'i kullanmanızdır. Bunu Linux gibi Windows tabanlı olmayan bir işletim sisteminde yapıyorsanız, bu konuda Aspose.Cells'in elektronik tablolarınızı en iyi şekilde aslına uygun olarak işlemesini nasıl sağlayacağınız açıklanmaktadır.

Aspose.Cells tarafından dönüştürülen elektronik tabloların orijinaline olabildiğince yakın görünmesini sağlamak için Linux sisteminize "Windows yazı tipleri" veya "TrueType yazı tipleri" yüklemeniz gerekebilir çünkü en sık kullanılan TrueType yazı tipleri önceden yüklenmiş olarak gelmez. Varsayılan olarak Linux dağıtımları.

Bir Linux sisteminde TrueType yazı tiplerini almanın iki ana yolu vardır:

1. Bir Windows makinesinden Linux makinenize yazı tipi dosyalarını (.TTF ve .TTC) kopyalayın.
1. msttcorefonts gibi bir TrueType yazı tipi paketi kurun.

{{% /alert %}}

## **Bir Windows Makinesinden Yazı Tiplerini Kopyalayın**

Kolay ve hızlı bir yol, .TTF ve .TTC dosyalarını bir Windows makinesindeki C:\Windows\Fonts dizininden Linux makinenizdeki bir dizine kopyalamaktır. Bu fontları herhangi bir şekilde Linux üzerinde kurmanız veya kaydettirmeniz gerekmez, uygulamanızda FontConfigs.setFontFolder yöntemini kullanarak fontların konumunu belirtmeniz yeterlidir.

{{% alert color="primary" %}}

Anlayabildiğimiz kadarıyla, Microsoft yazı tiplerini herkesin özgürce kullanması için lisanslıyor, ancak lütfen yazı tipi lisanslarını kendiniz kontrol edin.

{{% /alert %}}

## **Bir TrueType Yazı Tipleri Paketi Kurun**

Aşağıda verilen bilgiler, Microsoft'in en ünlü TrueType yazı tiplerini Fedora ve Red Hat Enterprise Linux (RHEL) gibi Linux dağıtımlarına yüklemek için size adım adım rehberlik edecektir.

{{% alert color="primary" %}}

'root' düzeyinde ayrıcalıklara ihtiyaç duyabilirsiniz, bu nedenle 'root' olarak oturum açın veya sudo'yu yapılandırın.

{{% /alert %}}

İşte Terminal kullanarak bunu nasıl yapacağınız.

1. Aşağıdaki RPM paketlerinin kurulu olduğundan emin olun.
   1. **rpm-inşa**: Kurulu değilse, rpm-build paketini kurmak için aşağıdaki komutu kullanın

{{< highlight "java" >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: Kurulu değilse, aşağıdaki komutu kullanın

{{< highlight "java" >}}

yum \-y install wget

{{< /highlight >}}

1. Aşağıdaki komutu kullanarak SourceForge'dan en son msttcorefonts spec dosyasını indirin,

{{< highlight "java" >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Daha önce indirilen spec dosyasını ve aşağıdaki komutu kullanarak bir RPM dosyası oluşturun,

{{< highlight "java" >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. RPM dosyası şu konumda saklanacaktır: /root/rpmbuild/RPMS/noarch/, aşağıdaki gibi kurun,

{{< highlight "java" >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. Değişikliklerin etkili olması için makineyi yeniden başlatın.

Yukarıda verilen talimatlar, aşağıdaki yazı tipi ailelerini içeren Microsoft TTFs paketini yükleyecektir:

1. Endülüs Mono
1. Arial Siyah/Arial (Kalın, İtalik, Kalın İtalik)
1. Comic Sans MS (Kalın)
1. Courier New (Kalın, İtalik, Kalın İtalik)
1. Gürcistan (Kalın, İtalik, Kalın İtalik)
1. Darbe
1. Tahoma
1. Times New Roman (Kalın, İtalik, Kalın İtalik)
1. Mancınık (Kalın, İtalik, Kalın İtalik)
1. Verdana (Kalın, İtalik, Kalın İtalik)
1. ağlar

{{% alert color="primary" %}}

 Ubuntu'da Synaptic Paket Yöneticisine gidin. bulun ve yükleyin**ttf-mscorefonts-yükleyici** paket.

{{% /alert %}}
