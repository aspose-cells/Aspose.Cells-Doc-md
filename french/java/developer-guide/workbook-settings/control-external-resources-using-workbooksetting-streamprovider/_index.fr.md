---
title: Contrôler les ressources externes à l'aide de WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /fr/java/control-external-resources-using-workbooksetting-streamprovider/
---
## **Scénarios d'utilisation possibles**
Parfois, votre fichier Excel contient des ressources externes, par exemple des images liées, etc. Aspose.Cells vous permet de contrôler ces ressources externes en utilisant[Workbook.Settings.StreamProviderWorkbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider)qui prend la mise en œuvre de[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)interface. Chaque fois que vous essayez de rendre votre feuille de calcul contenant des ressources externes, par exemple des images liées, les méthodes de[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)sera invoquée, ce qui vous permettra de prendre les mesures appropriées pour vos ressources externes.
## **Contrôler les ressources externes à l'aide de WorkbookSetting.StreamProvider**
L'exemple de code suivant explique l'utilisation de[Workbook.Settings.StreamProviderWorkbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider). Il charge le[exemple de fichier Excel](61767877.xlsx)contenant une image liée. Le code remplace l'image liée par[Aspose Logo](61767874.png)et rend la feuille entière en une seule image en utilisant[FeuilleRendu](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)classe. La capture d'écran suivante montre l'exemple de fichier Excel et son[image de sortie rendue](61767874.png)pour une référence. Comme vous pouvez le voir, l'image liée cassée est remplacée par le logo Aspose.

![tâche : image_autre_texte](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
