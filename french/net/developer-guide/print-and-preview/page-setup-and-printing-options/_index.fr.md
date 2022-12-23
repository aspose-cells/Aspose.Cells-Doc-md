---
title: Configuration de la page et options d'impression
type: docs
weight: 60
url: /fr/net/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

Parfois, les développeurs doivent configurer la mise en page et les paramètres d'impression pour contrôler le processus d'impression. La mise en page et les paramètres d'impression offrent diverses options et sont entièrement pris en charge dans Aspose.Cells.

Cet article montre comment créer une application console dans Visual Studio.Net et appliquer les options de mise en page et d'impression à une feuille de calcul avec quelques lignes de code simples à l'aide du Aspose.Cells API.

{{% /alert %}}

## **Utilisation des paramètres de page et d'impression**

Pour cet exemple, nous avons créé un classeur dans Microsoft Excel et utilisons Aspose.Cells pour définir la mise en page et les options d'impression.

### **Utilisation de Aspose.Cells pour définir les options de mise en page**

Créez d'abord une feuille de calcul simple dans Microsoft Excel. Ensuite, appliquez-lui les options de configuration de la page. L'exécution du code modifie les options de mise en page comme dans la capture d'écran ci-dessous.

|**Fichier de sortie.**|
|:- |
|![tâche : image_autre_texte](page-setup-and-printing-options_1.png)|

1. Créez une feuille de calcul avec des données dans Microsoft Excel :
 1. Ouvrez un nouveau classeur dans Microsoft Excel.
 1. Ajoutez des données.
1. Définissez les options de configuration de la page :
 Appliquez les options de mise en page au fichier. Vous trouverez ci-dessous une capture d'écran des options par défaut, avant que les nouvelles options ne soient appliquées.

|**Options de configuration de page par défaut.**|
|:- |
|![tâche : image_autre_texte](page-setup-and-printing-options_2.png)|

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger](https://downloads.aspose.com/cells/net) Aspose.Cells pour .Net.
 1. Installez-le sur votre ordinateur de développement.
 Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il injecte uniquement des filigranes dans les documents produits.
1. Créer un projet :
 1. Démarrez Visual Studio. Filet.
 1. Créez une nouvelle application console.
 Cet exemple montre une application console C#, mais vous pouvez également utiliser VB.NET.
1. Ajoutez des références :
 1. Cet exemple utilise Aspose.Cells donc ajoutez une référence à ce composant au projet. Par exemple:
 …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Écrivez l'application qui invoque le API :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

### **Définition des options d'impression**

Les paramètres de mise en page fournissent également plusieurs options d'impression (également appelées options de feuille) qui permettent aux utilisateurs de contrôler la manière dont les pages de la feuille de calcul sont imprimées. Ils permettent aux utilisateurs de :

- Sélectionnez une zone d'impression spécifique d'une feuille de calcul.
- Titres imprimés.
- Imprimer le quadrillage.
- Imprimer les en-têtes de lignes/colonnes.
- Atteindre la qualité brouillon.
- Imprimer les commentaires.
- Erreurs de cellule d'impression.
- Définissez l'ordre des pages.

L'exemple qui suit applique les options d'impression au fichier créé dans l'exemple ci-dessus (PageSetup.xls). La capture d'écran ci-dessous montre les options d'impression par défaut avant l'application des nouvelles options.

|**Document d'entrée**|
|:- |
|![tâche : image_autre_texte](page-setup-and-printing-options_3.png)|
L'exécution du code modifie les options d'impression.

|**Fichier de sortie**|
|:- |
|![tâche : image_autre_texte](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
