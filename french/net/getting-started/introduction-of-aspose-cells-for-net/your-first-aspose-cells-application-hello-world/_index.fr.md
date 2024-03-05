---
title: Votre première demande Aspose.Cells - Hello World
type: docs
weight: 30
url: /fr/net/your-first-aspose-cells-application-hello-world/
description: Créez, modifiez et enregistrez votre premier fichier Excel dans tous les formats pris en charge en utilisant le Aspose.Cells for .NET pour découvrir sa simplicité et sa puissance au C#.
keywords: C# Hello World, Aspose.Cells for .NET Hello World, The first application using Aspose.Cells for .NET, The first program via Aspose.Cells for .NET.
---
{{% alert color="primary" %}}

Ce didacticiel montre comment créer une toute première application (Hello World) à l'aide du simple Aspose.Cells 'API. Cette application simple crée un fichier Excel Microsoft avec le texte 'Hello World' dans une cellule de feuille de calcul spécifiée.

{{% /alert %}}

##  **Comment créer l'application Hello World**

Les étapes ci-dessous créent l'application Hello World à l'aide du Aspose.Cells API :

1.  Créez une instance du[Cahier d'exercices](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe.
1.  Si vous avez un permis, alors[applique-le](/cells/fr/net/licensing/).
 Si vous utilisez la version d'évaluation, ignorez les lignes de code liées à la licence.
1. Créez un nouveau fichier Excel ou ouvrez un fichier Excel existant.
1. Accédez à n’importe quelle cellule souhaitée d’une feuille de calcul dans le fichier Excel.
1.  Insérez les mots**Hello World!** dans une cellule accessible.
1. Générez le fichier Excel Microsoft modifié.

La mise en œuvre des étapes ci-dessus est démontrée dans les exemples ci-dessous.

###  **Comment créer un nouveau classeur**

L'exemple suivant crée un nouveau classeur à partir de zéro, écrit Hello World ! dans la cellule A1 de la première feuille de calcul et enregistre le fichier Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **Comment ouvrir un fichier existant**

L'exemple suivant ouvre un fichier modèle Excel Microsoft existant nommé « Sample.xlsx », saisit « Hello World ! » texte dans la cellule A1 de la première feuille de calcul et enregistre le classeur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
