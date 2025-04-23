---
title: Changements d API publics dans Aspose.Cells 8.4.2
type: docs
weight: 160
url: /fr/java/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.4.1 à la version 8.4.2 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement de nouvelles méthodes publiques et mises à jour, [classes ajoutées etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-4-2/), mais aussi une description de tout changement de comportement interne dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Mécanisme de création de graphique amélioré**
La classe com.aspose.cells.charts.Chart a exposé la méthode setChartDataRange pour faciliter la tâche de création de graphiques. La méthode setChartDataRange accepte deux paramètres, où le premier paramètre est de type chaîne qui spécifie la zone de cellules à partir de laquelle tracer les séries de données. Le deuxième paramètre est de type Boolean qui spécifie l'orientation du tracé, c'est-à-dire; s'il faut tracer les séries de données du graphique à partir d'une plage de valeurs de cellules par ligne ou par colonnes.

Le snippet de code suivant montre comment créer un graphique à colonnes avec quelques lignes de code en supposant que les données de séries de tracé du graphique sont présentes sur la même feuille de calcul de la cellule A1 à D4.

**Java**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **Ajout de la méthode VbaModuleCollection.add**
Aspose.Cells for Java 8.4.2 a exposé la méthode VbaModuleCollection.add pour ajouter un nouveau module VBA à l'instance de Workbook. La méthode VbaModuleCollection.add accepte un paramètre de type Worksheet pour ajouter un module spécifique à la feuille.

L'extrait de code suivant montre comment utiliser la méthode VbaModuleCollection.add.

**Java**

{{< highlight csharp >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add VBA module

int idx = workbook.getVbaProject().getModules().add(worksheet);

//Access the VBA Module, set its name and code

VbaModule module = workbook.getVbaProject().getModules().get(idx);

module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub");

//Save the workbook

workbook.save(output, SaveFormat.XLSM);

{{< /highlight >}}

### **Méthode surchargée Cells.copyColumns ajoutée**
Aspose.Cells for Java 8.4.2 a exposé une version surchargée de la méthode Cells.copyColumns pour répéter les colonnes source sur la destination. La nouvelle méthode accepte au total 5 paramètres, les 4 premiers étant les mêmes que ceux de la méthode Cells.copyColumns commune. Cependant, le dernier paramètre de type int spécifie le nombre de colonnes de destination sur lesquelles les colonnes source doivent être répétées.

L'extrait de code suivant montre comment utiliser la méthode Cells.copyColumns récemment exposée.

**Java**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.copyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **Ajout des énumérations PasteType.DEFAULT et PasteType.ALL_EXCEPT_BORDERS**
Avec la sortie de v8.4.2, l'API Aspose.Cells a ajouté 2 nouvelles énumérations pour PasteType comme détaillé ci-dessous.

- PasteType.DEFAULT : Fonctionne de manière similaire à la fonctionnalité "Tout" d'Excel pour coller une plage de cellules.
- PasteType.ALL_EXCEPT_BORDERS : Fonctionne de manière similaire à la fonctionnalité "Tout sauf les bordures" d'Excel pour coller une plage de cellules.

Le code d'exemple suivant démontre l'utilisation du champ PasteType.DEFAULT.

**Java**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Create source & destination ranges

Range source = cells.createRange("A1:B6");

Range destination = cells.createRange("D1:E6");

//Create an instance of PasteOptions and set its PasteType property

PasteOptions options = new PasteOptions();

options.setPasteType(PasteType.DEFAULT);

//Copy the source range onto the destination range with everything except column widths

destination.copy(source, options);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

À partir de la version Aspose.Cells for Java 8.4.2, le champ d'énumération PasteType.ALL se comporte différemment par rapport à la fonctionnalité "Tout" d'Excel pour coller une plage de cellules. Maintenant, le PasteType.ALL copie également la largeur des colonnes sur la plage de destination, contrairement à la fonctionnalité "Tout" d'Excel. Pour reproduire le comportement "Tout" d'Excel, veuillez utiliser le PasteType.DEFAULT.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
