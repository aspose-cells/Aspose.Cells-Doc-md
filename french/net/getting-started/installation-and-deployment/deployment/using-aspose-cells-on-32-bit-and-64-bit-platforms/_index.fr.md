---
title: Utilisation de Aspose.Cells sur les plates-formes 32 bits et 64 bits
type: docs
weight: 10
url: /fr/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---
{{% alert color="primary" %}} 

Aspose.Cells est un composant .NET pur qui peut simplifier votre processus de déploiement en utilisant le déploiement XCOPY. Pour installer Aspose.Cells, vous pouvez simplement copier l'assemblage du composant (Aspose.Cells.dll) dans un répertoire pour votre application : l'application peut commencer à l'utiliser immédiatement. Cela est possible en raison de la nature auto-descriptive des composants .NET. Ce type de déploiement n'a également aucun impact sur le processus d'installation.

{{% /alert %}} 
## **Déploiement**
Aspose.Cells prend en charge les environnements 32 bits et 64 bits. Lorsque vous installez le composant Aspose.Cells for .NET à l'aide du programme d'installation MSI Aspose.Cells, différentes DLL sont ajoutées à différents dossiers dans le ou les dossiers Aspose.Cells ${installation_Path}. Consultez la description dans le tableau du dossier contenant les assemblages que vous devez utiliser avec une version particulière du Framework .NET.

|**Dossier**|**Description**|
|:- |:- |
|net2.0|Contient des assemblys à utiliser avec .NET Framework 2.0, 3.0, 3.5, 4.0 et Mono. Ce sont les assemblys que vous devez normalement utiliser pour les environnements 32 bits et 64 bits.|
|net2.0_AuthenticodeSigned|Comme ci-dessus, mais les assemblages sont signés numériquement avec Authenticode. Les assemblys signés peuvent se charger plus lentement que sans Authenticode|
|net3.5_ClientProfile|Contient des assemblys à utiliser avec le profil client .NET Framework 3.5 ou 4.0.|
|net3.5_Profil client_AuthenticodeSigned|Comme ci-dessus, mais les assemblages sont signés numériquement avec Authenticode. Les assemblys signés peuvent se charger plus lentement que sans Authenticode.|
|net3.5|Contient des assemblys à utiliser avec .NET Framework 3.5 ou 4.0.|
|net3.5_AuthenticodeSigned|Comme ci-dessus, mais les assemblages sont signés numériquement avec Authenticode. Les assemblys signés peuvent se charger plus lentement que sans Authenticode.|
|net4.0|Contient des assemblys à utiliser avec .NET Framework 4.0 et 4.5.|
|netStandard|Contient des assemblys à utiliser avec .Net Standard 2.0|
|netcoreapp2.1|Contient des assemblys à utiliser avec .Net core 2.1|
|Xamarin.iOS|Contient des assemblys à utiliser avec Xamarin.iOS|
|Xamarin.Android|Contient des assemblys à utiliser avec Xamarin.Android|
|net5.0|Contient des assemblys à utiliser avec .net5.0.|
|net6.0|Contient des assemblys à utiliser avec .net6.0.|
{{% alert color="primary" %}} 

Dans les projets VS.NET (par exemple 2005, 2008, 2010, 2012, etc.), lors de l'ajout d'une référence à Aspose.Cells, la boîte de dialogue Ajouter une référence fait référence aux fichiers Aspose.Cells.dll dans le(s) dossier(s) net2.0 ou net3.5 respectivement. (Pour plus de références, lisez Référencement Aspose.Cells à partir d'un projet .NET.) Vous pouvez modifier la référence à la bibliothèque en fonction de votre environnement. Veuillez noter que si le framework cible du projet est .NET Framework 3.5/4 Client Profile, utilisez le fichier de composant Aspose.Cells.dll situé dans le dossier net_ClientProfile.

{{% /alert %}}
