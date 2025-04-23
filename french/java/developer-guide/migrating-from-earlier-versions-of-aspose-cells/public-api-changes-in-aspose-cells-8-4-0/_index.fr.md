---
title: Modifications de l API publique dans Aspose.Cells 8.4.0
type: docs
weight: 140
url: /fr/java/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.3.2 à la version 8.4.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, [les classes ajoutées, etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-4-0/) et [les classes supprimées, etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-4-0/), mais aussi une description de toute modification du comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Mécanisme pour modifier le code VBA/Macro dans les feuilles de calcul**
Afin de fournir la fonctionnalité de [Manipulation du code VBA/Macro](/cells/fr/java/modifying-vba-or-macro-code-using-aspose-cells/), le Aspose.Cells for Java 8.4.0 a exposé une série de nouvelles classes et propriétés dans le package com.aspose.cells.Vba. Quelques détails importants de ces nouvelles classes sont les suivants.

- La classe VbaProject peut être utilisée pour récupérer le projet VBA à partir d'une feuille de calcul donnée.
- La classe VbaModuleCollection représente la collection de modules VBA qui font partie d'un VbaProject donné.
- La classe VbaModule représente un seul module de la VbaModuleCollection.

Le code suivant montre comment modifier dynamiquement les segments de code VBA.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

VbaModuleCollection modules = workbook.getVbaProject().getModules();

for(int i=0; i < modules.getCount(); i++)

{

	VbaModule module = modules.get(i);

    String code = module.getCodes();

    //Replace the original message with the modified message

    if (code.contains("This is test message."))

    {

        code = code.replace("This is test message.", "This is Aspose.Cells message.");

        module.setCodes(code);

    }

}

//Save the output Excel file

workbook.save("output.xlsm");

{{< /highlight >}}
### **Capacité de supprimer une table de pivot**
Aspose.Cells for Java 8.4.0 a exposé deux méthodes pour la collection de PivotTable afin de fournir la fonctionnalité de suppression de la table de pivot d'une feuille de calcul donnée. Les détails desdites méthodes sont les suivants.

- La méthode PivotTableCollection.remove accepte un objet PivotTable et le supprime de la collection.
- La méthode PivotTableCollection.removeAt accepte une valeur entière basée sur l'index zéro et supprime la table de pivot particulière de la collection.

Le code suivant montre comment supprimer la table de pivot en utilisant les deux méthodes mentionnées ci-dessus.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first pivot table object

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Remove pivot table using pivot table object

worksheet.getPivotTables().remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.getPivotTables().removeAt(0);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Support pour différents agencements de table de pivot**
Aspose.Cells for Java 8.4.0 fournit le support pour différents agencements prédéfinis pour les tables de pivot. Afin de fournir cette fonctionnalité, les API Aspose.Cells ont exposé trois méthodes pour la classe PivotTable comme détaillé ci-dessous.

- La méthode PivotTable.showInCompactForm rend la table de pivot dans une disposition compacte.
- La méthode PivotTable.showInOutlineForm rend la table de pivot dans une disposition de plan.
- La méthode PivotTable.showInTabularForm rend la table de pivot dans une disposition tabulaire.

{{% alert color="primary" %}} 

Il est important d'appeler PivotTable.refreshData et PivotTable.calculateData après avoir défini l'un des agencements mentionnés ci-dessus. 

{{% /alert %}} 

Le code d'exemple suivant définit différents agencements pour une table de pivot et stocke le résultat sur le disque.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//1 - Show the pivot table in compact form

pivotTable.showInCompactForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("CompactForm.xlsx");

//2 - Show the pivot table in outline form

pivotTable.showInOutlineForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("OutlineForm.xlsx");

//3 - Show the pivot table in tabular form

pivotTable.showInTabularForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("TabularForm.xlsx");

{{< /highlight >}}
### **Classe TxtLoadStyleStrategy & Propriété TxtLoadOptions.LoadStyleStrategy Ajoutées**
Aspose.Cells for Java 8.4.0 a exposé la classe TxtLoadStyleStrategy et la propriété TxtLoadOptions.LoadStyleStrategy afin de spécifier la stratégie pour formater les valeurs analysées lors de la conversion d'une valeur de chaîne en nombre ou en heure.
### **Méthode DataBar.ToImage ajoutée**
Avec la version 8.4.0, l'API Aspose.Cells a fourni la méthode DataBar.toImage pour enregistrer la DataBar formatée conditionnellement au format image. La méthode {DataBar.toImage}} accepte deux paramètres comme détaillé ci-dessous.

- Le premier paramètre est de type com.aspose.cells.Cell sur lequel la mise en forme conditionnelle a été appliquée.
- Le second paramètre est de type com.aspose.cells.rendering.ImageOrPrintOptions afin de définir différents paramètres de l'image résultante.

L'exemple de code suivant démontre l'utilisation de la méthode DataBar.toImage pour rendre le DataBar au format image.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.getCells().get("C1");

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.getFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc.get(0).getDataBar();

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setImageFormat(ImageFormat.getPng());

//Get the image bytes of the databar

byte[] imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **Propriété Border.ThemeColor ajoutée**
Les API Aspose.Cells permettent d'extraire des données liées au thème des feuilles de calcul. Avec la sortie de Aspose.Cells for Java 8.4.0, l'API a exposé la propriété Border.ThemeColor qui peut être utilisée pour récupérer les attributs de couleur du thème des bordures de cellules.
### **Propriété DrawObject.ImageBytes ajoutée**
Aspose.Cells for Java 8.4.0 a exposé la propriété DrawObject.ImageBytes pour obtenir les données de l'image du graphique ou de la forme.
### **Propriété HtmlSaveOptions.ExportBogusRowData ajoutée**
Aspose.Cells for Java 8.4.0 a fourni la propriété {HtmlSaveOptions.ExportBogusRowData}}. La propriété de type booléen détermine si l'API injectera de fausses données de rangée inférieure lors de l'exportation de la feuille de calcul au format HTML. 

{{% alert color="primary" %}} 

La valeur par défaut est true.

{{% /alert %}} 

L'exemple de code suivant illustre l'utilisation de la propriété susmentionnée.

**Java**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Propriété HtmlSaveOptions.CellCssPrefix ajoutée**
La nouvelle propriété ajoutée HtmlSaveOptions.CellCssPrefix permet de définir le préfixe des fichiers CSS lors de l'exportation des feuilles de calcul au format HTML.

{{% alert color="primary" %}} 

La valeur par défaut est "" (chaîne vide).

{{% /alert %}}
## **API obsolètes**
### **Méthodes Cells.getCellByIndex & Row.getCellByIndex obsolètes**
Utilisez la méthode getEnumerator pour itérer sur toutes les cellules à la place.
### **La propriété DrawObject.Image obsolète**
Utilisez la propriété DrawObject.ImageBytes pour obtenir les données de l'image à la place.
{{< app/cells/assistant language="java" >}}
