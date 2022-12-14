---
title: Contrôlez le chargement des ressources externes dans le classeur MS Excel lors du rendu au format PDF
type: docs
weight: 40
url: /fr/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **Scénarios d'utilisation possibles**

Votre fichier Excel peut contenir des ressources externes, par exemple des images ou des objets liés. Lorsque vous convertissez votre fichier Excel en PDF, Aspose.Cells récupère ces ressources externes et les restitue en PDF. Mais parfois, vous ne souhaitez pas charger ces ressources externes et plus que cela, vous souhaitez les manipuler. Vous pouvez le faire en utilisant[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)qui met en œuvre le[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)interface.

## **Contrôlez le chargement des ressources externes dans le classeur MS Excel lors du rendu au format PDF**

L'exemple de code suivant explique comment utiliser[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)pour contrôler le chargement des ressources externes et les manipuler. S'il vous plaît, vérifiez le[exemple de fichier Excel](50528353.xlsx)utilisé à l'intérieur du code et le[PDF de sortie](50528354.pdf)généré par le code. La[capture d'écran](50528357.png)montre comment le[ancienne image externe](50528356.png)dans l'exemple de fichier Excel a été remplacé par un[Nouvelle image](50528355.png)dans le PDF de sortie.

![tâche : image_autre_texte](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
