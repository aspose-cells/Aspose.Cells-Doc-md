---
title: Convertir entre les formats Excel
type: docs
weight: 20
url: /fr/net/convert-between-excel-formats/
---

## **Conversion d'Excel en PDF**

Les fichiers **PDF** sont largement utilisés pour l'échange de documents entre les organisations, les secteurs gouvernementaux et les individus. Il s'agit d'un format de document standard et les développeurs de logiciels sont souvent invités à trouver un moyen de convertir les fichiers Microsoft Excel en documents **PDF**.
**Aspose.Cells** prend en charge la conversion des fichiers Excel en PDF et maintient une haute fidélité visuelle lors de la conversion.

Aspose.Cells for .NET prend en charge la conversion de feuilles de calcul au format PDF indépendamment d'autres logiciels. Enregistrez un fichier Excel au format PDF à l'aide de la méthode Enregistrer de la classe Workbook. La méthode Enregistrer fournit l'énumération SaveFormat.Pdf qui convertit les fichiers Excel natifs au format PDF.

**Convertissez** directement depuis le tableur vers PDF, au lieu d'utiliser un outil tiers ou une API externe, présente plusieurs **avantages** :

1. La conversion directe ne nécessite pas de fichiers temporaires car tout le processus peut être effectué en mémoire.
1. Aucun fichier XML n'est nécessaire, donc les gros fichiers peuvent facilement être convertis.
1. La vitesse de conversion est beaucoup plus rapide.

**Pour convertir des fichiers en PDF:**

1. Instanciez un objet de la classe **Workbook** en appelant son constructeur vide.
1. Vous pouvez **ouvrir/charger** un fichier de modèle existant ou sauter cette étape si vous créez le classeur à partir de zéro.
1. Effectuez votre travail souhaité (saisie de données, application de formatage, définition de formules, insertion d'images ou d'autres objets graphiques, etc.) sur la feuille de calcul en utilisant les API Aspose.Cells.
1. Lorsque le code de la feuille de calcul est complet, appelez la méthode **Save** de la classe **Workbook** pour enregistrer la feuille de calcul. Le format de fichier doit être PDF, donc sélectionnez Pdf (une valeur prédéfinie) dans l'énumération SaveFormat pour générer le document PDF final.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Conversion d'Excel en MHTML**

**MHTML** combine du HTML normal avec des ressources externes (c'est-à-dire, du contenu qui est généralement lié, comme des images, des animations, de l'audio, etc.) en un seul fichier. Ils sont utilisés pour les emails avec l'extension de fichier .mht.
Aspose.Cells prend en charge la lecture et l'écriture des fichiers MHTML.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Conversion d'Excel en XPS**

Parfois, vous voulez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats texte (par exemple TXT, TabDelim, CSV, etc.), à la fois Microsoft Excel et Aspose.Cells enregistrent par défaut le contenu de la feuille de calcul active uniquement.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **Télécharger le code source d'exemple**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
