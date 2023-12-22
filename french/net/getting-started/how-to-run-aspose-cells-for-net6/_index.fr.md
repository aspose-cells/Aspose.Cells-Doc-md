---
title: Comment exécuter Aspose.Cells pour .Net6
type: docs
description: Comment exécuter Aspose.Cells pour .Net6
weight: 138
url: /fr/net/how-to-run-aspose-cells-for-net6/
---
##  Aperçu

 Pour les plates-formes .NET6 (ou ultérieures), par rapport aux plates-formes précédentes (.netcore31 ou antérieures), une différence importante concerne la bibliothèque graphique.
 Dans ce fonctionnaire[Microsoft Document](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), il explique que pour .NET6 ou les versions ultérieures, la bibliothèque graphique "System.Drawing.Common" ne sera prise en charge que sur Windows et donne des recommandations pour remplacer la bibliothèque graphique.

Pour le produit Apose.Cells, nous avons effectué l'évaluation et terminé la migration de la bibliothèque graphique. Nous utilisons SkiaSharp au lieu de System.Drawing.Common dans les systèmes non-Windows, comme suggéré dans la documentation officielle de Microsoft. Veuillez noter que ce changement critique prendra effet dans la version Aspose.Cells 22.10.1 ou version ultérieure pour .Net6.

Pour .netcore31 ou version antérieure, pour des raisons de compatibilité et de stabilité, nous utilisons toujours actuellement la bibliothèque graphique "System.Drawing.Common". Les dépendances pour .netcore31 ou version antérieure sont les suivantes :
- Système.Drawing.Common, 4.7.0.
- Système.Sécurité.Cryptographie.Pkcs, 5.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

##  Exécutez Aspose.Cells pour .Net6 sur Windows

Vous pouvez d’abord créer une application .net6 avec VS2022, puis choisir les options d’installation suivantes :

###  Installer via nuget

1.  Recherchez Aspose.Cells à partir de NuGet :[Aspose.Cells for .NET NuGet Paquet](https://www.nuget.org/packages/Aspose.Cells/). 
Vous pouvez également installer Aspose.Cells à partir du gestionnaire de packages Nuget dans VS2022.

2. "SkiaSharp" ou "System.Drawing.Common" sera installé automatiquement en tant que dépendance de Aspose.Cells 22.10.1 ou version ultérieure pour les plates-formes .Net6, qui dépend de la configuration du "OS cible" dans votre projet.
- Définissez le "OS cible" sur "Windows" pour votre projet, vous utiliserez "System.Drawing.Common" comme dépendance sur votre système Windows pour le projet .Net6. Dans cette configuration, le résultat du dessin est plus proche de .netcore31 ou antérieur.
**![Configurer le système d'exploitation cible](TargetOS.png)**
-  Définissez le "OS cible" sur "Aucun" ou d'autres options pour votre projet, vous utiliserez "SkiaSharp" comme dépendance sur votre système Windows pour le projet .Net6.*Veuillez noter que la version qui utilise « SkiaSharp » comme dépendance ne prend pas en charge la fonction d'impression sur imprimante.*

###  Installer via msi ou DLL

1. [Téléchargez Aspose.Cells.msi ou DLL](https://releases.aspose.com/cells/net/)

2. Ouvrez le répertoire d'installation ou le répertoire DLL, puis sélectionnez l'étape 3 ou 4 ci-dessous :

3. localisez le sous-répertoire "net6.0-windows", ajoutez-y le Aspose.Cells.dll à votre application .net6. Ajoutez manuellement les packages nuget suivants à votre projet .net6 :
- Système.Drawing.Common, 4.7.0.
- Système.Sécurité.Cryptographie.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages, 4.7.0.

De cette façon, vous utiliserez "System.Drawing.Common" comme dépendance de votre système Windows pour le projet .Net6. Dans cette configuration, le résultat du dessin est plus proche de .netcore31 ou antérieur.

4. localisez le sous-répertoire "net6.0", ajoutez-y le Aspose.Cells.dll à votre application .net6. Ajoutez manuellement les packages nuget suivants à votre projet .net6 :
- SkiaSharp, 2.88.6.
- Système.Sécurité.Cryptographie.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages, 4.7.0.

 De cette façon, vous utiliserez "SkiaSharp" comme dépendance sur votre système Windows pour le projet .Net6.*Veuillez noter que la version qui utilise « SkiaSharp » comme dépendance ne prend pas en charge la fonction d'impression sur imprimante.*
##  Exécutez Aspose.Cells pour .Net6 sous Linux

Reportez-vous à la méthode d'installation sur Windows, vous pouvez uniquement sélectionner SkiaSharp comme dépendance de bibliothèque graphique sur le système Linux.

Vous devez effectuer les opérations supplémentaires suivantes pour garantir une bonne utilisation de SkiaSharp sous Linux :

1. Exécutez la commande suivante sur votre système Linux :
```
apt-get update && apt-get install -y libfontconfig1
```
OR
```
apk update && apk add fontconfig 
```

2. Ajoutez les packages nuget « SkiaSharp.NativeAssets.Linux 2.88.6 » à votre projet .net6.

3. Ou vous pouvez choisir d'ajouter les packages nuget « SkiaSharp.NativeAssets.Linux.NoDependencies 2.88.6 » à votre projet .net6, au lieu des deux étapes ci-dessus.

###  Exemple de fichier Docker pour Ubuntu

1. Ajoutez les packages nuget "SkiaSharp.NativeAssets.Linux 2.88.6" à votre projet .net6.

2. Utilisez le fichier Docker suivant :
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

###  Exemple de fichier Docker pour Alpine

1. Ajoutez les packages nuget "SkiaSharp.NativeAssets.Linux 2.88.6" à votre projet .net6.

2. Utilisez le fichier Docker suivant :
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
