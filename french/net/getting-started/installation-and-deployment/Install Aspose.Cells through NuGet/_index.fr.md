---
title: Installer Aspose Cells via NuGet
type: docs
weight: 30
url: /fr/net/installation/
---


## **Installer Aspose.Cells for .NET via NuGet**
NuGet est le moyen le plus simple de télécharger et d'installer les API Aspose pour .NET. Ouvrez Microsoft Visual Studio et le gestionnaire de packages NuGet. Recherchez "aspose" pour trouver l'API Aspose souhaitée. Cliquez sur "Installer", l'API sélectionnée sera téléchargée et référencée dans votre projet.

Remarque : Vous pouvez visiter la page Web de NuGet pour Aspose.Cells pour plus d'informations : 
[Paquet NuGet Aspose.Cells for .NET](https://www.nuget.org/packages/Aspose.Cells/)

### **Installer Aspose.Cells en utilisant l'interface graphique du gestionnaire de packages**
Suivez ces étapes pour référencer le composant Aspose.Cells en utilisant l'interface graphique du gestionnaire de packages :

- Ouvrez votre solution/projet dans Visual Studio.
- Cliquez sur **Outils** -> **Gestionnaire de paquets NuGet** -> **Gérer les packages NuGet** depuis la Solution. Vous pouvez également accéder facilement à la même option par le biais de l'Explorateur de solutions. Cliquez avec le bouton droit sur la solution ou le projet et sélectionnez **Gérer les packages NuGet** dans le menu contextuel.
- Sélectionnez **En ligne** dans le menu de gauche et tapez "Aspose.Cells" dans la zone de recherche pour trouver le package Aspose.Cells .NET.
- Cliquez sur le bouton **Installer** à côté de l'entrée Aspose.Cells for .NET pour installer la dernière version dans votre projet.
### **Installer Aspose.Cells à l'aide de la Console du Gestionnaire de packages**
Vous pouvez suivre les étapes ci-dessous pour référencer le composant Aspose.Cells en utilisant la console du gestionnaire de packages :

- Ouvrez votre solution/projet dans Visual Studio.
- Sélectionnez **Outils** -> **Gestionnaire de paquets** -> **Console du Gestionnaire de packages** dans le menu pour ouvrir la console du gestionnaire de packages.
  - Tapez la commande "Install-Package Aspose.Cells" et appuyez sur Entrée pour installer la dernière version complète dans votre application. Alternativement, vous pouvez ajouter le suffixe "-prerelease" à la commande afin de spécifier que la dernière version incluant les correctifs est également à installer.
- Vous verrez apparaître le message "Téléchargement de Aspose.Cells..." en bas à gauche de la fenêtre indiquant que le téléchargement est en cours.
- Une fois le téléchargement terminé, vous verrez les messages de confirmation suivants. Si vous n'êtes pas familier avec l'EULA d'Aspose, il est conseillé de lire la licence référencée dans l'URL.
- Vous devriez maintenant constater que Aspose.Cells a été ajouté et référencé avec succès dans votre application.
## **Référencer Aspose.Cells à partir d'un projet .NET**
Pour utiliser Aspose.Cells dans une application, ajoutez une référence. Pour ajouter une référence à l'aide de Visual Studio :

1. Dans l'**Explorateur de solutions**, développez le nœud du projet auquel vous souhaitez ajouter une référence.
1. Cliquez avec le bouton droit sur le nœud **Références** du projet et sélectionnez **Ajouter une référence** dans le menu.
1. Dans la boîte de dialogue **Ajouter une référence**, sélectionnez l'onglet .NET (sélectionné par défaut). Si vous l'avez installé à l'aide du programme d'installation MSI, Aspose.Cells apparaîtra dans le volet supérieur.
1. Sélectionnez-le et cliquez sur **Sélectionner**.

Si vous avez téléchargé ou décompressé uniquement le fichier DLL :

1. Localisez le fichier Aspose.Cells.dll en utilisant le bouton **Parcourir**. Aspose.Cells devrait apparaître dans le volet **Composants sélectionnés** de la boîte de dialogue.
1. Cliquez sur **OK**. La référence à Aspose.Cells apparaîtra sous le nœud **Références** du projet.
### **Faire référence au composant à partir d'un projet Profil client VS.NET 2010**
Si le framework cible de votre projet est .NET Framework 3.5/4 Profil client, utilisez le fichier de composant Aspose.Cells.dll situé dans le dossier net_ClientProfile de votre répertoire d'installation. Par exemple :

- Dans **Explorateur de solutions** de VS.NET 2010 pour votre projet, cliquez avec le bouton droit sur **Références** et sélectionnez **Ajouter une référence**.
- Sélectionnez l'onglet **Parcourir** dans la boîte de dialogue et cliquez sur la liste déroulante Rechercher.
- Trouvez et sélectionnez le fichier de composant Aspose.Cells.dll dans votre répertoire d'installation, par exemple: .../Program Files/Aspose/Aspose.Cells for .NET/Bin/net_ClientProfile/ **(Assurez-vous d'avoir installé le produit à l'aide de l'installateur MSI sur votre machine.)**
- Cliquez sur **OK** pour fermer la boîte de dialogue

{{% alert color="primary" %}} 

Si le framework cible de votre projet VS.NET 2010 est ".NET Framework 4" ou autre, utilisez simplement le fichier de composant Aspose.Cells.dll situé dans le dossier net4.0/net2.0.

{{% /alert %}} 
## **Faire référence aux contrôles de grille Aspose.Cells depuis un projet .NET**
Pour utiliser un contrôle de grille dans votre application, ajoutez une référence. Pour faire référence à un contrôle de grille dans Visual Studio, faites ce qui suit :

- Dans **l'Explorateur de solutions**, développez le nœud du projet auquel vous voulez ajouter une référence.
- Cliquez avec le bouton droit sur le nœud **Références** du projet et sélectionnez **Ajouter une référence** dans le menu.
- Dans la boîte de dialogue **Ajouter une référence**, sélectionnez l'onglet **.NET** (sélectionné par défaut). Si vous avez utilisé l'installateur MSI pour installer Aspose.Cells for .NET, Aspose.Cells.GridDesktop et Aspose.Cells.GridWeb apparaissent dans le volet supérieur.
- Sélectionnez-les et cliquez sur **Sélectionner**.
- Les références Aspose.Cells.GridDesktop et Aspose.Cells.GridWeb apparaissent sous le nœud Références du projet.

Si vous avez téléchargé et décompressé uniquement le DLL :

- Localisez les fichiers Aspose.Cells.GridDesktop.dll et Aspose.Cells.GridWeb.dll à l'aide du bouton Parcourir. Aspose.Cells Grid Suite a été référencé et devrait apparaître dans le volet **Composants sélectionnés** de la boîte de dialogue.
- Cliquez sur **OK.**
## **Désinstallation de Aspose.Cells for .NET**
Si vous avez utilisé l'installateur MSI pour déployer Aspose.Cells for .NET, suivez ces étapes pour supprimer complètement le composant et les contrôles, les démonstrations associées et la documentation :

- Dans le menu **Démarrer**, sélectionnez **Paramètres**, suivi de **Panneau de configuration**.
- Cliquez sur **Ajouter ou supprimer des programmes**.
- Sélectionnez Aspose.Cells for .NET (version).
- Cliquez sur **Modifier/Supprimer** pour supprimer Aspose.Cells.
{{< app/cells/assistant language="csharp" >}}
