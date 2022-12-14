---
title: Configuration de la page et options d'impression
type: docs
weight: 10
url: /fr/java/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

Parfois, les développeurs doivent configurer la mise en page et les paramètres d'impression pour contrôler le processus d'impression. La mise en page et les paramètres d'impression offrent diverses options et sont entièrement pris en charge dans Aspose.Cells.

Cet article explique comment créer une application console et appliquer les options de mise en page et d'impression à une feuille de calcul avec quelques lignes de code simples à l'aide du Aspose.Cells API.

{{% /alert %}}

## **Utilisation des paramètres de page et d'impression**

Pour cet exemple, nous avons créé un classeur dans Microsoft Excel et utilisons Aspose.Cells pour définir la mise en page et les options d'impression.

### **Définition des options de mise en page**

Créez d'abord une feuille de calcul simple dans Microsoft Excel. Ensuite, appliquez-lui les options de configuration de la page. L'exécution du code modifie les options de mise en page comme dans la capture d'écran ci-dessous.

**Fichier de sortie** 

![tâche : image_autre_texte](page-setup-and-printing-options_1.png)

1. Créez une feuille de calcul avec des données dans Microsoft Excel :
 1. Ouvrez un nouveau classeur dans Microsoft Excel.
 1. Ajoutez des données.
 Ci-dessous une capture d'écran du fichier.

      **Fichier d'entrée**

![tâche : image_autre_texte](page-setup-and-printing-options_2.png)

1. Définissez les options de configuration de la page :
 Appliquez les options de mise en page au fichier. Vous trouverez ci-dessous une capture d'écran des options par défaut, avant que les nouvelles options ne soient appliquées.

   **Options de configuration de page par défaut**

![tâche : image_autre_texte](page-setup-and-printing-options_3.png)

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
 1. Décompressez-le sur votre ordinateur de développement.
 Tout[Aspose](http://www.aspose.com/) les composants, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il injecte uniquement des filigranes dans les documents produits.
1. Créez un projet.
 Créez un projet à l'aide d'un éditeur Java, par exemple Eclipse, ou créez un programme simple à l'aide d'un éditeur de texte.
1. Ajoutez un chemin de classe.
1. Extrayez les fichiers Aspose.Cells.jar et dom4j_1.6.1.jar de Aspose.Cells.zip.
 1. Définissez le chemin de classe du projet dans Eclipse :
 1. Sélectionnez votre projet dans Eclipse puis cliquez sur**Projet** suivie par**Propriétés**.
 1. Sélectionnez**Java Chemin de construction**à gauche de la boîte de dialogue.
 1. Sélectionnez l'onglet Bibliothèques, cliquez sur**Ajouter des JAR** ou**Ajouter des fichiers JAR externes** pour sélectionner Aspose.Cells.jar et dom4j_1.6.1.jar et les ajouter aux chemins de génération.
 Ou vous pouvez le définir lors de l'exécution à une invite DOS dans Windows :

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. Écrivez l'application qui appelle les API :
 Vous trouverez ci-dessous le code utilisé par le composant dans cet exemple.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

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
**Document d'entrée**

![tâche : image_autre_texte](page-setup-and-printing-options_4.png)

L'exécution du code modifie les options d'impression.
**Fichier de sortie**

![tâche : image_autre_texte](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **Sommaire**

{{% alert color="primary" %}}

Cet article explique comment définir les options de mise en page et d'impression de feuille à l'aide de Aspose.Cells. J'espère qu'il vous donnera un aperçu et que vous pourrez utiliser ces options dans vos propres scénarios.

 Aspose.Cells bénéficie d'années de recherche, de conception et de réglage minutieux. Nous accueillons chaleureusement vos questions, commentaires et suggestions à[Aspose.CellsForum](https://forum.aspose.com/c/cells/9). Nous garantissons une réponse rapide.

{{% /alert %}}
