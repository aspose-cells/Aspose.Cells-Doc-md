---
title: Calculer ou recalculer les formules dynamiquement
type: docs
weight: 10
url: /fr/net/calculate-or-recalculate-formulas-dynamically/
---

Le moteur de **calcul de formule** est intégré dans **Aspose.Cells**. Il peut non seulement recalculer la formule importée à partir du fichier de conception mais prend également en charge le calcul des résultats des formules ajoutées à l'exécution.
## **Ajout de formules et calcul de résultats**
Aspose.Cells prend en charge la plupart des formules ou fonctions qui font partie de Microsoft Excel. Les développeurs peuvent utiliser ces formules à l'aide de l'API ou des feuilles de calcul du concepteur. Aspose.Excel prend en charge un vaste ensemble de formules mathématiques, de chaînes, logiques, de date/heure, statistiques, de base de données, de recherche et de référence.

Utilisez la propriété de formule de la classe Cell pour ajouter une formule à une cellule. Lors de l'application d'une formule à une cellule, commencez toujours la chaîne par un signe égal (=) comme vous le faites lors de la création d'une formule dans Microsoft Excel. Utilisez une virgule (,) pour délimiter les paramètres de la fonction.

Pour calculer les résultats des formules, appelez la méthode CalculateFormula de la classe Excel qui traite toutes les formules intégrées dans un fichier Excel. Lisez la [url: liste des fonctions prises en charge par la méthode CalculateFormula](/cells/fr/net/supported-formula-functions/).

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Adding a value to "A1" cell

worksheet.Cells["A1"].PutValue(1);

//Adding a value to "A2" cell

worksheet.Cells["A2"].PutValue(2);

//Adding a value to "A3" cell

worksheet.Cells["A3"].PutValue(3);

//Adding a SUM formula to "A4" cell

worksheet.Cells["A4"].Formula = "=SUM(A1:A3)";

//Calculating the results of formulas

workbook.CalculateFormula();

//Get the calculated value of the cell

string value = worksheet.Cells["A4"].Value.ToString();

//Saving the Excel file

workbook.Save("Adding Formula.xls");

{{< /highlight >}}
## **Calcul des formules une seule fois**
Lorsque l'utilisateur appelle Workbook.CalculateFormula() pour calculer les valeurs des formules à l'intérieur du modèle de classeur, Aspose.Cells crée une chaîne de calcul. Cela améliore les performances lorsque les formules sont calculées pour la deuxième ou troisième fois, etc.
Cependant, si le modèle utilisateur contient de nombreuses formules diverses, la première fois du calcul de la formule peut consommer beaucoup de temps de traitement CPU et de mémoire.

Aspose.Cells vous permet de désactiver la création d'une chaîne de calcul, ce qui est utile dans les scénarios où vous souhaitez calculer les formules de votre fichier une seule fois.

Si vous cherchez à améliorer les performances des calculs de formules par Aspose.Cells et que vous ne voulez pas créer de chaîne de calcul de formule, veuillez définir **FormulaSettings.EnableCalculationChain** sur **false**. Par défaut, il est défini sur **true**.

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Adding Formula.xlsx";

//Load the template workbook

Workbook workbook = new Workbook(FileName);

//Print the time before formula calculation

Console.WriteLine(DateTime.Now);

//Set the CreateCalcChain as false

workbook.Settings.FormulaSettings.EnableCalculationChain = false;

//Calculate the workbook formulas

workbook.CalculateFormula();

//Print the time after formula calculation

Console.WriteLine(DateTime.Now);

workbook.Save(FileName);

{{< /highlight >}}
## **Calcul direct de formule**
Le moteur de calcul de formule est intégré dans Aspose.Cells. En outre, en recalculant la formule importée à partir du fichier de conception, Aspose.Cells prend également en charge le calcul des résultats des formules directement.
Parfois, vous devez calculer directement les résultats des formules sans les ajouter réellement dans une feuille de calcul. Les valeurs des cellules utilisées dans la formule existent déjà dans une feuille de calcul et tout ce dont vous avez besoin est de trouver le résultat de ces valeurs en fonction de certaines formules Ms-Excel sans ajouter la formule dans une feuille de calcul.

Vous pouvez utiliser l'API de moteur de calcul de formules d'Aspose.Cells, c'est-à-dire **worksheet.Calculate(string formula)** pour calculer les résultats de telles formules sans les ajouter réellement dans la feuille de calcul.

{{< highlight csharp >}}

 //Create a workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put 20 in cell A1

Cell cellA1 = worksheet.Cells["A1"];

cellA1.PutValue(20);

//Put 30 in cell A2

Cell cellA2 = worksheet.Cells["A2"];

cellA2.PutValue(30);

//Calculate the Sum of A1 and A2

var results = worksheet.CalculateFormula("=Sum(A1:A2)");

Cell cellA3 = worksheet.Cells["A3"];

cellA3.PutValue(results);

//Print the output

Debug.WriteLine("Value of A1: " + cellA1.StringValue);

Debug.WriteLine("Value of A2: " + cellA2.StringValue);

Debug.WriteLine("Result of Sum(A1:A2): " + results.ToString());

workbook.Save("Calulate Any Formulae.xls");

{{< /highlight >}}
## **Télécharger le code source d'exemple**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
