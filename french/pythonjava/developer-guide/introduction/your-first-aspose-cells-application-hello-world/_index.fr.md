---
title: Votre première demande Aspose.Cells - Hello World
type: docs
weight: 30
url: /fr/python-java/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

Cette rubrique pour débutant montre comment les développeurs peuvent créer une première application simple (Hello World) en utilisant Aspose.Cells' simple API. L'application crée un fichier Excel Microsoft avec les mots Hello World dans une cellule spécifiée d'une feuille de calcul.

{{% /alert %}}

### **Création de l'application Hello World**

Pour créer l'application Hello World à l'aide de Aspose.Cells API :

1.  Créer une instance de**[Classeur](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)**classer.
1. Appliquer la licence :
1. Si vous avez acheté une licence, utilisez la licence dans votre application pour accéder à toutes les fonctionnalités de Aspose.Cells.
 1. Si vous utilisez la version d'évaluation du composant (si vous utilisez Aspose.Cells sans licence), ignorez cette étape.
1. Créez un nouveau fichier Excel Microsoft ou ouvrez un fichier existant dans lequel vous souhaitez ajouter/mettre à jour du texte.
1. Accédez à n'importe quelle cellule d'une feuille de calcul dans le fichier Excel Microsoft.
1.  Insérez les mots**Hello World!** dans une cellule accessible.
1. Générez le fichier Excel Microsoft modifié.

Les exemples ci-dessous illustrent les étapes ci-dessus.

#### **Création d'un classeur**

L'exemple suivant crée un nouveau classeur à partir de zéro, écrit les mots "Hello World!" dans la cellule A1 de la première feuille de calcul et enregistre le fichier.

**La feuille de calcul générée** 

![tâche : image_autre_texte](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFile.py" >}}

#### **Ouvrir un fichier existant**

 L'exemple suivant ouvre un fichier de modèle Excel Microsoft existant appelé**livre1.xls**, écrit les mots "Hello World!" dans la cellule A1 de la première feuille de calcul et enregistre le classeur en tant que nouveau fichier.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpeningExistingFile.py" >}}
