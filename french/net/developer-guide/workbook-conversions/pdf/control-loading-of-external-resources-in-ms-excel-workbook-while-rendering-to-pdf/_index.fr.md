---
title: Contrôler le chargement des ressources externes dans le classeur MS Excel lors du rendu en PDF
type: docs
weight: 40
url: /fr/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **Scénarios d'utilisation possibles**

Votre fichier Excel peut contenir des ressources externes telles que des images ou des objets liés. Lorsque vous convertissez votre fichier Excel en PDF, Aspose.Cells récupère ces ressources externes et les rend en PDF. Mais parfois, vous ne voulez pas charger ces ressources externes et, de plus, vous voulez les manipuler. Vous pouvez le faire en utilisant [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) qui implémente l'interface [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider).

## **Contrôler le chargement des ressources externes dans le classeur MS Excel lors du rendu en PDF**

Le code d'exemple suivant explique comment utiliser [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) pour contrôler le chargement des ressources externes et les manipuler. Veuillez consulter le [fichier Excel d'exemple](50528322.xlsx) utilisé dans le code et le [PDF de sortie](50528325.pdf) généré par le code. La [capture d'écran](50528326.png) montre comment l'[ancienne image externe](50528324.png) dans le fichier Excel d'exemple a été remplacée par une [nouvelle image](50528323.png) dans le PDF généré.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
