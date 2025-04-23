---
title: Comment exécuter Aspose.Cells pour .Net6
type: docs
description: "Comment exécuter Aspose.Cells pour .Net6."
weight: 138
url: /fr/net/how-to-run-aspose-cells-for-net6/
---

## Aperçu

Pour les plates-formes .NET6 (ou ultérieures), comparé aux plates-formes précédentes (.netcore31 ou antérieures), une différence importante concerne la bibliothèque graphique. 
Dans ce document officiel de [Microsoft](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), il est expliqué que pour les versions .NET6 ou ultérieures, la bibliothèque graphique "System.Drawing.Common" sera uniquement prise en charge sur Windows, et donne des recommandations pour remplacer la bibliothèque graphique.

Pour le produit Aspose.Cells, nous avons effectué l'évaluation et avons terminé la migration de la bibliothèque graphique. Nous utilisons SkiaSharp au lieu de System.Drawing.Common dans les systèmes non-Windows, comme suggéré dans la documentation officielle de Microsoft. Veuillez noter que ce changement critique prendra effet dans Aspose.Cells 22.10.1 ou ultérieur pour .Net6.

Pour .netcore31 ou antérieur, pour la compatibilité et la stabilité, nous utilisons actuellement la bibliothèque graphique "System.Drawing.Common". Les dépendances pour .netcore31 ou antérieur sont les suivantes :
- System.Drawing.Common, 5.0.3.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

## Exécuter Aspose.Cells pour .Net6 sur Windows

Tout d'abord, vous pouvez créer une application .net6 avec VS2022, puis vous pouvez choisir les options d'installation suivantes :

### Installer via nuget

1. Recherchez Aspose.Cells dans NuGet : [Paquet NuGet Aspose.Cells for .NET](https://www.nuget.org/packages/Aspose.Cells/). 
Vous pouvez également installer Aspose.Cells depuis le gestionnaire de paquets NuGet dans VS2022.

2. "SkiaSharp" ou "System.Drawing.Common" seront installés automatiquement en tant que dépendance de Aspose.Cells 22.10.1 ou ultérieur pour les plateformes .Net6, en fonction de la configuration "Système cible" dans votre projet.
- Définissez le « Système d'exploitation cible » sur « Windows » pour votre projet, vous utiliserez « System.Drawing.Common » comme dépendance sur votre système Windows pour le projet .Net6. Dans cette configuration, le résultat du dessin se rapproche de .netcore31 ou avant.
**![Cible de configuration OS](TargetOS.png)**
- Définissez le « Système d'exploitation cible » sur « Aucun » ou d'autres options pour votre projet, vous utiliserez « SkiaSharp » comme dépendance sur votre système Windows pour le projet .Net6. *Veuillez noter que la version qui utilise « SkiaSharp » comme dépendance ne prend pas en charge la fonction d'impression sur l'imprimante.*

### Installation via msi ou DLL

1. [Téléchargez Aspose.Cells.msi ou DLL](https://releases.aspose.com/cells/net/)

2. Ouvrez le répertoire d'installation ou le répertoire DLL, puis sélectionnez l'étape 3 ou 4 ci-dessous :

3. localisez le sous-répertoire « net6.0-windows », ajoutez le fichier Aspose.Cells.dll pour votre application .net6. Ajoutez manuellement les packages NuGet suivants à votre projet .net6 :
- System.Drawing.Common, 6.0.0.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

De cette manière, vous utiliserez « System.Drawing.Common » comme dépendance sur votre système Windows pour le projet .Net6. Dans cette configuration, le résultat du dessin se rapproche de .netcore31 ou avant.

4. localisez le sous-répertoire « net6.0 », ajoutez le fichier Aspose.Cells.dll pour votre application .net6. Ajoutez manuellement les packages NuGet suivants à votre projet .net6 :
- SkiaSharp, 3.116.1.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

De cette manière, vous utiliserez « SkiaSharp » comme dépendance sur votre système Windows pour le projet .Net6. *Veuillez noter que la version qui utilise « SkiaSharp » comme dépendance ne prend pas en charge la fonction d'impression sur l'imprimante.*
## Exécution d'Aspose.Cells pour .Net6 sur Linux

Consultez la méthode d'installation sur Windows, vous pouvez uniquement sélectionner SkiaSharp comme dépendance de bibliothèque graphique sur le système Linux.

Vous devez effectuer les opérations supplémentaires suivantes pour assurer l'utilisation correcte de SkiaSharp sous Linux :

1. Exécutez la commande suivante sur votre système Linux :
```
apt-get update && apt-get install -y libfontconfig1
```
OU
```
apk update && apk add fontconfig 
```

2. Ajoutez le pacote NuGet "SkiaSharp.NativeAssets.Linux 3.116.1" à votre projet .net6.
3. Ou vous pouvez choisir d'ajouter le pacote NuGet "SkiaSharp.NativeAssets.Linux.NoDependencies 3.116.1" à votre projet .net6, au lieu des deux étapes ci-dessus.

*Veuillez noter que la version du package ajouté "SkiaSharp.NativeAssets.Linux" ou "SkiaSharp.NativeAssets.Linux.NoDependencies" doit correspondre à la version de "SkiaSharp" référencée par Aspose.Cells for .NET. Les versions de Aspose.Cells for .NET et les versions correspondantes de "SKiaSharp" référencées sont décrites comme suit :*

| Aspose.Cells for .NET |                SkiaSharp                |
| :--------------------: | :-------------------------------------: |
| >= 22.10.1 && <= 22.11 |                 2.88.0                  |
|  >= 22.12 && <= 23.9   |                 2.88.3                  |
|  >= 23.10 && <= 24.12  |                 2.88.6                  |
|        = 25.1.1        |                 3.116.1                 |
|        >=25.1.2        | 2.88.9 (net6.0, net8.0), 3.116.1 (net9.0) |



### Exemple de Dockerfile pour Ubuntu

1. Ajoutez le pacote NuGet "SkiaSharp.NativeAssets.Linux 3.116.1" à votre projet .net6.

2. Utilisez le Dockerfile suivant :
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

### Exemple de Dockerfile pour Alpine

1. Ajoutez le pacote NuGet "SkiaSharp.NativeAssets.Linux 3.116.1" à votre projet .net6.

2. Utilisez le Dockerfile suivant :
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
