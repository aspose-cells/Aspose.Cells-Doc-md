---
title: Comment utiliser Aspose.Cells.GridWeb avec .NET Core
type: docs
weight: 40
url: /fr/net/how-to-use-aspose-cells-gridweb-with-net-core/
---
{{% alert color="primary" %}} 

Cette rubrique explique comment utiliser Aspose.Cells.GridWeb avec les applications .NET Core à l'aide de Visual Studio.NET 2019. Cette rubrique est utile pour les développeurs débutants travaillant avec Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Utilisez Aspose.Cells.GridWeb avec .NET Core**
Cette rubrique montre comment utiliser Aspose.Cells.GridWeb en créant un exemple de site Web dans Visual Studio 2019. Le processus a été divisé en étapes.
### **Étape 1 : Création d'un nouveau projet**
1. Ouvrez Visual Studio 2019.
1.  Du**Dossier** menu, sélectionnez**Nouveau** , alors**Projet**.
 La boîte de dialogue Créer un nouveau projet s'ouvre.
1.  Sélectionner**ASP.NET Application Web de base** à partir des modèles de projet installés dans Visual Studio et cliquez sur**Prochain**.

![tâche : image_autre_texte](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1.  Spécifiez un emplacement où l'emplacement et le nom du projet et cliquez sur**Créer**.

![tâche : image_autre_texte](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1.  Sélectionnez le**Application Web (Modèle-Vue-Contrôleur)** modèle et assurez-vous que**ASP .NET Noyau 2.1** est sélectionné.

![tâche : image_autre_texte](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1.  Cliquez sur**Créer**.
### **Étape 2 : Vérification de la vue initiale**
L'exécution du projet nouvellement créé affiche le modèle par défaut dans le navigateur, comme indiqué dans l'image ci-dessous.



![tâche : image_autre_texte](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **Étape 3 : Ajout de Aspose.Cells.GridWeb**
1. Ajoutez les packages Nuget suivants au projet

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Ajouter le package Aspose.Cells.GridWeb

![tâche : image_autre_texte](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Ajoutez ce qui suit au fichier **_ViewImports.cshtml** dans le dossier Views.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

Le fichier ressemblera à ceci après les modifications

![tâche : image_autre_texte](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. Placez le code suivant dans la méthode Index du HomeController.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

N'oubliez pas de mettre à jour les chemins SessionStorePath et ImportExcelFile.

{{% /alert %}} 

![tâche : image_autre_texte](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1.  Ajoutez le code suivant dans le**Index.cshtml** fichier dans le répertoire Affichage > Accueil.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

Le fichier ressemblera à ceci après le changement.

![tâche : image_autre_texte](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Ajoutez la prise en charge de Session et GridScheduedService dans le fichier Startup.cs
 1. Ajoutez l'extrait de code suivant dans la méthode ConfigureServices.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![tâche : image_autre_texte](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. Ajoutez l'extrait de code suivant dans la méthode Configure.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![tâche : image_autre_texte](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. Mettez le dernier acw_client dans le répertoire : **wwwroot/js** {{% alert color="primary" %}} {{% /alert %}}
1.  Ajouter**Contrôleur Acw**dans les contrôleurs pour gérer la carte de route acw qui peut fournir toutes les opérations par défaut pour une action d'édition générale.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![tâche : image_autre_texte](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **Étape 4 : Testez l'application**
L'exécution de l'application donnera une sortie similaire à celle illustrée dans l'image ci-dessous.

![tâche : image_autre_texte](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
