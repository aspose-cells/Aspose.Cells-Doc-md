---
title: Aperçu avant impression du classeur et de la feuille de calcul
type: docs
weight: 130
url: /fr/java/workbook-and-worksheet-print-preview/
---
## **Scénario d'utilisation**

Il peut y avoir des cas où des fichiers Excel avec des millions de pages doivent être convertis en PDF ou en images. Le traitement de tels fichiers consommera beaucoup de temps et de ressources. Dans de tels cas, la fonctionnalité Aperçu avant impression du classeur et de la feuille de calcul peut s'avérer utile. Avant de convertir de tels fichiers, l'utilisateur peut vérifier le nombre total de pages, puis décider si le fichier doit être converti ou non. Cet article se concentre sur l'utilisation de[**ClasseurImpressionAperçu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)et[**FeuilleImpressionAperçu**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)classes pour connaître le nombre total de pages.

## **Aperçu avant impression du classeur et de la feuille de calcul**

Aspose.Cells fournit la fonction d'aperçu avant impression. Pour cela, le API fournit[**ClasseurImpressionAperçu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)et[**FeuilleImpressionAperçu**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)Des classes. Pour créer l'aperçu avant impression de l'ensemble du classeur, créez une instance de[**ClasseurImpressionAperçu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)classe en passant[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)et[**Options d'image ou d'impression**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)objets au constructeur. Le[**ClasseurImpressionAperçu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)classe offre une[**Nombre de pages évaluées**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount)méthode qui renvoie le nombre de pages dans l'aperçu généré. Semblable à[**ClasseurImpressionAperçu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)classe, la[**FeuilleImpressionAperçu**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)La classe est utilisée pour générer un aperçu avant impression pour une feuille de calcul spécifique. Pour créer l'aperçu avant impression d'une feuille de calcul, créez une instance de[**FeuilleImpressionAperçu**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)classe en passant[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)et[**Options d'image ou d'impression**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)objets au constructeur. Le[**FeuilleImpressionAperçu**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)classe offre également une[**Nombre de pages évaluées**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount)méthode qui renvoie le nombre de pages dans l'aperçu généré.

L'extrait de code suivant illustre l'utilisation des deux[**ClasseurImpressionAperçu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)et[**FeuilleImpressionAperçu**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)cours en utilisant le[exemple de fichier excel](Book1.xlsx).

### **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

Voici la sortie générée en exécutant le code ci-dessus.

### **Sortie console**

Nombre de pages du classeur : 1</br>
Nombre de pages de la feuille de calcul : 1
