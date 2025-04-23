---
title: Docker da Aspose.Cells ı Çalıştırma
type: docs
description: Linux, Windows Sunucusu ve herhangi bir işletim sisteminde Aspose.Cells ı Docker konteynırında çalıştırın.
weight: 139
url: /tr/net/how-to-run-aspose-cells-in-docker/
---

Mikrohizmetler, konteynerleştirme ile birleştirildiğinde, teknolojileri kolayca birleştirmeyi mümkün kılar. Docker, geliştirme yığınızda hangi teknolojinin olduğundan bağımsız olarak Aspose.Cells işlevselliğini kolayca entegre etmenize olanak tanır.

Mikrohizmetleri hedefliyorsanız veya yığınınızda temel teknoloji .NET, C++ veya Java değilse ancak Aspose.Cells işlevselliğine ihtiyacınız varsa veya zaten yığınınızda Docker kullanıyorsanız, bu durumda Aspose.Cells'ı bir Docker konteynırında kullanmayı düşünebilirsiniz.

## Önkoşullar

- Docker'ın sisteminizde yüklü olması gerekmektedir. Windows veya Mac'te Docker'ı nasıl yükleyeceğinizle ilgili bilgi için, "Ayrıca Bakınız" bölümündeki bağlantılara başvurun.

- Ayrıca, aşağıda sağlanan örnekte Visual Studio 2019, .NET Core 3.1 SDK'nın kullanıldığını unutmayın.


## Merhaba Dünya Uygulaması

Bu örnekte, desteklenen tüm kaydetme formatlarında "Merhaba Dünya!" belgesi oluşturan ve kaydeden basit bir Merhaba Dünya konsol uygulaması oluşturursunuz. Uygulama ardından Docker'da derlenebilir ve çalıştırılabilir.

### Konsol Uygulaması Oluşturma

Merhaba Dünya programını oluşturmak için aşağıdaki adımları izleyin:
1. Docker kurulduktan sonra varsayılan olarak Linux Konteynerları kullanıldığından emin olun. Gerekirse, Docker Desktop menüsünden Linux konteynerlerine geçiş seçeneğini seçin.
1. In Visual Studio, create a .NET Core console application.<br>
![todo:image_alt_text](create-a-new-project.png)<br>
1. Install the latest Aspose.Cells version from NuGet. System.Drawing.Common and System.Text.Encoding.CodePages will be installed as a dependency of Aspose.Cells.<br>
![todo:image_alt_text](nuget-aspose-cells.png)<br>
1. Uygulama Linux'ta çalıştırılacağından, uygun yerel Linux varlıkları yüklü olmalıdır. .Net core sdk 3.1 taban görüntüsü ile başlayın ve libgdiplus libc6-dev'i yükleyin.
1. When all required dependencies are added, write a simple program that creates a “Hello World!” workbook and saves it in all supported save formats:<br>
**.NET**<br>
{{< highlight csharp >}}
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

Dikkat edin, "TestOut" klasörü, çıktı belgelerini kaydetmek için bir çıkış klasörü olarak belirtilir. Docker'da uygulamayı çalıştırdığınızda, ana makinedeki bir klasör, bu klasöre konteynerde birleştirilir. Bu, Docker konteynerinde Aspose.Cells tarafından oluşturulan çıktıları kolayca görüntülemenizi sağlar.

### Bir Dockerfile Yaplandırma

Bir sonraki adım, Dockerfile'ı oluşturmak ve yapılandırmaktır.

1. Dockerfile'ı oluşturun ve uygulamanızın çözüm dosyasının yanına yerleştirin. Bu dosya adını uzantısız tutun (varsayılan).
1. Dockerfile'da aşağıdakileri belirtin:

{{< highlight plain >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

Yukarıdaki, aşağıdaki talimatları içeren basit bir Dockerfile'dır:

- Kullanılacak SDK görüntüsü. Burada .Net Core SDK 3.1 görüntüsüdür. Docker, derleme çalıştırıldığında bu, indirecektir. SDK'nın sürümü etiket olarak belirtilmiştir.
- Fontları yükle çünkü SDK imajı çok az font içerir. Komut, yereldeki font dosyalarını docker imajına kopyalar. Yüklemeniz gereken tüm fontları içeren yerel bir "fonts" dizininiz olduğundan emin olun. Bu örnekte, yerel "fonts" dizini, Dockerfile ile aynı dizine konulmuştur.
- Çalışma dizini, bir sonraki satırda belirtildiği gibi.
- Her şeyi konteynıra kopyalama, uygulamayı yayınlama ve giriş noktasını belirtme komutu.
- İlgili komut, System.Drawing.Common tarafından gereklidir ve libgdiplus kurulumunu çalıştırmaktadır.

### Docker'da Uygulamanın Derlenmesi ve Çalıştırılması

Artık uygulama Docker'da derlenebilir ve çalıştırılabilir. Favori komut istemini açın, uygulamanın bulunduğu klasöre değiştirin (çözüm dosyası ve Dockerfile'ın yerleştirildiği klasör) ve aşağıdaki komutu çalıştırın:

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

Bu komutun ilk kez çalıştırılması biraz daha uzun sürebilir, çünkü Docker'ın gereken görüntüleri indirmesi gerekir. Önceki komut tamamlandıktan sonra aşağıdaki komutu çalıştırın:

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

Dikkatlice dağınık argümanına dikkat edin, çünkü daha önce belirtildiği gibi, ana makinedeki bir klasör, uygulama çalıştırılmasının sonuçlarını kolayca görmek için konteynerin klasörüne birleştirilir. Linux'taki yollar büyük harfe duyarlıdır.

{{% /alert %}}

## Aspose.Cells'i Destekleyen Görüntüler

- Aspose.Cells for .NET Standart Linux'ta EMF ve TIFF'i desteklemez.


## Daha Fazla Örnek

***1. Windows Server 2019'da uygulamayı çalıştırmak için***

- Dockerfile

{{< highlight plain >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

- Docker İmajı Oluştur

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Docker İmajını Çalıştır

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. Linux'ta uygulamayı çalıştırmak için***

- Bir font klasörü belirleyen basit bir program yazın, "Merhaba Dünya!" çalışma kitabını oluşturun ve kaydedin.

{{< highlight csharp >}}
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
- Dockerfile

{{< highlight plain >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.Fonts.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.Fonts.dll"]
{{< /highlight >}}

- Docker İmajı Oluştur

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Docker İmajını Çalıştır

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## Ayrıca Bakınız

- [Windows'ta Docker Desktop Kurulumu](https://docs.docker.com/docker-for-windows/install/)
- [Mac'te Docker Desktop Kurulumu](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- Linux konteynerlerine geçiş seçeneği
- [.NET Core SDK](https://hub.docker.com/_/microsoft-dotnet) hakkında ek bilgi
{{< app/cells/assistant language="csharp" >}}
