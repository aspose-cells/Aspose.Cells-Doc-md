---
title: Configuration de la mise en page et des options d impression
type: docs
weight: 60
url: /fr/net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

Parfois, les développeurs doivent configurer la mise en page et les paramètres d'impression pour contrôler le processus d'impression. Les paramètres de mise en page et d'impression offrent diverses options et sont entièrement pris en charge dans Aspose.Cells.

Cet article montre comment créer une application console dans Visual Studio.Net, et appliquer des options de mise en page et d'impression à une feuille de calcul avec quelques lignes de code simples en utilisant l'API Aspose.Cells.

{{% /alert %}}

## **Travailler avec la mise en page et les paramètres d'impression**

Pour cet exemple, nous avons créé un classeur dans Microsoft Excel et utilisons Aspose.Cells pour définir la mise en page et les options d'impression.

### **Utilisation d'Aspose.Cells pour définir les options de mise en page**

Créez d'abord une feuille de calcul simple dans Microsoft Excel. Ensuite, appliquez des options de mise en page. L'exécution du code modifie les options de mise en page comme dans la capture d'écran ci-dessous.

| **Fichier de sortie.** |
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Créez une feuille de calcul avec des données dans Microsoft Excel:
   1. Ouvrir un nouveau classeur dans Microsoft Excel.
   1. Ajoutez des données.
1. Définir les options de mise en page :
   Appliquer les options de mise en page au fichier. Ci-dessous se trouve une capture d'écran des options par défaut, avant l'application des nouvelles options.

| **Options de mise en page par défaut.** |
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger](https://downloads.aspose.com/cells/net) Aspose.Cells pour .Net.
   1. Installez-le sur votre ordinateur de développement.
      Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits.
1. Créer un projet :
   1. Démarrer Visual Studio. Net.
   1. Créez une nouvelle application console.
      Cet exemple montrera une application console en C#, mais vous pouvez également utiliser VB.NET.
1. Ajouter des références:
   1. Cet exemple utilise Aspose.Cells, donc ajoutez une référence à ce composant dans le projet. Par exemple :
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Écrivez l'application qui invoque l'API :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

### **Paramétrage des options d'impression**

Les paramètres de mise en page fournissent également plusieurs options d'impression (appelées également options de feuille) qui permettent aux utilisateurs de contrôler l'impression des pages de feuille de calcul. Ils permettent aux utilisateurs de :

- Sélectionner une zone d'impression spécifique d'une feuille de calcul.
- Imprimer les titres.
- Imprimer les quadrillages.
- Imprimer les en-têtes de lignes/colonnes.
- Obtenir une qualité brouillon.
- Imprimer des commentaires.
- Imprimer les erreurs de cellules.
- Définir l'ordre des pages.

L'exemple qui suit applique des options d'impression au fichier créé dans l'exemple ci-dessus (PageSetup.xls). La capture d'écran ci-dessous montre les options d'impression par défaut avant l'application de nouvelles options.

|**Document d'entrée**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
L'exécution du code modifie les options d'impression.

|**Fichier de sortie**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
