---
title: Contrôler le chargement des ressources externes dans le classeur MS Excel lors du rendu en PDF
type: docs
weight: 40
url: /fr/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **Scénarios d'utilisation possibles**

Votre fichier Excel peut contenir des ressources externes comme des images ou des objets liés. Lorsque vous convertissez votre fichier Excel en PDF, Aspose.Cells récupère ces ressources externes et les rend en PDF. Mais parfois, vous ne voulez pas charger ces ressources externes et en plus de cela, vous voulez les manipuler. Vous pouvez le faire en utilisant [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) qui implémente l'interface [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider).

## **Contrôler le chargement des ressources externes dans le classeur MS Excel lors du rendu en PDF**

Le code d'exemple suivant explique comment utiliser [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) pour contrôler le chargement des ressources externes et les manipuler. Veuillez consulter le [fichier Excel d'exemple](50528353.xlsx) utilisé dans le code et le [PDF de sortie](50528354.pdf) généré par le code. La [capture d'écran](50528357.png) montre comment l'[ancienne image externe](50528356.png) du fichier Excel d'exemple a été remplacée par une [nouvelle image](50528355.png) dans le PDF de sortie.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
{{< app/cells/assistant language="java" >}}
