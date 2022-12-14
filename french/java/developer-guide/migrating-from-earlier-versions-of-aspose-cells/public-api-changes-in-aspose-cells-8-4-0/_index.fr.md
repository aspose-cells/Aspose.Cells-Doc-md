---
title: Public API Changements dans Aspose.Cells 8.4.0
type: docs
weight: 140
url: /fr/java/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.3.2 à 8.4.0 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour,[classes ajoutées, etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-4-0/) et[classes supprimées, etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-4-0/), mais aussi une description de tout changement de comportement dans les coulisses du Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Mécanisme pour modifier le code VBA/Macro dans les feuilles de calcul**
 Afin de fournir la fonctionnalité de[Manipulation de code VBA/macro](/cells/fr/java/modifying-vba-or-macro-code-using-aspose-cells/), le Aspose.Cells for Java 8.4.0 a exposé une série de nouvelles classes et propriétés dans le package com.aspose.cells.Vba. Voici quelques-uns des détails importants de ces nouvelles classes.

- La classe VbaProject peut être utilisée pour récupérer le projet VBA à partir d'une feuille de calcul donnée.
- La classe VbaModuleCollection représente la collection de modules VBA qui font partie d'un VbaProject donné.
- La classe VbaModule représente un seul module de VbaModuleCollection.

L'extrait de code suivant montre comment modifier dynamiquement les segments de code VBA.

**Java**

{{< highlight "csharp" >}}

 Classeur classeur = nouveau classeur("source.xlsm");

//Modifier le code du module VBA

Modules VbaModuleCollection = classeur.getVbaProject().getModules();

 pour(int je=0; je< modules.getCount(); i++)

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
### **Possibilité de supprimer le tableau croisé dynamique**
Aspose.Cells for Java 8.4.0 a exposé deux méthodes pour la PivotTableCollection afin de fournir la fonctionnalité de suppression du tableau croisé dynamique d'une feuille de calcul donnée. Les détails des procédés susmentionnés sont les suivants.

- La méthode PivotTableCollection.remove accepte un objet de tableau croisé dynamique et le supprime de la collection.
- La méthode PivotTableCollection.removeAt accepte une valeur entière basée sur un index zéro et supprime le tableau croisé dynamique particulier de la collection.

L'extrait de code suivant montre comment supprimer le tableau croisé dynamique à l'aide des deux méthodes mentionnées ci-dessus.

**Java**

{{< highlight "csharp" >}}

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
### **Prise en charge de différentes dispositions de tableau croisé dynamique**
Aspose.Cells for Java 8.4.0 prend en charge différentes dispositions prédéfinies pour les tableaux croisés dynamiques. Afin de fournir cette fonctionnalité, les API Aspose.Cells ont exposé trois méthodes pour la classe PivotTable, comme détaillé ci-dessous.

- La méthode PivotTable.showInCompactForm restitue le tableau croisé dynamique dans la disposition compacte.
- La méthode PivotTable.showInOutlineForm restitue le tableau croisé dynamique dans la disposition Plan.
- La méthode PivotTable.showInTabularForm restitue le tableau croisé dynamique dans la disposition tabulaire.

{{% alert color="primary" %}} 

 Il est important d'appeler PivotTable.refreshData & PivotTable.calculateData après avoir défini l'une des dispositions mentionnées ci-dessus.

{{% /alert %}} 

L'exemple de code suivant définit différentes dispositions pour un tableau croisé dynamique et stocke le résultat sur disque.

**Java**

{{< highlight "csharp" >}}

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
### **Classe TxtLoadStyleStrategy et propriété TxtLoadOptions.LoadStyleStrategy ajoutée**
Aspose.Cells for Java 8.4.0 a exposé la classe TxtLoadStyleStrategy et la propriété TxtLoadOptions.LoadStyleStrategy afin de spécifier la stratégie de formatage des valeurs analysées lors de la conversion de la valeur de chaîne en nombre ou en date/heure.
### **Méthode DataBar.ToImage ajoutée**
Avec la version v8.4.0, le Aspose.Cells API a fourni la méthode DataBar.toImage pour enregistrer la DataBar formatée de manière conditionnelle au format image. La méthode {DataBar.toImage}} accepte deux paramètres comme détaillé ci-dessous.

- Le premier paramètre est de type com.aspose.cells.Cell sur lequel une mise en forme conditionnelle a été appliquée.
- Le deuxième paramètre est de type com.aspose.cells.rendering.ImageOrPrintOptions afin de définir différents paramètres de l'image résultante.

L'exemple de code suivant illustre l'utilisation de la méthode DataBar.toImage pour restituer la DataBar au format image.

**Java**

{{< highlight "csharp" >}}

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

byte[]imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **Propriété Border.ThemeColor ajoutée**
Aspose.Cells Les API permettent d'extraire des données liées au thème des feuilles de calcul. Avec la sortie de Aspose.Cells for Java 8.4.0, le API a exposé la propriété Border.ThemeColor qui peut être utilisée pour récupérer les attributs de couleur de thème des bordures Cell.
### **Propriété DrawObject.ImageBytes ajoutée**
Aspose.Cells for Java 8.4.0 a exposé la propriété DrawObject.ImageBytes pour obtenir les données d'image de Chart ou Shape.
### **Propriété HtmlSaveOptions.ExportBogusRowData ajoutée**
 Aspose.Cells for Java 8.4.0 a fourni la propriété {HtmlSaveOptions.ExportBogusRowData}}. La propriété de type booléen détermine si API injectera de fausses données de ligne inférieure lors de l'exportation de la feuille de calcul au format HTML.

{{% alert color="primary" %}} 

La valeur par défaut est true.

{{% /alert %}} 

L'exemple de code suivant illustre l'utilisation de la propriété susmentionnée.

**Java**

{{< highlight "csharp" >}}

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
La propriété nouvellement ajoutée HtmlSaveOptions.CellCssPrefix permet de définir le préfixe pour les fichiers CSS lors de l'exportation des feuilles de calcul au format HTML.

{{% alert color="primary" %}} 

La valeur par défaut est "" (chaîne vide).

{{% /alert %}}
## **API obsolètes**
### **Méthodes Cells.getCellByIndex & Row.getCellByIndex Obsolète**
Utilisez la méthode getEnumerator pour itérer toutes les cellules à la place.
### **Propriété DrawObject.Image obsolète**
Utilisez plutôt la propriété DrawObject.ImageBytes pour obtenir des données d'image.
