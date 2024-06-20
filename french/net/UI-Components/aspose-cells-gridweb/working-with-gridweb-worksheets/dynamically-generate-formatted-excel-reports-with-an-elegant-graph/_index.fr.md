---
title: Générer dynamiquement des rapports Excel formatés avec un graphique élégant
type: docs
weight: 130
url: /fr/net/aspose-cells-gridweb/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
keywords: GridWeb, générer un rapport, rapport
description: Cet article présente comment générer un rapport dans GridWeb.
---

{{% alert color="primary" %}} 

Ce document est conçu pour fournir les informations nécessaires sur la manière dont nous pouvons extraire des données d'une source de données vers un contrôle de type grille splendide, coller un graphique et exporter le rapport avec le graphique vers MS Excel pour effectuer des analyses, des comparaisons et des impressions.

{{% /alert %}} 
## **Vue d'ensemble**
Il existe certains scénarios Web qui exigent à la fois le Reporting et les présentations. Un mélange de parties ou d'objets qui peuvent bien fonctionner ensemble. Cet article explique à quel point il est facile de concevoir et de générer des rapports Excel élégants de manière dynamique de manière WYSIWYG. Il exporte des données à partir d'un fichier XML (vous pouvez également utiliser d'autres sources de données) vers le contrôle Aspose.Cells.GridWeb qui vous offre un environnement réel vous permettant d'appliquer un format riche et attrayant aux données et de calculer les résultats des formules comme MS Excel. Il génère également un graphique sophistiqué à partir des données sources de la feuille de calcul à l'aide du composant [Aspose.Cells](https://products.aspose.com/cells/) et colle l'image du graphique dans le rapport de ventes. Enfin, le rapport Excel avec le graphique attaché est enregistré sur le disque à l'aide du composant Aspose.Cells.

Cet article comprend le code source et un projet de démonstration entièrement fonctionnel pour une telle fonctionnalité.

Il permet aux utilisateurs de comprendre en détail comment créer un rapport d'entreprise pour saisir des données dans une feuille de calcul de la grille et appliquer un formatage à des cellules dans les lignes et les colonnes, intégrer un graphique basé sur la plage source de données avant d'enregistrer le rapport Excel sur le disque.
## **Les composants Aspose**
J'utilise trois des composants d'[Aspose](http://www.aspose.com/) pour réaliser la tâche facilement. [Aspose](http://www.aspose.com/), l'éditeur de composants .NET et Java, propose une variété de composants riches en fonctionnalités. [Aspose](http://www.aspose.com/) propose une excellente gamme de composants .NET et Java. Faisant confiance à des milliers de clients dans le monde entier, les produits comprennent des composants de format de fichier, des produits de reporting, des composants visuels et des composants utilitaires qui permettent d'ouvrir, de modifier, de générer, de sauvegarder, de fusionner, de convertir, etc. des documents dans divers formats, y compris DOC, RTF, WordML, HTML, PDF, XLS, SpreadsheetML, tabulations, CSV, PPT, SWF, EMF, WMF, MPX, MPD et autres formats.

Je profiterais de cette occasion pour vous présenter trois de ces composants qui ont été utilisés dans cette quête.
## **Contrôles de grille Aspose.Cells**
Les contrôles de grille Aspose.Cells offrent une solution de grille complète. Les contrôles de grille Aspose.Cells sont fournis avec deux composants .NET GUI différents (Aspose.Cells.GridDesktop et Aspose.Cells.GridWeb) : l'un pour prendre en charge les applications de bureau et l'autre pour prendre en charge les applications Web. Les deux versions sont également adaptées afin de faciliter la mise en œuvre dans l'une ou l'autre plate-forme. Aspose.Cells.GridWeb offre la possibilité d'importer et d'exporter des feuilles de calcul Excel. Ainsi, toute personne familiarisée avec Excel (même les utilisateurs finaux) peut concevoir l'apparence d'une grille. Aspose.Cells.GridWeb offre également une API facile à utiliser et riche en fonctionnalités qui offre aux développeurs un contrôle complet sur l'apparence, le rendu et le comportement de leur grille. Pour en savoir plus sur le produit, ses fonctionnalités et pour un guide des programmeurs, veuillez consulter le résumé de la liste des fonctionnalités, la documentation de Aspose.Cells.GridWeb et les [démos](https://aspose.github.io/) en ligne.
## **Aspose.Cells**
**Aspose.Cells** est un composant de génération de rapports de feuille de calcul Excel qui vous permet de lire et d'écrire des feuilles de calcul Excel sans utiliser Microsoft Excel installé côté client ou côté serveur. **Aspose.Cells** est un composant riche en fonctionnalités qui offre bien plus que l'exportation de données de base. Avec **Aspose.Cells**, les développeurs peuvent exporter des données, formater des feuilles de calcul dans les moindres détails et à tous les niveaux, importer des images, importer des graphiques, créer des graphiques, manipuler des graphiques, diffuser des données Excel, les enregistrer dans différents formats, y compris XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML (intégré [Aspose.Pdf](https://products.aspose.com/pdf/)) et bien d'autres encore. **Aspose.Cells** offre une API facile à utiliser et riche en fonctionnalités pour les programmeurs. Il dispose d'une longue liste de fonctionnalités. Pour en savoir plus sur le produit, ses fonctionnalités et pour un guide des programmeurs, veuillez consulter le résumé de la liste des fonctionnalités, la documentation Aspose.Cells et les démos en ligne. Vous pouvez [télécharger](https://downloads.aspose.com/cells) sa version d'évaluation gratuitement.
## **Conception de l'interface**
Nous commençons par créer une nouvelle application Web Asp.Net dans Visual Studio.Net.

J'ajoute les références aux trois composants, à savoir Aspose.Cells.GridWeb.dll, Aspose.Chart.dll et Aspose.Cells.dll, au projet en premier. J'ajoute ensuite quelques contrôles sur la page et définis leurs propriétés, notamment une liste déroulante, un bouton de commande et une étiquette. Je place ensuite le contrôle **Aspose.Cells.GridWeb** sur celui-ci à partir de la boîte à outils, puisque, après avoir ajouté des références aux trois composants, le contrôle **GridWeb** apparaît dans la boîte à outils. Les deux autres composants (Aspose.Chart et Aspose.Cells) sont simplement des bibliothèques, qui sont seulement référencées dans le projet.

Je crée également deux dossiers "fichier" et "images", j'ajoute "Products.xml" et "chart.gif" à ces dossiers respectivement. Le fichier XML est un fichier source de données à partir duquel les données seront extraites pour remplir la feuille de calcul **GridWeb**. Le fichier image fournira une image pour un bouton personnalisé placé sur le contrôle **GridWeb**.

Je crée maintenant un bouton de commande personnalisé. Je clique simplement avec le bouton droit sur le contrôle **GridWeb** et je sélectionne l'option "Boutons de commande personnalisés...".

Cela activera l'éditeur de bouton de commande personnalisé, qui vous permet de créer des boutons d'image de commande personnalisés avec une info-bulle attachée. Je spécifie les valeurs pour certaines propriétés du bouton, par exemple, Commande (Nom) -> "btnChart", ImageUrl -> donne le chemin du fichier image ("chart.gif") et Info-bulle -> donne l'info-bulle.

Ainsi, le bouton de commande personnalisé est ajouté comme vous pouvez le voir (encerclé en rouge) dans la capture d'écran suivante.

|![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
| :- |


Enfin, je définis certaines attributs de police (gras) pour l'étiquette et le bouton de commande. J'ajuste également la taille des contrôles pour obtenir le résultat final.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **Récupération de données à partir d'un fichier XML**
Voici la structure du fichier XML utilisée dans le projet.
### **Structure du fichier XML**
**XML**

{{< highlight csharp >}}

 <?xml version="1.0" standalone="yes"?>

<SalesData>

  <Products>

    <ProductName>Data</ProductName>

    <QuantityPerUnit>Data</QuantityPerUnit>

    <CategoryName>Data</CategoryName>

    <UnitPrice>Data</UnitPrice>

    <Sale>Data</Sale>

  </Products>

 .........

</SalesData>



{{< /highlight >}}

{{< highlight java >}}

 private void Page_Load(object sender, System.EventArgs e)

{

if (!IsPostBack)

{

	// Uncomment the code below when you have purchased license

	// for Aspose.Cells.GridWeb, Aspose.Chart and Aspose.Cells. You need

	// to deploy the licenses in the same folder as your executable,

      // alternatively you can add the license files as an embedded

      // resource to your project.

	//

	// Set the license for Aspose.Cells.GridWeb

	// Aspose.Cells.GridWeb.License gridwebLicense = new

	// Aspose.Cells.GridWeb.License();

	// gridwebLicense.SetLicense("Aspose.Grid.lic");

	//

	// // Set the license for Aspose.Chart

	// Aspose.Chart.License chartLicense = new

	// Aspose.Chart.License();

	// chartLicense.SetLicense("Aspose.Chart.lic");

	//

	// // Set the license for Aspose.Cells

	// Aspose.Cells.License cellsLicense = new

	// Aspose.Cells.License();

	// cellsLicense.SetLicense("Aspose.Cells.lic");

	//Create a DataSet object.

	DataSet ds = new DataSet();

	//Get the Virtual Folder Path.

	string path = MapPath(".");

	//Reads XML data from xml file into DataSet object.

	ds.ReadXml(path + "\\file\\Products.xml");

	//Call the custom method to obtain distinct values from

	//CategoryName field and store data into an object array.

	object [] drs = GetDistinctValues(ds.Tables[0],"CategoryName");

	//Fill the drop down list with distinct field items.

	for(int i = 0;i<drs.Length;i++)

	{

		DropDownList1.Items.Add(drs[i].ToString());

	}

}

}

//This method is used to filter distinct values from CategoryName field in the datatable.

private object[] GetDistinctValues(DataTable dtable, string colName)

{

	// Create a Hashtable object.

	Hashtable hTable = new Hashtable();

	// Loop through the datatable rows and add distinct values to

	// Hashtable object minimizing the duplicates in the field.

	foreach (DataRow drow in dtable.Rows)

	if(!hTable.ContainsKey(drow[colName]))

	hTable.Add(drow[colName], string.Empty);

	// Create an object array based on the distinct key values of the Hashtable object.

	object[] objArray = new object[hTable.Keys.Count];

	// Copy the disctinct values to fill the array.

	hTable.Keys.CopyTo(objArray, 0);

	// Return the array object.

	return objArray;

}

{{< /highlight >}}
## **Remplir la feuille de calcul du contrôle Aspose.Cells.GridWeb avec des données**
J'utilise une API du contrôle GridWeb pour remplir une feuille de calcul avec des données provenant du fichier XML source. J'écris du code dans le gestionnaire d'événements de clic du bouton de commande (étiqueté "Afficher le rapport"). Le rapport de données est filtré en fonction de l'élément sélectionné dans la liste déroulante.



{{< highlight java >}}

 //Clears datasheets of the GridWeb control.

GridWeb1.WebWorksheets.Clear();

//Create a DataSet object.

DataSet ds = new DataSet();

//Get the Virtual Folder path.

string path = MapPath(".");

//Reads XML data from xml file into DataSet object.

ds.ReadXml(path + "\\file\\Products.xml");

//Create a DataView based on the datatable.

DataView dv = new DataView(ds.Tables[0]);

//Filter data in the DataView object based on the selected drop down list item.

dv.RowFilter = "CategoryName ='" + DropDownList1.SelectedItem.Text + "'";

//Importing data from the filtered DataView object to create and

//fill "Products" Worksheet start from A4 cell.

GridWeb1.WebWorksheets.ImportDataView(dv, null, null,"Products",3,0);

{{< /highlight >}}
## **Mise en forme des données dans les cellules**
Pour distinguer différents types d'informations sur une feuille de calcul, pour afficher de manière optimale les données sur votre feuille de calcul et pour faciliter la visualisation d'une feuille de calcul, vous devez la mettre en forme. Un 'Format' représente un style et est défini comme un ensemble de caractéristiques, telles que les polices et tailles de police, les formats de nombre, les bordures de cellules, le remplissage des cellules avec une couleur d'arrière-plan unie ou un motif de couleur spécifique, l'indentation, l'alignement et l'orientation du texte dans les cellules.

J'ajoute quelques lignes de code ci-dessus. Je place le titre/sous-titre du rapport, je fais une mise en forme pour les cellules de titre, de sous-titre et de détail. J'applique également un formatage numérique aux deux champs (définir le format de nombre de devise pour les champs Prix unitaire et Vente) et ajuste la hauteur / largeur des lignes et des colonnes à l'aide de l'API Aspose.Cells.GridWeb.



{{< highlight java >}}

 //Create the title cell (A1) in the sheet and apply formattings.

//The following lines input a string value to the cell, specify

//font size, specify horizontal and vertical align settings, set

//foreground and background colors and merge cells (A1:E2).

WebWorksheet sheet = GridWeb1.WebWorksheets[0];

sheet.Cells["A1"].PutValue("Product Sales By Category");

sheet.Cells["A1"].Style.Font.Size = new FontUnit("20pt");

sheet.Cells["A1"].Style.HorizontalAlign = HorizontalAlign.Center;

sheet.Cells["A1"].Style.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A1"].Style.BackColor = Color.SkyBlue;

sheet.Cells["A1"].Style.ForeColor = Color.Blue;

sheet.Cells.Merge(0, 0, 2, 5);

//Create the subtitle cell (A3) in the sheet and apply formattings.

//The following lines input a string value to the cell, specify

//font size with attributes, specify horizontal and vertical align

//settings, set foreground and background colors and merge cells

//(A3:E3).

sheet.Cells["A3"].PutValue(DropDownList1.SelectedItem.Text);

sheet.Cells["A3"].Style.Font.Size = new FontUnit("13pt");

sheet.Cells["A3"].Style.Font.Bold = true;

sheet.Cells["A3"].Style.Font.Italic = true;

sheet.Cells["A3"].Style.HorizontalAlign = HorizontalAlign.Left;

sheet.Cells["A3"].Style.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A3"].Style.BackColor = Color.SeaGreen;

sheet.Cells["A3"].Style.ForeColor = Color.Yellow;

sheet.Cells.Merge(2, 0, 1, 5);

//Obtain the last row and column (which contain data) indexes.

int totalrow = sheet.Cells.MaxRow +1;

int totalcol = sheet.Cells.MaxColumn;

//Get the sheet Cells collections

WebCells cells = sheet.Cells;

//Define the Cell object.

WebCell cell;

//Loop through the data in the sheet and format two fields with

//Currency number style.

for (int i = 4;i<=totalrow;i++)

{

	//Format the Sale Column.

	cell = cells[i,totalcol];

	cell.PutValue(cell.StringValue,true);

	cell.NumberType = NumberType.Currency1;

	//Format the UnitPrice Column.

	cell = cells[i,totalcol-1];

	cell.PutValue(cell.StringValue,true);

	cell.NumberType = NumberType.Currency1;

}

//Insert the Total row with data, formula and formatting style.

//It will calculate the total Sales of a Category.

cells[totalrow,0].PutValue( DropDownList1.SelectedItem.Text + " Total" );

cells[totalrow,0].Style.Font.Bold = true;

cells[totalrow,totalcol].Formula = "=SUM(E5:E" + totalrow.ToString() + ")";

cells[totalrow,totalcol].Style.Font.Bold = true;

//Specify some Row and Column formattings. It will set row height

//and column width accordingly.

cells.SetRowHeight(2, new Unit("17pt"));

cells.SetColumnWidth(0, new Unit("157pt"));

cells.SetColumnWidth(1, new Unit("106pt"));

cells.SetColumnWidth(2, new Unit("87pt"));

cells.SetColumnWidth(3, new Unit("56pt"));

cells.SetColumnWidth(4, new Unit("50pt"));



{{< /highlight >}}
## **Production du rapport formaté (.XLS) avec un graphique à l'aide du composant Aspose.Cells**
Maintenant, je vais écrire du code pour enregistrer le rapport formaté avec un graphique sur le disque. J'utilise le bouton 'Enregistrer' de GridWeb. L'événement 'SaveCommand' de GridWeb est déclenché lorsque vous cliquez sur le bouton Enregistrer, alors je vais le gérer. Ici, j'utilise le composant Aspose.Cells pour exporter le rapport formaté vers MS Excel, générer un graphique et l'intégrer dans le fichier Excel de sortie. Je n'ai pas inséré l'image du graphique (créée par le composant Aspose.Chart) mais créé un graphique similaire à l'aide de l'API Aspose.Cells, afin que vous puissiez modifier le graphique dans MS Excel selon vos besoins.





{{< highlight java >}}

 //This GridWeb control event is fired when you click on the "Save" button

//of the control. After Clicking this button "File Download" dialog is

//displayed and you may open into MS Excel / save the output excel file //with graph to disk.

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

	//Create MemoryStream object.

	System.IO.MemoryStream ms = new System.IO.MemoryStream();

	//Save the GridWeb's Report to the stream.

	this.GridWeb1.WebWorksheets.SaveToExcelFile(ms);

	//Create a new Workbook.

	Workbook workbook = new Workbook();

	//Open the stream into the Workbook.

	workbook.Open(ms);

	//Call the custom method which creates Chart.

	Workbook book = CellsChart(workbook);

	//Save the excel file displaying "File Download" dialog box.

	book.Save(ms, FileFormatType.Default);

	this.Response.ContentType = "application/vnd.ms-excel";

	this.Response.AddHeader("content-disposition", "attachment; filename=Export.xls");

	this.Response.BinaryWrite(ms.ToArray());

}

//This custom method is used to create the Chart based on the data source

//range in the GridWeb control. In this method we will use Aspose.Cells

//APIs to create the graph which will be saved later into the output //excel file.

private Workbook CellsChart(Workbook workbook)

{

	//Get the first Worksheet.

	Aspose.Cells.Worksheet sheet = workbook.Worksheets[0];

	//Get the Cells collection in the sheet.

	Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

	//Get the last row index.

	int maxrow = sheet.Cells.MaxDataRow;

	//Unmerge the cells.

	sheet.Cells.UnMerge(maxrow,0,15,10);

	int chartIndex = 0;

	//Add a new Chart into the sheet's Chart Collection.

chartIndex = sheet.Charts.Add(Aspose.Cells.ChartType.Pie,maxrow,0,maxrow+28,5);

	//Get the Chart object.

	Aspose.Cells.Chart chart = sheet.Charts[chartIndex];

	//Set the Chart Area.

	Aspose.Cells.ChartArea chartarea = chart.ChartArea;

	chartarea.Area.Formatting = FormattingType.Custom;

	chartarea.Border.IsVisible = false;

		chartarea.Area.FillFormat.SetTwoColorGradient(Color.PowderBlue, Color.LightSkyBlue, GradientStyleType.FromCenter,1);

	//Set some properties of Chart Plot Area.

	chart.PlotArea.Area.Formatting = FormattingType.None;

	chart.PlotArea.Border.IsVisible = false;

	//Set properties of Chart Title.

	chart.Title.Text = DropDownList1.SelectedItem.Text + " Sales";

	chart.Title.TextFont.Size = 20;

	//Set properties of NSeries

	int lastdatarow = maxrow-1;

	chart.NSeries.Add("E5:E" + lastdatarow.ToString(), true);

	chart.NSeries.CategoryData = "A5:A" + lastdatarow.ToString();

	//Set the Data Labels in the chart

	Aspose.Cells.DataLabels datalabels;

	for ( int i = 0; i < chart.NSeries.Count ;i ++ )

	{

		datalabels = chart.NSeries[i].DataLabels;

		datalabels.Postion = Aspose.Cells.LabelPositionType.Center;

		datalabels.IsPercentageShown = true;

	}

	//Set the Legend settings.

	Aspose.Cells.Legend legend = chart.Legend;

	legend.Position = Aspose.Cells.LegendPositionType.Bottom;

	legend.Height = 85;

	legend.Width = 330;

	legend.AutoScaleFont = true;

	legend.Border.Color = Color.Blue;

	legend.Area.Formatting = FormattingType.Custom;

	FillFormat fillformat = legend.Area.FillFormat;

	legend.Area.Formatting = FormattingType.None;

	legend.Border.IsVisible = false;

	//Autofit the first column.

	sheet.AutoFitColumn(0);

	//Return the Workbook.

	return workbook;

}



{{< /highlight >}}
## **Exécution de l'application**
Maintenant, je lance l'application. La liste déroulante est remplie avec les catégories distinctes.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

Je sélectionne une catégorie pour afficher le rapport de ventes et clique sur le bouton 'Afficher le rapport'.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

Le rapport est affiché dans GridWeb en fonction de la catégorie sélectionnée. Le rapport est mis en forme par défaut en fonction du code (écrit précédemment).

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

Si vous souhaitez mettre en forme les données dans certaines cellules de manière WYSIWYG, vous pouvez le faire assez facilement. Aspose.Cells.GridWeb fournit un éditeur de 'Mise en forme des cellules', sélectionnez la ou les cellules souhaitées, faites un clic droit dessus, cliquez sur l'option 'Formater la cellule...'.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

La boîte de dialogue Formater la cellule s'affiche.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

Je spécifie certains attributs de police et clique sur OK.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

Et obtiens le résultat.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

En plus de la mise en forme des cellules, vous pouvez également éditer les valeurs de vos cellules. Double-cliquez sur la ou les cellules souhaitées et modifiez la valeur.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

Pour soumettre le résultat de l'édition et recalculer toutes les formules, je clique sur le bouton correspondant (cercle en rouge) pour mettre à jour le rapport.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

Maintenant je vais créer le graphique et le coller dans le contrôle. Je clique sur le bouton de commande personnalisé (cercle en rouge) pour créer le graphique circulaire basé sur la plage de données.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

Enfin, j'exporterai ce rapport de données avec le graphique vers MS Excel. Je clique sur le bouton 'Enregistrer' (cercle en rouge). En cliquant sur le bouton 'Enregistrer', une boîte de dialogue 'Télécharger le fichier' s'affichera, vous pouvez soit 'Ouvrir' le rapport résultant (fichier excel de sortie avec graphique) dans MS Excel, soit l'enregistrer sur le disque.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

Lorsque je clique sur le bouton 'Ouvrir' (boîte de dialogue 'Télécharger le fichier'), le rapport.Excel avec graphique est exporté dans MS Excel. La partie supérieure du rapport est affichée.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

La partie inférieure du rapport Excel est affichée.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
