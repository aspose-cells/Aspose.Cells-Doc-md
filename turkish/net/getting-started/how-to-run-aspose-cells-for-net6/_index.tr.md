---
title: .Net6 için Aspose.Cells Nasıl Çalıştırılır
type: docs
description: .Net6 için Aspose.Cells Nasıl Çalıştırılır
weight: 138
url: /tr/net/how-to-run-aspose-cells-for-net6/
---
## genel bakış

 .NET6 (veya üstü) platformları için, önceki platformlarla (.netcore31 veya öncesi) karşılaştırıldığında, grafik kitaplığıyla ilgili önemli bir fark vardır.
 bu resmi makamda[Microsoft Belge](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only).NET6 veya sonraki sürümler için "System.Drawing.Common" grafik kitaplığının yalnızca Windows'de destekleneceğini açıklar ve grafik kitaplığının değiştirilmesi için önerilerde bulunur.

Apose.Cells ürünü için değerlendirme yaptık ve grafik kitaplığının geçişini tamamladık. Microsoft'in resmi belgelerinde önerildiği gibi, Windows olmayan sistemlerde System.Drawing.Common yerine SkiaSharp kullanıyoruz. Lütfen bu kritik değişikliğin .Net6 için Aspose.Cells 22.10.1 veya sonrasında geçerli olacağını unutmayın.

.netcore31 veya öncesi için uyumluluk ve kararlılık için şu anda hala "System.Drawing.Common" grafik kitaplığını kullanıyoruz. .netcore31 veya öncesi için bağımlılıklar aşağıdaki gibidir:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 5.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

## Windows'de .Net6 için Aspose.Cells'i çalıştırın

Öncelikle VS2022 ile bir .net6 uygulaması oluşturabilir, ardından aşağıdaki kurulum seçeneklerini seçebilirsiniz:

### nuget aracılığıyla yükleyin

1.  NuGet'den Aspose.Cells'i arayın:[Aspose.Cells for .NET NuGet Paket](https://www.nuget.org/packages/Aspose.Cells/). 
Aspose.Cells'i VS2022'deki Nuget paket yöneticisinden de kurabilirsiniz.

2. "SkiaSharp" veya "System.Drawing.Common", projenizdeki "Hedef İşletim Sistemi" yapılandırmasına bağlı olan .Net6 platformları için Aspose.Cells 22.10.1 veya sonraki sürümlerin bir bağımlılığı olarak otomatik olarak kurulacaktır.
- Projeniz için "Hedef İşletim Sistemi"ni "Windows" olarak ayarlayın, "System.Drawing.Common"u .Net6 projeniz için Windows sisteminize bağımlı olarak kullanacaksınız. Bu konfigürasyonda, çizimin sonucu .netcore31'e veya daha öncesine yakındır.
**![Hedef işletim sistemini yapılandır](TargetOS.png)**
- Projeniz için "Hedef İşletim Sistemi"ni "Yok" veya diğer seçenekler olarak ayarlayın, "SkiaSharp"ı .Net6 projesi için Windows sisteminize bir bağımlılık olarak kullanacaksınız. Lütfen SkiaSharp'ın şu anda pencerelerde EMF gibi biçimleri desteklemediğini unutmayın.

### msi veya DLL aracılığıyla yükleyin

1. [Aspose.Cells.msi veya DLL dosyasını indirin](https://releases.aspose.com/cells/net/)

2. Kurulum dizinini veya DLL dizinini açın, ardından aşağıdaki 3. veya 4. adımı seçin:

3. "net6.0-windows" alt dizinini bulun, içindeki Aspose.Cells.dll dosyasını .net6 uygulamanıza ekleyin. Aşağıdaki nuget paketlerini .net6 projenize manuel olarak ekleyin:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 6.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

Bu sayede .Net6 projeniz için windows sisteminize bağımlı olarak "System.Drawing.Common" kullanmış olacaksınız. Bu konfigürasyonda, çizimin sonucu .netcore31'e veya daha öncesine yakındır.

4. "net6.0" alt dizinini bulun, içindeki Aspose.Cells.dll dosyasını .net6 uygulamanıza ekleyin. Aşağıdaki nuget paketlerini .net6 projenize manuel olarak ekleyin:
- SkiaSharp, 2.88.3.
- System.Security.Cryptography.Pkcs, 6.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

Bu sayede .Net6 projesi için Windows sisteminizde "SkiaSharp"ı bağımlılık olarak kullanmış olacaksınız. Lütfen SkiaSharp'ın şu anda pencerelerde EMF gibi biçimleri desteklemediğini unutmayın.

## Linux'ta .Net6 için Aspose.Cells'i çalıştırın

Windows adresindeki kurulum yöntemine bakın, SkiaSharp'ı yalnızca Linux sisteminde bir grafik kitaplığı bağımlılığı olarak seçebilirsiniz.

SkiaSharp'ın Linux altında doğru şekilde kullanılmasını sağlamak için aşağıdaki ek işlemleri yapmanız gerekir:

1. Linux Sisteminizde aşağıdaki komutu çalıştırın:
```
apt-get update && apt-get install -y libfontconfig1
```
VEYA
```
apk update && apk add fontconfig 
```

2. "SkiaSharp.NativeAssets.Linux 2.88.3" nuget paketlerini .net6 projenize ekleyin.

3. Veya yukarıdaki iki adım yerine .net6 projenize "SkiaSharp.NativeAssets.Linux.NoDependencies 2.88.3" nuget paketlerini eklemeyi seçebilirsiniz.

### Ubuntu için Örnek Dockerfile

1. "SkiaSharp.NativeAssets.Linux 2.88.3" nuget paketlerini .net6 projenize ekleyin.

2. Aşağıdaki Docker dosyasını kullanın:
{{< highlight "plain" >}}
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
COPY ["Ubuntu_Docker.csproj", "."]RUN dotnet restore "./Ubuntu_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Ubuntu_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ubuntu_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ubuntu_Docker.dll"]{{< /highlight >}}

### Alpine için Örnek Dockerfile

1. "SkiaSharp.NativeAssets.Linux 2.88.3" nuget paketlerini .net6 projenize ekleyin.

2. Aşağıdaki Docker dosyasını kullanın:
{{< highlight "plain" >}}
# Alpine 3.16
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
COPY ["Alpine_Docker.csproj", "."]RUN dotnet restore "./Alpine_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Alpine_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Alpine_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Alpine_Docker.dll"]{{< /highlight >}}
