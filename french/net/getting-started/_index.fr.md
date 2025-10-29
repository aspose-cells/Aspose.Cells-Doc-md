---
title: Pour commencer
type: docs
weight: 10
url: /fr/net/getting-started/
---

{{% alert color="primary" %}} 

Cette page vous montrera comment installer Aspose Cells et créer une application Hello World.

{{% /alert %}}

## **Installation**

### **Installez Aspose.Cells via NuGet**

NuGet est le moyen le plus simple de télécharger et d'installer Aspose.Cells for .NET. 

1. Ouvrez Microsoft Visual Studio et le gestionnaire de package NuGet. 
1. Recherchez "aspose.cells" pour trouver le Aspose.Cells for .NET désiré. 
1. Cliquez sur "Installer", Aspose.Cells for .NET sera téléchargé et référencé dans votre projet.
**![Installez Aspose Cells via NuGet](install-through-nuget.png)**

Vous pouvez aussi le télécharger à partir de la page web de nuget pour aspose.cells : 
[Paquet NuGet Aspose.Cells for .NET](https://www.nuget.org/packages/Aspose.Cells/)

[Plus d'étapes pour les détails](/cells/fr/net/installation/)

### **Installez Aspose.Cells sur Windows**

1. Téléchargez Aspose.Cells.msi à partir de la page suivante :
[Téléchargez Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. Double-cliquez sur Aspose Cells msi et suivez les instructions pour l'installer :

**![Installez Aspose Cells sur Windows](install-on-windows.png)**

[Plus d'étapes pour les détails](/cells/fr/net/installing-aspose-cells-on-windows/)

### **Installer Aspose.Cells sur linux**

Dans cet exemple, j'utilise Ubuntu pour montrer comment commencer à utiliser Aspose.Cells sur linux.

1. Créez une application .NET Core, nommée "AsposeCellsTest".
2. Ouvrez le fichier "AsposeCellsTest.csproj", ajoutez les lignes suivantes pour les références au package Aspose.Cells :
{{< highlight plain >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="25.10" />
  </ItemGroup>
{{< /highlight >}}
3. Ouvrez le projet avec VSCode sur Ubuntu :
**![Installer Aspose Cells sur linux](install-on-linux.png)**
4. Exécutez le test avec le code suivant :
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Remarque : Aspose.Cells For .NetStandard peut répondre à vos besoins sur linux.

S'applique à : NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 et versions avancées.

### **Installer Aspose.Cells sur MAC OS**

Dans cet exemple, j'utilise macOS High Sierra pour montrer comment commencer à utiliser Aspose.Cells sur MAC OS.

1. Créez une application .NET Core, nommée "AsposeCellsTest".
2. Ouvrez l'application avec Visual Studio pour Mac, puis installez Aspose Cells via NuGet :
**![Installer Aspose Cells sur macOS](install-on-mac-os.png)**
3. Exécutez le test avec le code suivant :
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Si vous avez besoin d'utiliser des fonctionnalités liées au dessin, veuillez installer libgdiplus sur macOS, voir :
[Comment installer libgdiplus sur macOS](/cells/fr/net/how-to-install-libgdiplus-in-macos/)

Remarque : Aspose.Cells For .NetStandard peut répondre à vos besoins sur MAC OS.

S'applique à : NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 et versions avancées.

### [**Run Aspose Cells in Docker**](/cells/fr/net/how-to-run-aspose-cells-in-docker/)

### **Comment utiliser la bibliothèque graphique sur des plateformes non-Windows avec Net6**

Aspose.Cells pour Net6 utilise désormais SkiaSharp comme bibliothèque graphique, comme recommandé dans [la déclaration officielle de Microsoft](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md). Pour plus de détails sur l'utilisation d'Aspose.Cells avec NET6, veuillez consulter [Comment exécuter Aspose.Cells pour .Net6](/cells/fr/net/how-to-run-aspose-cells-for-net6/).

## **Création de l'application Hello World**

Les étapes ci-dessous créent l'application Bonjour le monde en utilisant l'API Aspose.Cells :

1. Si vous avez une licence, alors [appliquez-la](/cells/fr/net/licensing/).
   Si vous utilisez la version d'évaluation, ignorez les lignes de code relatives à la licence.
1. Créez une instance de la classe [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) pour créer un nouveau fichier Excel, ouvrir un fichier Excel existant.
1. Accédez à n'importe quelle cellule souhaitée d'une feuille de calcul dans le fichier Excel.
1. Insérez les mots **Bonjour le Monde !** dans une cellule accessible.
1. Générez le fichier Microsoft Excel modifié.

La mise en œuvre des étapes ci-dessus est démontrée dans les exemples ci-dessous.

### **Exemple de Code: Création d'un Nouveau Classeur**

L'exemple suivant crée un nouveau classeur à partir de zéro, insère "Hello World!" dans la cellule A1 de la première feuille de calcul et enregistre en tant que fichier Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Exemple de Code: Ouverture d'un Fichier Existant**

L'exemple suivant ouvre un fichier de modèle Microsoft Excel existant "Sample.xlsx", insère "Hello World!" dans la cellule A1 de la première feuille de calcul et enregistre en tant que fichier Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
