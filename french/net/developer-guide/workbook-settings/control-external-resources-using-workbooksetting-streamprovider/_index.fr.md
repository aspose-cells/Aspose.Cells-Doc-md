---
title: Contrôler les ressources externes à l aide de WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /fr/net/control-external-resources-using-workbooksetting-streamprovider/
---

## **Scénarios d'utilisation possibles**

Parfois, votre fichier Excel contient des ressources externes telles que des images liées, etc. Aspose.Cells vous permet de contrôler ces ressources externes à l'aide de [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) qui prend en charge l'implémentation de l'interface [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider). Chaque fois que vous essayez de rendre votre feuille de calcul contenant des ressources externes telles que des images liées, les méthodes de l'interface [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) seront invoquées, ce qui vous permettra de prendre les mesures appropriées pour vos ressources externes.

## **Contrôler les ressources externes à l'aide de WorkbookSetting.StreamProvider**

Le code d'exemple suivant explique l'utilisation de [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider). Il charge le [fichier Excel d'exemple](61767863.xlsx) contenant une image liée. Le code remplace l'image liée par [le logo Aspose](61767862.png) et rend l'ensemble de la feuille dans une seule image en utilisant la classe [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender). La capture d'écran suivante montre le fichier Excel d'exemple et son [image de sortie rendue](61767865.png) pour référence. Comme vous pouvez le voir, l'image liée non prise en charge a été remplacée par le logo Aspose.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
