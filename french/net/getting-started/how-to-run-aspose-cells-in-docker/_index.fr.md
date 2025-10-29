---
title: Comment exécuter Aspose.Cells dans Docker
type: docs
description: "Exécutez Aspose.Cells dans un conteneur Docker pour Linux, Windows Server et tout autre système d exploitation."
weight: 139
url: /fr/net/how-to-run-aspose-cells-in-docker/
---

Les microservices, conjointement avec la conteneurisation, permettent de combiner facilement les technologies. Docker vous permet d'intégrer facilement la fonctionnalité Aspose.Cells dans votre application, quelle que soit la technologie utilisée dans votre pile de développement.

Si vous visez les microservices, ou si la technologie principale de votre pile n'est pas .NET, C++ ou Java, mais que vous avez besoin de la fonctionnalité Aspose.Cells, ou si vous utilisez déjà Docker dans votre pile, alors vous pourriez être intéressé par l'utilisation Aspose.Cells dans un conteneur Docker.

## Prérequis

- Docker doit être installé sur votre système. Pour des informations sur l'installation de Docker sur Windows ou Mac, reportez-vous aux liens dans la section "Voir aussi".

- De plus, notez que Visual Studio 2019, .NET Core 3.1 SDK est utilisé dans l'exemple ci-dessous.


## Application Hello World

Dans cet exemple, vous créez une simple application console Hello World qui crée un document "Hello World!" et l'enregistre dans tous les formats d'enregistrement pris en charge. L'application peut ensuite être construite et exécutée dans Docker.

### Création de l'application Console

Pour créer le programme Hello World, suivez les étapes ci-dessous:
1. Une fois Docker est installé, assurez-vous qu'il utilise les conteneurs Linux (par défaut). Si nécessaire, sélectionnez l'option Changer pour les conteneurs Linux dans le menu de Docker Desktops.
1. In Visual Studio, create a .NET Core console application.<br>
![todo:image_alt_text](create-a-new-project.png)<br>
1. Install the latest Aspose.Cells version from NuGet. System.Drawing.Common and System.Text.Encoding.CodePages will be installed as a dependency of Aspose.Cells.<br>
![todo:image_alt_text](nuget-aspose-cells.png)<br>
1. Comme l'application sera exécutée sur Linux, les ressources natives Linux appropriées doivent être installées. Commencez par l'image de base dotnet core sdk 3.1 et installez libgdiplus libc6-dev.
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

Notez que le dossier "TestOut" est spécifié comme dossier de sortie pour sauvegarder les documents de sortie. Lors de l'exécution de l'application dans Docker, un dossier sur la machine hôte sera monté dans ce dossier du conteneur. Cela vous permettra de facilement visualiser la sortie générée par Aspose.Cells dans le conteneur Docker.

### Configuration d'un Dockerfile

La prochaine étape consiste à créer et configurer le Dockerfile.

1. Créez le Dockerfile et placez-le à côté du fichier de solution de votre application. Gardez ce nom de fichier sans extension (par défaut).
1. Dans le Dockerfile, spécifiez:

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

Ci-dessus se trouve un Dockerfile simple, contenant les instructions suivantes:

- L'image SDK à utiliser. Ici, il s'agit de l'image .Net Core SDK 3.1. Docker la téléchargera lors de l'exécution de la construction. La version du SDK est spécifiée en tant que balise.
- Installer les polices car l'image SDK contient très peu de polices. La commande copie les fichiers de police du local à l'image docker. Assurez-vous d'avoir un répertoire local de "polices" contenant toutes les polices dont vous avez besoin d'installer. Dans cet exemple, le répertoire local de "polices" est placé dans le même répertoire que le Dockerfile.
- Le répertoire de travail, qui est spécifié à la ligne suivante.
- La commande pour copier tout dans le conteneur, publier l'application et spécifier le point d'entrée.
- La commande pour installer libgdiplus est exécutée dans le conteneur. Ceci est requis par System.Drawing.Common.

### Construction et Exécution de l'Application dans Docker

Maintenant l'application peut être construite et exécutée dans Docker. Ouvrez votre invite de commande préférée, changez de répertoire vers le dossier de l'application (dossier où le fichier de solution et le Dockerfile sont placés) et exécutez la commande suivante:

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

La première fois que cette commande est exécutée, cela peut prendre plus de temps, car Docker doit télécharger les images requises. Une fois la commande précédente terminée, exécutez la commande suivante:

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

Faites attention à l'argument de montage, car, comme mentionné précédemment, un dossier sur la machine hôte est monté dans le dossier du conteneur, pour voir facilement les résultats de l'exécution de l'application. Les chemins sous Linux sont sensibles à la casse.

{{% /alert %}}

## Images Supportant Aspose.Cells

- Aspose.Cells for .NET Standard ne prend pas en charge EMF et TIFF sur Linux.


## Plus d'exemples

***1. Pour exécuter l'application dans Windows Server 2019***

- Dockerfile

{{< highlight plain >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

- Construire l'image Docker

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Exécuter l'image Docker

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. Pour exécuter l'application dans Linux***

- Écrire un programme simple qui définit le dossier de police, crée un classeur “Hello World!” et l'enregistre.

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

- Construire l'image Docker

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Exécuter l'image Docker

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

## Solution recommandée

Pour les plates-formes .NET6 (ou ultérieures), comparé aux plates-formes précédentes (.netcore31 ou antérieures), une différence importante concerne la bibliothèque graphique. 
Dans ce document officiel de [Microsoft](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), il est expliqué que pour les versions .NET6 ou ultérieures, la bibliothèque graphique "System.Drawing.Common" sera uniquement prise en charge sur Windows, et donne des recommandations pour remplacer la bibliothèque graphique.

Ainsi, Aspose.Cells fournit une solution qui repose sur la bibliothèque graphique SkiaSharp sur les plateformes non-Windows. Nous recommandons d'utiliser SkiaSharp comme bibliothèque sur macOS, ce qui signifie également qu'il n'est pas nécessaire d'installer libgdiplus.

Pour obtenir des informations sur l'installation d'Aspose.Cells sur les plateformes non-Windows et l'utilisation de SkiaSharp comme bibliothèque graphique, veuillez consulter l'article suivant :
[Comment exécuter Aspose.Cells pour .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

## Voir aussi

- [Installer Docker Desktop sur Windows](https://docs.docker.com/docker-for-windows/install/)
- [Installer Docker Desktop sur Mac](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- Option pour [passer aux conteneurs Linux](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers)
- Informations supplémentaires sur le [.NET Core SDK](https://hub.docker.com/_/microsoft-dotnet-sdk)
{{< app/cells/assistant language="csharp" >}}
