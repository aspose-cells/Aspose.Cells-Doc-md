---
title: Copier des formes entre des feuilles de calcul dans Aspose.Cells
type: docs
weight: 30
url: /fr/net/copy-shapes-between-worksheets-in-aspose-cells/
---
{{% alert color="primary" %}} 

Parfois, vous devez copier des éléments sur une feuille de calcul, par exemple des images, des graphiques et d'autres objets de dessin, entre les feuilles de calcul. Aspose.Cells prend en charge cette fonctionnalité. Les graphiques, images et autres objets peuvent être copiés avec le plus haut degré de précision.

Cet article vous explique en détail comment copier des formes entre des feuilles de calcul. Pour illustrer, il crée une application console dans Visual Studio.Net, copie des images, des graphiques et d'autres objets de dessin entre des feuilles de calcul à l'aide de Aspose.Cells.

{{% /alert %}} 

Vous trouverez ci-dessous le code permettant de copier un graphique d'une feuille de calcul à une autre

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Copy Shapes between Worksheets.xlsx";

//Open the template file

Workbook workbook = new Workbook(FileName);

//Get the Chart from the "Chart" worksheet.

Aspose.Cells.Charts.Chart source = workbook.Worksheets["Chart"].Charts[0];

Aspose.Cells.Drawing.ChartShape cshape = source.ChartObject;

//Copy the Chart to the Result Worksheet

workbook.Worksheets["Result"].Shapes.AddCopy(cshape, 20, 0, 2, 0);

//Save the Worksheet

workbook.Save(FileName);



{{< /highlight >}}

**Noter:** Pour plus de détails sur la copie de plusieurs formes, vous devez visiter[ici](/cells/fr/net/copy-shapes-between-worksheets/)
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **Télécharger l'exemple d'exécution**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
