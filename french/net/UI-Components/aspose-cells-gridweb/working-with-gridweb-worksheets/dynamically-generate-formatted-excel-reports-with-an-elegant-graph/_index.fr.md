---
title: Générez dynamiquement des rapports Excel formatés avec un graphique élégant
type: docs
weight: 130
url: /fr/net/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
---
{{% alert color="primary" %}} 

Ce document est conçu pour fournir les informations nécessaires sur la façon dont nous pouvons extraire des données d'une source de données vers une magnifique grille comme un contrôle, y coller un graphique et exporter le rapport avec le graphique vers MS Excel pour effectuer des analyses, des comparaisons et des impressions.

{{% /alert %}} 
## **Aperçu**
Certains scénarios Web exigent à la fois des rapports et des présentations, une combinaison de parties ou d'objets qui peuvent bien fonctionner ensemble. L'article explique à quel point il est facile de concevoir et de générer dynamiquement des rapports Excel élégants de manière WYSIWYG. Il exporte les données d'un fichier XML (vous pouvez également utiliser d'autres sources de données) vers le contrôle Aspose.Cells.GridWeb qui vous fournit l'environnement réel qui vous permet d'appliquer un format riche et attrayant aux données et de calculer les résultats de formules comme MS Excel. Il génère également un graphique sophistiqué basé sur les données source de la feuille de travail à l'aide de[Aspose.Cells](https://products.aspose.com/cells/) composant et colle l'image du graphique dans le rapport des ventes. Enfin, le rapport Excel avec graphique joint est enregistré sur le disque à l'aide du composant Aspose.Cells.

Cet article inclut le code source et le projet de démonstration complet pour une telle fonctionnalité.

Il permet aux utilisateurs ayant une vision détaillée de la création d'un rapport d'activité de saisir des données dans une feuille de calcul de la grille et d'appliquer une mise en forme aux cellules des lignes et des colonnes, d'intégrer un graphique basé sur la plage de données source avant d'enregistrer le rapport Excel sur le disque.
## **Les composants Aspose**
 j'en utilise trois[Aspose](http://www.aspose.com/) les composants pour effectuer la tâche avec facilité.[Aspose](http://www.aspose.com/) , l'éditeur de composants .NET et Java, fournit une variété de composants riches en fonctionnalités.[Aspose](http://www.aspose.com/) fournit une excellente gamme de composants .NET et Java. Reconnus par des milliers de clients dans le monde, les produits comprennent des composants de format de fichier, des produits de rapport, des composants visuels et des composants utilitaires qui permettent d'ouvrir, de modifier, de générer, d'enregistrer, de fusionner, de convertir, etc. par programmation des documents dans divers formats, notamment DOC, RTF, WordML, HTML, PDF, XLS, SpreadsheetML, délimité par des tabulations, CSV, PPT, SWF, EMF, WMF, MPX, MPD et autres formats.

J'en profite pour vous présenter trois de ces composants qui ont été utilisés dans cette quête.
## **Aspose.Cells Commandes de grille**
 Aspose.Cells Grid Controls est une solution totale de grille. Aspose.Cells Grid Controls est fourni avec deux composants GUI .NET différents (Aspose.Cells.GridDesktop et Aspose.Cells.GridWeb) : un pour prendre en charge les applications de bureau et l'autre pour prendre en charge les applications Web. Les deux versions sont également adaptées afin de faciliter la mise en œuvre sur l'une ou l'autre plate-forme. Aspose.Cells.GridWeb offre la possibilité d'importer et d'exporter vers des feuilles de calcul Excel. Ainsi, toute personne familiarisée avec Excel (même les utilisateurs finaux) peut concevoir l'apparence d'une grille. Aspose.Cells.GridWeb offre également un API facile à utiliser et riche en fonctionnalités qui offre aux développeurs un contrôle total sur l'apparence, la convivialité et le comportement de leur grille. Pour en savoir plus sur le produit, ses fonctionnalités et pour un guide des programmeurs, veuillez consulter le résumé de la liste des fonctionnalités, Aspose.Cells.GridWeb Documentation et en ligne en vedette[Démos](https://aspose.github.io/)
## **Aspose.Cells**
**Aspose.Cells**est un composant de rapport de feuille de calcul Excel qui vous permet de lire et d'écrire des feuilles de calcul Excel sans utiliser Microsoft Excel à installer côté client ou côté serveur.**Aspose.Cells** est un composant riche en fonctionnalités qui offre bien plus qu'une simple exportation de données de base. Avec**Aspose.Cells** les développeurs peuvent exporter des données, formater des feuilles de calcul dans les moindres détails et à tous les niveaux, importer des images, importer des graphiques, créer des graphiques, manipuler des graphiques, diffuser des données Excel, enregistrer dans divers formats, notamment XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML ([Aspose.Pdf](https://products.aspose.com/pdf/) intégré) et bien d'autres.**Aspose.Cells** offre un outil facile à utiliser et riche en fonctionnalités**API** pour les programmeurs. Il a une énorme liste de fonctionnalités. Pour en savoir plus sur le produit, ses fonctionnalités et pour un guide du programmeur, veuillez consulter le résumé de**Liste des fonctionnalités**, **Aspose.Cells Documents** et des démos en ligne. Tu peux[Télécharger](https://downloads.aspose.com/cells) sa version d'évaluation gratuitement.
## **Conception de l'interface**
Nous commençons à créer une nouvelle application Web Asp.Net dans Visual Studio.Net.

 je**Ajouter une référence**aux trois composants, c'est-à-dire Aspose.Cells.GridWeb.dll, Aspose.Chart.dll et Aspose.Cells.dll au projet en premier. Je place un certain contrôle sur la page et définit leurs propriétés, c'est-à-dire une liste déroulante, un bouton de commande et une étiquette. je place ensuite**Aspose.Cells.GridWeb****contrôler**(**GrilleWeb**) à partir de la boîte à outils, car après avoir ajouté des références aux trois composants, le**GrilleWeb**le contrôle est apparu sur la boîte à outils. Les deux autres composants (**Aspose.Chart**et**Aspose.Cells**) ne sont que des bibliothèques, ne sont référencées qu'au projet.

Je crée également deux dossiers "fichier" et "images", ajoute respectivement "Products.xml" et "chart.gif" à ces dossiers. Le fichier xml est un fichier source de données dont les données seront extraites pour remplir le**GrilleWeb**feuille de travail. Le fichier image fournira une image pour un bouton personnalisé placé sur le**GrilleWeb**contrôler.

Je crée maintenant un bouton de commande personnalisé. Je fais simplement un clic droit sur**GrilleWeb**contrôlez et cliquez sur l'option "Boutons de commande personnalisés…".

Il activera l'éditeur de boutons de commande personnalisés, l'éditeur vous permet de créer des boutons d'image de commande personnalisés avec une info-bulle jointe. Je spécifie les valeurs de certaines propriétés du bouton, par exemple, Command (Name) -> "btnChart", ImageUrl -> donne le chemin vers le fichier image ("chart.gif") et ToolTip -> donne l'info-bulle.

Ainsi, le bouton de commande personnalisé est ajouté comme vous pouvez le voir (entouré de couleur rouge) dans la capture d'écran suivante.

|![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
|:- |


Enfin, j'ai défini des attributs de police (gras) pour l'étiquette et le bouton de commande. J'ajuste également la taille des contrôles pour obtenir le rendu final.

![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **Récupération de données à partir d'un fichier XML**
Voici la structure de fichier XML utilisée dans le projet.
### **Structure du fichier XML**
**XML**

{{< highlight "csharp" >}}

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

{{< highlight "java" >}}

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

private object[]GetDistinctValues(DataTable dtable, string colName)

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
## **Remplissage de la feuille de calcul du contrôle Aspose.Cells.GridWeb avec des données**
J'utilise certains API du**GrilleWeb**contrôle pour remplir une feuille de calcul avec les données du fichier XML source. J'écris du code dans le gestionnaire d'événements de clic du bouton de commande (intitulé "Afficher le rapport"). Le rapport de données est filtré en fonction de l'élément sélectionné dans la liste déroulante.



{{< highlight "java" >}}

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
## **Formatage des données dans le Cells**
Pour distinguer les différents types d'informations sur une feuille de calcul, pour un affichage optimal des données sur votre feuille de calcul et pour faciliter la numérisation d'une feuille de calcul, vous formatez la feuille de calcul. UN**Format**représente un style et est défini comme un ensemble de caractéristiques, telles que les polices et les tailles de police, les formats de nombre, les bordures de cellule, l'ombrage des cellules avec une couleur d'arrière-plan unie ou un motif de couleur spécifique, l'indentation, l'alignement et l'orientation du texte dans les cellules.

Je fusionne quelques lignes de code supplémentaires ci-dessus. Je place le titre/sous-titre du rapport, je mets en forme les cellules de titre, de sous-titre et de détail. J'applique également la mise en forme des nombres aux deux champs (définissez le format de nombre de devises sur les champs UnitPrice et Sale) et ajustez la hauteur / largeur des lignes et des colonnes à l'aide de**Aspose.Cells.GridWeb**API.



{{< highlight "java" >}}

 //Créez la cellule de titre (A1) dans la feuille et appliquez les mises en forme.

//Les lignes suivantes entrent une valeur de chaîne dans la cellule, spécifiez

//taille de la police, spécifiez les paramètres d'alignement horizontal et vertical, définissez

//couleurs de premier plan et d'arrière-plan et fusionner les cellules (A1:E2).

Feuille WebWorksheet = GrilleWeb1.WebWorksheets[0] ;

sheet.Cells["A1"].PutValue("Ventes de produits par catégorie");

feuille.Cells["A1"].Style.Font.Size = new FontUnit("20pt");

feuille.Cells["A1"].Style.HorizontalAlign = HorizontalAlign.Center ;

feuille.Cells["A1"].Style.VerticalAlign = VerticalAlign.Middle ;

feuille.Cells["A1"].Style.BackColor = Couleur.SkyBlue ;

feuille.Cells["A1"].Style.ForeColor = Couleur.Bleu ;

feuille.Cells.Fusionner(0, 0, 2, 5);

//Créez la cellule de sous-titre (A3) dans la feuille et appliquez les mises en forme.

//Les lignes suivantes entrent une valeur de chaîne dans la cellule, spécifiez

//taille de police avec attributs, spécifiez l'alignement horizontal et vertical

// paramètres, définir les couleurs de premier plan et d'arrière-plan et fusionner les cellules

//(A3:E3).

feuille.Cells["A3"].PutValue(DropDownList1.SelectedItem.Text);

feuille.Cells["A3"].Style.Font.Size = new FontUnit("13pt");

feuille.Cells["A3"].Style.Font.Bold = true ;

feuille.Cells["A3"].Style.Font.Italic = true;

feuille.Cells["A3"].Style.HorizontalAlign = HorizontalAlign.Left ;

feuille.Cells["A3"].Style.VerticalAlign = VerticalAlign.Middle ;

feuille.Cells["A3"].Style.BackColor = Couleur.SeaGreen ;

feuille.Cells["A3"].Style.ForeColor = Couleur.Jaune ;

feuille.Cells.Fusionner(2, 0, 1, 5);

//Obtenir les derniers index de ligne et de colonne (qui contiennent des données).

int totalrow = feuille.Cells.MaxRow +1 ;

int totalcol = feuille.Cells.MaxColumn ;

//Récupérer la fiche Cells collections

Cellules WebCells = feuille.Cells ;

//Définir l'objet Cell.

Cellule WebCell ;

//Parcourez les données de la feuille et formatez deux champs avec

// Style de numéro de devise.

pour (int i = 4;i<=totalrow;i++)

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
## **Production du rapport formaté (fichier .XLS) avec graphique à l'aide du composant Aspose.Cells**
Maintenant, je vais écrire du code pour enregistrer le rapport formaté avec le graphique sur le disque. j'utilise**GrilleWeb** c'est**sauvegarder**bouton, le**GrilleWeb** c'est**Enregistrer la commande**L'événement est déclenché lorsque vous cliquez sur le bouton Enregistrer, donc je vais le gérer. Ici, j'utilise**Aspose.Cells**composant pour exporter le rapport formaté vers MS Excel, générer un graphique et l'intégrer dans le fichier Excel de sortie. Je n'ai pas inséré l'image du graphique (créé par**Aspose.Chart**composant) créez plutôt le graphique similaire en utilisant le API de**Aspose.Cells**afin que vous puissiez modifier le graphique dans MS Excel selon vos besoins.





{{< highlight "java" >}}

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

![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

Je sélectionne une catégorie par laquelle je veux afficher le rapport des ventes et je clique sur le bouton "Afficher le rapport".

![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

Ainsi, le rapport est affiché dans le**GrilleWeb**en fonction de la catégorie sélectionnée. Le rapport est formaté par défaut en fonction du code (écrit précédemment).

![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

Si vous souhaitez formater des données dans certaines cellules de manière WYSIWYG, vous pouvez le faire assez facilement.**Aspose.Cells.GridWeb**fournit**Format Cells**éditeur, sélectionnez la ou les cellules souhaitées et cliquez dessus avec le bouton droit de la souris, cliquez sur l'option "Format Cell…".

![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

La boîte de dialogue Formater Cell s'affiche.

![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

Je spécifie des attributs de police et clique sur OK.

![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

Et obtenez le résultat.

![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

Outre le formatage des cellules, vous pouvez également modifier les valeurs de vos cellules. Double-cliquez sur la ou les cellules souhaitées et modifiez la valeur.

![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

Pour soumettre le résultat de la modification et recalculer toute la formule, je clique sur le bouton correspondant (entouré de couleur rouge) pour mettre à jour le rapport.

![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

Maintenant, je vais créer le graphique et le coller dans le contrôle. Je clique sur le bouton de commande personnalisé (entouré de couleur rouge) pour créer le graphique à secteurs basé sur la plage de données.

![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

Enfin, j'exporterai ce rapport de données avec graphique vers MS Excel. je clique sur le**sauvegarder**bouton (entouré de couleur rouge). En cliquant sur le**sauvegarder**le bouton affichera**Téléchargement de fichier**boîte de dialogue, vous pouvez soit**Ouvert**le rapport résultant (fichier Excel de sortie avec graphique) dans MS Excel ou enregistrez-le sur le disque.

![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

Lorsque je clique sur le bouton Ouvrir (boîte de dialogue Téléchargement de fichier), le rapport Excel avec graphique est exporté vers MS Excel. La partie supérieure du rapport s'affiche.

![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

La partie inférieure du rapport Excel est affichée.

![tâche : image_autre_texte](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
