---
title: Comment exécuter Aspose.Cells dans Docker
type: docs
description: Exécutez Aspose.Cells dans un conteneur Docker pour Linux, Windows Server et n'importe quel système d'exploitation.
weight: 139
url: /fr/net/how-to-run-aspose-cells-in-docker/
---
Les microservices, associés à la conteneurisation, permettent de combiner facilement les technologies. Docker vous permet d'intégrer facilement la fonctionnalité Aspose.Cells dans votre application, quelle que soit la technologie de votre pile de développement.

Si vous ciblez des microservices, ou si la technologie principale de votre pile n'est pas .NET, C++ ou Java, mais que vous avez besoin de la fonctionnalité Aspose.Cells, ou si vous utilisez déjà Docker dans votre pile, vous pourriez être intéressé à utiliser Aspose.Cells dans un Docker récipient.

## Conditions préalables

- Docker doit être installé sur votre système. Pour plus d'informations sur l'installation de Docker sur Windows ou Mac, reportez-vous aux liens de la section "Voir aussi".

- Notez également que Visual Studio 2019, .NET Core 3.1 SDK est utilisé dans l'exemple fourni ci-dessous.


## Hello World Demande

Dans cet exemple, vous créez une simple application de console Hello World qui crée un "Hello World!" document et l'enregistre dans tous les formats d'enregistrement pris en charge. L'application peut ensuite être créée et exécutée dans Docker.

### Création de l'application console

Pour créer le programme Hello World, suivez les étapes ci-dessous :
1. Une fois Docker installé, assurez-vous qu'il utilise des conteneurs Linux (par défaut). Si nécessaire, sélectionnez l'option Passer aux conteneurs Linux dans le menu Docker Desktops.
1. Dans Visual Studio, créez une application console .NET Core.<br>
![tâche : image_autre_texte](create-a-new-project.png)<br>
1. Installez la dernière version Aspose.Cells à partir de NuGet. System.Drawing.Common et System.Text.Encoding.CodePages seront installés en tant que dépendance de Aspose.Cells.<br>
![tâche : image_autre_texte](nuget-aspose-cells.png)<br>
1. Étant donné que l'application sera exécutée sur Linux, les actifs Linux natifs appropriés doivent être installés. Commencez avec l'image de base dotnet core sdk 3.1 et installez libgdiplus libc6-dev.
1. Lorsque toutes les dépendances requises sont ajoutées, écrivez un programme simple qui crée un "Hello World!" classeur et l'enregistre dans tous les formats d'enregistrement pris en charge :<br>
**.NET**<br>
{{< highlight "csharp" >}}
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

Notez que le dossier "TestOut" est spécifié comme dossier de sortie pour enregistrer les documents de sortie. Lors de l'exécution de l'application dans Docker, un dossier sur la machine hôte sera monté sur ce dossier dans le conteneur. Cela vous permettra de visualiser facilement la sortie générée par Aspose.Cells dans le conteneur Docker.

### Configuration d'un Dockerfile

L'étape suivante consiste à créer et configurer le Dockerfile.

1. Créez le Dockerfile et placez-le à côté du fichier de solution de votre application. Conservez ce nom de fichier sans extension (valeur par défaut).
1. Dans le Dockerfile, spécifiez :

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

Ce qui précède est un simple Dockerfile, qui contient les instructions suivantes :

- L'image SDK à utiliser. Voici l'image .Net Core SDK 3.1. Docker le téléchargera lors de l'exécution de la construction. La version du SDK est spécifiée sous forme de balise.
- Installez les polices car l'image du SDK contient très peu de polices. La commande copie les fichiers de police de l'image locale vers l'image Docker. Assurez-vous d'avoir un répertoire "fonts" local contenant toutes les polices que vous devez installer. Dans cet exemple, le répertoire local "fonts" est placé dans le même répertoire que le Dockerfile.
- Le répertoire de travail, qui est spécifié à la ligne suivante.
- La commande pour tout copier dans le conteneur, publier l'application et spécifier le point d'entrée.
- La commande d'installation de libgdiplus est exécutée dans le conteneur. Ceci est requis par System.Drawing.Common.

### Construire et exécuter l'application dans Docker

L'application peut maintenant être créée et exécutée dans Docker. Ouvrez votre invite de commande préférée, changez de répertoire dans le dossier avec l'application (dossier où sont placés le fichier de solution et le Dockerfile) et exécutez la commande suivante :

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

La première fois que cette commande est exécutée, cela peut prendre plus de temps, car Docker doit télécharger les images requises. Une fois la commande précédente terminée, exécutez la commande suivante :

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

Faites attention à l'argument de montage, car, comme mentionné précédemment, un dossier sur la machine hôte est monté dans le dossier du conteneur, pour voir facilement les résultats de l'exécution de l'application. Les chemins sous Linux sont sensibles à la casse.

{{% /alert %}}

## Images prenant en charge Aspose.Cells

- Aspose.Cells for .NET La norme ne prend pas en charge EMF et TIFF sous Linux.


## Plus d'exemples

***1. Pour exécuter l'application dans Windows Server 2019***

- Fichier Docker

{{< highlight "plain" >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

- Créer une image Docker

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Exécuter l'image Docker

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. Pour exécuter l'application sous Linux***

- Écrivez un programme simple qui définit le dossier de polices, crée un "Hello World!" classeur et l'enregistre.

{{< highlight "csharp" >}}
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
- Fichier Docker

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.Fonts.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.Fonts.dll"]{{< /highlight >}}

- Créer une image Docker

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Exécuter l'image Docker

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## Voir également

- [Installez Docker Desktop sur Windows](https://docs.docker.com/docker-for-windows/install/)
- [Installer Docker Desktop sur Mac](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, SDK .NET Core 3.1](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- [Passer aux conteneurs Linux](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers) option
-  Informations complémentaires sur[.NET SDK principal](https://hub.docker.com/_/microsoft-dotnet-sdk)
