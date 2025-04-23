---
title: Aperçu avant impression des classeurs et des feuilles de calcul
type: docs
weight: 130
url: /fr/java/workbook-and-worksheet-print-preview/
---

## **Scénario d'utilisation**

Il peut arriver que des fichiers Excel avec des millions de pages doivent être convertis en PDF ou en images. Le traitement de tels fichiers consommera beaucoup de temps et de ressources. Dans de tels cas, la fonctionnalité d'aperçu avant impression du classeur et de la feuille de calcul pourrait s'avérer utile. Avant de convertir de tels fichiers, l'utilisateur peut vérifier le nombre total de pages et décider ensuite si le fichier doit être converti ou non. Cet article se concentre sur l'utilisation des classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) pour connaître le nombre total de pages.

## **Aperçu avant impression des classeurs et des feuilles de calcul**

Aspose.Cells offre la fonction d'aperçu avant impression. Pour cela, l'API fournit les classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview). Pour créer l'aperçu avant impression de l'ensemble du classeur, créez une instance de la classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) en passant les objets [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) au constructeur. La classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) fournit une méthode [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount) qui retourne le nombre de pages dans l'aperçu généré. De même que la classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview), la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) est utilisée pour générer un aperçu avant impression pour une feuille de calcul spécifique. Pour créer l'aperçu avant impression d'une feuille de calcul, créez une instance de la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) en passant les objets [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) au constructeur. La classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) fournit également une méthode [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount) qui retourne le nombre de pages dans l'aperçu généré.

Le code d'exemple suivant démontre l'utilisation des classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) en utilisant le [fichier excel d'exemple](Book1.xlsx).

### **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

Voici la sortie générée en exécutant le code ci-dessus.

### **Sortie console**

{{< highlight java >}}

Workbook page count: 1</br>
Worksheet page count: 1

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
