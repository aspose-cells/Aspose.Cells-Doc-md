---
title: Commencer
type: docs
weight: 10
url: /fr/net/getting-started/
---
{{% alert color="primary" %}} 

Cette page vous montrera comment installer Aspose Cells et créer une application Hello World.

{{% /alert %}}

## **Installation**

### **Installez Aspose.Cells à NuGet**

NuGet est le moyen le plus simple de télécharger et d'installer Aspose.Cells for .NET.

1.  Ouvrez Microsoft Visual Studio et le gestionnaire de packages NuGet.
1.  Recherchez "aspose.cells" pour trouver le Aspose.Cells for .NET souhaité.
1. Cliquez sur "Installer", Aspose.Cells for .NET sera téléchargé et référencé dans votre projet.
**![Installer Aspose Cells à NuGet](install-through-nuget.png)**

 Vous pouvez également le télécharger à partir de la page Web nuget pour aspose.cells :
[Aspose.Cells for .NET NuGet Colis](https://www.nuget.org/packages/Aspose.Cells/)

[Plus d'étape pour les détails](/cells/fr/net/installation/)

### **Installez Aspose.Cells sur Windows**

1. Téléchargez Aspose.Cells.msi à partir de la page suivante :
[Télécharger Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. Double-cliquez sur le Aspose Cells msi et suivez les instructions pour l'installer :

**![Installer Aspose Cells sur Windows](install-on-windows.png)**

[Plus d'étape pour les détails](/cells/fr/net/installing-aspose-cells-on-windows/)

### **Installez Aspose.Cells sur Linux**

Dans cet exemple, j'utilise Ubuntu pour montrer comment commencer à utiliser Aspose.Cells sous Linux.

1. Créez une application .netcore, nommée "AsposeCellsTest".
2. Ouvrez le fichier "AsposeCellsTest.csproj", ajoutez-y les lignes suivantes pour les références de package Aspose.Cells :
{{< highlight "plain" >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="22.12" />
  </ItemGroup>
{{< /highlight >}}
3. Ouvrez le projet avec VSCode sur Ubuntu :
**![Installer Aspose Cells sur Linux](install-on-linux.png)**
4. exécutez le test avec le code suivant :
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Remarque : Aspose.Cells pour .NetStandard peut prendre en charge vos besoins sous Linux.

S'applique à : NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 et version avancée.

### **Installez Aspose.Cells sur MAC OS**

Dans cet exemple, j'utilise macOS High Sierra pour montrer comment commencer à utiliser Aspose.Cells sur MAC OS.

1. Créez une application .netcore, nommée "AsposeCellsTest".
2. Ouvrez l'application avec Visual Studio pour Mac, puis installez Aspose Cells à NuGet :
**![Installer Aspose Cells sur macOS](install-on-mac-os.png)**
3. exécutez le test avec le code suivant :
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Si vous avez besoin d'utiliser des fonctionnalités liées au dessin, veuillez installer libgdiplus dans macOS, voir :
[Comment installer libgdiplus dans macOS](/cells/fr/net/how-to-install-libgdiplus-in-macos/)

Remarque : Aspose.Cells pour .NetStandard peut prendre en charge vos besoins sur MAC OS.

S'applique à : NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 et version avancée.

### **[Exécuter Aspose Cells dans Docker](/cells/net/how-to-run-aspose-cells-in-docker/)**

### **Comment utiliser la bibliothèque graphique sur des plates-formes non Windows avec Net6**

 Aspose.Cells pour Net6 utilise désormais SkiaSharp comme bibliothèque graphique, comme recommandé dans[communiqué du Microsoft](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md) . Pour plus de détails sur l'utilisation de Aspose.Cells avec NET6, veuillez consulter[Comment exécuter Aspose.Cells pour .Net6](/cells/fr/net/how-to-run-aspose-cells-for-net6/).

## **Création de l'application Hello World**

Les étapes ci-dessous créent l'application Hello World en utilisant le Aspose.Cells API :

1.  Si vous avez une licence, alors[appliquez-le](/cells/fr/net/licensing/).
 Si vous utilisez la version d'évaluation, ignorez les lignes de code liées à la licence.
1.  Créer une instance de[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook) class pour créer un nouveau fichier Excel ou ouvrir un fichier Excel existant.
1. Accédez à n'importe quelle cellule souhaitée d'une feuille de calcul dans le fichier Excel.
1.  Insérez les mots**Hello World!** dans une cellule accessible.
1. Générez le fichier Excel Microsoft modifié.

La mise en œuvre des étapes ci-dessus est illustrée dans les exemples ci-dessous.

### **Exemple de code : création d'un nouveau classeur**

L'exemple suivant crée un nouveau classeur à partir de zéro, insère "Hello World!" dans la cellule A1 de la première feuille de calcul et l'enregistre en tant que fichier Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Exemple de code : ouverture d'un fichier existant**

L'exemple suivant ouvre un fichier de modèle Excel Microsoft existant "Sample.xlsx", insère "Hello World!" dans la cellule A1 de la première feuille de calcul et l'enregistre en tant que fichier Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
