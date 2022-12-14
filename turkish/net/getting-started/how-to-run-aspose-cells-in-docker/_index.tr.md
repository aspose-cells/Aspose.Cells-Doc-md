---
title: Docker'da Aspose.Cells Nasıl Çalıştırılır?
type: docs
description: Aspose.Cells'i Linux, Windows Sunucusu ve herhangi bir işletim sistemi için bir Docker kapsayıcısında çalıştırın.
weight: 139
url: /tr/net/how-to-run-aspose-cells-in-docker/
---
Mikro hizmetler, kapsayıcılıkla birlikte teknolojileri kolayca birleştirmeyi mümkün kılar. Docker, geliştirme yığınınızda hangi teknolojinin bulunduğundan bağımsız olarak Aspose.Cells işlevselliğini uygulamanıza kolayca entegre etmenize olanak tanır.

Mikro hizmetleri hedefliyorsanız veya yığınınızdaki ana teknoloji .NET, C++ veya Java değilse, ancak Aspose.Cells işlevine ihtiyacınız varsa veya yığınınızda zaten Docker kullanıyorsanız, Docker'da Aspose.Cells kullanmak ilginizi çekebilir konteyner.

## Önkoşullar

- Docker sisteminizde yüklü olmalıdır. Docker'ı Windows veya Mac'e nasıl yükleyeceğiniz hakkında bilgi için "Ayrıca Bakınız" bölümündeki bağlantılara bakın.

- Ayrıca, aşağıda verilen örnekte Visual Studio 2019, .NET Core 3.1 SDK'nın kullanıldığını unutmayın.


## Hello World Başvuru

Bu örnekte, "Hello World!" yapan basit bir Hello World konsol uygulaması oluşturuyorsunuz. belge ve desteklenen tüm kaydetme biçimlerinde kaydeder. Uygulama daha sonra Docker'da oluşturulabilir ve çalıştırılabilir.

### Konsol Uygulamasını Oluşturma

Hello World programını oluşturmak için aşağıdaki adımları takip ediniz:
1. Docker yüklendikten sonra, Linux Kapsayıcılarını (varsayılan) kullandığından emin olun. Gerekirse, Docker Masaüstü menüsünden Linux kapsayıcılarına geç seçeneğini seçin.
1. Visual Studio'da bir .NET Core konsol uygulaması oluşturun.<br>
![yapılacaklar:resim_alternatif_Metin](create-a-new-project.png)<br>
1. NuGet'den en son Aspose.Cells sürümünü yükleyin. System.Drawing.Common ve System.Text.Encoding.CodePages, Aspose.Cells'in bir bağımlılığı olarak kurulacaktır.<br>
![yapılacaklar:resim_alternatif_Metin](nuget-aspose-cells.png)<br>
1. Uygulama Linux üzerinde çalışacağından, uygun yerel Linux varlıklarının yüklenmesi gerekir. Dotnet core sdk 3.1 temel görüntüsüyle başlayın ve libgdiplus libc6-dev'i kurun.
1. Gerekli tüm bağımlılıklar eklendiğinde, “Hello World!” Oluşturan basit bir program yazın. çalışma kitabı ve onu desteklenen tüm kaydetme biçimlerinde kaydeder:<br>
**.NET**<br>
{{< highlight "csharp" >}}
using System;
namespace Aspose.Cells.Docker
{
    class Program
    {
        static void Main(string[] args)
        {
            Workbook workbook = new Workbook();
            workbook.Worksheets[0].Cells[0, 0].PutValue("Hello from Aspose.Cells!!!");
            foreach (SaveFormat sf in Enum.GetValues(typeof(SaveFormat)))
            {
                if (sf != SaveFormat.Unknown)
                {
                    try
                    {
                        // The folder specified will be mounted as a volume when run the application in Docker image.
                        var fileName = string.Format("out{0}", FileFormatUtil.SaveFormatToExtension(sf));
                        workbook.Save(fileName, sf);
                        Console.WriteLine("Saving {0}\t\t[OK]", sf);
                    }
                    catch
                    {
                        Console.WriteLine("Saving {0}\t\t[FAILED]", sf);
                    }
                }
            }
        }
    }
}

{{< /highlight >}}

"TestOut" klasörünün, çıktı belgelerinin kaydedilmesi için bir çıktı klasörü olarak belirtildiğine dikkat edin. Uygulamayı Docker'da çalıştırırken, kapsayıcıdaki bu klasöre ana makinedeki bir klasör monte edilecektir. Bu, Docker kapsayıcısında Aspose.Cells tarafından oluşturulan çıktıyı kolayca görüntülemenizi sağlayacaktır.

### Dockerfile Yapılandırma

Bir sonraki adım, Dockerfile dosyasını oluşturmak ve yapılandırmaktır.

1. Dockerfile dosyasını oluşturun ve uygulamanızın çözüm dosyasının yanına yerleştirin. Bu dosya adını uzantısız tutun (varsayılan).
1. Dockerfile'da şunları belirtin:

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

Yukarıdaki, aşağıdaki talimatları içeren basit bir Docker dosyasıdır:

- Kullanılacak SDK görüntüsü. İşte .Net Core SDK 3.1 görüntüsü. Derleme çalıştırıldığında Docker onu indirecektir. SDK'nın sürümü bir etiket olarak belirtilir.
- Yazı Tiplerini yükleyin çünkü SDK görüntüsü çok az yazı tipi içerir. Komut, yazı tipi dosyalarını yerelden docker görüntüsüne kopyalar. Yüklemeniz gereken tüm yazı tiplerini içeren yerel bir "yazı tipleri" dizinine sahip olduğunuzdan emin olun. Bu örnekte, yerel "fontlar" dizini Dockerfile ile aynı dizine konulmuştur.
- Bir sonraki satırda belirtilen çalışma dizini.
- Her şeyi kaba kopyalama, uygulamayı yayınlama ve giriş noktasını belirleme komutu.
- Libgdiplus'ı kurma komutu kapsayıcıda çalıştırılır. Bu, System.Drawing.Common tarafından gereklidir.

### Docker'da Uygulama Oluşturma ve Çalıştırma

Artık uygulama Docker'da oluşturulabilir ve çalıştırılabilir. Favori komut isteminizi açın, dizini uygulamanın bulunduğu klasöre (çözüm dosyasının ve Dockerfile'nin yerleştirildiği klasör) değiştirin ve aşağıdaki komutu çalıştırın:

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

Docker'ın gerekli görüntüleri indirmesi gerektiğinden, bu komut ilk kez çalıştırıldığında daha uzun sürebilir. Önceki komut tamamlandığında, aşağıdaki komutu çalıştırın:

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

Bağlama bağımsız değişkenine dikkat edin, çünkü daha önce belirtildiği gibi, uygulamanın yürütülmesinin sonuçlarını kolayca görmek için ana makinedeki bir klasör kapsayıcının klasörüne bağlanır. Linux'taki yollar büyük/küçük harfe duyarlıdır.

{{% /alert %}}

## Destekleyen Görseller Aspose.Cells

- Aspose.Cells for .NET Standart, Linux'ta EMF ve TIFF'i desteklemez.


## Daha fazla örnek

***1. Uygulamayı Windows Server 2019'da çalıştırmak için***

- liman işçisi dosyası

{{< highlight "plain" >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

- Docker Görüntüsü Oluşturun

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Docker Görüntüsünü Çalıştır

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. Uygulamayı Linux'ta çalıştırmak için***

- Yazı tipi klasörünü ayarlayan basit bir program yazın, bir “Hello World!” çalışma kitabı ve kaydeder.

{{< highlight "csharp" >}}
namespace Aspose.Cells.Docker.Fonts
{
    using System;
    using System.IO;

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Set font folders on linux.
                string[] fonts = { "/Fonts" };
                FontConfigs.SetFontFolders(fonts, true);
                // build workbook
                Workbook workbook = new Workbook();
                MemoryStream memoryStream = new MemoryStream();
                workbook.Worksheets[0].Cells[0, 0].PutValue("Hello from Aspose.Cells!!!");
                Style style = workbook.CreateStyle();
                style.Font.Name = "Arial";
                style.Font.Size = 16;
                workbook.Worksheets[0].Cells[0, 0].SetStyle(style);
                workbook.Save("/TestOut/TestFontsOut.xlsx");
            }
            catch (Exception e)
            {
                Console.WriteLine("Saving outfonts.xlsx\t\t[FAILED],{0}", e.Message);
            }
           
        }
    }
}

{{< /highlight >}}
- liman işçisi dosyası

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.Fonts.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.Fonts.dll"]{{< /highlight >}}

- Docker Görüntüsü Oluşturun

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Docker Görüntüsünü Çalıştır

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## Ayrıca bakınız

- [Docker Desktop'ı Windows'e kurun](https://docs.docker.com/docker-for-windows/install/)
- [Mac'te Docker Desktop'ı Kurun](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Çekirdek 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- [Linux kapsayıcılarına geçin](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers) seçenek
-  hakkında ek bilgi[.NET Çekirdek SDK'sı](https://hub.docker.com/_/microsoft-dotnet-sdk)
