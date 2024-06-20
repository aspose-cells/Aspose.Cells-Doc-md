---
title: Générer un graphique en traitant des marqueurs intelligents
type: docs
weight: 180
url: /fr/java/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}} 

Les API Aspose.Cells fournissent la classe WorkbookDesigner pour travailler avec les Smart Markers où la mise en forme et les formules sont placées dans les feuilles de calcul du concepteur, puis traitées par rapport aux sources de données spécifiées pour remplir les données selon les Smart Markers. Il est également possible de créer des graphiques Excel en traitant les Smart Markers, ce qui nécessitera les étapes suivantes.

- Création de la feuille de calcul du concepteur
- Traitement de la feuille de calcul du concepteur par rapport à la source de données spécifiée
- Création d'un graphique basé sur des données populées

{{% /alert %}} 
## **Création de la feuille de calcul du concepteur**
Une feuille de calcul de concepteur est un simple fichier Excel créé avec l'application Microsoft Excel ou les API Aspose.Cells contenant la mise en forme visuelle, les formules et les smart markers, où le contenu doit être peuplé à l'exécution.

{{% alert color="primary" %}} 

Des informations détaillées sur les Smart Markers sont disponibles [ici](/cells/fr/java/smart-markers/)

{{% /alert %}} 

Dans un souci de simplicité, nous créerons la feuille de calcul du concepteur en utilisant l'API Aspose.Cells for Java, puis nous la traiterons par la suite contre une source de données créée dynamiquement à des fins de démonstration.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access the first (default) Worksheet from the collection

Worksheet dataSheet = book.getWorksheets().get(0);

//Name the first Worksheet for referencing

dataSheet.setName("ChartData");

//Access the CellsCollection of ChartData Worksheet

Cells cells = dataSheet.getCells();

//Place the markers in the Worksheet according to desired layout

cells.get("A1").putValue("&=$Headers(horizontal)");

cells.get("A2").putValue("&=$Year2000(horizontal)");

cells.get("A3").putValue("&=$Year2005(horizontal)");

cells.get("A4").putValue("&=$Year2010(horizontal)");

cells.get("A5").putValue("&=$Year2015(horizontal)");

{{< /highlight >}}

Si vous enregistrez la feuille de calcul résultante à ce stade, les données dans la feuille de calcul ressembleront à ceci.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_1.png)
## **Traitement de la feuille de calcul du concepteur**
Pour traiter la feuille de calcul du concepteur, nous devons disposer d'une source de données qui correspond aux Smart Markers utilisés dans la feuille de calcul du concepteur. Par exemple, nous avons créé une entrée de Smart Marker comme **&=$Headers(horizontal)**, qui représente la variable par le nom Headers alors que la clé **(horizontal)** suggère que les données doivent être remplies horizontalement.

Pour démontrer ce cas d'utilisation, nous allons créer la source de données à partir de zéro et la traiter contre la feuille de calcul du concepteur créée à l'étape précédente. Cependant, dans un scénario en temps réel, les données pourraient déjà être disponibles pour un traitement ultérieur, vous pouvez donc ignorer la création de la source de données si les données sont déjà disponibles.

**Java**

{{< highlight csharp >}}

 //Create string arrays which will serve as data sources to the smart markers

String[] headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[] year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[] year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[] year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[] year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

Le traitement des Smart Markers est assez simple comme suit.

**Java**

{{< highlight csharp >}}

 //Create an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner();

//Set the Workbook property for the instance of WorkbookDesigner

designer.setWorkbook(book);

//Set data sources for smart markers

designer.setDataSource("Headers", headers);

designer.setDataSource("Year2000", year2000);

designer.setDataSource("Year2005", year2005);

designer.setDataSource("Year2010", year2010);

designer.setDataSource("Year2015", year2015);

//Process the designer spreadsheet against the provided data sources

designer.process();

{{< /highlight >}}

Si vous enregistrez la feuille de calcul à ce stade, les données ressembleront à ceci.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

Le snippet de code ci-dessus utilise l'instance existante de la classe Workbook créée à la première étape. Si vous avez déjà le fichier de feuille de calcul du concepteur sur le disque ou en mémoire, vous pouvez créer une instance de la classe Workbook en chargeant la feuille de calcul du concepteur existante.

{{% /alert %}} 
## **Création d'un graphique**
Une fois les données en place, tout ce que nous avons à faire est de créer un graphique basé sur la source de données. Afin de garder l'exemple simple, nous utiliserons la méthode Chart.setChartDataRange pour éviter de configurer davantage le graphique.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





Le graphique final ressemble à ceci.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_3.png)
