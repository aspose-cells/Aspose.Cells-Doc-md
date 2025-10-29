---
title: Comment installer libgdiplus sur macOS
type: docs
description: "Cet article explique comment installer libgdiplus sur macOS, tel que Monterey 12.4."
weight: 150
url: /fr/net/how-to-install-libgdiplus-in-macos/
---

## Aperçu

Dans certaines situations, vous pouvez choisir d’utiliser Aspose.Cells et de dépendre de la bibliothèque graphique System.Drawing.Common. Cette situation survient souvent dans les versions antérieures de .NET Core (par exemple .NET Core 3.1 ou versions antérieures).

Étant donné que la bibliothèque graphique System.Drawing.Common dépend de libgdiplus, cet article explique comment installer libgdiplus sur macOS.

## Installer Homebrew dans macOS

Tout d’abord, vous pouvez installer Homebrew sur macOS en exécutant la commande suivante dans Terminal.

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## Installer libgdiplus dans macOS

Après avoir installé Homebrew, vous pouvez installer libgdiplus dans macOS :

```cs

brew install mono-libgdiplus

```

## Solution recommandée

Pour les plates-formes .NET6 (ou ultérieures), comparé aux plates-formes précédentes (.netcore31 ou antérieures), une différence importante concerne la bibliothèque graphique. 
Dans ce document officiel de [Microsoft](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), il est expliqué que pour les versions .NET6 ou ultérieures, la bibliothèque graphique "System.Drawing.Common" sera uniquement prise en charge sur Windows, et donne des recommandations pour remplacer la bibliothèque graphique.

Ainsi, Aspose.Cells fournit une solution basée sur la bibliothèque graphique SkiaSharp sur les plateformes non-Windows. Nous recommandons d’utiliser SkiaSharp comme bibliothèque sur macOS, ce qui signifie également qu’il n’est pas nécessaire d’installer libgdiplus.

Pour plus d’informations sur l’installation d’Aspose.Cells sur des plateformes non-Windows et l’utilisation de SkiaSharp comme bibliothèque graphique, veuillez consulter l’article suivant :
[Comment exécuter Aspose.Cells pour .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
