---
title: Copier des formes entre des feuilles de calcul dans Aspose.Cells
type: docs
weight: 30
url: /fr/net/copy-shapes-between-worksheets-in-aspose-cells/
---

{{% alert color="primary" %}} 

Parfois, vous avez besoin de copier des éléments d'une feuille de calcul, par exemple des images, des graphiques et autres objets graphiques, entre des feuilles de calcul. Aspose.Cells prend en charge cette fonctionnalité. Les graphiques, les images et d'autres objets peuvent être copiés avec le plus haut degré de précision.

Cet article vous donne une compréhension détaillée de comment copier des formes entre des feuilles de calcul. Pour illustrer, il crée une application console dans Visual Studio.Net, copie des images, des graphiques et d'autres objets graphiques entre des feuilles de calcul en utilisant Aspose.Cells.

{{% /alert %}} 

Voici le code pour copier un graphique d'une feuille de calcul à une autre

**C#**

{{< highlight csharp >}}

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

**Remarque :** Pour plus de détails sur la copie de plusieurs formes, vous devez visiter [ici](/cells/fr/net/copy-shapes-between-worksheets/)
## **Télécharger le code source d'exemple**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **Télécharger un exemple en cours d'exécution**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
