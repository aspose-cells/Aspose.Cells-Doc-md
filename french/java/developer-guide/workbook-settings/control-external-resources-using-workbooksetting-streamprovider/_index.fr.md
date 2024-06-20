---
title: Contrôler les ressources externes à l aide de WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /fr/java/control-external-resources-using-workbooksetting-streamprovider/
---

## **Scénarios d'utilisation possibles**
Parfois, votre fichier Excel contient des ressources externes telles que des images liées, etc. Aspose.Cells vous permet de contrôler ces ressources externes à l'aide de Workbook.Settings.StreamProvider qui prend en charge la mise en œuvre de l'interface IStreamProvider. Chaque fois que vous essayerez de générer votre feuille de calcul contenant des ressources externes par exemple des images liées, les méthodes de l'interface IStreamProvider seront invoquées, ce qui vous permettra de prendre des mesures appropriées pour vos ressources externes.
## **Contrôler les ressources externes à l'aide de WorkbookSetting.StreamProvider**
Le code d'exemple suivant explique l'utilisation de Workbook.Settings.StreamProvider. Il charge l'échantillon de fichier Excel contenant une image liée. Le code remplace l'image liée par le logo Aspose et génère l'ensemble de la feuille dans une seule image à l'aide de la classe SheetRender. La capture d'écran suivante montre le fichier Excel d'exemple et son image de sortie générée à des fins de référence. Comme vous pouvez le voir, l'image liée cassée est remplacée par le logo Aspose.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
