---
title: Aspose.Cells for .Net6 yı Nasıl Çalıştırılır
type: docs
description: "Aspose.Cells for .Net6 yı Nasıl Çalıştırılır."
weight: 138
url: /tr/net/how-to-run-aspose-cells-for-net6/
---

## Genel Bakış

.NET6 (veya sonrası) platformları için, önceki platformlarla (örneğin .netcore31 veya önceki sürümler) karşılaştırıldığında önemli bir fark grafik kütüphanesiyle ilgilidir. 
Bu resmi [Microsoft Belgesi](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only) .NET6 veya sonraki sürümler için grafik kütüphanesi "System.Drawing.Common"'ın sadece Windows'ta destekleneceğini açıklar ve grafik kütüphanesini değiştirmek için öneriler sunar.

Apose.Cells ürünü için değerlendirmeyi gerçekleştirdik ve grafik kütüphanesinin göçünü tamamladık. Microsoft'un resmi belgesinde önerildiği gibi, .Net6 için Windows dışı sistemlerde System.Drawing.Common yerine SkiaSharp kullanıyoruz. Lütfen bu kritik değişikliğin Aspose.Cells 22.10.1 veya sonrasında .Net6 için geçerli olacağını unutmayın.

 .netcore31 veya önceki sürümler için, uyumluluk ve kararlılık için şu anda "System.Drawing.Common" grafik kütüphanesini kullanmaya devam ediyoruz. .netcore31 veya önceki sürümler için bağımlılıklar şunlardır:
- System.Drawing.Common, 5.0.3.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

## Windows'ta Aspose.Cells for .Net6 (veya daha yeni sürüm) çalıştırın

İlk olarak, VS2022 ile bir .net6 (veya daha yeni sürüm) uygulaması oluşturabilirsiniz, ardından aşağıdaki kurulum seçeneklerini tercih edebilirsiniz:

### Nuget ile kurulum

1. NuGet'ten Aspose.Cells'i arayın: [Aspose.Cells for .NET NuGet Paketi](https://www.nuget.org/packages/Aspose.Cells/). 
VS2022'de Nuget paket yöneticisinden de Aspose.Cells'i kurabilirsiniz.

2. "SkiaSharp" veya "System.Drawing.Common" otomatik olarak Aspose.Cells 22.10.1 veya daha yeni sürümleri için bağımlılık olarak kurulacaktır; bu, projenizde "Hedef İşletim Sistemi" yapılandırmasına bağlıdır.
- Projeniz için "Hedef İşletim Sistemi"ni "Windows" olarak ayarlayın, Windows sisteminizde .Net6 (veya daha yeni) projenizde "System.Drawing.Common" bağımlılığı kullanacaksınız. Bu yapılandırmada, çizim sonucu .netcore31 veya öncesine daha yakındır.
**![Hedef İşletim Sistemi yapılandırması](TargetOS.png)**
- Projeniz için "Hedef İşletim Sistemi"ni "None" veya diğer seçenekler olarak ayarlayın, Windows sisteminizde "SkiaSharp" bağımlılığı kullanacaksınız. *Lütfen "SkiaSharp" bağımlılığı kullanan sürümün yazdırma özelliğini desteklemediğine dikkat edin.*

### Msi veya DLL ile kurulum

1. [Aspose.Cells.msi veya DLL'yi indirin](https://releases.aspose.com/cells/net/)

2. Kurulum dizinini veya DLL dizinini açın, ardından aşağıdaki adımlardan 3 veya 4'ü seçin:

3. "net6.0-windows" alt dizinini bulun, içindeki Aspose.Cells.dll'yi .net6 uygulamanıza ekleyin. Ayrıca aşağıdaki nuget paketlerini .net6 projenize manuel olarak ekleyin:
- System.Drawing.Common, 6.0.0.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

Bu şekilde, Windows sisteminizde .Net6 (veya daha yeni) projenizde "System.Drawing.Common" bağımlılığı kullanacaksınız. Bu yapılandırmada, çizim sonucu .netcore31 veya öncesine daha yakındır.

4. "net6.0" alt dizinini bulun, içindeki Aspose.Cells.dll'yi .net6 uygulamanıza ekleyin. Ayrıca aşağıdaki nuget paketlerini .net6 projenize manuel olarak ekleyin:
- SkiaSharp, 3.116.1.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

Bu şekilde, Windows sisteminizde .Net6 (veya daha yeni) projenizde "SkiaSharp" bağımlılığı kullanacaksınız. *Lütfen "SkiaSharp" bağımlılığı kullanan sürümün yazdırma özelliğini desteklemediğine dikkat edin.*

## Linux'ta Aspose.Cells for .Net6 (veya daha yeni sürüm) çalıştırın

Windows'ta kurulum yöntemine atıfta bulunarak, Linux sistemine yalnızca SkiaSharp'ı grafik kütüphanesi bağımlılığı olarak seçebilirsiniz.

SkiaSharp'ın Linux altında uygun şekilde kullanımını sağlamak için aşağıdaki ek işlemleri yapmanız gerekmektedir;

1. Linux Sisteminizde aşağıdaki komutu çalıştırın:
```
apt-get update && apt-get install -y libfontconfig1
```
VEYA
```
apk update && apk add fontconfig 
```

2. Nuget paketi "SkiaSharp.NativeAssets.Linux 3.116.1"'i .net6 (veya daha yeni sürüm) projenize ekleyin.
3. Veya yukarıdaki iki adıma ek olarak, "SkiaSharp.NativeAssets.Linux.NoDependencies 3.116.1" nuget paketini projenize eklemeyi tercih edebilirsiniz.

*Lütfen, eklenen paketin "SkiaSharp.NativeAssets.Linux" veya "SkiaSharp.NativeAssets.Linux.NoDependencies" sürümünün, Aspose.Cells for .NET tarafından referans verilen "SkiaSharp" sürümü ile uyumlu olması gerektiğine dikkat edin. Aspose.Cells for .NET ve karşılık gelen referans "SKiaSharp" sürümlerinin detayları aşağıda belirtilmiştir:*

| Aspose.Cells for .NET  |                SkiaSharp                |
| :--------------------: | :-------------------------------------: |
| >= 22.10.1 && <= 22.11 |                 2.88.0                  |
|  >= 22.12 && <= 23.9   |                 2.88.3                  |
|  >= 23.10 && <= 24.12  |                 2.88.6                  |
|        = 25.1.1        |                 3.116.1                 |
|        >=25.1.2        | 2.88.9(net6.0, net8.0), 3.116.1(net9.0) |



### Ubuntu için Örnek Docker Dosyası

1. Nuget paketi "SkiaSharp.NativeAssets.Linux 3.116.1"'i .net6 (veya daha yeni sürüm) projenize ekleyin.

2. Aşağıdaki Docker dosyasını kullanın:
{{< highlight plain >}}
# Ubuntu 20.04
FROM mcr.microsoft.com/dotnet/runtime:6.0-focal AS base
WORKDIR /app

# add "libfontconfig1" package if using "SkiaSharp.NativeAssets.Linux" in your project
# Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apt-get update && apt-get install -y libfontconfig1

# Copy fonts from local to docker
# For example, put a "fonts" folder in your project folder, and put the font files in it,
# then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build
WORKDIR /src
COPY ["Ubuntu_Docker.csproj", "."]
RUN dotnet restore "./Ubuntu_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Ubuntu_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ubuntu_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ubuntu_Docker.dll"]
{{< /highlight >}}

### Alpine için Örnek Docker Dosyası

1. Nuget paketi "SkiaSharp.NativeAssets.Linux 3.116.1"'i .net6 (veya daha yeni sürüm) projenize ekleyin.

2. Aşağıdaki Docker dosyasını kullanın:
{{< highlight plain >}}
#Alpine 3.16
FROM mcr.microsoft.com/dotnet/runtime:6.0-alpine3.16 AS base
WORKDIR /app

# add "fontconfig" package if using "SkiaSharp.NativeAssets.Linux" in your project
# Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apk update && apk add fontconfig 

# Copy fonts from local to docker
# For example, put a "fonts" folder in your project folder, and put the font files in it,
# then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-alpine3.16 AS build
WORKDIR /src
COPY ["Alpine_Docker.csproj", "."]
RUN dotnet restore "./Alpine_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Alpine_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Alpine_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Alpine_Docker.dll"]
{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
