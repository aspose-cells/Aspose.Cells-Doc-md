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
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 5.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

Windows'ta Aspose.Cells for .Net6'yı Çalıştırmak

Öncelikle VS2022 ile .net6 uygulaması oluşturabilir, ardından aşağıdaki kurulum seçeneklerini seçebilirsiniz:

### Nuget ile kurulum

1. NuGet'ten Aspose.Cells'i arayın: [Aspose.Cells for .NET NuGet Paketi](https://www.nuget.org/packages/Aspose.Cells/). 
VS2022'de Nuget paket yöneticisinden de Aspose.Cells'i kurabilirsiniz.

2. .Net6 platformları için Aspose.Cells 22.10.1 veya sonrası için "SkiaSharp" veya "System.Drawing.Common" otomatik olarak bağımlılık olarak yüklenecektir, bu da projenizdeki "Hedef İşletim Sistemi" yapılandırmasına bağlıdır.
- Projemiz için "Hedef İşletim Sistemi"'ni "Windows" olarak ayarlarsanız, .Net6 projesinizde Windows sisteminizde "System.Drawing.Common"'ı bir bağımlılık olarak kullanacaksınız. Bu yapılandırmada çizimin sonucu .netcore31 veya öncekine daha yakın olacaktır.
**![Hedef İşletim Sistemi yapılandırması](TargetOS.png)**
- Projemiz için "Hedef İşletim Sistemi"'ni "None" veya diğer seçeneklere ayarlarsanız, .Net6 projesinizde Windows sisteminizde "SkiaSharp"'ı bir bağımlılık olarak kullanacaksınız. *Lütfen "SkiaSharp"'ı bağımlılık olarak kullanan sürümün yazıcıya yazdırma özelliğini desteklemediğini unutmayın.*

### Msi veya DLL ile kurulum

1. [Aspose.Cells.msi veya DLL'yi indirin](https://releases.aspose.com/cells/net/)

2. Kurulum dizinini veya DLL dizinini açın, ardından aşağıdaki adımlardan 3 veya 4'ü seçin:

3. "net6.0-windows" alt dizinini bulun, içindeki Aspose.Cells.dll'yi .net6 uygulamanıza ekleyin. Ayrıca aşağıdaki nuget paketlerini .net6 projenize manuel olarak ekleyin:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages, 4.7.0.

Bu şekilde, .Net6 projesinizde Windows sisteminizde "System.Drawing.Common"'ı bir bağımlılık olarak kullanacaksınız. Bu yapılandırmada çizimin sonucu .netcore31 veya öncekine daha yakın olacaktır.

4. "net6.0" alt dizinini bulun, içindeki Aspose.Cells.dll'yi .net6 uygulamanıza ekleyin. Ayrıca aşağıdaki nuget paketlerini .net6 projenize manuel olarak ekleyin:
- SkiaSharp, 2.88.6.
- System.Security.Cryptography.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages, 4.7.0.

Bu şekilde, .Net6 projesinizde Windows sistemine "SkiaSharp" bağımlılığı olarak kullanacaksınız. *Lütfen, bağımlılık olarak "SkiaSharp" kullanan sürümün yazıcıya yazdırma özelliğini desteklemediğini unutmayın.*
## Linux'ta Aspose.Cells for .Net6'u Çalıştır

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

2. .net6 projenize "SkiaSharp.NativeAssets.Linux 2.88.6" nuget paketlerini ekleyin.

3. Ya da yukarıdaki iki adımın yerine, .net6 projenize "SkiaSharp.NativeAssets.Linux.NoDependencies 2.88.6" nuget paketlerini eklemeyi seçebilirsiniz.

### Ubuntu için Örnek Docker Dosyası

1. .net6 projenize "SkiaSharp.NativeAssets.Linux 2.88.6" nuget paketlerini ekleyin.

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

1. .net6 projenize "SkiaSharp.NativeAssets.Linux 2.88.6" nuget paketlerini ekleyin.

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
