---
title: .Net6 için Aspose.Cells Nasıl Çalıştırılır
type: docs
description: .Net6 için Aspose.Cells Nasıl Çalıştırılır
weight: 138
url: /tr/net/how-to-run-aspose-cells-for-net6/
---
##  Genel Bakış

 .NET6 (veya üstü) platformları için, önceki platformlarla (.netcore31 veya öncesi) karşılaştırıldığında önemli bir fark grafik kitaplığıyla ilgilidir.
 Bu resmi makamda[Microsoft Belge](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only).NET6 veya üzeri sürümler için "System.Drawing.Common" grafik kitaplığının yalnızca Windows'de destekleneceğini açıklar ve grafik kitaplığının değiştirilmesine ilişkin öneriler verir.

Apose.Cells ürünü için değerlendirmeyi gerçekleştirdik ve grafik kütüphanesinin geçişini tamamladık. Microsoft'in resmi belgelerinde önerildiği gibi, Windows olmayan sistemlerde System.Drawing.Common yerine SkiaSharp'ı kullanıyoruz. Bu kritik değişikliğin .Net6 için Aspose.Cells 22.10.1 veya sonrasında geçerli olacağını lütfen unutmayın.

.netcore31 veya öncesi için uyumluluk ve kararlılık açısından şu anda hala "System.Drawing.Common" grafik kütüphanesini kullanıyoruz. .netcore31 veya öncesi için bağımlılıklar aşağıdaki gibidir:
- System.Drawing.Common, 4.7.0.
- Sistem.Güvenlik.Kriptografi.Pkcs, 5.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

##  Windows'de .Net6 için Aspose.Cells'i çalıştırın

Öncelikle VS2022 ile bir .net6 uygulaması oluşturabilir, ardından aşağıdaki kurulum seçeneklerini seçebilirsiniz:

###  nuget aracılığıyla yükleyin

1.  NuGet'den Aspose.Cells'i arayın:[Aspose.Cells for .NET NuGet Paket](https://www.nuget.org/packages/Aspose.Cells/). 
Ayrıca VS2022'deki Nuget paket yöneticisinden Aspose.Cells'i de yükleyebilirsiniz.

2. "SkiaSharp" veya "System.Drawing.Common", projenizdeki "Target OS" yapılandırmasına bağlı olarak .Net6 platformları için Aspose.Cells 22.10.1 veya sonraki bir bağımlılık olarak otomatik olarak yüklenecektir.
- Projeniz için "Target OS"yi "Windows" olarak ayarlayın, .Net6 projesi için "System.Drawing.Common"u Windows sisteminize bağımlılık olarak kullanacaksınız. Bu konfigürasyonda çizimin sonucu .netcore31 veya öncesine yakındır.
**![Hedef işletim sistemini yapılandır](TargetOS.png)**
-  Projeniz için "Hedef İşletim Sistemi"ni "Yok" veya diğer seçeneklere ayarlayın, .Net6 projesi için Windows sisteminize bağımlılık olarak "SkiaSharp"ı kullanacaksınız.*Bağımlılık olarak "SkiaSharp" kullanan sürümün yazıcıya yazdırma özelliğini desteklemediğini lütfen unutmayın.*

###  Msi veya DLL aracılığıyla yükleyin

1. [Aspose.Cells.msi veya DLL dosyasını indirin](https://releases.aspose.com/cells/net/)

2. Kurulum dizinini veya DLL dizinini açın ve ardından aşağıdaki 3 veya 4. adımı seçin:

3. "net6.0-windows" alt dizinini bulun, içindeki Aspose.Cells.dll dosyasını .net6 uygulamanıza ekleyin. Aşağıdaki nuget paketlerini .net6 projenize manuel olarak ekleyin:
- System.Drawing.Common, 4.7.0.
- Sistem.Güvenlik.Şifreleme.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages, 4.7.0.

Bu sayede .Net6 projesi için Windows sisteminize bağımlılık olarak "System.Drawing.Common" kullanacaksınız. Bu konfigürasyonda çizimin sonucu .netcore31 veya öncesine yakındır.

4. "net6.0" alt dizinini bulun ve içindeki Aspose.Cells.dll dosyasını .net6 uygulamanıza ekleyin. Aşağıdaki nuget paketlerini .net6 projenize manuel olarak ekleyin:
- SkiaSharp, 2.88.6.
- Sistem.Güvenlik.Şifreleme.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages, 4.7.0.

 Bu sayede .Net6 projesi için "SkiaSharp"ı Windows sisteminize bağımlılık olarak kullanacaksınız.*Bağımlılık olarak "SkiaSharp" kullanan sürümün yazıcıya yazdırma özelliğini desteklemediğini lütfen unutmayın.*
##  Linux'ta .Net6 için Aspose.Cells'i çalıştırın

Windows'deki kurulum yöntemine bakın, SkiaSharp'ı yalnızca Linux sisteminde grafik kitaplığı bağımlılığı olarak seçebilirsiniz.

SkiaSharp'ın Linux altında doğru kullanımını sağlamak için aşağıdaki ek işlemleri yapmanız gerekir:

1. Linux Sisteminizde aşağıdaki komutu çalıştırın:
```
apt-get update && apt-get install -y libfontconfig1
```
OR
```
apk update && apk add fontconfig 
```

2. nuget "SkiaSharp.NativeAssets.Linux 2.88.6" paketlerini .net6 projenize ekleyin.

3. Veya yukarıdaki iki adım yerine .net6 projenize nuget "SkiaSharp.NativeAssets.Linux.NoDependegency 2.88.6" paketini eklemeyi seçebilirsiniz.

###  Ubuntu için Örnek Docker dosyası

1. nuget "SkiaSharp.NativeAssets.Linux 2.88.6" paketlerini .net6 projenize ekleyin.

2. Aşağıdaki Docker dosyasını kullanın:
{{< highlight "plain" >}}
#  Ubuntu 20.04
FROM mcr.microsoft.com/dotnet/runtime:6.0-focal AS base
WORKDIR /app

#  add "libfontconfig1" package if using "SkiaSharp.NativeAssets.Linux" in your project
#  Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apt-get update && apt-get install -y libfontconfig1

#  Copy fonts from local to docker
#  For example, put a "fonts" folder in your project folder, and put the font files in it,
#  then, use the following line:
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

###  Alpine için örnek Docker dosyası

1. nuget "SkiaSharp.NativeAssets.Linux 2.88.6" paketlerini .net6 projenize ekleyin.

2. Aşağıdaki Docker dosyasını kullanın:
{{< highlight "plain" >}}
# Alpine 3.16
FROM mcr.microsoft.com/dotnet/runtime:6.0-alpine3.16 AS base
WORKDIR /app

#  add "fontconfig" package if using "SkiaSharp.NativeAssets.Linux" in your project
#  Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apk update && apk add fontconfig 

#  Copy fonts from local to docker
#  For example, put a "fonts" folder in your project folder, and put the font files in it,
#  then, use the following line:
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
