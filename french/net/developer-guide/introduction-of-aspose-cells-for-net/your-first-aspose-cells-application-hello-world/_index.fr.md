---
title: Votre première demande Aspose.Cells - Hello World
type: docs
weight: 30
url: /fr/net/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

Ce tutoriel montre comment créer une toute première application (Hello World) en utilisant Aspose.Cells' simple API. Cette application simple crée un fichier Excel Microsoft avec le texte 'Hello World' dans une cellule de feuille de calcul spécifiée.

{{% /alert %}}

## **Création de l'application Hello World**

Les étapes ci-dessous créent l'application Hello World en utilisant le Aspose.Cells API :

1.  Créer une instance de[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe.
1.  Si vous avez une licence, alors[appliquez-le](/cells/fr/net/licensing/).
 Si vous utilisez la version d'évaluation, ignorez les lignes de code liées à la licence.
1. Créez un nouveau fichier Excel ou ouvrez un fichier Excel existant.
1. Accédez à n'importe quelle cellule souhaitée d'une feuille de calcul dans le fichier Excel.
1.  Insérez les mots**Hello World!** dans une cellule accessible.
1. Générez le fichier Excel Microsoft modifié.

La mise en œuvre des étapes ci-dessus est illustrée dans les exemples ci-dessous.

### **Exemple de code : création d'un nouveau classeur**

L'exemple suivant crée un nouveau classeur à partir de zéro, écrit Hello World ! dans la cellule A1 de la première feuille de calcul et enregistre le fichier Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Exemple de code : ouverture d'un fichier existant**

L'exemple suivant ouvre un fichier de modèle Excel Microsoft existant nommé "Sample.xlsx", entrées "Hello World!" texte dans la cellule A1 de la première feuille de calcul et enregistre le classeur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
