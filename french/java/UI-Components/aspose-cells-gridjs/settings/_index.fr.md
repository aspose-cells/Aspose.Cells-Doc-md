---
title: Paramètres pour GridJs
type: docs
weight: 250
url: /fr/java/aspose-cells-gridjs/settings/
description: Cet article décrit le paramétrage de GridJs.
keywords: GridJs, paramètres, GridWorkbookSettings
aliases:
  - /java/aspose-cells-gridjs/how-to-use-setting/
  - /java/aspose-cells-gridjs/work-with-setting/
---


Il existe certains paramètres que nous pouvons spécifier en définissant GridWorkbookSettings :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/GridWorkbookSettings)


Par exemple, le code suivant définit ReCalculateOnOpen sur false pour arrêter le calcul à l'ouverture du fichier :
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.setReCalculateOnOpen(false);
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
 le code suivant définit l'auteur du fichier :
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.setAuthor("peter");
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
Vous pouvez vérifier plus de paramètres dans cette classe.

