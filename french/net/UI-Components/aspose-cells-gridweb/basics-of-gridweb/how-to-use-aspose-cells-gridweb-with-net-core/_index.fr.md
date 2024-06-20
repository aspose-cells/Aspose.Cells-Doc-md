---
title: Comment utiliser Aspose.Cells.GridWeb avec .NET Core
type: docs
weight: 40
url: /fr/net/aspose-cells-gridweb/how-to-use-aspose-cells-gridweb-with-net-core/
keywords: GridWeb,dotnetcore
description: Cet article présente comment utiliser GridWeb dans une application Web .NET Core
---

{{% alert color="primary" %}} 

Ce sujet explique comment utiliser Aspose.Cells.GridWeb avec des applications .NET Core à l'aide de Visual Studio.NET 2019. Ce sujet est utile pour les développeurs débutants travaillant avec Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Utiliser Aspose.Cells.GridWeb avec .NET Core**
Ce sujet montre comment utiliser Aspose.Cells.GridWeb en créant un site Web exemple dans Visual Studio 2019. Le processus a été divisé en étapes.
### **Étape 1: Créer un nouveau projet**
1. Ouvrez Visual Studio 2019.
1. Dans le menu **Fichier**, sélectionnez **Nouveau**, puis **Projet**.
   La boîte de dialogue Créer un nouveau projet est ouverte.
1. Sélectionnez **Application Web ASP.NET Core** dans les modèles de projet installés de Visual Studio et cliquez sur **Suivant**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1. Spécifiez un emplacement où se trouve le nom du projet et cliquez sur **Créer**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1. Sélectionnez le modèle **Application Web (Modèle-Vue-Contrôleur)** et assurez-vous que **ASP .NET Core 2.1** est sélectionné. 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1. Cliquez sur **Créer**.
### **Étape 2 : Vérifier la vue initiale**
L'exécution du projet nouvellement créé affiche le modèle par défaut dans le navigateur, comme indiqué dans l'image ci-dessous.



![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **Étape 3: Ajout d'Aspose.Cells.GridWeb**
1. Ajoutez les packages Nuget suivants au projet

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Ajouter le package Aspose.Cells.GridWeb

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Ajoutez ce qui suit au fichier **_ViewImports.cshtml** dans le dossier Views.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

Le fichier ressemblera à ceci après les modifications

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. Placez le code suivant dans la méthode Index du contrôleur HomeController.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

N'oubliez pas de mettre à jour le chemin SessionStorePath et le chemin ImportExcelFile.

{{% /alert %}} 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1. Ajoutez le code suivant dans le fichier **Index.cshtml** dans le répertoire View > Home.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

Le fichier ressemblera à ceci après le changement.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Ajoutez la prise en charge de Session et GridScheduedService dans le fichier Startup.cs
   1. Ajoutez l'extrait de code suivant dans la méthode ConfigureServices.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. Ajoutez l'extrait de code suivant dans la méthode Configure.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. Mettez à jour le dernier acw_client dans le répertoire : **wwwroot/js** {{% alert color="primary" %}}   {{% /alert %}}
1. Ajoutez **AcwController** dans les contrôleurs pour gérer la carte de routage acw qui peut fournir toutes les opérations par défaut pour l'action d'édition générale.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **Étape 4: Testez l'application**
L'exécution de l'application produira une sortie similaire à celle présentée dans l'image ci-dessous.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
