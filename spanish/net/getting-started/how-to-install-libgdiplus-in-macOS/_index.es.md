---
title: Cómo instalar libgdiplus en macOS
type: docs
description: "Este artículo explica cómo instalar libgdiplus en macOS, como Monterey 12.4."
weight: 150
url: /es/net/how-to-install-libgdiplus-in-macos/
---

## Resumen

En algunas situaciones, puede optar por usar Aspose.Cells y confiar en la biblioteca gráfica System.Drawing.Common. Esta situación ocurre a menudo en versiones anteriores de .netcore (por ejemplo, .netcore31 o anteriores).

Dado que la biblioteca gráfica System.Drawing.Common necesita depender de libgdiplus, este artículo explica cómo instalar libgdiplus en macOS.

## Instalar Homebrew en macOS

Primero, puedes instalar Homebrew en macOS ejecutando el siguiente comando en Terminal.

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## Instalar libgdiplus en macOS

Después de instalar Homebrew, puede instalar libgdiplus en macOS:

```cs

brew install mono-libgdiplus

```

## Solución recomendada

Para las plataformas .NET6 (o posterior), en comparación con plataformas anteriores (.netcore31 o antes), una diferencia importante es sobre la biblioteca gráfica. 
En este [Documento oficial de Microsoft](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), explica que para .NET6 o versiones posteriores la biblioteca gráfica "System.Drawing.Common" solo será compatible en Windows, y da recomendaciones para reemplazar la biblioteca gráfica.

Por lo tanto, Aspose.Cells ofrece una solución que depende de la biblioteca gráfica SkiaSharp en plataformas no Windows. Recomendamos usar SkiaSharp como biblioteca en macOS, lo que también significa que no es necesario instalar libgdiplus.

Para obtener información sobre cómo instalar Aspose.Cells en plataformas no Windows y usar SkiaSharp como biblioteca gráfica, por favor consulta el siguiente artículo:
[Cómo ejecutar Aspose.Cells para .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
