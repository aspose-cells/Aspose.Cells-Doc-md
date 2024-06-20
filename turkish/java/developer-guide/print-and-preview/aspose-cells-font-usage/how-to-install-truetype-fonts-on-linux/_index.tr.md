---
title: Linux ta TrueType Fontlarını Nasıl Yükleyebilirsiniz
type: docs
weight: 20
url: /tr/java/how-to-install-truetype-fonts-on-linux/
---

{{% alert color="primary" %}}

Muhtemelen sen Aspose.Cells'i elektronik tabloları PDF'e dönüştürmek için kullanıyorsun. Eğer bunu Linux gibi Windows olmayan bir işletim sistemi üzerinde yapıyorsanız, bu konu Aspose.Cells'in elektronik tablolarınızı en iyi sadakatle renderlamasını nasıl sağlayacağını açıklar.

Aspose.Cells tarafından dönüştürülen elektronik tabloların orijinale mümkün olan en yakın şekilde görünmesini sağlamak için, Linux sisteminize "Windows fontları" veya "TrueType fontları" yüklemeniz gerekebilir, çünkü en yaygın kullanılan TrueType fontlar Linux dağıtımlarıyla varsayılan olarak gelmez.

Linux sistemine TrueType fontları almanın iki ana yolu vardır:

1. Windows makinesinden font dosyalarını (.TTF ve .TTC) Linux makinenize kopyalayın.
1. msttcorefonts gibi bir TrueType font paketi yükleyin.

{{% /alert %}}

## **Bir Windows Makinesinden Yazı Tiplerini Kopyalama**

Windows makinesinin C:\Windows\Fonts dizininden .TTF ve .TTC dosyalarını Linux makinenizdeki bir dizine kopyalamak için kolay ve hızlı bir yol. Bu yazı tiplerini Linux'ta herhangi bir şekilde yüklemenize veya kaydetmenize gerek yok, uygulamanızda FontConfigs.setFontFolder yöntemini kullanarak yazı tiplerinin konumunu belirtmeniz yeterli.

{{% alert color="primary" %}}

Microsoft'un yazı tiplerini özgürce kullanmak için lisansladığını belirleyebildiğimiz kadarıyla, ancak lütfen yazı tipi lisansını kendiniz kontrol edin.

{{% /alert %}}

## **TrueType Yazı Tipleri Paketi Yükleme**

Aşağıdaki bilgiler, Fedora ve Red Hat Enterprise Linux (RHEL) gibi Linux dağıtımlarına Microsoft'un en ünlü TrueType yazı tiplerini nasıl yükleyeceğinizi adım adım gösterecektir.

{{% alert color="primary" %}}

'root' seviye yetkilerine ihtiyacınız olabilir, bu nedenle 'root' olarak oturum açın veya sudo yapılandırın.

{{% /alert %}}

Bunu Terminal kullanarak nasıl yapılacağı

1. Aşağıdaki RPM paketlerinin yüklü olduğundan emin olun.
   1. **rpm-build**: Yüklü değilse, rpm-build paketini yüklemek için aşağıdaki komutu kullanın

{{< highlight java >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: Yüklü değilse, aşağıdaki komutu kullanarak yükleyin

{{< highlight java >}}

yum \-y install wget

{{< /highlight >}}

1. En son msttcorefonts spec dosyasını SourceForge'dan aşağıdaki komutu kullanarak indirin

{{< highlight java >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Önceki indirilen spec dosyasını ve aşağıdaki komutu kullanarak bir RPM dosyası oluşturun

{{< highlight java >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. RPM dosyası şurada depolanacaktır: /root/rpmbuild/RPMS/noarch/, aşağıdaki gibi yükleyin

{{< highlight java >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. Değişikliklerin etkili olması için makineyi yeniden başlatın.

Yukarıda verilen talimatlar, aşağıdaki font ailelerini içeren Microsoft TTF paketini yükleyecektir:

1. Andale Mono
1. Arial Black/Arial (Kalın, İtalik, Kalın İtalik)
1. Comic Sans MS (Kalın)
1. Courier New (Kalın, İtalik, Kalın İtalik)
1. Georgia (Kalın, İtalik, Kalın İtalik)
1. Impact
1. Tahoma
1. Times New Roman (Kalın, İtalik, Kalın İtalik)
1. Trebuchet (Kalın, İtalik, Kalın İtalik)
1. Verdana (Kalın, İtalik, Kalın İtalik)
1. Webdings

{{% alert color="primary" %}}

Ubuntu'da, Synaptic Paket Yöneticisine gidin. **ttf-mscorefonts-installer** paketini bulun ve yükleyin.

{{% /alert %}}
