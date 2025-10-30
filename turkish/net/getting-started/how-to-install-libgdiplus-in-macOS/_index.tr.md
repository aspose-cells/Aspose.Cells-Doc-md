---
title: macOS ta libgdiplus Nasıl Kurulur
type: docs
description: "Bu makale, Monterey 12.4 gibi macOS ta libgdiplus ın nasıl kurulacağını açıklar."
weight: 150
url: /tr/net/how-to-install-libgdiplus-in-macos/
---

## Genel Bakış

Bazı durumlarda, Aspose.Cells kullanabilir ve System.Drawing.Common grafik kütüphanesine güvenebilirsiniz. Bu durum genellikle .netcore'un eski sürümlerinde (örneğin .netcore31 veya öncesi) meydana gelir.

System.Drawing.Common grafik kütüphanesi libgdiplus bağımlılığı gerektirdiği için, bu makalede macOS'ta libgdiplus'un nasıl kurulacağı anlatılmaktadır.

macOS'ta Homebrew Nasıl Kurulur

İlk olarak, Terminal'da aşağıdaki komutu çalıştırarak macOS'ta Homebrew kurabilirsiniz.

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

macOS'ta libgdiplus Nasıl Kurulur

Homebrew'u kurduktan sonra, macOS'ta libgdiplus'u kurabilirsiniz:

```cs

brew install mono-libgdiplus

```

## Önerilen çözüm

.NET6 (veya sonrası) platformları için, önceki platformlarla (örneğin .netcore31 veya önceki sürümler) karşılaştırıldığında önemli bir fark grafik kütüphanesiyle ilgilidir. 
Bu resmi [Microsoft Belgesi](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only) .NET6 veya sonraki sürümler için grafik kütüphanesi "System.Drawing.Common"'ın sadece Windows'ta destekleneceğini açıklar ve grafik kütüphanesini değiştirmek için öneriler sunar.

Yani, Aspose.Cells, Windows olmayan platformlarda SkiaSharp grafik kütüphanesine dayanan bir çözüm sağlar. macOS'ta kütüphane olarak SkiaSharp kullanmanızı öneririz, bu da libgdiplus kurulumuna gerek olmadığı anlamına gelir.

Aspose.Cells'in Windows olmayan platformlara nasıl kurulacağı ve SkiaSharp'ı grafik kütüphanesi olarak nasıl kullanacağınız hakkında bilgi için aşağıdaki makaleye bakabilirsiniz:
[Aspose.Cells for .Net6 Nasıl Çalıştırılır](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
