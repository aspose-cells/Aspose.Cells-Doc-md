---
title: Convertir entre les formats Excel
type: docs
weight: 20
url: /fr/net/convert-between-excel-formats/
---
## **Conversion d'Excel en PDF**

**PDF** Les fichiers sont largement utilisés pour l'échange de documents entre les organisations, les secteurs gouvernementaux et les particuliers. Il s'agit d'un format de document standard et les développeurs de logiciels sont souvent invités à trouver un moyen de convertir les fichiers Excel Microsoft en**PDF** documents.
**Aspose.Cells** prend en charge la conversion de fichiers Excel en PDF et maintient une haute fidélité visuelle lors de la conversion.

Aspose.Cells for .NET prend en charge la conversion de feuilles de calcul en PDF indépendamment des autres logiciels. Enregistrez un fichier Excel au format PDF à l'aide de la méthode Save de la classe Workbook. La méthode Save fournit le membre enum SaveFormat.Pdf qui convertit les fichiers Excel natifs au format PDF.

**Conversion** directement de la feuille de calcul au PDF, au lieu d'utiliser un outil tiers ou externe API, a plusieurs**avantages**:

1. La conversion directe ne nécessite pas de fichiers temporaires car l'ensemble du processus peut être effectué en mémoire.
1. Aucun fichier XML n'est nécessaire, les fichiers volumineux peuvent donc être facilement convertis.
1. La vitesse de conversion est beaucoup plus rapide.

**Pour convertir des fichiers en PDF :**

1.  Instancier un objet de la**Cahier** classe en appelant son constructeur vide.
1.  Tu peux**ouvrir/charger** un fichier de modèle existant ou ignorez cette étape si vous créez le classeur à partir de rien.
1. Effectuez le travail souhaité (saisissez des données, appliquez une mise en forme, définissez des formules, insérez des images ou d'autres objets de dessin, etc.) sur la feuille de calcul à l'aide des API Aspose.Cells.
1.  Lorsque le code de la feuille de calcul est terminé, appelez le**Méthode Save de la classe Workbook** pour enregistrer la feuille de calcul. Le format de fichier doit être PDF. Sélectionnez donc Pdf (une valeur prédéfinie) dans l'énumération SaveFormat pour générer le document PDF final.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Conversion d'Excel en MHTML**

**MHTML** combine le HTML normal avec des ressources externes (c'est-à-dire du contenu généralement lié, comme des images, des animations, de l'audio, etc.) dans un seul fichier. Ils sont utilisés pour les e-mails avec l'extension de fichier .mht.
Aspose.Cells prend en charge la lecture et l'écriture de fichiers MHTML.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Conversion d'Excel en XPS**

Parfois, vous souhaitez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats de texte (par exemple TXT, TabDelim, CSV, etc.), par défaut, Microsoft Excel et Aspose.Cells enregistrent uniquement le contenu de la feuille de calcul active.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **Télécharger l'exemple de code**

- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
